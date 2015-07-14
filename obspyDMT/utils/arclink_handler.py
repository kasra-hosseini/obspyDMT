#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  arclink_handler.py
#   Purpose:   handling ArcLink in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from datetime import datetime
import multiprocessing
try:
    from obspy.clients.arclink import Client as Client_arclink
except Exception, e:
    from obspy.arclink import Client as Client_arclink
from obspy.core import UTCDateTime
import os
import pickle
import time

from event_handler import quake_info, create_folders_files
from format_converter import writesac_all
from resample_handler import resample_all
from utility_codes import read_list_stas, calculate_time_phase, getFolderSize

# ##################### Arclink_network #################################


def ARC_network(input_dics, events):
    """
    Returns information about what time series data is available
    at the ArcLink nodes for all requested events
    """
    print '\n***********************************************************'
    print 'ArcLink -- Download waveforms, response files and meta-data'
    print '***********************************************************'
    period = '{0:s}_{1:s}_{2:s}_{3:s}'.format(
        input_dics['min_date'].split('T')[0],
        input_dics['max_date'].split('T')[0],
        str(input_dics['min_mag']),
        str(input_dics['max_mag']))
    eventpath = os.path.join(input_dics['datapath'], period)

    if input_dics['FDSN'] != 'Y':
        print 'Initializing folders and files...',
        create_folders_files(events, eventpath, input_dics)
        print 'DONE'

    for i in range(len(events)):
        t_arc_1 = datetime.now()
        target_path = os.path.join(eventpath, events[i]['event_id'])

        if not input_dics['list_stas']:
            Stas_arc = ARC_available(input_dics, events[i],
                                     target_path, event_number=i)
        else:
            Stas_arc = read_list_stas(input_dics['list_stas'],
                                      normal_mode_syn='N',
                                      specfem3D='N')

        print '\nArcLink-Availability for event: %s/%s  ---> DONE' \
              % (i+1, len(events))
        print 'Time for checking the availability: %s' \
              % (datetime.now() - t_arc_1)

        if Stas_arc != [[]]:
            ARC_waveform(input_dics, events, Stas_arc, i, req_type='save')
        else:
            print 'No available station in ArcLink for your request and ' \
                  'for event %s!' % str(i+1)
            continue

# ##################### ARC_available ###################################


def ARC_available(input_dics, event, target_path, event_number):
    """
    Check the availability of ArcLink stations
    """
    print "Check the availability of ArcLink stations"
    client_arclink = Client_arclink(user='test@obspy.org',
                                    timeout=input_dics['arc_avai_timeout'])
    Sta_arc = []
    try:
        inventories = client_arclink.getInventory(
            network=input_dics['net'],
            station=input_dics['sta'],
            location=input_dics['loc'],
            channel=input_dics['cha'],
            starttime=UTCDateTime(event['t1']),
            endtime=UTCDateTime(event['t2']),
            min_latitude=input_dics['mlat_rbb'],
            max_latitude=input_dics['Mlat_rbb'],
            min_longitude=input_dics['mlon_rbb'],
            max_longitude=input_dics['Mlon_rbb'])

        for inv_key in inventories.keys():
            netsta = inv_key.split('.')
            if len(netsta) == 4:
                sta = '%s.%s' % (netsta[0], netsta[1])
                if not inventories[sta]['depth']:
                    inventories[sta]['depth'] = 0.0
                Sta_arc.append([netsta[0], netsta[1], netsta[2], netsta[3],
                                inventories[sta]['latitude'],
                                inventories[sta]['longitude'],
                                inventories[sta]['elevation'],
                                inventories[sta]['depth']])

    except Exception as e:
        exc_file = open(os.path.join(target_path, 'info', 'exception'), 'a+')
        ee = 'arclink -- Event: %s --- %s\n' % (str(event_number+1), e)
        exc_file.writelines(ee)
        exc_file.close()
        print 'ERROR: %s' % ee

    if len(Sta_arc) == 0:
        Sta_arc.append([])
    Sta_arc.sort()
    return Sta_arc

# ##################### Arclink_waveform ############################


