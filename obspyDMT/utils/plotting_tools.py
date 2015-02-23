#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  plotting_tools.py
#   Purpose:   Collection of plotting tools
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import fnmatch
import glob
import matplotlib.pyplot as plt
import math as math
from mpl_toolkits.basemap import Basemap
import numpy as np
from obspy import read_inventory
from obspy.signal import pazToFreqResp
from obspy.core.util import locations2degrees
from obspy.core import read
from obspy.imaging.beachball import Beach
import os
import random
import sys

from event_handler import quake_info
from utility_codes import read_station_event, read_event_dic

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### plot_tools ############################################


def plot_tools(input_dics, clients):
    """
    Managing the required inputs for plotting tools
    :param input_dics:
    :param clients:
    :return:
    """
    events = None
    for i in ['plot_sta', 'plot_ev', 'plot_ray', 'plot_ray_gmt', 'plot_epi',
              'plot_dt']:
        if input_dics[i]:
            events, address_events = quake_info(input_dics['plot_dir'], 'info')
            break

    ls_saved_stas = []
    ls_add_stas = []
    for k in ['plot_sta', 'plot_ev', 'plot_ray', 'plot_ray_gmt', 'plot_epi']:
        if input_dics[k] == 'N':
            continue
        for i in range(len(events)):
            ls_saved_stas_tmp = []
            ls_add_stas_tmp = []
            sta_ev = read_station_event(address_events[i])
            event_dic = read_event_dic(address_events[i])

            for j in range(len(sta_ev[0])):
                if input_dics['plot_type'].lower() == 'raw':
                    BH_file = 'BH_RAW'
                    network = sta_ev[0][j][0]
                elif input_dics['plot_type'].lower() == 'corrected':
                    if input_dics['corr_unit'].lower() == 'dis':
                        BH_file = 'BH'
                        network = 'dis.%s' % sta_ev[0][j][0]
                    elif input_dics['corr_unit'].lower() == 'vel':
                        BH_file = 'BH_VEL'
                        network = 'vel.%s' % sta_ev[0][j][0]
                    elif input_dics['corr_unit'].lower() == 'acc':
                        BH_file = 'BH_ACC'
                        network = 'acc.%s' % sta_ev[0][j][0]

                station_id = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
                             % (network, sta_ev[0][j][1], sta_ev[0][j][2],
                                sta_ev[0][j][3], sta_ev[0][j][4],
                                sta_ev[0][j][5], sta_ev[0][j][6],
                                sta_ev[0][j][7], sta_ev[0][j][8],
                                sta_ev[0][j][9], sta_ev[0][j][10],
                                sta_ev[0][j][11], sta_ev[0][j][12],
                                sta_ev[0][j][13])

                if input_dics['plot_all'] != 'Y':
                    if clients == sta_ev[0][j][13]:
                        station_id = station_id.split(',')
                        station_id.extend(event_dic['focal_mechanism'])
                        ls_saved_stas_tmp.append(station_id)
                        ls_add_stas_tmp.append(
                            os.path.join(address_events[i], BH_file,
                                         '%s.%s.%s.%s'
                                         % (network, sta_ev[0][j][1],
                                            sta_ev[0][j][2],
                                            sta_ev[0][j][3])))

                elif input_dics['plot_all'] == 'Y':
                    station_id = station_id.split(',')
                    station_id.extend(event_dic['focal_mechanism'])
                    ls_saved_stas_tmp.append(station_id)
                    ls_add_stas_tmp.append(
                        os.path.join(address_events[i], BH_file,
                                     '%s.%s.%s.%s'
                                     % (network, sta_ev[0][j][1],
                                        sta_ev[0][j][2], sta_ev[0][j][3])))

            ls_saved_stas.append(ls_saved_stas_tmp)
            ls_add_stas.append(ls_add_stas_tmp)

    import ipdb; ipdb.set_trace()
    for i in ['plot_sta', 'plot_ev', 'plot_ray']:
        if input_dics[i]:
            plot_se_ray(input_dics, ls_saved_stas)

    if input_dics['plot_ray_gmt'] != 'N':
        plot_ray_gmt(input_dics, ls_saved_stas)

    if input_dics['plot_epi'] != 'N':
        plot_epi(input_dics, ls_add_stas, ls_saved_stas)

    if input_dics['plot_dt'] != 'N':
        plot_dt(input_dics, address_events)

# ##################### plot_sta_ev_ray ###############################


