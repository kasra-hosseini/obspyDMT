#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  plotxml_handler.py
#   Purpose:   exploring stationXML files
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from __future__ import print_function
from builtins import input as raw_input_built
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from obspy import read_inventory
try:
    from obspy.signal import pazToFreqResp
except Exception as e:
    from obspy.signal.invsim import paz_to_freq_resp as pazToFreqResp
try:
    from obspy.geodetics import locations2degrees
except Exception as e:
    from obspy.core.util import locations2degrees
import os
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### plot_xml_response ###############################


def plot_xml_response(input_dics):
    """
    plot the transfer function of stationXML file(s)
    :param input_dics:
    :return:
    """
    plt.rc('font', family='serif')
    print('[INFO] plotting StationXML file/files in: %s' % \
          input_dics['datapath'])
    if not os.path.isdir('./stationxml_plots'):
        print('[INFO] creating stationxml_plots directory...')
        os.mkdir('./stationxml_plots')

    # assign the input_dics parameters to the running parameters:
    stxml_dir = input_dics['datapath']
    plotxml_datetime = input_dics['plotxml_date']
    min_freq = input_dics['plotxml_min_freq']
    output = input_dics['plotxml_output']
    if 'dis' in output.lower():
        output = 'DISP'
    elif 'vel' in output.lower():
        output = 'VEL'
    elif 'acc' in output.lower():
        output = 'ACC'
    else:
        output = output.upper()
    start_stage = input_dics['plotxml_start_stage']
    end_stage_input = input_dics['plotxml_end_stage']
    percentage = input_dics['plotxml_percentage']/100.
    threshold = input_dics['plotxml_phase_threshold']
    plot_response = input_dics['plotxml_response']
    plotstage12 = input_dics['plotxml_plotstage12']
    plotpaz = input_dics['plotxml_paz']
    plotallstages = input_dics['plotxml_allstages']
    plot_map_compare = input_dics['plotxml_map_compare']

    if os.path.isfile(stxml_dir):
        addxml_all = glob.glob(os.path.join(stxml_dir))
    elif os.path.isdir(stxml_dir):
        addxml_all = glob.glob(os.path.join(stxml_dir, 'STXML.*'))
    else:
        try:
            addxml_all = glob.glob(os.path.join(stxml_dir))
        except Exception as error:
            print('[ERROR] %s' % error)
            sys.exit('[ERROR] wrong address: %s' % stxml_dir)

    addxml_all.sort()

    sta_lat = []
    sta_lon = []
    latlon_color = []
    report_fio = open(os.path.join('stationxml_plots',
                                   'report_stationxml'), 'wt')
    report_fio.writelines('channel_id\t\t\t\t%(phase_diff)\t\t'
                          'abs(max_diff)\tlat\t\t\tlon\t\t\tdatetime\t'
                          'decimation delay\tdecimation corr\n')
    report_fio.close()

    add_counter = 0
    for addxml in addxml_all:
        end_stage = end_stage_input
        add_counter += 1
        print(40*'-')
        print('%s/%s' % (add_counter, len(addxml_all)))
        try:
            xml_inv = read_inventory(addxml, format='stationXML')
            print("[STATIONXML] %s" % addxml)
            # we only take into account the first channel...
            cha_name = xml_inv.get_contents()['channels'][0]
            if plotxml_datetime:
                cha_date = plotxml_datetime
            else:
                cha_date = xml_inv.networks[0][0][-1].start_date
                print('[INFO] plotxml_date has not been set, the start_date ' \
                      'of the last channel in stationXML file will be used ' \
                      'instead: %s' % cha_date)

            xml_response = xml_inv.get_response(cha_name, cha_date + 0.1)
            if xml_inv[0][0][0].sample_rate:
                sampling_rate = xml_inv[0][0][0].sample_rate
            else:
                for stage in xml_response.response_stages[::-1]:
                    if (stage.decimation_input_sample_rate is not None) and\
                            (stage.decimation_factor is not None):
                        sampling_rate = (stage.decimation_input_sample_rate /
                                         stage.decimation_factor)
                        break

            t_samp = 1.0 / sampling_rate
            nyquist = sampling_rate / 2.0
            nfft = int(sampling_rate / min_freq)

            end_stage = min(len(xml_response.response_stages), end_stage)

            if plotallstages:
                plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft,
                                       min_freq, output,
                                       start_stage, end_stage, cha_name)

            try:
                cpx_response, freq = xml_response.get_evalresp_response(
                    t_samp=t_samp, nfft=nfft, output=output,
                    start_stage=start_stage, end_stage=end_stage)
                cpx_12, freq = xml_response.get_evalresp_response(
                    t_samp=t_samp, nfft=nfft, output=output, start_stage=1,
                    end_stage=2)
            except Exception as error:
                print('[WARNING] %s' % error)
                continue

            paz, decimation_delay, decimation_correction = \
                convert_xml_paz(xml_response, output, cha_name, cha_date)
            if not paz:
                continue

            h, f = pazToFreqResp(paz['poles'], paz['zeros'], paz['gain'],
                                 1./sampling_rate, nfft, freq=True)

            phase_resp = np.angle(cpx_response)
            phase_12 = np.angle(cpx_12)

            if plot_response:
                plt.figure(figsize=(20, 10))
                plt.suptitle(cha_name, size=24, weight='bold')
                if plotpaz or plotstage12:
                    plt.subplot(2, 2, 1)
                else:
                    plt.subplot(2, 1, 1)
                plt.loglog(freq, abs(cpx_response), color='blue',
                           lw=3, label='full-resp')
                if plotstage12:
                    plt.loglog(freq, abs(cpx_12), ls='--', color='black',
                               lw=3, label='Stage1,2')
                if plotpaz:
                    plt.loglog(f, abs(h)*paz['sensitivity'], color='red',
                               lw=3, label='PAZ')
                plt.axvline(nyquist, ls="--", color='black', lw=3)
                plt.ylabel('Amplitude', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.ylim(ymax=max(1.2*abs(cpx_response)))
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()

                if plotpaz or plotstage12:
                    plt.subplot(2, 2, 3)
                else:
                    plt.subplot(2, 1, 2)
                plt.semilogx(freq, phase_resp, color='blue',
                             lw=3, label='full-resp')
                if plotstage12:
                    plt.semilogx(freq, phase_12, ls='--', color='black',
                                 lw=3, label='Stage1,2')
                if plotpaz:
                    plt.semilogx(f, np.angle(h), color='red',
                                 lw=3, label='PAZ')
                plt.axvline(nyquist, ls="--", color='black', lw=3)
                plt.xlabel('Frequency [Hz]', size=24, weight='bold')
                plt.ylabel('Phase [rad]', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()

                if plotstage12 or plotpaz:
                    ax_222 = plt.subplot(2, 2, 2)
                    y_label = 'Amplitude ratio'
                    if plotstage12:
                        plt.loglog(freq, abs(abs(cpx_response) / abs(cpx_12)),
                                   '--', color='black', lw=3,
                                   label='|full-resp|/|Stage1,2|')
                        y_label = '|full-resp|/|Stage1,2|'
                    amp_ratio = 1
                    if plotpaz:
                        amp_ratio = abs(abs(cpx_response) /
                                        (abs(h)*paz['sensitivity']))
                        plt.loglog(f, amp_ratio,
                                   color='red', lw=3,
                                   label='|full-resp|/|PAZ|')
                        y_label = '|full-resp|/|PAZ|'
                    plt.axvline(nyquist, ls="--", color='black', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='black', lw=3)
                    plt.ylabel(y_label, size=24, weight='bold')
                    plt.xticks(size=18, weight='bold')
                    plt.yticks(size=18, weight='bold')
                    plt.xlim(xmin=min_freq, xmax=nyquist+5)
                    plt.ylim(ymax=1.2*max(amp_ratio[np.logical_not(
                        np.isnan(amp_ratio))]))
                    plt.grid()

                    ax_224 = plt.subplot(2, 2, 4)
                    y_label = 'Phase difference [rad]'
                    if plotstage12:
                        plt.semilogx(freq, abs(phase_resp - phase_12),
                                     color='black', ls='--', lw=3,
                                     label='|full-resp - Stage1,2|')
                        y_label = '|full-resp - Stage1,2| [rad]'
                    if plotpaz:
                        plt.semilogx(freq, abs(phase_resp - np.angle(h)),
                                     color='red', lw=3,
                                     label='|full-resp - PAZ|')
                        y_label = '|full-resp - PAZ|'
                    plt.axvline(nyquist, ls="--", color='black', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='black', lw=3)
                    plt.xlabel('Frequency [Hz]', size=24, weight='bold')
                    plt.ylabel(y_label,
                               size=24, weight='bold')
                    plt.xticks(size=18, weight='bold')
                    plt.yticks(size=18, weight='bold')
                    plt.xlim(xmin=min_freq, xmax=nyquist+5)
                    plt.grid()
                plt.savefig(os.path.join('stationxml_plots',
                                         cha_name + '.png'))
                plt.close()

            # compare = abs(phase[:int(0.8*len(phase))] -
            #              np.angle(h[:int(0.8*len(phase))]))
            # if len(compare[compare>0.1]) > 0:
            #    lat_red.append(xml_inv.get_coordinates(cha_name)['latitude'])
            #    lon_red.append(xml_inv.get_coordinates(cha_name)['longitude'])
            #    print cha_name
            #    print paz
            # else:
            #    lat_blue.append(xml_inv.get_coordinates(cha_name)['latitude'])
            #    lon_blue.append(xml_inv.get_coordinates(cha_name)['longitude'])

            phase_resp_check = phase_resp[:int(percentage*len(phase_resp))]
            phase_h_check = np.angle(h)[:int(percentage*len(np.angle(h)))]
            if not len(phase_resp_check) == len(phase_h_check):
                sys.exit('[ERROR] lengths of phase responses do not match: '
                         '%s (StationXML) != %s (PAZ)'
                         % (len(phase_resp_check), len(phase_h_check)))
            compare = abs(phase_resp_check - phase_h_check)
            percent_compare = \
                float(len(compare[compare >= 0.05]))/len(compare)*100
            latlondep = get_coordinates(xml_inv.networks[0],
                                        cha_name,
                                        cha_date + 0.1)
            sta_lat.append(latlondep['latitude'])
            sta_lon.append(latlondep['longitude'])

            d_c = np.sum(decimation_delay) - np.sum(decimation_correction)
            if not d_c == 0:
                latlon_color.append(0.)
            else:
                latlon_color.append(percent_compare)

            if percent_compare >= threshold:
                plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft,
                                       min_freq, output,
                                       start_stage, end_stage, cha_name)
            report_fio = open(os.path.join('stationxml_plots',
                                           'report_stationxml'), 'at')
            report_fio.writelines(
                '%s\t\t\t%6.2f\t\t\t%6.2f\t\t\t%6.2f\t\t%7.2f\t\t%s\t%s\t%s\n'
                % (cha_name,
                   round(percent_compare, 2),
                   round(max(abs(compare)), 2),
                   round(sta_lat[-1], 2),
                   round(sta_lon[-1], 2),
                   cha_date,
                   np.sum(decimation_delay),
                   np.sum(decimation_correction)))
            report_fio.close()
        except Exception as error:
            print('[Exception] %s' % error)

    if plot_map_compare:
        plt.figure()

        m = Basemap(projection='robin', lon_0=input_dics['plot_lon0'], lat_0=0)

        m.fillcontinents()
        m.drawparallels(np.arange(-90., 120., 30.))
        m.drawmeridians(np.arange(0., 420., 60.))
        m.drawmapboundary()

        x, y = m(sta_lon, sta_lat)
        m.scatter(x, y, 100, c=latlon_color, marker="v",
                  edgecolor='none', zorder=10, cmap='rainbow')
        plt.colorbar(orientation='horizontal')
        plt.savefig(os.path.join('stationxml_plots', 'compare_plots.png'))
        plt.show()
        raw_input_built('Press Enter...')
    sys.exit('[EXIT] obspyDMT finished normally...')

# ##################### get_coordinates ##########################


def get_coordinates(xml_network, seed_id, datetime=None):
    """
    FROM OBSPY REPOSITORY!

    Return coordinates for a given channel.

    :type seed_id: str
    :param seed_id: SEED ID string of channel to get coordinates for.
    :type datetime: :class:`~obspy.core.utcdatetime.UTCDateTime`, optional
    :param datetime: Time to get coordinates for.
    :rtype: dict
    :return: Dictionary containing coordinates (latitude, longitude,
        elevation)
    """
    network, station, location, channel = seed_id.split(".")
    coordinates = []
    if xml_network.code != network:
        pass
    elif xml_network.start_date and xml_network.start_date > datetime:
        pass
    elif xml_network.end_date and xml_network.end_date < datetime:
        pass
    else:
        for sta in xml_network.stations:
            # skip wrong station
            if sta.code != station:
                continue
            # check datetime only if given
            if datetime:
                # skip if start date before given datetime
                if sta.start_date and sta.start_date > datetime:
                    continue
                # skip if end date before given datetime
                if sta.end_date and sta.end_date < datetime:
                    continue
            for cha in sta.channels:
                # skip wrong channel
                if cha.code != channel:
                    continue
                # skip wrong location
                if cha.location_code != location:
                    continue
                # check datetime only if given
                if datetime:
                    # skip if start date before given datetime
                    if cha.start_date and cha.start_date > datetime:
                        continue
                    # skip if end date before given datetime
                    if cha.end_date and cha.end_date < datetime:
                        continue
                # prepare coordinates
                data = {}
                # if channel latitude or longitude is not given use station
                data['latitude'] = cha.latitude or sta.latitude
                data['longitude'] = cha.longitude or sta.longitude
                data['elevation'] = cha.elevation
                data['local_depth'] = cha.depth
                coordinates.append(data)
    if len(coordinates) > 1:
        msg = "Found more than one matching coordinates. Returning first."
        warnings.warn(msg)
    elif len(coordinates) < 1:
        msg = "No matching coordinates found."
        raise Exception(msg)
    return coordinates[0]

# ##################### plot_xml_plotallstages ##########################


def plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft, min_freq,
                           output, start_stage, end_stage, cha_name):
    """
    plot all the stages in a StationXML file. This is controlled by
    start_stage and end_stage
    :param xml_response:
    :param t_samp:
    :param nyquist:
    :param nfft:
    :param min_freq:
    :param output:
    :param start_stage:
    :param end_stage:
    :param cha_name:
    :return:
    """
    plt.rc('font', family='serif')
    if not os.path.isdir('./stationxml_plots'):
        print('[INFO] creating stationxml_plots directory...', end='')
        os.mkdir('./stationxml_plots')
        print('DONE')

    plt.figure(figsize=(20, 10))
    plt.suptitle(cha_name, size=24, weight='bold')
    l_style = ['-', '-', '-', '-', '-', '-', '-',
               '--', '--', '--', '--', '--', '--']
    counter = -1
    for i in range(start_stage, end_stage+1):
        counter += 1
        try:
            cpx_response, freq = xml_response.get_evalresp_response(
                t_samp=t_samp, nfft=nfft, output=output,
                start_stage=i, end_stage=i)
        except Exception as error:
            print('[WARNING] %s' % error)
            continue

        try:
            inp = xml_response.response_stages[i-1].input_units
        except Exception as error:
            print('[WARNING] %s' % error)
            inp = ''
        try:
            out = xml_response.response_stages[i-1].output_units
        except Exception as error:
            print('[WARNING] %s' % error)
            out = ''

        phase_resp = np.angle(cpx_response)

        ax = plt.subplot(2, 1, 1)
        ax.loglog(freq, abs(cpx_response), lw=3, ls=l_style[counter],
                  label='%s (%s->%s)' % (i, inp, out))
        ax.axvline(nyquist, ls="--", color='black', lw=3)

        plt.ylabel('Amplitude', size=24, weight='bold')
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.xlim(xmin=min_freq, xmax=nyquist+5)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.95, box.height])
        ax.legend(loc='center left', prop={'size': 18, 'weight': 'bold'},
                  bbox_to_anchor=(1, 0.5))
        ax.grid()

        ax = plt.subplot(2, 1, 2)
        ax.semilogx(freq, phase_resp, lw=3, ls=l_style[counter],
                    label='%s (%s->%s)' % (i, inp, out))
        ax.axvline(nyquist, ls="--", color='black', lw=3)

        plt.xlabel('Frequency [Hz]', size=24, weight='bold')
        plt.ylabel('Phase [rad]', size=24, weight='bold')
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.xlim(xmin=min_freq, xmax=nyquist+5)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.95, box.height])
        ax.legend(loc='center left', prop={'size': 18, 'weight': 'bold'},
                  bbox_to_anchor=(1, 0.5))
        ax.grid()
    plt.savefig(os.path.join('stationxml_plots',
                             '%s_stages.png' % cha_name))
    plt.close()

