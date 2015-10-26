#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  local_handler.py
#   Purpose:   handling local processing/plotting in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import multiprocessing
import numpy as np
from obspy.imaging.beachball import Beach
from obspy import UTCDateTime, read
try:
    from obspy.geodetics import locations2degrees
except:
    from obspy.core.util import locations2degrees
try:
    from obspy.geodetics.base import gps2dist_azimuth as gps2DistAzimuth
except:
    try:
        from obspy.geodetics import gps2DistAzimuth
    except:
        from obspy.core.util import gps2DistAzimuth
import os
import sys

from .data_handler import update_sta_ev_file
from .kml_handler import create_ev_sta_kml
from process_unit import process_unit
from .utility_codes import locate, check_par_jobs, plot_filter_station

# ###################### process_data #########################################


def process_data(input_dics, event):
    """
    prepare the target directories and pass them to process_serial_parallel
    :param input_dics:
    :param event:
    :return:
    """
    target_path = locate(input_dics['datapath'], event['event_id'])
    if len(target_path) > 1:
        print("[LOCAL] more than one path was found for one event:")
        print(target_path)
        print("use the first one:")
        target_path = target_path[0]
        print(target_path)
    else:
        print("[LOCAL] Path:")
        target_path = target_path[0]
        print(target_path)
    print("[INFO] update station_event file...")
    update_sta_ev_file(target_path)
    sta_ev_arr = np.loadtxt(os.path.join(target_path, 'info', 'station_event'),
                            delimiter=',', dtype='object')
    if len(sta_ev_arr) > 0:
        process_serial_parallel(sta_ev_arr, input_dics, target_path)
    else:
        print("[LOCAL] no waveform to process for %s!" % target_path)

# ###################### process_serial_parallel ##############################


def process_serial_parallel(sta_ev_arr, input_dics, target_path):
    """
    run the processing unit in parallel or in serial
    :param sta_ev_arr:
    :param input_dics:
    :param target_path:
    :return:
    """
    if input_dics['parallel_process']:
        start = 0
        end = int(len(sta_ev_arr))
        step = (end - start) / input_dics['process_np'] + 1
        step = int(step)

        jobs = []
        for index in xrange(input_dics['process_np']):
            starti = start + index * step
            endi = min(start + (index + 1) * step, end)
            p = multiprocessing.Process(target=process_core_iterate,
                                        args=(sta_ev_arr, input_dics,
                                              target_path,
                                              starti, endi))
            jobs.append(p)
        for i in range(len(jobs)):
            jobs[i].start()
        check_par_jobs(jobs)

    else:
        process_core_iterate(sta_ev_arr, input_dics, target_path,
                             0, len(sta_ev_arr))

# ###################### process_core_iterate #################################


def process_core_iterate(sta_ev_arr, input_dics, target_path, starti, endi):
    """
    running the process_unit for starti and endi defined by
    either serial or parallel mode
    :param sta_ev_arr:
    :param input_dics:
    :param target_path:
    :param starti:
    :param endi:
    :return:
    """
    for i in range(starti, endi):
        staev_ar = sta_ev_arr[i]
        station_id = '%s.%s.%s.%s' % (staev_ar[0], staev_ar[1],
                                      staev_ar[2], staev_ar[3])
        tr_add = os.path.join(target_path, 'raw', station_id)
        data_source = staev_ar[8]
        if input_dics['pre_process']:
            process_unit(tr_add, target_path, input_dics, staev_ar)

# ###################### plot_unit ############################################


def plot_unit(input_dics, events):
    """
    this function re-direct the flow to the relevant plotting function
    :param input_dics:
    :param events:
    :return:
    """
    del_index = []
    for ev in range(len(events)):
        if not plot_filter_event(input_dics, events[ev]):
            del_index.append(ev)
    del_index.sort(reverse=True)
    for di in del_index:
        del events[di]
    if input_dics['create_kml']:
        create_ev_sta_kml(input_dics, events)
    if input_dics['plot_seismicity']:
        plot_seismicity(input_dics, events)
    if input_dics['plot_ev'] or input_dics['plot_sta'] or \
            input_dics['plot_availability'] or input_dics['plot_ray']:
        plot_sta_ev_ray(input_dics, events)
    if input_dics['plot_waveform']:
        plot_waveform(input_dics, events)

# ##################### plot_filter_event #####################################


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
    if not event_dic['magnitude'] < 0:
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

# ##################### plot_waveform #########################################