def plot_sta_ev_ray(input_dics, sta_ev, ev_info, events, stations, ray_path):
    """
    Plots stations, events and ray paths on a map with basemap.
    :param input_dics:
    :param sta_ev:
    :param ev_info:
    :param events:
    :param stations:
    :param ray_path:
    :return:
    """

    if input_dics['evlatmin'] is None:
        evlatmin = -90
        evlatmax = +90
        evlonmin = -180
        evlonmax = +180
        glob_map = True
    else:
        evlatmin = input_dics['evlatmin']
        evlatmax = input_dics['evlatmax']
        evlonmin = input_dics['evlonmin']
        evlonmax = input_dics['evlonmax']
        glob_map = False

    if ray_path:
        # hammer, kav7, cyl, mbtfpq, moll
        m = Basemap(projection='aeqd', lon_0=0, lat_0=0)
        m.fillcontinents(color='lightgray', lake_color='lightblue')
        m.drawmapboundary(fill_color='lightblue')
        m.drawcoastlines(color='darkgray')
        parallels = np.arange(-90, 90, 30.)
        m.drawparallels(parallels, color='gray')
        meridians = np.arange(-180., 180., 60.)
        m.drawmeridians(meridians, color='gray')
        width_beach = 5e5
        width_station = 10
        plt.title('')
    elif not glob_map:
        m = Basemap(projection='cyl',
                    llcrnrlat=evlatmin,
                    urcrnrlat=evlatmax,
                    llcrnrlon=evlonmin,
                    urcrnrlon=evlonmax,
                    resolution=None)
        width_beach = 5
        width_station = 10
        parallels = np.arange(-90, 90, 5.)
        m.drawparallels(parallels, labels=[1, 0, 0, 1], fontsize=8)
        meridians = np.arange(-180., 180., 5.)
        m.drawmeridians(meridians, labels=[1, 0, 0, 1], fontsize=8)
        plt.title('')
    elif glob_map:
        # hammer, kav7, cyl, mbtfpq, moll
        m = Basemap(projection='mbtfpq', lon_0=0, resolution=None)
        width_beach = 5e5
        width_station = 10
        parallels = np.arange(-90, 90, 30.)
        m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=8)
        meridians = np.arange(-180., 180., 60.)
        m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=8)
        plt.title('')
    else:
        sys.exit('Available options: ray_path and glob_map')

    if not ray_path:
        raw_input_resp = raw_input('Choose your map style:\n'
                                   '1. Bluemarble\n'
                                   '2. Etopo\n'
                                   '3. Shaderelief')
        if raw_input_resp == '1':
            m.bluemarble(scale=0.5)
        elif raw_input_resp == '2':
            m.etopo(scale=0.5)
        elif raw_input_resp == '3':
            m.shadedrelief(scale=0.1)
        else:
            print "Available options: 1, 2, 3...Proceed with ETOPO"
            m.etopo(scale=0.5)

    if events:
        for i in range(len(ev_info)):
            try:
                ev_lon = ev_info.events[i].preferred_origin().longitude
                ev_lat = ev_info.events[i].preferred_origin().latitude

                ev_mrr = ev_info.events[i].preferred_focal_mechanism().moment_tensor.tensor.m_rr
                ev_mtt = ev_info.events[i].preferred_focal_mechanism().moment_tensor.tensor.m_tt
                ev_mpp = ev_info.events[i].preferred_focal_mechanism().moment_tensor.tensor.m_pp
                ev_mrt = ev_info.events[i].preferred_focal_mechanism().moment_tensor.tensor.m_rt
                ev_mrp = ev_info.events[i].preferred_focal_mechanism().moment_tensor.tensor.m_rp
                ev_mtp = ev_info.events[i].preferred_focal_mechanism().moment_tensor.tensor.m_tp

                x, y = m(ev_lon, ev_lat)
                focmecs = [ev_mrr, ev_mtt, ev_mpp, ev_mrt, ev_mrp, ev_mtp]
                ax = plt.gca()
                b = Beach(focmecs, xy=(x, y), facecolor='red', width=width_beach, linewidth=1, alpha=0.85)
                b.set_zorder(10)
                ax.add_collection(b)
            except Exception as e:
                x, y = m(ev_lon, ev_lat)
                magnitude = ev_info.events[i].preferred_magnitude().mag
                m.scatter(x, y, color="red", marker="o", s=10*magnitude, zorder=5, alpha=0.6)
        if Exception:
            print 'WARNING: %s' % Exception
    else:
        print 'No events will be plotted.'

    if stations == True:
        for i in range(len(sta_ev[0])):
            x, y = m(sta_ev[0][i][5], sta_ev[0][i][4])
            m.scatter(x, y, color='black', s=width_station, marker="v", zorder=4, alpha=0.9)
    else:
        print 'No stations will be plotted on your map!'

    if events == stations == ray_path ==True:
        print 'Map with ray paths is created!'
        for i in range(len(sta_ev[0])):
            for j in range(len(ev_info)):
                ev_lon = ev_info.events[j].preferred_origin().longitude
                ev_lat = ev_info.events[j].preferred_origin().latitude

                m.drawgreatcircle(ev_lon, ev_lat, eval(sta_ev[0][i][5]), eval(sta_ev[0][i][4]), color= 'red', alpha=0.1)
    else:
        print 'No rays path will be plotted on your map!'

    plt.show()

# ##################### plot_xml_response ###############################


