#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  plotting_tools.py
#   Purpose:   Collection of plotting tools
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import fnmatch
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from obspy import read_inventory
try:
    from obspy.signal import pazToFreqResp
except Exception, e:
    from obspy.signal.invsim import paz_to_freq_resp as pazToFreqResp
try:
    from obspy.geodetics import locations2degrees
except Exception, e:
    from obspy.core.util import locations2degrees
from obspy.core import read, UTCDateTime
from obspy.imaging.beachball import Beach
import os
import sys

from event_handler import quake_info
from utility_codes import read_station_event, read_event_dic

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### plot_tools ############################################


def plot_tools(input_dics, clients, all_events=False, all_stations=False):
    """
    Managing the required inputs for plotting tools
    :param input_dics:
    :param clients:
    :return:
    """
    if input_dics['plot_dir'].lower() != 'n':
        events, address_events = quake_info(input_dics['plot_dir'], 'info')
    else:
        sys.exit('ERROR: --plot_dir has not set!')

    ls_saved_stas = []
    ls_add_stas = []
    for i in range(len(events)):
        ls_saved_stas_tmp = []
        ls_add_stas_tmp = []
        sta_ev = read_station_event(address_events[i])
        event_dic = read_event_dic(address_events[i])

        pass_ev = True
        if not all_events:
            pass_ev = plot_filter_event(input_dics, event_dic)
        if not pass_ev:
            continue
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

            pass_sta = True
            if not all_stations:
                pass_sta = plot_filter_station(input_dics, sta_ev[0][j])
            if not pass_sta:
                continue
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
                    if event_dic['focal_mechanism']:
                        station_id.extend(event_dic['focal_mechanism'])
                    else:
                        station_id.extend('False')
                    ls_saved_stas_tmp.append(station_id)
                    ls_add_stas_tmp.append(
                        os.path.join(address_events[i], BH_file,
                                     '%s.%s.%s.%s'
                                     % (network, sta_ev[0][j][1],
                                        sta_ev[0][j][2],
                                        sta_ev[0][j][3])))

            elif input_dics['plot_all'] == 'Y':
                station_id = station_id.split(',')
                if event_dic['focal_mechanism']:
                    station_id.extend(event_dic['focal_mechanism'])
                else:
                    station_id.extend('False')
                ls_saved_stas_tmp.append(station_id)
                ls_add_stas_tmp.append(
                    os.path.join(address_events[i], BH_file,
                                 '%s.%s.%s.%s'
                                 % (network, sta_ev[0][j][1],
                                    sta_ev[0][j][2], sta_ev[0][j][3])))

        ls_saved_stas.append(ls_saved_stas_tmp)
        ls_add_stas.append(ls_add_stas_tmp)

    if input_dics['plot_ray_gmt']:
        plot_ray_gmt(input_dics, ls_saved_stas)
    else:
        for k in ['plot_sta', 'plot_ev', 'plot_ray']:
            if input_dics[k]:
                plot_sta_ev_ray(input_dics, ls_saved_stas)
                break

    if input_dics['plot_epi']:
        plot_epi(input_dics, ls_add_stas, ls_saved_stas)

    if input_dics['plot_dt']:
        plot_dt(input_dics, address_events)

# ##################### plot_filter_event ###############################


def plot_filter_event(input_dics, event_dic):
    """
    check whether the event can pass the criteria
    :param input_dics:
    :param event_dic:
    :return:
    """
    if not event_dic['datetime'] <= UTCDateTime(input_dics['max_date']):
        return False
    if not event_dic['datetime'] >= UTCDateTime(input_dics['min_date']):
        return False
    if not event_dic['magnitude'] <= float(input_dics['max_mag']):
        return False
    if not event_dic['magnitude'] >= float(input_dics['min_mag']):
        return False
    if not event_dic['depth'] <= float(input_dics['max_depth']):
        return False
    if not event_dic['depth'] >= float(input_dics['min_depth']):
        return False
    if isinstance(input_dics['evlatmin'], float):
        if not event_dic['latitude'] <= float(input_dics['evlatmax']):
            return False
        if not event_dic['longitude'] <= float(input_dics['evlonmax']):
            return False
        if not event_dic['latitude'] >= float(input_dics['evlatmin']):
            return False
        if not event_dic['longitude'] >= float(input_dics['evlonmin']):
            return False
    return True