def plot_waveform(input_dics, events):
    """
    plot waveforms arranged by the epicentral distance
    :param input_dics:
    :param events:
    :return:
    """
    try:
        plt.style.use('ggplot')
    except Exception, error:
        print("[WARNING] %s" % error)
    for ei in range(len(events)):
        target_path = locate(input_dics['datapath'], events[ei]['event_id'])
        if len(target_path) > 1:
            print("[LOCAL] more than one path was found for the event:")
            print(target_path)
            print("[INFO] use the first one:")
            target_path = target_path[0]
            print(target_path)
        else:
            print("[LOCAL] Path:")
            target_path = target_path[0]
            print(target_path)

        update_sta_ev_file(target_path)
        sta_ev_arr = np.loadtxt(
            os.path.join(target_path, 'info', 'station_event'),
            delimiter=',', dtype='object')
        del_index = []
        for sti in range(len(sta_ev_arr)):
            if not plot_filter_station(input_dics, sta_ev_arr[sti]):
                del_index.append(sti)
        del_index.sort(reverse=True)
        for di in del_index:
            sta_ev_arr[di] = np.delete(sta_ev_arr, (di), axis=0)

        for si in range(len(sta_ev_arr)):
            sta_id = sta_ev_arr[si, 0] + '.' + sta_ev_arr[si, 1] + '.' + \
                     sta_ev_arr[si, 2] + '.' + sta_ev_arr[si, 3]
            try:
                tr = read(os.path.join(target_path,
                                       input_dics['plot_dir_name'],
                                       sta_id))[0]
                time_diff = tr.stats.starttime - events[ei]['datetime']
                taxis = tr.times() + time_diff

                dist, azi, bazi = gps2DistAzimuth(events[ei]['latitude'],
                                                  events[ei]['longitude'],
                                                  float(sta_ev_arr[si, 4]),
                                                  float(sta_ev_arr[si, 5]))
                epi_dist = dist/111.194/1000.
                if input_dics['min_azi'] or input_dics['max_azi'] or \
                        input_dics['min_epi'] or input_dics['max_epi']:
                    if input_dics['min_epi']:
                        if epi_dist < input_dics['min_epi']:
                            continue
                    if input_dics['max_epi']:
                        if epi_dist > input_dics['max_epi']:
                            continue
                    if input_dics['min_azi']:
                        if azi < input_dics['min_azi']:
                            continue
                    if input_dics['max_azi']:
                        if azi > input_dics['max_azi']:
                            continue
                plt.plot(taxis, tr.normalize().data + epi_dist, c='k',
                         alpha=0.5)
            except:
                continue

    plt.xlabel('Time (sec)', size=18, weight='bold')
    plt.ylabel('Epicentral Distance (deg)', size=18, weight='bold')
    plt.xticks(size=18, weight='bold')
    plt.yticks(size=18, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(input_dics['plot_save'],
                             'waveforms.%s' % input_dics['plot_format']))
    plt.show()

# ##################### plot_sta_ev_ray ###############################


