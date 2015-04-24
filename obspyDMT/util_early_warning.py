#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  util_early_warning.py
#   Purpose:   utility codes for early_warning.py
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from obspy import UTCDateTime
from obspy import read
try:
    from obspy.geodetics import locations2degrees
except Exception, e:
    from obspy.core.util import locations2degrees
from obspy.taup import getTravelTimes
from obspy.taup import tau
import os
import time

from utils.utility_codes import read_station_event

# ##################### output_printer ##################################


def output_printer(ev):
    """
    Print event information
    :param ev:
    :return:
    """
    print "\n======================"
    print "event resource: %s" % ev.resource_id
    print "Time: %s" % ev.preferred_origin().time
    print "Magnitude: %s%s" % (ev.preferred_magnitude().mag,
                               ev.preferred_magnitude().magnitude_type)
    print "Lat: %s" % ev.preferred_origin().latitude
    print "Lon: %s" % ev.preferred_origin().longitude
    print "Depth: %s" % ev.preferred_origin().depth

# ##################### create_dmt_commands ##################################


def create_dmt_commands(passed_events, resources_id, resources_done,
                        all_events, waveform_length, min_req_stations,
                        client_fdsn):
    """
    Create obspyDMT command line
    :param passed_events:
    :param resources_id:
    :param resources_done:
    :param all_events:
    :param waveform_length:
    :param min_req_stations:
    :param client_fdsn:
    :return:
    """
    for i in range(len(passed_events)):
        ev = passed_events[i]
        if ev.resource_id.id not in resources_id:
            resources_id.append(ev.resource_id.id)
            resources_done.append(False)
            all_events.append(ev)

    dmt_commands = []
    for i in range(len(resources_id)):
        ev = all_events[i]
        sta_fdsn = []
        if resources_done[i]:
            continue
        ev_datetime = UTCDateTime(ev.preferred_origin().time)
        output_printer(ev)
        print 'time since event: %s' % (time.time() - ev_datetime.timestamp)
        if (time.time() - ev_datetime.timestamp) < waveform_length:
            print '[INFO] required wave-length %s is not satisfied!' \
                  % waveform_length
            continue
        ev_id = str(ev_datetime).replace('-', '_').replace(':', '_').\
            replace('.', '_')
        ev_id = ev_id.split('Z')[0]
        ev_id = ev_id + '_' + str(i)
        available = client_fdsn.get_stations(
            network='_GSN',
            station='*',
            location='*',
            channel='BHZ',
            starttime=ev_datetime,
            endtime=ev_datetime+waveform_length,
            latitude=ev.preferred_origin().latitude,
            longitude=ev.preferred_origin().longitude,
            minradius=0.,
            maxradius=90.,
            level='channel')
        for network in available.networks:
            for station in network:
                for channel in station:
                    sta_fdsn.append([network.code, station.code,
                                     channel.location_code, channel.code,
                                     channel.latitude, channel.longitude,
                                     channel.elevation, channel.depth])
        print "[INFO] number of available stations: %s" % len(sta_fdsn)
        if len(sta_fdsn) < min_req_stations:
            print '[INFO] requested number of stations %s is not satisfied!' \
                  % min_req_stations
            continue
        dmt_commands.append(
            ["./obspyDMT.py --datapath early_warning/%s --continuous "
             "--min_date %s --max_date %s "
             "--net _GSN --cha BHZ "
             "--req_parallel --req_np 10 "
             "--ic_parallel --ic_np 4 --merge_no --reset --test 10"
             % (ev_id, ev.preferred_origin().time,
                ev.preferred_origin().time+waveform_length), i, ev_id])
    return dmt_commands, resources_id, resources_done, all_events

# ##################### plot_src_rcv_pairs ##################################