def ARC_waveform(input_dics, events, Sta_req, i, req_type):
    """
    Gets Waveforms, Response files and meta-data from ArcLink
    """
    t_wave_1 = datetime.now()

    add_event = []
    if req_type == 'save':
        period = '{0:s}_{1:s}_{2:s}_{3:s}'.\
            format(input_dics['min_date'].split('T')[0],
                   input_dics['max_date'].split('T')[0],
                   str(input_dics['min_mag']),
                   str(input_dics['max_mag']))
        eventpath = os.path.join(input_dics['datapath'], period)
        for k in range(len(events)):
            add_event.append(os.path.join(eventpath, events[k]['event_id']))
            if not os.path.isfile(os.path.join(add_event[k],
                                               'info', 'event.pkl')):
                events_fio = open(os.path.join(add_event[k],
                                               'info', 'event.pkl'), 'w')
                pickle.dump(events[k], events_fio)
                events_fio.close()
    elif req_type == 'update':
        events, add_event = \
            quake_info(input_dics['arc_update'], target='info')

    if input_dics['test'] == 'Y':
        len_req_arc = input_dics['test_num']
    else:
        len_req_arc = len(Sta_req)

    ARC_serial_parallel(i, events, add_event, Sta_req, input_dics,
                        len_req_arc)

    if input_dics['resample_raw']:
        print '\nResample RAW traces to %sHz...' % input_dics['resample_raw'],
        resample_all(i=i, address_events=add_event,
                     des_sr=input_dics['resample_raw'],
                     resample_method=input_dics['resample_method'])
        print 'DONE'
    if input_dics['SAC'] == 'Y':
        print '\nConverting the MSEED files to SAC...',
        writesac_all(i=i, address_events=add_event)
        print 'DONE'

    try:
        len_sta_ev_open = open(os.path.join(add_event[i], 'info',
                                            'station_event'), 'r')
        len_sta_ev = len(len_sta_ev_open.readlines())
    except IOError:
        len_sta_ev = 'Can not open station_event file: %s' \
                     % (os.path.join(add_event[i], 'info', 'station_event'))

    ARC_reporter(i, add_event, events, input_dics, Sta_req, len_sta_ev,
                 req_type, t_wave_1)

# ##################### ARC_serial_parallel ############################


def ARC_serial_parallel(i, events, add_event, Sta_req, input_dics,
                        len_req_arc):
    """
    ArcLink serial/parallel request
    """
    dic = {}
    print '\nArcLink-Event: %s/%s' % (i+1, len(events))

    client_arclink = Client_arclink(user='test@obspy.org',
                                    timeout=input_dics['arc_wave_timeout'])

    if input_dics['req_parallel'] == 'Y':
        print "Parallel request with %s processes.\n" % input_dics['req_np']
        parallel_len_req_arc = range(len_req_arc)
        len_par_grp = [parallel_len_req_arc[n:n+input_dics['req_np']] for n in
                       range(0, len(parallel_len_req_arc),
                             input_dics['req_np'])]
        par_jobs = []
        for j in range(len_req_arc):
            p = multiprocessing.Process(target=ARC_download_core,
                                        args=(i, j, dic, len(events),
                                              events, add_event, Sta_req,
                                              input_dics, client_arclink))
            par_jobs.append(p)
        for l in range(len(len_par_grp)):
            for ll in len_par_grp[l]:
                par_jobs[ll].start()
                time.sleep(0.01)
            for ll in len_par_grp[l]:
                while par_jobs[ll].is_alive():
                    time.sleep(0.01)
    else:
        for j in range(len_req_arc):
            ARC_download_core(i=i, j=j, dic=dic, len_events=len(events),
                              events=events, add_event=add_event,
                              Sta_req=Sta_req, input_dics=input_dics,
                              client_arclink=client_arclink)

# ##################### ARC_download_core ###############################