def plot_xml_response(input_dics):
    """
    This function plots the response file of stationXML file(s)
    It has several modes such as:
    plotting all the stages
    plotting full response file
    plotting selected stages
    plotting only PAZ
    :param input_dics:
    :return:
    """

    print '[INFO] plotting StationXML file/files in: %s' % \
          input_dics['plotxml_dir']
    if not os.path.isdir('./stationxml_plots'):
        print '[INFO] creating stationxml_plots directory...',
        os.mkdir('./stationxml_plots')
        print 'DONE'

    # Assign the input_dics parameters to the running parameters
    # in this function:
    stxml_dir = input_dics['plotxml_dir']
    plotxml_datetime = input_dics['plotxml_date']
    min_freq = input_dics['plotxml_min_freq']
    output = input_dics['plotxml_output']
    if output.lower() == 'dis':
        output = 'DISP'
    start_stage = input_dics['plotxml_start_stage']
    end_stage = input_dics['plotxml_end_stage']
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
        except Exception, e:
            print 'ERROR: %s' % e
            sys.exit('[ERROR] wrong address: %s' % stxml_dir)

    addxml_all.sort()

    sta_lat = []
    sta_lon = []
    latlon_color = []
    report_fio = open(os.path.join('./stationxml_plots',
                                   'report_stationxml'), 'w')
    report_fio.writelines('#channel\t\t\t\t%(Phase)\t\t'
                          'Max Diff(abs) \tLat\t\t\tLon\t\t\tDatetime\n')
    report_fio.close()
    add_counter = 0
    for addxml in addxml_all:
        add_counter += 1
        print 40*'-'
        print '%s/%s' % (add_counter, len(addxml_all))
        try:
            xml_inv = read_inventory(addxml, format='stationXML')
            print "[STATIONXML] %s" % addxml
            cha_name = xml_inv.get_contents()['channels'][0]
            if plotxml_datetime:
                cha_date = plotxml_datetime
            else:
                cha_date = xml_inv.networks[0][0][-1].start_date
                print '[INFO] plotxml_date has not been set, the start_date ' \
                      'of the last channel in stationXML file will be used ' \
                      'instead: %s' % cha_date

            xml_response = xml_inv.get_response(cha_name, cha_date + 0.1)
            for stage in xml_response.response_stages[::-1]:
                if (stage.decimation_input_sample_rate is not None
                        and stage.decimation_factor is not None):
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
            except Exception, e:
                print 'WARNING: %s' % e
                continue

            paz = convert_xml_paz(xml_response, output, cha_name, cha_date)
            if not paz:
                continue
            h, f = pazToFreqResp(paz['poles'], paz['zeros'], paz['gain'],
                                 1./sampling_rate, nfft, freq=True)

            phase_resp = np.angle(cpx_response)
            phase_12 = np.angle(cpx_12)

            if plot_response:
                plt.close()
                plt.ion()
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
                plt.axvline(nyquist, ls="--", color='blue', lw=3)
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
                plt.axvline(nyquist, ls="--", color='blue', lw=3)
                plt.xlabel('Frequency [Hz]', size=24, weight='bold')
                plt.ylabel('Phase [rad]', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()

                if plotstage12 or plotpaz:
                    plt.subplot(2, 2, 2)
                    if plotstage12:
                        plt.loglog(freq, abs(abs(cpx_response) - abs(cpx_12)),
                                   '--', color='black', lw=3,
                                   label='|full-resp - Stage1,2|')
                    if plotpaz:
                        plt.loglog(f, abs(abs(cpx_response) -
                                          abs(h)*paz['sensitivity']),
                                   color='red', lw=3,
                                   label='|full-resp - PAZ|')
                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                    plt.ylabel('Amplitude Difference', size=24, weight='bold')
                    plt.xticks(size=18, weight='bold')
                    plt.yticks(size=18, weight='bold')
                    plt.xlim(xmin=min_freq, xmax=nyquist+5)
                    plt.ylim(ymax=max(1.2*abs(cpx_response)))
                    plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                    plt.grid()

                    plt.subplot(2, 2, 4)
                    if plotstage12:
                        plt.semilogx(freq, abs(phase_resp - phase_12),
                                     color='black', ls='--', lw=3,
                                     label='|full-resp - Stage1,2|')
                    if plotpaz:
                        plt.semilogx(freq, abs(phase_resp - np.angle(h)),
                                     color='red', lw=3,
                                     label='|full-resp - PAZ|')
                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                    plt.xlabel('Frequency [Hz]', size=24, weight='bold')
                    plt.ylabel('Phase Difference [rad]',
                               size=24, weight='bold')
                    plt.xticks(size=18, weight='bold')
                    plt.yticks(size=18, weight='bold')
                    plt.xlim(xmin=min_freq, xmax=nyquist+5)
                    plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                    plt.grid()
                plt.savefig(os.path.join('stationxml_plots',
                                         cha_name + '.png'))

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
                sys.exit('Lengths of phase responses do not match: '
                         '%s (StationXML) != %s (PAZ)'
                         % (len(phase_resp_check), len(phase_h_check)))
            compare = abs(phase_resp_check - phase_h_check)
            percent_compare = \
                float(len(compare[compare >= 0.05]))/len(compare)*100
            sta_lat.append(
                xml_inv.get_coordinates(cha_name, cha_date + 0.1)['latitude'])
            sta_lon.append(
                xml_inv.get_coordinates(cha_name, cha_date + 0.1)['longitude'])
            latlon_color.append(percent_compare)
            if percent_compare >= threshold:
                plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft,
                                       min_freq, output,
                                       start_stage, end_stage, cha_name)
            report_fio = open(os.path.join('./stationxml_plots',
                                           'report_stationxml'), 'a')
            report_fio.writelines(
                '%s\t\t\t%6.2f\t\t\t%6.2f\t\t\t%6.2f\t\t%7.2f\t\t%s\n'
                % (cha_name,
                   round(percent_compare, 2),
                   round(max(abs(compare)), 2),
                   round(sta_lat[-1], 2),
                   round(sta_lon[-1], 2),
                   cha_date))
            report_fio.close()
        except Exception, e:
            print 'Exception: %s' % e

    if plot_map_compare:
        plt.figure()
        m = Basemap(projection='robin', lon_0=0, lat_0=0)
        # m.drawcoastlines()
        m.fillcontinents()
        m.drawparallels(np.arange(-90., 120., 30.))
        m.drawmeridians(np.arange(0., 420., 60.))
        m.drawmapboundary()

        x, y = m(sta_lon, sta_lat)
        m.scatter(x, y, 100, c=latlon_color, marker="v",
                  edgecolor='none', zorder=10, cmap='hot_r')
        plt.colorbar(orientation='horizontal')
        plt.savefig(os.path.join('stationxml_plots', 'compare_plots.png'))
        plt.show()
        raw_input('Press Enter...')
    sys.exit('[EXIT] obspyDMT finished normally...')