# ##################### convert_xml_paz ######################################


def convert_xml_paz(xml_response, output, cha_name, cha_date):
    """
    convert Stationxml file into PAZ dictionary
    :param xml_response:
    :param output:
    :param cha_name:
    :param cha_date:
    :return:
    """
    gain_arr = []
    normalization_factor = []
    poles = []
    zeros = []

    decimation_delay = []
    decimation_correction = []

    for resp_stage in xml_response.response_stages:
        gain_arr.append(resp_stage.stage_gain)
        try:
            poles.append(resp_stage.poles)
            zeros.append(resp_stage.zeros)
            normalization_factor.append(resp_stage.normalization_factor)
        except:
            pass
        if resp_stage.decimation_delay:
            decimation_delay.append(resp_stage.decimation_delay)
        if resp_stage.decimation_correction:
            decimation_correction.append(resp_stage.decimation_correction)

    if len(poles) > 1:
        print('[WARNING] More than one group of poles was found: %s' % poles)
    if len(zeros) > 1:
        print('[WARNING] More than one group of zeros was found: %s' % zeros)

    normalization_factor = normalization_factor[0]
    poles = poles[0]
    zeros = zeros[0]

    pz_type = xml_response.response_stages[0].pz_transfer_function_type
    if 'hertz' in pz_type.lower():
        poles = np.array(poles)*2*np.pi
        zeros = np.array(zeros)*2*np.pi
        normalization_factor *= np.power(2*np.pi, len(poles) - len(zeros))
    elif 'radian' in pz_type.lower():
        poles = np.array(poles)
        zeros = np.array(zeros)
    else:
        sys.exit('pz_type: %s' % pz_type)

    input_units = xml_response.response_stages[0].input_units
    if not input_units.lower() in ['m', 'm/s', 'm/s**2', 'pa']:
        print('[ERROR] input unit is not defined: %s\nContact the developer'
              % input_units)
        error_fio = open(os.path.join('./stationxml_plots',
                                      'error_format'), 'at')
        error_fio.writelines('%s\t\t%s\t\t%s\n' % (cha_name, cha_date,
                                                   input_units))
        return False

    poles = poles.tolist()
    zeros = zeros.tolist()

    if input_units.lower() == 'm':
        if output.lower() == 'vel':
            poles.append(0.0j)
        if output.lower() == 'acc':
            poles.append(0.0j)
            poles.append(0.0j)
    if input_units.lower() == 'm/s':
        if output.lower() == 'disp':
            zeros.append(0.0j)
        if output.lower() == 'acc':
            poles.append(0.0j)
    if input_units.lower() == 'm/s**2':
        if output.lower() == 'disp':
            zeros.append(0.0j)
            zeros.append(0.0j)
        if output.lower() == 'vel':
            zeros.append(0.0j)

    paz = {'poles': poles}
    paz['zeros'] = zeros
    paz['gain'] = normalization_factor
    paz['sensitivity'] = np.prod(np.array(gain_arr))
    print('[INFO] final PAZ:')
    print('zeros: ', paz['zeros'])
    print('poles: ', paz['poles'])
    print('gain: ', paz['gain'])
    print('sensitivity: ', paz['sensitivity'])
    return paz, decimation_delay, decimation_correction