def ARC_download_core(i, j, dic, len_events, events, add_event,
                      Sta_req, input_dics, client_arclink):
    """
    Downloading waveforms, response files and metadata
    This program should be normally called by some higher-level functions
    """

    dummy = 'Initializing'
    info_req = 'None'
    t11 = datetime.now()
    try:
        info_req = '[%s/%s-%s/%s-%s] ' % (i+1, len_events, j+1,
                                          len(Sta_req), input_dics['cha'])

        if Sta_req[j][2] == '--' or Sta_req[j][2] == '  ':
                Sta_req[j][2] = ''

        if input_dics['cut_time_phase']:
            t_start, t_end = calculate_time_phase(events[i], Sta_req[j])
        else:
            t_start = events[i]['t1']
            t_end = events[i]['t2']

        if input_dics['waveform'] == 'Y':
            dummy = 'Waveform'
            client_arclink.saveWaveform(os.path.join(add_event[i],
                                                     'BH_RAW',
                                                     '%s.%s.%s.%s'
                                                     % (Sta_req[j][0],
                                                        Sta_req[j][1],
                                                        Sta_req[j][2],
                                                        Sta_req[j][3])),
                                        Sta_req[j][0], Sta_req[j][1],
                                        Sta_req[j][2], Sta_req[j][3],
                                        t_start, t_end)

            print '%ssaving waveform for: %s.%s.%s.%s  ---> DONE' \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        if input_dics['response'] == 'Y':
            dummy = 'Response'
            client_arclink.saveResponse(os.path.join(add_event[i], 'Resp',
                                                     'DATALESS.%s.%s.%s.%s'
                                                     % (Sta_req[j][0],
                                                        Sta_req[j][1],
                                                        Sta_req[j][2],
                                                        Sta_req[j][3])),
                                        Sta_req[j][0], Sta_req[j][1],
                                        Sta_req[j][2], Sta_req[j][3],
                                        t_start, t_end)

            print "%ssaving Response for: %s.%s.%s.%s  ---> DONE" \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        if input_dics['paz'] == 'Y':
            dummy = 'PAZ'
            paz_arc = client_arclink.getPAZ(Sta_req[j][0], Sta_req[j][1],
                                            Sta_req[j][2], Sta_req[j][3],
                                            time=t_start)
            paz_file = open(os.path.join(add_event[i], 'Resp',
                                         'PAZ.%s.%s.%s.%s.paz'
                                         % (Sta_req[j][0], Sta_req[j][1],
                                            Sta_req[j][2], Sta_req[j][3])),
                            'w')
            pickle.dump(paz_arc, paz_file)
            paz_file.close()

            print "%ssaving PAZ for     : %s.%s.%s.%s  ---> DONE" \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        dummy = 'Meta-data'
        dic[j] = {'info': '%s.%s.%s.%s' % (Sta_req[j][0], Sta_req[j][1],
                                           Sta_req[j][2], Sta_req[j][3]),
                  'net': Sta_req[j][0],
                  'sta': Sta_req[j][1],
                  'latitude': Sta_req[j][4],
                  'longitude': Sta_req[j][5],
                  'loc': Sta_req[j][2],
                  'cha': Sta_req[j][3],
                  'elevation': Sta_req[j][6],
                  'depth': Sta_req[j][7]}
        Syn_file = open(os.path.join(add_event[i], 'info',
                                     'station_event'), 'a')
        syn = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,arc,\n' \
              % (dic[j]['net'], dic[j]['sta'],
                 dic[j]['loc'], dic[j]['cha'],
                 dic[j]['latitude'], dic[j]['longitude'],
                 float(dic[j]['elevation']),
                 float(dic[j]['depth']),
                 events[i]['event_id'], events[i]['latitude'],
                 events[i]['longitude'], events[i]['depth'],
                 events[i]['magnitude'])
        Syn_file.writelines(syn)
        Syn_file.close()

        print "%ssaving Metadata for: %s.%s.%s.%s  ---> DONE" \
              % (info_req, Sta_req[j][0], Sta_req[j][1],
                 Sta_req[j][2], Sta_req[j][3])

        t22 = datetime.now()
        if input_dics['time_arc'] == 'Y':
            time_arc = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_arc'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,+,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_arc.seconds,
                                                time_arc.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()
    except Exception as e:
        t22 = datetime.now()
        if input_dics['time_arc'] == 'Y':
            time_arc = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_arc'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,-,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_arc.seconds,
                                                time_arc.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()

        if len(Sta_req[j]) != 0:
            print '%s%s---%s.%s.%s.%s' % (info_req, dummy,
                                          Sta_req[j][0],
                                          Sta_req[j][1],
                                          Sta_req[j][2],
                                          Sta_req[j][3])
            ee = 'arc -- %s---%s-%s---%s.%s.%s.%s---%s\n' \
                 % (dummy, i+1, j+1,
                    Sta_req[j][0], Sta_req[j][1], Sta_req[j][2],
                    Sta_req[j][3], e)
        else:
            ee = 'There is no available station for this event.'
        Exception_file = open(os.path.join(add_event[i],
                                           'info', 'exception'), 'a')
        Exception_file.writelines(ee)
        Exception_file.close()
        print 'ERROR: %s' % ee