def plot_sta_ev_ray(input_dics, events):
    """
    plot stations, events and ray paths on a map using basemap.
    :param input_dics:
    :param events:
    :return:
    """
    plt.figure(figsize=(20., 10.))
    plt_stations = input_dics['plot_sta']
    plt_availability = input_dics['plot_availability']
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
        m = Basemap(projection='robin', lon_0=input_dics['plot_lon0'])
        parallels = np.arange(-90, 90, 30.)
        m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
        meridians = np.arange(-180., 180., 60.)
        m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)
        width_beach = 5e5
        width_station = 50
    else:
        sys.exit('[ERROR] can not continue, error:\n%s' % input_dics)

    raw_input_resp = raw_input('choose the map style:\n'
                               '1. bluemarble (PIL should be installed)\n'
                               '2. etopo (PIL should be installed)\n'
                               '3. shaderelief (PIL should be installed)\n'
                               '4. simple\n')
    if int(raw_input_resp) == 1:
        m.bluemarble(scale=0.5)
    elif int(raw_input_resp) == 2:
        m.etopo(scale=0.5)
    elif int(raw_input_resp) == 3:
        m.shadedrelief(scale=0.1)
    else:
        m.fillcontinents()

    for ei in range(len(events)):
        if plt_events:
            if input_dics['plot_focal']:
                if not events[ei]['focal_mechanism']:
                    sys.exit('[ERROR] moment tensor does not exist!')
                x, y = m(events[ei]['longitude'],
                         events[ei]['latitude'])
                focmecs = [float(events[ei]['focal_mechanism'][0]),
                           float(events[ei]['focal_mechanism'][1]),
                           float(events[ei]['focal_mechanism'][2]),
                           float(events[ei]['focal_mechanism'][3]),
                           float(events[ei]['focal_mechanism'][4]),
                           float(events[ei]['focal_mechanism'][5])]
                ax = plt.gca()
                b = Beach(focmecs, xy=(x, y), facecolor='blue',
                          width=width_beach, linewidth=1, alpha=0.85)
                b.set_zorder(10)
                ax.add_collection(b)
            else:
                x, y = m(events[ei]['longitude'],
                         events[ei]['latitude'])
                magnitude = float(events[ei]['magnitude'])
                m.scatter(x, y, color="blue", s=10*magnitude,
                          edgecolors='none', marker="o",
                          zorder=5, alpha=0.65)
        if plt_stations or plt_availability or plt_ray_path:
            target_path = locate(input_dics['datapath'],
                                 events[ei]['event_id'])
            if len(target_path) > 1:
                print("[LOCAL] more than one path was found for the event:")
                print(target_path)
                print("[INFO] use the first one:")
                target_path = target_path[0]
                print(target_path)
            else:
                print("[LOCAL] Path:")
                target_path = target_path[0]
                print(target_path)

            update_sta_ev_file(target_path)
            if not input_dics['plot_availability']:
                sta_ev_arr = np.loadtxt(os.path.join(target_path,
                                                     'info', 'station_event'),
                                        delimiter=',', dtype='object')
            else:
                sta_ev_arr = np.loadtxt(os.path.join(target_path,
                                                     'info',
                                                     'availability.txt'),
                                        delimiter=',', dtype='object')

            if events[ei]['magnitude'] > 0:
                del_index = []
                for sti in range(len(sta_ev_arr)):

                    if not plot_filter_station(input_dics, sta_ev_arr[sti]):
                        del_index.append(sti)

                    dist, azi, bazi = gps2DistAzimuth(
                        events[ei]['latitude'],
                        events[ei]['longitude'],
                        float(sta_ev_arr[sti, 4]),
                        float(sta_ev_arr[sti, 5]))

                    epi_dist = dist/111.194/1000.
                    if input_dics['min_azi'] or input_dics['max_azi'] or \
                            input_dics['min_epi'] or input_dics['max_epi']:
                        if input_dics['min_epi']:
                            if epi_dist < input_dics['min_epi']:
                                del_index.append(sti)
                        if input_dics['max_epi']:
                            if epi_dist > input_dics['max_epi']:
                                del_index.append(sti)
                        if input_dics['min_azi']:
                            if azi < input_dics['min_azi']:
                                del_index.append(sti)
                        if input_dics['max_azi']:
                            if azi > input_dics['max_azi']:
                                del_index.append(sti)

                del_index = list(set(del_index))
                del_index.sort(reverse=True)
                for di in del_index:
                    sta_ev_arr = np.delete(sta_ev_arr, (di), axis=0)

        if plt_stations or plt_availability:
            if len(sta_ev_arr) > 0:
                x, y = m(sta_ev_arr[:, 5], sta_ev_arr[:, 4])
                m.scatter(x, y, color='red', s=width_station,
                          edgecolors='none', marker='v',
                          zorder=4, alpha=0.9)

        if plt_ray_path:
            for si in range(len(sta_ev_arr)):
                gcline = m.drawgreatcircle(float(events[ei]['longitude']),
                                           float(events[ei]['latitude']),
                                           float(sta_ev_arr[si][5]),
                                           float(sta_ev_arr[si][4]),
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
                    m.drawgreatcircle(float(events[ei]['longitude']),
                                      float(events[ei]['latitude']),
                                      float(sta_ev_arr[si][5]),
                                      float(sta_ev_arr[si][4]),
                                      color='k', alpha=0.1)

    plt.savefig(os.path.join(input_dics['plot_save'],
                             'event_station.%s' % input_dics['plot_format']))
    plt.show()

# ##################### plot_seismicity #######################################


def plot_seismicity(input_dics, events):
    """
    create a seismicity map with some basic statistical analysis on the results
    :param input_dics:
    :param events:
    :return:
    """
    print('\n==============')
    print('Seismicity map')
    print('==============\n')

    if not len(events) > 0:
        print("[WARNING] no event passed the given criteria!")
        print("[WARNING] can not create any seismicity map.")
        return

    if input_dics['evlatmin'] is None:
        input_dics['evlatmin'] = -90
        input_dics['evlatmax'] = +90
        input_dics['evlonmin'] = -180
        input_dics['evlonmax'] = +180
        map_proj = 'cyl'
    else:
        map_proj = 'cyl'

    # set-up the map
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

    raw_input_resp = raw_input('choose the map style:\n'
                               '1. bluemarble (PIL should be installed)\n'
                               '2. etopo (PIL should be installed)\n'
                               '3. shaderelief (PIL should be installed)\n'
                               '4. simple\n')
    if int(raw_input_resp) == 1:
        m.bluemarble(scale=0.5)
    elif int(raw_input_resp) == 2:
        m.etopo(scale=0.5)
    elif int(raw_input_resp) == 3:
        m.shadedrelief(scale=0.1)
    else:
        m.fillcontinents()

    # defining labels
    x_ev, y_ev = m(-360, 0)
    m.scatter(x_ev, y_ev, 20, color='red', marker="o",
              edgecolor="black", zorder=10, label='0-70km')
    m.scatter(x_ev, y_ev, 20, color='green', marker="o",
              edgecolor="black", zorder=10, label='70-300km')
    m.scatter(x_ev, y_ev, 20, color='blue', marker="o",
              edgecolor="black", zorder=10, label='300< km')

    m.scatter(x_ev, y_ev, 10, color='white', marker="o",
              edgecolor="black", zorder=10, label='< 4.0')
    m.scatter(x_ev, y_ev, 40, color='white', marker="o",
              edgecolor="black", zorder=10, label='4.0-5.0')
    m.scatter(x_ev, y_ev, 70, color='white', marker="o",
              edgecolor="black", zorder=10, label='5.0-6.0')
    m.scatter(x_ev, y_ev, 100, color='white', marker="o",
              edgecolor="black", zorder=10, label='6.0<=')

    ev_dp_all = []
    ev_mag_all = []
    ev_info_ar = np.array([])
    plot_focal_mechanism = False
    for ev in events:
        x_ev, y_ev = m(float(ev['longitude']), float(ev['latitude']))
        ev_dp_all.append(abs(float(ev['depth'])))
        ev_mag_all.append(abs(float(ev['magnitude'])))

        if abs(float(ev['depth'])) < 70.0:
            color = 'red'
        elif 70.0 <= abs(float(ev['depth'])) < 300.0:
            color = 'green'
        elif 300.0 <= abs(float(ev['depth'])):
            color = 'blue'

        if float(ev['magnitude']) < 4.0:
            size = 10
        elif 4.0 <= float(ev['magnitude']) < 5.0:
            size = 40
        elif 5.0 <= float(ev['magnitude']) < 6.0:
            size = 70
        elif 6.0 <= float(ev['magnitude']):
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

        if int(raw_input_resp) == 1:
            m.bluemarble(scale=0.5)
        elif int(raw_input_resp) == 2:
            m.etopo(scale=0.5)
        elif int(raw_input_resp) == 3:
            m.shadedrelief(scale=0.1)
        else:
            m.fillcontinents()

        for evfoc in ev_info_ar:
            focmec = False
            try:
                ax = plt.gca()
                focmec = (float(evfoc[5]), float(evfoc[6]), float(evfoc[7]),
                          float(evfoc[8]), float(evfoc[9]), float(evfoc[10]))
                b = Beach(focmec, xy=(float(evfoc[1]), float(evfoc[2])),
                          facecolor=evfoc[4], width=float(evfoc[3])/100.,
                          linewidth=1, alpha=0.85)
                b.set_zorder(10)
                ax.add_collection(b)
            except Exception, error:
                print('[EXCEPTION] focal mechanism:')
                print(focmec)
                print('[EXCEPTION] error: %s' % error)

    if len(events) > 0:
        try:
            plt.style.use('ggplot')
        except Exception, error:
            print("[WARNING] %s" % error)
        plt.figure()
        plt.hist(ev_dp_all, input_dics['depth_bins_seismicity'],
                 alpha=0.75, log=True,
                 histtype='stepfilled')

        plt.xlabel('Depth', size=18, weight='bold')
        plt.ylabel('#Events (log)', size=18, weight='bold')
        plt.yscale('log')
        plt.ylim(ymin=0.2)
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.tight_layout()

        plt.figure()
        plt.hist(ev_mag_all,
                 bins=np.linspace(int(float(input_dics['min_mag'])),
                                  int(float(input_dics['max_mag'])),
                                  (int(float(input_dics['max_mag'])) -
                                  int(float(input_dics['min_mag'])))*2+1),
                 alpha=0.75, log=True,
                 histtype='stepfilled')
        plt.xlabel('Magnitude', size=18, weight='bold')
        plt.ylabel('#Events (log)', size=18, weight='bold')
        plt.yscale('log')
        plt.ylim(ymin=0.2)
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.tight_layout()

    plt.show()