# ##################### plot_filter_station ###############################


def plot_filter_station(input_dics, sta_ev):
    """
    check whether the station can pass the criteria
    :param input_dics:
    :param sta_ev:
    :return:
    """
    if not fnmatch.fnmatch(sta_ev[0], input_dics['net']):
        return False
    if not fnmatch.fnmatch(sta_ev[1], input_dics['sta']):
        return False
    if not fnmatch.fnmatch(sta_ev[2], input_dics['loc']):
        return False
    if not fnmatch.fnmatch(sta_ev[3], input_dics['cha']):
        return False
    if isinstance(input_dics['mlat_rbb'], float):
        if not float(sta_ev[4]) <= input_dics['Mlat_rbb']:
            return False
        if not float(sta_ev[4]) >= input_dics['mlat_rbb']:
            return False
        if not float(sta_ev[5]) <= input_dics['Mlon_rbb']:
            return False
        if not float(sta_ev[5]) >= input_dics['mlon_rbb']:
            return False
    return True

# ##################### plot_sta_ev_ray ###############################


def plot_sta_ev_ray(input_dics, ls_saved_stas):
    """
    Plots stations, events and ray paths on a map with basemap.
    :param input_dics:
    :param ls_saved_stas:
    :return:
    """

    plt.figure(figsize=(20., 10.))
    plt_stations = input_dics['plot_sta']
    plt_events = input_dics['plot_ev']
    plt_ray_path = input_dics['plot_ray']

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

    if plt_ray_path:
        # # hammer, kav7, cyl, mbtfpq, moll
        # m = Basemap(projection='aeqd', lon_0=0, lat_0=0)
        # parallels = np.arange(-90, 90, 30.)
        # m.drawparallels(parallels, color='gray')
        # meridians = np.arange(-180., 180., 60.)
        # m.drawmeridians(meridians, color='gray')
        m = Basemap(projection='robin', lon_0=input_dics['plot_lon0'])
        parallels = np.arange(-90, 90, 30.)
        m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
        meridians = np.arange(-180., 180., 60.)
        m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)
        width_beach = 10e5
        width_station = 50
    elif not glob_map:
        m = Basemap(projection='cyl', llcrnrlat=evlatmin, urcrnrlat=evlatmax,
                    llcrnrlon=evlonmin, urcrnrlon=evlonmax)
        parallels = np.arange(-90, 90, 5.)
        m.drawparallels(parallels, labels=[1, 0, 0, 1], fontsize=12)
        meridians = np.arange(-180., 180., 5.)
        m.drawmeridians(meridians, labels=[1, 0, 0, 1], fontsize=12)
        width_beach = 5
        width_station = 10
    elif glob_map:
        # hammer, kav7, cyl, mbtfpq, moll
        m = Basemap(projection='robin', lon_0=input_dics['plot_lon0'])
        parallels = np.arange(-90, 90, 30.)
        m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
        meridians = np.arange(-180., 180., 60.)
        m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)
        width_beach = 5e5
        width_station = 50
    else:
        sys.exit('ERROR: %s' % input_dics)

    raw_input_resp = raw_input('Choose your map style:\n'
                               '1. Bluemarble (PIL should be installed)\n'
                               '2. Etopo (PIL should be installed)\n'
                               '3. Shaderelief (PIL should be installed)\n'
                               '4. Simple\n')
    if raw_input_resp == '1':
        m.bluemarble(scale=0.5)
    elif raw_input_resp == '2':
        m.etopo(scale=0.5)
    elif raw_input_resp == '3':
        m.shadedrelief(scale=0.1)
    else:
        m.fillcontinents()

    len_src_rcv = 0
    for i in range(len(ls_saved_stas)):
        len_src_rcv += len(ls_saved_stas[i])
    print 'Length src-rcv pairs: %s' % len_src_rcv 
    if plt_events:
        for i in range(len(ls_saved_stas)):
            if input_dics['plot_focal']:
                if ls_saved_stas[i][0][14] == 'F':
                    sys.exit('ERROR:\nMoment tensor does not exists!')
                x, y = m(float(ls_saved_stas[i][0][10]),
                         float(ls_saved_stas[i][0][9]))
                focmecs = [float(ls_saved_stas[i][0][14]),
                           float(ls_saved_stas[i][0][15]),
                           float(ls_saved_stas[i][0][16]),
                           float(ls_saved_stas[i][0][17]),
                           float(ls_saved_stas[i][0][18]),
                           float(ls_saved_stas[i][0][19])]
                ax = plt.gca()
                b = Beach(focmecs, xy=(x, y), facecolor='blue',
                          width=width_beach, linewidth=1, alpha=0.85)
                b.set_zorder(10)
                ax.add_collection(b)
            else:
                x, y = m(float(ls_saved_stas[i][0][10]),
                         float(ls_saved_stas[i][0][9]))
                magnitude = float(ls_saved_stas[i][0][12])
                m.scatter(x, y, color="blue", s=10*magnitude,
                          edgecolors='none', marker="o",
                          zorder=5, alpha=0.65)
    else:
        print 'No events will be plotted.'

    if plt_stations:
        for i in range(len(ls_saved_stas)):
            for j in range(len(ls_saved_stas[i])):
                x, y = m(float(ls_saved_stas[i][j][5]),
                         float(ls_saved_stas[i][j][4]))
                m.scatter(x, y, color='red', s=width_station,
                          edgecolors='none', marker='v',
                          zorder=4, alpha=0.9)
    else:
        print 'No stations will be plotted on your map!'

    if plt_ray_path:
        for i in range(len(ls_saved_stas)):
            print 'Projecting Event: %s/%s' % (i+1, len(ls_saved_stas))
            for j in range(len(ls_saved_stas[i])):
                gcline = m.drawgreatcircle(
                    float(ls_saved_stas[i][j][10]),
                    float(ls_saved_stas[i][j][9]),
                    float(ls_saved_stas[i][j][5]),
                    float(ls_saved_stas[i][j][4]),
                    color='k', alpha=0.0)
                gcx, gcy = gcline[0].get_data()
                gcx_diff = gcx[0:-1] - gcx[1:]
                gcy_diff = gcy[0:-1] - gcy[1:]
                if np.max(abs(gcx_diff))/abs(gcx_diff[0]) > 300:
                    gcx_max_arg = abs(gcx_diff).argmax()
                    plt.plot(gcx[0:gcx_max_arg], gcy[0:gcx_max_arg],
                             color='k', alpha=0.1)
                    plt.plot(gcx[gcx_max_arg+1:], gcy[gcx_max_arg+1:],
                             color='k', alpha=0.1)
                elif np.max(abs(gcy_diff))/abs(gcy_diff[0]) > 400:
                    gcy_max_arg = abs(gcy_diff).argmax()
                    plt.plot(gcy[0:gcy_max_arg], gcy[0:gcy_max_arg],
                             color='k', alpha=0.1)
                    plt.plot(gcy[gcy_max_arg+1:], gcy[gcy_max_arg+1:],
                             color='k', alpha=0.1)
                else:
                    m.drawgreatcircle(
                        float(ls_saved_stas[i][j][10]),
                        float(ls_saved_stas[i][j][9]),
                        float(ls_saved_stas[i][j][5]),
                        float(ls_saved_stas[i][j][4]),
                        color='k', alpha=0.1)
    else:
        print 'No rays path will be plotted on your map!'

    plt.savefig(os.path.join(input_dics['plot_save'],
                             'ev_sta_ray.%s' % input_dics['plot_format']))
    plt.show()