# ##################### ARC_reporter ###############################


def ARC_reporter(i, add_event, events, input_dics, Sta_req, len_sta_ev,
                 req_type, t_wave_1):
    """
    Writing reports for the request
    :param i:
    :param add_event:
    :param events:
    :param input_dics:
    :param Sta_req:
    :param len_sta_ev:
    :param req_type:
    :param t_wave_1:
    :return:
    """
    report = open(os.path.join(add_event[i], 'info', 'report_st'), 'a')
    eventsID = events[i]['event_id']
    report.writelines('<><><><><><><><><><><><><><><><><>\n')
    report.writelines(eventsID + '\n')
    report.writelines('---------------ARC---------------\n')
    report.writelines('---------------%s---------------\n' % input_dics['cha'])
    rep = 'ARC-Available stations for channel %s and for event-%s: %s\n' \
          % (input_dics['cha'], i, len(Sta_req))
    report.writelines(rep)
    rep = 'ARC-%s stations for channel %s and for event-%s: %s\n' \
          % (req_type, input_dics['cha'], i, len_sta_ev)
    report.writelines(rep)
    report.writelines('----------------------------------\n')

    t_wave = datetime.now() - t_wave_1

    rep = 'Time for %sing Waveforms from ArcLink: %s\n' % (req_type, t_wave)
    report.writelines(rep)
    report.writelines('----------------------------------\n')
    report.close()

    if input_dics['req_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(add_event[i], 'info',
                                                 'report_parallel'), 'a')
        report_parallel_open.writelines('---------------ARC---------------\n')
        report_parallel_open.writelines('Request\n')
        report_parallel_open.writelines('Number of Nodes: %s\n'
                                        % input_dics['req_np'])

        size = getFolderSize(os.path.join(add_event[i]))
        ti = '%s,%s,%s,+,\n' % (t_wave.seconds,
                                t_wave.microseconds,
                                size/(1024.**2))

        report_parallel_open.writelines('Total Time     : %s\n' % t_wave)
        report_parallel_open.writelines(ti)
        report_parallel_open.close()

    print "\n------------------------"
    print 'ArcLink for event-%s is Done' % (i+1)
    print 'Total Time: %s' % t_wave
    print "------------------------"

# -------------------------------- TRASH
# par_jobs = []
# for j in range(len_req_arc):
#     p = multiprocessing.Process(target=ARC_download_core,
#                                 args=(i, j, dic, type, len(events),
#                                       events, add_event, Sta_req,
#                                       input,))
#     par_jobs.append(p)
# sub_par_jobs = []
# for l in range(len(par_jobs)):
#     counter = input['req_np']
#     while counter >= input['req_np']:
#         counter = 0
#         for ll in range(len(sub_par_jobs)):
#             if par_jobs[sub_par_jobs[ll]].is_alive():
#                 counter += 1
#         if not counter == input['req_np']:
#             print 'counter: %s' % counter

#     par_jobs[l].start()
#     sub_par_jobs.append(l)
#     print 'length of sub_pat_jobs: %s' % len(sub_par_jobs)

# counter = input['req_np']
# while counter > 0:
#     counter = 0
#     for ll in range(len(par_jobs)):
#         if par_jobs[ll].is_alive():
#             counter += 1