# ##################### plot_xml_plotallstages ##########################


def plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft, min_freq,
                           output, start_stage, end_stage, cha_name):
    """
    plot all the stages in a StationXML file.
    This is controlled by start_stage and end_stage
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

    if not os.path.isdir('./stationxml_plots'):
        print '[INFO] creating stationxml_plots directory...',
        os.mkdir('./stationxml_plots')
        print 'DONE'
    plt.close()
    plt.ion()
    plt.figure(figsize=(20, 10))
    plt.suptitle(cha_name, size=24, weight='bold')
    for i in range(start_stage, end_stage+1):
        try:
            cpx_response, freq = xml_response.get_evalresp_response(
                t_samp=t_samp, nfft=nfft, output=output,
                start_stage=i, end_stage=i)
        except Exception, e:
            print 'WARNING: %s' % e
            continue

        try:
            inp = xml_response.response_stages[i-1].input_units
        except Exception, e:
            print 'WARNING: %s' % e
            inp = ''
        try:
            out = xml_response.response_stages[i-1].output_units
        except Exception, e:
            print 'WARNING: %s' % e
            out = ''

        phase_resp = np.angle(cpx_response)

        ax = plt.subplot(2, 1, 1)
        ax.loglog(freq, abs(cpx_response), lw=3,
                  label='%s (%s->%s)' % (i, inp, out))
        ax.axvline(nyquist, ls="--", color='blue', lw=3)
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
        ax.semilogx(freq, phase_resp, lw=3,
                    label='%s (%s->%s)' % (i, inp, out))
        ax.axvline(nyquist, ls="--", color='blue', lw=3)
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
    for resp_stage in xml_response.response_stages:
        gain_arr.append(resp_stage.stage_gain)
        try:
            normalization_factor.append(resp_stage.normalization_factor)
            if not isinstance(resp_stage, 'PolesZerosResponseStage'):
                print 'WARNING: normalization factor read from a stage ' \
                      'other than PAZ'
        except Exception as e:
            pass
        try:
            poles.append(resp_stage.poles)
            zeros.append(resp_stage.zeros)
            if not isinstance(resp_stage, 'PolesZerosResponseStage'):
                print 'WARNING: Poles and Zeros read from a stage ' \
                      'other than PAZ'
        except Exception as e:
            pass

    if len(poles) > 1:
        print 'WARNING: More than one group of poles was found: %s' % poles
        for i in range(1, len(poles)):
            poles[0].extend(poles[i])
    if len(zeros) > 1:
        print 'WARNING: More than one group of zeros was found: %s' % zeros
        for i in range(1, len(zeros)):
            zeros[0].extend(zeros[i])

    paz = {'poles': poles[0]}

    input_units = xml_response.response_stages[0].input_units
    if not input_units.lower() in ['m', 'm/s', 'm/s**2']:
        print('ERROR: input unit is not defined: %s\nContact the developer'
              % input_units)
        error_fio = open(os.path.join('./stationxml_plots',
                                      'error_format'), 'a')
        error_fio.writelines('%s\t\t%s\t\t%s\n' % (cha_name, cha_date,
                                                   input_units))
        return False
    if input_units.lower() == 'm/s':
        if output.lower() == 'disp':
            zeros[0].append(0.0j)
    if input_units.lower() == 'm/s**2':
        if output.lower() == 'disp':
            zeros[0].append(0.0j)
            zeros[0].append(0.0j)
        if output.lower() == 'vel':
            zeros[0].append(0.0j)
    if output.lower() == 'acc':
        sys.exit('%s output has not implemented!' % output)
    paz['zeros'] = zeros[0]
    paz['gain'] = np.prod(np.array(normalization_factor))
    paz['sensitivity'] = np.prod(np.array(gain_arr))
    return paz

# ##################### seismicity ######################################


def seismicity(input_dics, events):
    """
    Create seismicity map
    :param input_dics:
    :param events:
    :return:
    """
    print '\n##############'
    print 'Seismicity map'
    print '##############\n'

    if input_dics['evlatmin'] is None:
        input_dics['evlatmin'] = -90
        input_dics['evlatmax'] = +90
        input_dics['evlonmin'] = -180
        input_dics['evlonmax'] = +180

    # Set-up the map
    m = Basemap(projection='cyl',
                llcrnrlat=input_dics['evlatmin'],
                urcrnrlat=input_dics['evlatmax'],
                llcrnrlon=input_dics['evlonmin'],
                urcrnrlon=input_dics['evlonmax'],
                resolution='l')
    # m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90., 120., 30.))
    m.drawmeridians(np.arange(0., 420., 60.))
    m.drawmapboundary()

    # Defining Labels:
    x_ev, y_ev = m(-360, 0)
    m.scatter(x_ev, y_ev, 20, color='red', marker="o",
              edgecolor="black", zorder=10, label='0-70km')
    m.scatter(x_ev, y_ev, 20, color='green', marker="o",
              edgecolor="black", zorder=10, label='70-300km')
    m.scatter(x_ev, y_ev, 20, color='blue', marker="o",
              edgecolor="black", zorder=10, label='300< km')

    m.scatter(x_ev, y_ev, 10, color='white', marker="o",
              edgecolor="black", zorder=10, label='<=4.0')
    m.scatter(x_ev, y_ev, 40, color='white', marker="o",
              edgecolor="black", zorder=10, label='4.0-5.0')
    m.scatter(x_ev, y_ev, 70, color='white', marker="o",
              edgecolor="black", zorder=10, label='5.0-6.0')
    m.scatter(x_ev, y_ev, 100, color='white', marker="o",
              edgecolor="black", zorder=10, label='6.0<')

    ev_dp_all = []
    ev_mag_all = []
    ev_info_ar = np.array([])
    plot_focal_mechanism = False
    for ev in events:
        x_ev, y_ev = m(float(ev['longitude']), float(ev['latitude']))
        ev_dp_all.append(abs(float(ev['depth'])))
        ev_mag_all.append(abs(float(ev['magnitude'])))
        if abs(float(ev['depth'])) <= 70.0:
            color = 'red'
        elif 70.0 < abs(float(ev['depth'])) <= 300.0:
            color = 'green'
        elif 300.0 < abs(float(ev['depth'])) <= 1000.0:
            color = 'blue'

        if float(ev['magnitude']) <= 4.0:
            size = 10
        elif 4.0 < float(ev['magnitude']) <= 5.0:
            size = 40
        elif 5.0 < float(ev['magnitude']) <= 6.0:
            size = 70
        elif 6.0 < float(ev['magnitude']):
            size = 100

        if ev['focal_mechanism']:
            plot_focal_mechanism = True
            f1 = ev['focal_mechanism'][0]
            f2 = ev['focal_mechanism'][1]
            f3 = ev['focal_mechanism'][2]
            f4 = ev['focal_mechanism'][3]
            f5 = ev['focal_mechanism'][4]
            f6 = ev['focal_mechanism'][5]
        else:
            f1 = False
            f2 = False
            f3 = False
            f4 = False
            f5 = False
            f6 = False
        if np.size(ev_info_ar) < 1:
            ev_info_ar = np.append(ev_info_ar,
                                   [float(ev['depth']), float(x_ev),
                                    float(y_ev), size, color,
                                    f1, f2, f3, f4, f5, f6])
        else:
            ev_info_ar = np.vstack((ev_info_ar,
                                    [float(ev['depth']), float(x_ev),
                                     float(y_ev), size, color,
                                     f1, f2, f3, f4, f5, f6]))
    ev_info_ar = sorted(ev_info_ar,
                        key=lambda ev_info_iter: float(ev_info_iter[0]))

    for ev in ev_info_ar:
        m.scatter(float(ev[1]), float(ev[2]), float(ev[3]),
                  color=ev[4], marker="o", edgecolor=None, zorder=10)

    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

    if plot_focal_mechanism:
        plt.figure()
        # Set-up the map
        m = Basemap(projection='cyl',
                    llcrnrlat=input_dics['evlatmin'],
                    urcrnrlat=input_dics['evlatmax'],
                    llcrnrlon=input_dics['evlonmin'],
                    urcrnrlon=input_dics['evlonmax'],
                    resolution='l')
        # m.drawcoastlines()
        m.fillcontinents()
        m.drawparallels(np.arange(-90., 120., 30.))
        m.drawmeridians(np.arange(0., 420., 60.))
        m.drawmapboundary()
        for evfoc in ev_info_ar:
            ax = plt.gca()
            focmec = (float(evfoc[5]), float(evfoc[6]), float(evfoc[7]),
                      float(evfoc[8]), float(evfoc[9]), float(evfoc[10]))
            b = Beach(focmec, xy=(float(evfoc[1]), float(evfoc[2])),
                      facecolor=evfoc[4], width=float(evfoc[3])/100.,
                      linewidth=1, alpha=0.85)
            b.set_zorder(10)
            ax.add_collection(b)

    plt.figure()
    plt.hist(ev_dp_all, input_dics['depth_bins_seismicity'],
             facecolor='green', alpha=0.75, log=True, histtype='stepfilled')
    plt.xlabel('Depth', size=24, weight='bold')
    plt.ylabel('#Events (log)', size=24, weight='bold')
    plt.yscale('log')
    plt.xticks(size=18, weight='bold')
    plt.yticks(size=18, weight='bold')
    plt.tight_layout()

    plt.figure()
    plt.hist(ev_mag_all,
             bins=np.linspace(int(float(input_dics['min_mag'])),
                              int(float(input_dics['max_mag'])),
                              (int(float(input_dics['max_mag'])) -
                              int(float(input_dics['min_mag'])))*2+1),
             facecolor='green', alpha=0.75, log=True, histtype='stepfilled')
    plt.xlabel('Magnitude', size=24, weight='bold')
    plt.ylabel('#Events (log)', size=24, weight='bold')
    plt.yscale('log')
    plt.xticks(size=18, weight='bold')
    plt.yticks(size=18, weight='bold')
    plt.tight_layout()

    plt.show()

# ##################### plot_se_ray #####################################


def plot_se_ray(input_dics, ls_saved_stas):
    """
    one of the following configurations (based on the inputs) will be Plotted:
    station
    event
    both station and event
    ray path
    """
    plt.clf()
    m = Basemap(projection='aeqd', lon_0=-100, lat_0=40)
    # m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90., 120., 30.))
    m.drawmeridians(np.arange(0., 420., 60.))
    m.drawmapboundary()

    pattern_sta = '%s.%s.%s' % (input_dics['sta'],
                                input_dics['loc'],
                                input_dics['cha'])
    for i in range(len(ls_saved_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%"
                         % ('='*int(100.*(i+1)/len(ls_saved_stas)),
                            100.*(i+1)/len(ls_saved_stas)))
        sys.stdout.flush()

        ls_stas = ls_saved_stas[i]
        if not input_dics['evlatmin']:
            input_dics['evlatmin'] = -90
            input_dics['evlatmax'] = +90
            input_dics['evlonmin'] = -180
            input_dics['evlonmax'] = +180
        if input_dics['plot_ev'] != 'N' or \
           input_dics['plot_ray'] != 'N':
            if not input_dics['evlatmin'] <= float(ls_stas[0][9]) <= \
                    input_dics['evlatmax'] or not \
                    input_dics['evlonmin'] <= \
                    float(ls_stas[0][10]) <= \
                    input_dics['evlonmax'] or not \
                    input_dics['max_depth'] <= \
                    float(ls_stas[0][11]) <= \
                    input_dics['min_depth'] or not \
                    input_dics['min_mag'] <= \
                    float(ls_stas[0][12]) <= \
                    input_dics['max_mag']:
                continue

        if input_dics['plot_ev'] != 'N' or \
           input_dics['plot_ray'] != 'N':
            x_ev, y_ev = m(float(ls_stas[0][10]), float(ls_stas[0][9]))
            m.scatter(x_ev, y_ev, math.log(float(ls_stas[0][12])) ** 6,
                      color="red", marker="o", edgecolor="black", zorder=10)

        for j in range(len(ls_stas)):
            try:
                station_name = '%s.%s.%s' % (ls_stas[j][1],
                                             ls_stas[j][2],
                                             ls_stas[j][3])
                # station_ID = ls_stas[j][0] + '.' + station_name

                if not fnmatch.fnmatch(station_name, pattern_sta):
                    continue
                if not input_dics['mlat_rbb']:
                    input_dics['mlat_rbb'] = -90.0
                    input_dics['Mlat_rbb'] = +90.0
                    input_dics['mlon_rbb'] = -180.0
                    input_dics['Mlon_rbb'] = +180.0
                if not input_dics['mlat_rbb'] <= \
                        float(ls_stas[j][4]) <= \
                        input_dics['Mlat_rbb'] or not \
                   input_dics['mlon_rbb'] <= \
                   float(ls_stas[j][5]) <= \
                   input_dics['Mlon_rbb']:
                    continue
                st_lat = float(ls_stas[j][4])
                st_lon = float(ls_stas[j][5])
                ev_lat = float(ls_stas[j][9])
                ev_lon = float(ls_stas[j][10])
                # ev_mag = float(ls_stas[j][12])

                if input_dics['plot_ray'] != 'N':
                    m.drawgreatcircle(ev_lon, ev_lat,
                                      st_lon, st_lat, alpha=0.1)
                if input_dics['plot_sta'] != 'N' or \
                   input_dics['plot_ray'] != 'N':
                    x_sta, y_sta = m(st_lon, st_lat)
                    m.scatter(x_sta, y_sta, 40, color='blue', marker="v",
                              edgecolor="black", zorder=10)

            except Exception as e:
                print 'WARNING: %s' % e
                pass

    print '\nSaving the plot in the following address:'
    print os.path.join(input_dics['plot_save'], 'plot.%s'
                       % input_dics['plot_format'])
    plt.savefig(os.path.join(input_dics['plot_save'],
                             'plot.%s' % input_dics['plot_format']))

# ##################### plot_ray_gmt ####################################


def plot_ray_gmt(input_dics, ls_saved_stas):
    """
    Plot: stations, events and ray paths for the specified directory using GMT
    """
    evsta_info_open = open(os.path.join(input_dics['plot_save'],
                                        'evsta_info.txt'), 'w')
    evsta_plot_open = open(os.path.join(input_dics['plot_save'],
                                        'evsta_plot.txt'), 'w')
    ev_plot_open = open(os.path.join(input_dics['plot_save'],
                                     'ev_plot.txt'), 'w')
    sta_plot_open = open(os.path.join(input_dics['plot_save'],
                                      'sta_plot.txt'), 'w')

    ls_sta = []
    for i in range(len(ls_saved_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%"
                         % ('='*int(100.*(i+1)/len(ls_saved_stas)),
                            100.*(i+1)/len(ls_saved_stas)))
        sys.stdout.flush()

        ls_stas = ls_saved_stas[i]
        if not input_dics['evlatmin']:
            input_dics['evlatmin'] = -90
            input_dics['evlatmax'] = +90
            input_dics['evlonmin'] = -180
            input_dics['evlonmax'] = +180
        if not input_dics['evlatmin'] <= \
                float(ls_stas[0][9]) <= \
                input_dics['evlatmax'] or not \
                input_dics['evlonmin'] <= \
                float(ls_stas[0][10]) <= \
                input_dics['evlonmax'] or not \
                input_dics['max_depth'] <= \
                float(ls_stas[0][11]) <= \
                input_dics['min_depth'] or not \
                input_dics['min_mag'] <= \
                float(ls_stas[0][12]) <= \
                input_dics['max_mag']:
            continue
        ev_plot_open.writelines('%s %s \n'
                                % (round(float(ls_stas[0][10]), 5),
                                   round(float(ls_stas[0][9]), 5)))
        pattern_sta = '%s.%s.%s' % (input_dics['sta'],
                                    input_dics['loc'],
                                    input_dics['cha'])

        for j in range(len(ls_stas)):
            station_name = '%s.%s.%s' % (ls_stas[j][1],
                                         ls_stas[j][2],
                                         ls_stas[j][3])
            station_ID = '%s.%s' % (ls_stas[j][0], station_name)

            if not fnmatch.fnmatch(station_name, pattern_sta):
                continue
            if not input_dics['mlat_rbb']:
                    input_dics['mlat_rbb'] = -90.0
                    input_dics['Mlat_rbb'] = +90.0
                    input_dics['mlon_rbb'] = -180.0
                    input_dics['Mlon_rbb'] = +180.0
            if not input_dics['mlat_rbb'] <= \
                    float(ls_stas[j][4]) <= \
                    input_dics['Mlat_rbb'] or not \
                    input_dics['mlon_rbb'] <= \
                    float(ls_stas[j][5]) <= \
                    input_dics['Mlon_rbb']:
                continue

            evsta_info_open.writelines('%s , %s , \n' % (ls_stas[j][8],
                                                         station_ID))

            evsta_plot_open.writelines(
                '> -G%s/%s/%s\n%s %s %s\n%s %s %s \n'
                % (int(random.random()*256), int(random.random()*256),
                   int(random.random()*256), round(float(ls_stas[j][10]), 5),
                   round(float(ls_stas[j][9]), 5), random.random(),
                   round(float(ls_stas[j][5]), 5),
                   round(float(ls_stas[j][4]), 5), random.random()))
            ls_sta.append([station_ID, [str(round(float(ls_stas[j][4]), 5)),
                                        str(round(float(ls_stas[j][5]), 5))]])

    for k in range(len(ls_sta)):
        sta_plot_open.writelines('%s %s \n'
                                 % (ls_sta[k][1][1], ls_sta[k][1][0]))

    evsta_info_open.close()
    evsta_plot_open.close()
    ev_plot_open.close()
    sta_plot_open.close()

    pwd_str = os.getcwd()

    os.chdir(input_dics['plot_save'])
    os.system('psbasemap -Rd -JK180/9i -B45g30 -K > output.ps')
    os.system('pscoast -Rd -JK180/9i -B45g30:."World-wide Ray Path Coverage": '
              '-Dc -A1000 -Glightgray -Wthinnest -t0 -O -K >> output.ps')
    os.system('psxy ./evsta_plot.txt -JK180/9i -Rd -O -K -W0.2 -t85 >> '
              'output.ps')
    os.system('psxy ./sta_plot.txt -JK180/9i -Rd -Si0.2c -Gblue -O -K >>'
              ' output.ps')
    os.system('psxy ./ev_plot.txt -JK180/9i -Rd -Sa0.28c -Gred -O >>'
              ' output.ps')
    os.system('ps2raster output.ps -A -P -Tf')

    os.system('mv output.ps plot.ps')
    os.system('mv output.pdf plot.pdf')

    os.system('xdg-open plot.pdf')

    os.chdir(pwd_str)

# ##################### plot_epi ########################################


def plot_epi(input_dics, ls_add_stas, ls_saved_stas):
    """
    Plot arranged waveforms by epicentral distance versus time
    """

    plt.clf()

    for target in range(len(ls_add_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%"
                         % ('='*int(100.*(target+1)/len(ls_add_stas)),
                            100.*(target+1)/len(ls_add_stas)))
        sys.stdout.flush()

        for i in range(len(ls_add_stas[target])):
            try:
                tr = read(ls_add_stas[target][i])[0]
                tr.normalize()
                dist = locations2degrees(float(ls_saved_stas[target][i][9]),
                                         float(ls_saved_stas[target][i][10]),
                                         float(ls_saved_stas[target][i][4]),
                                         float(ls_saved_stas[target][i][5]))
                if input_dics['min_epi'] <= dist <= input_dics['max_epi']:
                    plt.plot(
                        np.linspace(0,
                                    (tr.stats.npts-1)/tr.stats.sampling_rate,
                                    tr.stats.npts), tr.data + dist,
                        color='black')
            except Exception as e:
                print 'WARNING: %s' % e
                pass
            plt.xlabel('Time (sec)')
            plt.ylabel('Epicentral distance (deg)')

    print '\nSaving the plot in the following address:'
    print os.path.join(input_dics['plot_save'],
                       'plot.%s' % input_dics['plot_format'])
    plt.savefig(os.path.join(input_dics['plot_save'],
                             'plot.%s' % input_dics['plot_format']))

# ##################### plot_dt #########################################


def plot_dt(input_dics, address_events):
    """
    Plot stored Data(MB) as a function of Time(Sec)
    """

    single_succ = None
    parallel_succ = None

    for i in range(len(address_events)):
        for client_time in ['time_fdsn', 'time_arc']:
            print 'Event address: %s' % address_events[i]
            if os.path.isfile(os.path.join(address_events[i], 'info',
                                           client_time)):
                plt.clf()
                dt_open = open(os.path.join(address_events[i], 'info',
                                            client_time))
                dt_read = dt_open.readlines()
                for j in range(len(dt_read)):
                    dt_read[j] = dt_read[j].split(',')

                time_single = 0
                succ = 0
                fail = 0
                MB_all = []
                time_all = []

                for k in range(len(dt_read)):
                    time_single += \
                        eval(dt_read[k][4]) + eval(dt_read[k][5])/(1024.**2)
                    time_all.append(time_single)

                    MB_single = eval(dt_read[k][6])
                    MB_all.append(MB_single)

                    if dt_read[k][7] == '+':
                        single_succ = plt.scatter(time_single,
                                                  MB_single,
                                                  s=1, c='b',
                                                  edgecolors='b', marker='o',
                                                  label='Serial (successful)')
                        succ += 1
                    elif dt_read[k][7] == '-':
                        # single_fail = plt.scatter(time_single,
                        #                           MB_single,
                        #                           s=1, c='r',
                        #                           edgecolors='r', marker='o',
                        #                           label='Serial (failed)')
                        fail += 1

                if input_dics['req_parallel'] == 'Y':
                    rep_par_open = open(os.path.join(address_events[i],
                                                     'info',
                                                     'report_parallel'))
                    rep_par_read = rep_par_open.readlines()
                    time_parallel = \
                        eval(rep_par_read[4].split(',')[0]) + \
                        eval(rep_par_read[4].split(',')[1])/(1024.**2)
                    MB_parallel = eval(rep_par_read[4].split(',')[2])
                    # trans_rate_parallel = MB_parallel/time_parallel*60
                    parallel_succ = plt.scatter(time_parallel,
                                                MB_parallel,
                                                s=30, c='r',
                                                edgecolors='r', marker='o',
                                                label='Parallel')

                time_array = np.array(time_all)
                MB_array = np.array(MB_all)

                poly = np.poly1d(np.polyfit(time_array, MB_array, 1))
                # time_poly = np.linspace(0, time_all[-1], len(time_all))
                plt.plot(time_array, poly(time_array), 'k--')

                trans_rate = (poly(time_array[-1]) -
                              poly(time_array[0])) / \
                             (time_array[-1]-time_array[0])*60

                plt.xlabel('Time (sec)', size='large', weight='bold')
                plt.ylabel('Stored Data (MB)', size='large', weight='bold')
                plt.xticks(size='large', weight='bold')
                plt.yticks(size='large', weight='bold')
                plt_title = \
                    '%s\nAll: %s--Succ: %s (%s%%)-Fail: %s (%s%%)--%sMb/min' \
                    % (client_time.split('_')[1].upper(), (succ + fail), succ,
                       round(float(succ)/(succ + fail)*100., 1), fail,
                       round(float(fail)/(succ + fail)*100., 1),
                       round(trans_rate, 2))
                plt.title(plt_title, size='x-large')

                if input_dics['req_parallel'] == 'Y':
                    plt.legend([single_succ, parallel_succ],
                               ['Serial', 'Parallel'], loc=4)

                plt.savefig(os.path.join(address_events[i], 'info',
                                         'Data-Time_%s.%s'
                                         % (client_time.split('_')[1],
                                            input_dics['plot_format'])))