# ##################### plot_ray_gmt ####################################


def plot_ray_gmt(input_dics, ls_saved_stas):
    """
    Plot: stations, events and ray paths for the specified directory using GMT
    :param input_dics:
    :param ls_saved_stas:
    :return:
    """
    if input_dics['plot_focal']:
        with open('./gmt_psmeca.txt', 'w') as outfile:
            outfile.write('lon lat depth mrr mtt mpp mrt mrp mtp iexp name \n')
            for i in range(len(ls_saved_stas)):
                if not ls_saved_stas[i][0][14]:
                    sys.exit('ERROR:\nMoment tensor does not exists!')
                ev_lon = ls_saved_stas[i][0][10]
                ev_lat = ls_saved_stas[i][0][9]
                ev_dep = ls_saved_stas[i][0][11]
                ev_mrr = float(ls_saved_stas[i][0][14])
                ev_mtt = float(ls_saved_stas[i][0][15])
                ev_mpp = float(ls_saved_stas[i][0][16])
                ev_mrt = float(ls_saved_stas[i][0][17])
                ev_mrp = float(ls_saved_stas[i][0][18])
                ev_mtp = float(ls_saved_stas[i][0][19])

                scalar_moment = np.sqrt(np.power(ev_mrr, 2) +
                                        np.power(ev_mtt, 2) +
                                        np.power(ev_mpp, 2) +
                                        np.power(ev_mrt, 2) +
                                        np.power(ev_mrp, 2) +
                                        np.power(ev_mtp, 2))/np.sqrt(2)

                ev_mom_max = max(abs(ev_mrr),
                                 abs(ev_mtt),
                                 abs(ev_mpp),
                                 abs(ev_mrt),
                                 abs(ev_mrp),
                                 abs(ev_mtp))
                ev_mrr_fl = format(ev_mrr/ev_mom_max, 'f')
                ev_mtt_fl = format(ev_mtt/ev_mom_max, 'f')
                ev_mpp_fl = format(ev_mpp/ev_mom_max, 'f')
                ev_mrt_fl = format(ev_mrt/ev_mom_max, 'f')
                ev_mrp_fl = format(ev_mrp/ev_mom_max, 'f')
                ev_mtp_fl = format(ev_mtp/ev_mom_max, 'f')

                outfile.write('%s  %s  %s  %s  %s  %s  %s  %s  %s  %s\n'
                              % (ev_lon, ev_lat, ev_dep,
                                 ev_mrr_fl,
                                 ev_mtt_fl,
                                 ev_mpp_fl,
                                 ev_mrt_fl,
                                 ev_mrp_fl,
                                 ev_mtp_fl,
                                 str(scalar_moment).split('e')[1][1:]))
    else:
        with open('./gmt_events.txt', 'w') as outfile:
            for i in range(len(ls_saved_stas)):
                ev_lon = ls_saved_stas[i][0][10]
                ev_lat = ls_saved_stas[i][0][9]
                outfile.write('%s   %s \n' % (ev_lon, ev_lat))
    outfile.close()

    with open('./gmt_sta_ev_path.txt', 'w') as outfile:
        for i in range(len(ls_saved_stas)):
            for j in range(len(ls_saved_stas[i])):
                ev_lon = ls_saved_stas[i][j][10]
                ev_lat = ls_saved_stas[i][j][9]
                sta_lon = ls_saved_stas[i][j][5]
                sta_lat = ls_saved_stas[i][j][4]
                outfile.write('%s   %s \n %s   %s\n'
                              % (ev_lon, ev_lat,
                                 sta_lon, sta_lat))
    outfile.close()

    with open('./gmt_station.txt', 'w') as outfile:
        for i in range(len(ls_saved_stas)):
            for j in range(len(ls_saved_stas[i])):
                sta_lon = ls_saved_stas[i][j][5]
                sta_lat = ls_saved_stas[i][j][4]
                outfile.write('%s   %s \n' % (sta_lon, sta_lat))
    outfile.close()

    # GMT part:
    os.system('psbasemap -Rd -JK180/9i -B45g30 -K -Xc -Yc> gmt_output.ps')

    os.system('pscoast -Rd -JK180/9i -B45g30:."World-wide Ray Path Coverage": '
              '-Dc -A1000 -Glightgray -Wthinnest -t0 -O -K >> gmt_output.ps')

    os.system('psxy ./gmt_sta_ev_path.txt -JK180/9i -Rd -O -K -W0.1,'
              'black -t20  >> gmt_output.ps')
    os.system('psxy ./gmt_station.txt -JK180/9i -Rd -Si0.2c -GRed -O -K >> '
              'gmt_output.ps')
    if input_dics['plot_focal']:
        os.system('psmeca gmt_psmeca.txt -h1 -JK180/9i -Rd -W1 -GBlue '
                  '-Sd1.0  -O >> gmt_output.ps')
    else:
        os.system('psxy ./gmt_events.txt -JK180/9i -Rd -Sc0.2c '
                  '-GBlue -O >> gmt_output.ps')

    os.system('ps2raster gmt_output.ps -A -P -Tf')

    os.system('mv gmt_output.ps ray_coverage_gmt.ps')
    os.system('mv gmt_output.pdf ray_coverage_gmt.pdf')

    os.system('xdg-open ray_coverage_gmt.pdf')