def plot_src_rcv_pairs(events, dmt_command, resources_done, min_req_stations):
    """
    Plot src-rcv pairs
    :param events:
    :param dmt_command:
    :param resources_done:
    :return:
    """
    event = events[dmt_command[1]]

    plt.figure(figsize=(20, 10))
    m = Basemap(projection='robin', lon_0=event.preferred_origin().longitude)
    parallels = np.arange(-90, 90, 30.)
    m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
    meridians = np.arange(-180., 180., 60.)
    m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)
    m.etopo(scale=0.5)

    x, y = m(float(event.preferred_origin().longitude),
             float(event.preferred_origin().latitude))
    magnitude = float(event.preferred_magnitude().mag)
    m.scatter(x, y, color="red", s=100*magnitude,
              edgecolors='none', marker="o",
              zorder=10, alpha=1)

    if not os.path.isdir('./events'):
        os.mkdir('./events')
        os.mkdir('./events/latest')

    staev = read_station_event('./early_warning/%s' % dmt_command[2])
    if len(staev[0]) < min_req_stations:
        resources_done[dmt_command[1]] = False
        print "[INFO] number of successfully retrieved stations: %s" \
              % len(staev[0])
        return resources_done
    else:
        resources_done[dmt_command[1]] = True

    for i in range(len(staev[0])):
        stla, stlo = staev[0][i][4], staev[0][i][5]
        x, y = m(float(stlo), float(stla))
        m.scatter(x, y, color="black", s=50,
                  edgecolors='none', marker="v",
                  zorder=5, alpha=1)

        gcline = m.drawgreatcircle(
            float(event.preferred_origin().longitude),
            float(event.preferred_origin().latitude),
            float(staev[0][i][5]),
            float(staev[0][i][4]),
            color='k', alpha=0.0)
        gcx, gcy = gcline[0].get_data()
        gcx_diff = gcx[0:-1] - gcx[1:]
        gcy_diff = gcy[0:-1] - gcy[1:]
        if np.max(abs(gcx_diff))/abs(gcx_diff[0]) > 800:
            gcx_max_arg = abs(gcx_diff).argmax()
            plt.plot(gcx[0:gcx_max_arg], gcy[0:gcx_max_arg],
                     color='k', alpha=0.6)
            plt.plot(gcx[gcx_max_arg+1:], gcy[gcx_max_arg+1:],
                     color='k', alpha=0.6)
        elif np.max(abs(gcy_diff))/abs(gcy_diff[0]) > 400:
            gcy_max_arg = abs(gcy_diff).argmax()
            plt.plot(gcy[0:gcy_max_arg], gcy[0:gcy_max_arg],
                     color='k', alpha=0.6)
            plt.plot(gcy[gcy_max_arg+1:], gcy[gcy_max_arg+1:],
                     color='k', alpha=0.6)
        else:
            m.drawgreatcircle(
                float(event.preferred_origin().longitude),
                float(event.preferred_origin().latitude),
                float(staev[0][i][5]),
                float(staev[0][i][4]),
                color='k', alpha=0.6)

    if not os.path.isdir(os.path.join('./events', dmt_command[2])):
        os.mkdir(os.path.join('./events', dmt_command[2]))
    plt.savefig('./events/%s/src_rcv.png' % dmt_command[2])

    # Plotting the waveforms
    plt.figure(figsize=(20, 10))
    st = read("./early_warning/%s/*/continuous1/BH/*" % dmt_command[2])
    for tr in st:
        dist = locations2degrees(float(event.preferred_origin().latitude),
                                 float(event.preferred_origin().longitude),
                                 tr.stats.sac.stla,
                                 tr.stats.sac.stlo)
        plt.plot(np.linspace(0, (tr.stats.npts-1)/tr.stats.sampling_rate,
                             tr.stats.npts),
                 tr.data/max(abs(tr.data)) + dist, 'k', lw=3)
    plt.xlabel('Time', size=32, weight='bold')
    plt.ylabel('Epicentral Distance', size=32, weight='bold')
    plt.xticks(size=24, weight='bold')
    plt.yticks(size=24, weight='bold')
    if len(st) > 0:
        plt.savefig('./events/%s/rcvs.png' % dmt_command[2])
    return resources_done

# ##################### plot_all_src ##################################


def plot_all_src(events):
    """
    Plot all the sources
    :param events:
    :param dmt_command:
    :return:
    """
    plt.figure(figsize=(20, 10))
    m = Basemap(projection='robin', lon_0=0)
    parallels = np.arange(-90, 90, 30.)
    m.drawparallels(parallels, labels=[1, 1, 1, 1], fontsize=24)
    meridians = np.arange(-180., 180., 60.)
    m.drawmeridians(meridians, labels=[1, 1, 1, 1], fontsize=24)
    m.etopo(scale=0.5)

    for i in range(len(events)):
        x, y = m(float(events[i].preferred_origin().longitude),
                 float(events[i].preferred_origin().latitude))
        magnitude = float(events[i].preferred_magnitude().mag)
        m.scatter(x, y, color="red", s=100*magnitude,
                  edgecolors='none', marker="o",
                  zorder=10, alpha=1)
    plt.savefig('./events/latest/src_rcv.png')