# ##################### plot_epi ########################################


def plot_epi(input_dics, ls_add_stas, ls_saved_stas):
    """
    Plot arranged waveforms by epicentral distance versus time
    :param input_dics:
    :param ls_add_stas:
    :param ls_saved_stas:
    :return:
    """

    for target in range(len(ls_add_stas)):
        plt.clf()
        plt.figure(figsize=(20., 10.))

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
                        color='black', lw=2)
            except Exception as e:
                print 'WARNING: %s' % e
                pass
            plt.xlabel('Time (sec)', size=24, weight='bold')
            plt.ylabel('Epicentral distance (deg)', size=24, weight='bold')
            plt.xticks(size=18, weight='bold')
            plt.yticks(size=18, weight='bold')

        print os.path.join(input_dics['plot_save'],
                           'epi_time_%s.%s'
                           % (ls_saved_stas[target][0][8],
                              input_dics['plot_format']))
        plt.savefig(os.path.join(input_dics['plot_save'],
                                 'epi_time_%s.%s'
                                 % (ls_saved_stas[target][0][8],
                                    input_dics['plot_format'])))

# ##################### plot_xml_response ###############################


def plot_xml_response(input_dics):
    """
    This function plots the response file of stationXML file(s)
    It has several modes such as:
    plotting all the stages
    plotting full response file
    plotting selected stages
    plotting only PAZ
    :param input_dics: input dictionary.
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
        except Exception, e:
            print 'ERROR: %s' % e
            sys.exit('[ERROR] wrong address: %s' % stxml_dir)

    addxml_all.sort()

    sta_lat = []
    sta_lon = []
    latlon_color = []
    report_fio = open(os.path.join('./stationxml_plots', 'report_stationxml'),
                      'w')
    report_fio.writelines('channel_id\t\t\t\t%(Phase)\t\t'
                          'Max Diff(abs) \tLat\t\t\tLon\t\t\tDatetime\t'
                          'decimation delay\tdecimation correction\n')
    report_fio.close()
    add_counter = 0
    for addxml in addxml_all:
        end_stage = end_stage_input
        add_counter += 1
        print 40*'-'
        print '%s/%s' % (add_counter, len(addxml_all))
        try:
            xml_inv = read_inventory(addxml, format='stationXML')
            print "[STATIONXML] %s" % addxml
            # we only take into account the first channel...
            cha_name = xml_inv.get_contents()['channels'][0]
            if plotxml_datetime:
                cha_date = plotxml_datetime
            else:
                cha_date = xml_inv.networks[0][0][-1].start_date
                print '[INFO] plotxml_date has not been set, the start_date ' \
                      'of the last channel in stationXML file will be used ' \
                      'instead: %s' % cha_date

            xml_response = xml_inv.get_response(cha_name, cha_date + 0.1)
            if xml_inv[0][0][0].sample_rate:
                sampling_rate = xml_inv[0][0][0].sample_rate
            else:
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
                    ax_222 = plt.subplot(2, 2, 2)
                    if plotstage12:
                        plt.loglog(freq, abs(abs(cpx_response) - abs(cpx_12)),
                                   '--', color='black', lw=3,
                                   label='|full-resp - Stage1,2|')
                    amp_ratio = 1
                    if plotpaz:
                        amp_ratio = abs(abs(cpx_response) /
                                        (abs(h)*paz['sensitivity']))
                        plt.loglog(f, amp_ratio,
                                   color='red', lw=3,
                                   label='|full-resp|/|PAZ|')
                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                    plt.ylabel('Amplitude ratio', size=24, weight='bold')
                    plt.xticks(size=18, weight='bold')
                    plt.yticks(size=18, weight='bold')
                    plt.xlim(xmin=min_freq, xmax=nyquist+5)
                    plt.ylim(ymax=1.2*max(amp_ratio[np.logical_not(
                        np.isnan(amp_ratio))]))
                    plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                    plt.grid()

                    ax_224 = plt.subplot(2, 2, 4)
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
                    plt.ylabel('Phase difference [rad]',
                               size=24, weight='bold')
                    plt.xticks(size=18, weight='bold')
                    plt.yticks(size=18, weight='bold')
                    plt.xlim(xmin=min_freq, xmax=nyquist+5)
                    plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
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
                sys.exit('Lengths of phase responses do not match: '
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
            report_fio = open(os.path.join('./stationxml_plots',
                                           'report_stationxml'), 'a')
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
        except Exception, e:
            print 'Exception: %s' % e

    if plot_map_compare:
        plt.figure()
        m = Basemap(projection='robin', lon_0=input_dics['plot_lon0'], lat_0=0)
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
        except Exception as e:
            pass
        if resp_stage.decimation_delay:
            decimation_delay.append(resp_stage.decimation_delay)
        if resp_stage.decimation_correction:
            decimation_correction.append(resp_stage.decimation_correction)

    if len(poles) > 1:
        print 'WARNING: More than one group of poles was found: %s' % poles
    if len(zeros) > 1:
        print 'WARNING: More than one group of zeros was found: %s' % zeros

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

    paz = {'poles': poles}

    input_units = xml_response.response_stages[0].input_units
    if not input_units.lower() in ['m', 'm/s', 'm/s**2', 'pa']:
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
    paz['zeros'] = zeros
    paz['gain'] = normalization_factor
    paz['sensitivity'] = np.prod(np.array(gain_arr))
    print 'Final PAZ:'
    print paz
    return paz, decimation_delay, decimation_correction

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
        map_proj = 'cyl'
    else:
        map_proj = 'cyl'

    # Set-up the map
    m = Basemap(projection=map_proj,
                llcrnrlat=input_dics['evlatmin'],
                urcrnrlat=input_dics['evlatmax'],
                llcrnrlon=input_dics['evlonmin'],
                urcrnrlon=input_dics['evlonmax'],
                lon_0=input_dics['plot_lon0'],
                resolution='l')
    parallels = np.arange(-90, 90, 30.)
    m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
    meridians = np.arange(-180., 180., 60.)
    m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)

    raw_input_resp = raw_input('Choose your map style:\n'
                               '1. Bluemarble (PIL should be installed)\n'
                               '2. Etopo (PIL should be installed)\n'
                               '3. Shaderelief (PIL should be installed)\n'
                               '4. Simple\n')
    if raw_input_resp == '1':
        m.bluemarble(scale=0.5)
    elif raw_input_resp == '2':
        m.etopo(scale=0.5)
    elif raw_input_resp == '3':
        m.shadedrelief(scale=0.1)
    else:
        m.fillcontinents()

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

    if np.shape(ev_info_ar)[0] == np.size(ev_info_ar):
        ev_info_ar = np.reshape(ev_info_ar, (1, 11))
    else:
        ev_info_ar = sorted(ev_info_ar,
                            key=lambda ev_info_iter: float(ev_info_iter[0]))

    for ev in ev_info_ar:
        m.scatter(float(ev[1]), float(ev[2]), float(ev[3]),
                  color=ev[4], marker="o", edgecolor=None, zorder=10)

    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

    if plot_focal_mechanism:
        plt.figure()
        # Set-up the map
        m = Basemap(projection=map_proj,
                    llcrnrlat=input_dics['evlatmin'],
                    urcrnrlat=input_dics['evlatmax'],
                    llcrnrlon=input_dics['evlonmin'],
                    urcrnrlon=input_dics['evlonmax'],
                    lon_0=input_dics['plot_lon0'],
                    resolution='l')
        parallels = np.arange(-90, 90, 30.)
        m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
        meridians = np.arange(-180., 180., 60.)
        m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)
        if raw_input_resp == '1':
            m.bluemarble(scale=0.5)
        elif raw_input_resp == '2':
            m.etopo(scale=0.5)
        elif raw_input_resp == '3':
            m.shadedrelief(scale=0.1)
        else:
            m.fillcontinents()
        for evfoc in ev_info_ar:
            try:
                ax = plt.gca()
                focmec = (float(evfoc[5]), float(evfoc[6]), float(evfoc[7]),
                          float(evfoc[8]), float(evfoc[9]), float(evfoc[10]))
                b = Beach(focmec, xy=(float(evfoc[1]), float(evfoc[2])),
                          facecolor=evfoc[4], width=float(evfoc[3])/100.,
                          linewidth=1, alpha=0.85)
                b.set_zorder(10)
                ax.add_collection(b)
            except Exception, e:
                print 'EXCEPTION: %s' % e
                print 'Focal Mechanism:'
                print focmec
                print '----------------'

    if not len(ev_dp_all) <= 1:
        plt.figure()
        plt.hist(ev_dp_all, input_dics['depth_bins_seismicity'],
                 facecolor='green', alpha=0.75, log=True,
                 histtype='stepfilled')
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
                 facecolor='green', alpha=0.75, log=True,
                 histtype='stepfilled')
        plt.xlabel('Magnitude', size=24, weight='bold')
        plt.ylabel('#Events (log)', size=24, weight='bold')
        plt.yscale('log')
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.tight_layout()

    plt.show()

# ##################### plot_dt #########################################


def plot_dt(input_dics, address_events):
    """
    Plot stored Data(MB) as a function of Time(Sec)
    :param input_dics:
    :param address_events:
    :return:
    """

    single_succ = None
    parallel_succ = None
    for i in range(len(address_events)):
        for client_time in ['time_fdsn', 'time_arc']:
            print 'Event address: %s' % address_events[i]
            if os.path.isfile(os.path.join(address_events[i],
                                           'info',
                                           client_time)):
                plt.clf()
                dt_open = open(os.path.join(address_events[i],
                                            'info',
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
                    time_single += eval(dt_read[k][4]) + \
                                   eval(dt_read[k][5])/1.e6
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
                        eval(rep_par_read[4].split(',')[1])/1.e6
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
                plt.plot(time_array, poly(time_array), 'k--')

                trans_rate = (poly(time_array[-1]) - poly(time_array[0])) / \
                             (time_array[-1]-time_array[0])

                plt.xlabel('Time (sec)', size='large', weight='bold')
                plt.ylabel('Stored Data (MB)', size='large', weight='bold')
                plt.xticks(size='large', weight='bold')
                plt.yticks(size='large', weight='bold')
                plt_title = \
                    '%s\nAll: %s--Succ: %s (%s%%)-Fail: %s (%s%%)--%sMB/sec' \
                    % (client_time.split('_')[1].upper(), (succ + fail), succ,
                       round(float(succ)/(succ + fail)*100., 1), fail,
                       round(float(fail)/(succ + fail)*100., 1),
                       round(trans_rate, 2))
                plt.title(plt_title, size='x-large')

                if input_dics['req_parallel'] == 'Y':
                    plt.legend([single_succ, parallel_succ],
                               ['Serial', 'Parallel'], loc=4)

                plt.savefig(
                    os.path.join('data-time_%s_%s.%s'
                                 % (client_time.split('_')[1],
                                    os.path.basename(address_events[i]),
                                    input_dics['plot_format'])))
