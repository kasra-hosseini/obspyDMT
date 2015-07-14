#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  fdsn_handler.py
#   Purpose:   handling FDSN in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from datetime import datetime
import fileinput
import glob
import multiprocessing
try:
    from obspy.clients.fdsn import Client as Client_fdsn
except Exception, e:
    from obspy.fdsn import Client as Client_fdsn
import os
import pickle

from event_handler import quake_info, create_folders_files
from format_converter import writesac_all
from resample_handler import resample_all
from utility_codes import read_list_stas, calculate_time_phase, getFolderSize

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ###################### FDSN_network ####################################


def FDSN_network(input_dics, events):
    """
    Availability and retrieivng functions are called with FDSN_network
    :param input_dics:
    :param events:
    :return:
    """
    print '\n********************************************************'
    print 'FDSN -- Download waveforms, StationXML files and meta-data'
    print '********************************************************'
    period = '{0:s}_{1:s}'.format(
        input_dics['min_date'].split('T')[0],
        input_dics['max_date'].split('T')[0])
    eventpath = os.path.join(input_dics['datapath'], period)

    print 'Initializing folders and files...',
    create_folders_files(events, eventpath, input_dics)
    print 'DONE'

    for i in range(len(events)):
        t_fdsn_1 = datetime.now()
        target_path = os.path.join(eventpath, events[i]['event_id'])

        if not input_dics['list_stas']:
            Stas_fdsn = FDSN_available(input_dics, events[i],
                                       target_path, event_number=i)
        else:
            Stas_fdsn = read_list_stas(input_dics['list_stas'],
                                       input_dics['normal_mode_syn'],
                                       input_dics['specfem3D'])
            if input_dics['fdsn_bulk'] == 'Y':
                FDSN_create_bulk_list(target_path, input_dics, Stas_fdsn,
                                      events[i])

        if input_dics['fdsn_bulk'] != 'Y':
            print '\n%s-Availability for event: %s/%s ---> DONE' \
                  % (input_dics['fdsn_base_url'], i+1, len(events))
        else:
            print '\nFDSN-bulkfile for event: %s/%s ---> DONE' \
                  % (i+1, len(events))

        print 'Time for checking the availability: %s' \
              % (datetime.now() - t_fdsn_1)

        if Stas_fdsn != [[]]:
            FDSN_waveform(input_dics, events, Stas_fdsn, i, req_type='save')
        else:
            print 'No available station in %s for your request and ' \
                  'for event %s!' % (input_dics['fdsn_base_url'], str(i+1))
            continue

# ##################### FDSN_available ##################################


def FDSN_available(input_dics, event, target_path, event_number):
    """
    Check the availablity of FDSN stations
    :param input_dics:
    :param event:
    :param target_path:
    :param event_number:
    :return:
    """
    print "Check the availablity of FDSN stations: %s" \
          % input_dics['fdsn_base_url']
    client_fdsn = Client_fdsn(base_url=input_dics['fdsn_base_url'],
                              user=input_dics['fdsn_user'],
                              password=input_dics['fdsn_pass'])
    Sta_fdsn = []
    try:
        if input_dics['fdsn_base_url'].lower() in ['resif']:
            # start_time = None
            # end_time = None
            start_time = event['t1']
            end_time = event['t2']
        else:
            start_time = event['t1']
            end_time = event['t2']
        available = client_fdsn.get_stations(
            network=input_dics['net'],
            station=input_dics['sta'],
            location=input_dics['loc'],
            channel=input_dics['cha'],
            starttime=start_time,
            endtime=end_time,
            latitude=input_dics['lat_cba'],
            longitude=input_dics['lon_cba'],
            minradius=input_dics['mr_cba'],
            maxradius=input_dics['Mr_cba'],
            minlatitude=input_dics['mlat_rbb'],
            maxlatitude=input_dics['Mlat_rbb'],
            minlongitude=input_dics['mlon_rbb'],
            maxlongitude=input_dics['Mlon_rbb'],
            level='channel')

        for network in available.networks:
            for station in network:
                for channel in station:
                    Sta_fdsn.append([network.code, station.code,
                                     channel.location_code, channel.code,
                                     channel.latitude, channel.longitude,
                                     channel.elevation, channel.depth])
        if input_dics['fdsn_bulk'] == 'Y':
            if input_dics['fdsn_update'] != 'N':
                if os.path.exists(os.path.join(target_path, 'info',
                                               'bulkdata.txt')):
                    os.remove(os.path.join(target_path, 'info',
                                           'bulkdata.txt'))
            if os.path.exists(os.path.join(target_path, 'info',
                                           'bulkdata.txt')):
                print 'bulkdata.txt exists in the directory!'
            else:
                print 'Start creating a list for bulk request'
                bulk_list = []
                for bulk_sta in Sta_fdsn:
                    if input_dics['cut_time_phase']:
                        t_start, t_end = calculate_time_phase(event, bulk_sta)
                    else:
                        t_start = event['t1']
                        t_end = event['t2']
                    bulk_list.append((bulk_sta[0], bulk_sta[1], bulk_sta[2],
                                      bulk_sta[3], t_start, t_end))

                bulk_list_fio = open(os.path.join(target_path, 'info',
                                                  'bulkdata_list'), 'a+')
                pickle.dump(bulk_list, bulk_list_fio)
                bulk_list_fio.close()
    except Exception as e:
        exc_file = open(os.path.join(target_path, 'info', 'exception'), 'a+')
        ee = 'fdsn -- Event: %s --- %s\n' % (str(event_number+1), e)
        exc_file.writelines(ee)
        exc_file.close()
        print 'ERROR: %s' % ee

    if len(Sta_fdsn) == 0:
        Sta_fdsn.append([])
    Sta_fdsn.sort()
    return Sta_fdsn

# ##################### FDSN_create_bulk_list ###############################


def FDSN_create_bulk_list(target_path, input_dics, Stas_fdsn, event):
    """
    Create bulkdata_list in case of --list_stas flag
    :param target_path:
    :param input_dics:
    :param Stas_fdsn:
    :param event:
    :return:
    """
    if input_dics['fdsn_update'] != 'N':
        if os.path.exists(os.path.join(target_path, 'info', 'bulkdata.txt')):
            os.remove(os.path.join(target_path, 'info', 'bulkdata.txt'))

    if os.path.exists(os.path.join(target_path, 'info', 'bulkdata.txt')):
        print 'bulkdata.txt exists in the directory!'
    else:
        print 'Start creating a list for bulk request'
        bulk_list = []
        for bulk_sta in Stas_fdsn:
            if input_dics['cut_time_phase']:
                t_start, t_end = calculate_time_phase(event, bulk_sta)
            else:
                t_start = event['t1']
                t_end = event['t2']
            bulk_list.append((bulk_sta[0], bulk_sta[1], bulk_sta[2],
                              bulk_sta[3], t_start, t_end))

        bulk_list_fio = open(os.path.join(target_path, 'info',
                                          'bulkdata_list'), 'a+')
        pickle.dump(bulk_list, bulk_list_fio)
        bulk_list_fio.close()

# ##################### FDSN_waveform ###############################


def FDSN_waveform(input_dics, events, Sta_req, i, req_type):
    """
    Gets Waveforms, StationXML files and meta-data from FDSN
    :param input_dics:
    :param events:
    :param Sta_req:
    :param i:
    :param req_type:
    :return:
    """
    t_wave_1 = datetime.now()

    add_event = []
    if req_type == 'save':
        period = '{0:s}_{1:s}'.\
            format(input_dics['min_date'].split('T')[0],
                   input_dics['max_date'].split('T')[0])
        eventpath = os.path.join(input_dics['datapath'], period)
        for k in range(len(events)):
            add_event.append(os.path.join(eventpath, events[k]['event_id']))
            events_fio = open(os.path.join(add_event[k],
                                           'info', 'event.pkl'), 'w')
            pickle.dump(events[k], events_fio)
            events_fio.close()
    elif req_type == 'update':
        events, add_event = \
            quake_info(input_dics['fdsn_update'], target='info')

    if input_dics['test'] == 'Y':
        len_req_fdsn = input_dics['test_num']
    else:
        len_req_fdsn = len(Sta_req)

    if input_dics['fdsn_bulk'] == 'Y':
        t11 = datetime.now()
        try:
            FDSN_bulk_request(i, add_event, input_dics)
        except Exception as e:
            print 'WARNING: %s' % e
        print 'DONE'

        # Following parameter is set to 'N' to avoid
        # retrieving the waveforms twice
        # When using bulk requests, waveforms are retreived in bulk
        # but not response/StationXML files and not metadata
        input_dics['waveform'] = 'N'
        t22 = datetime.now()
        print '\nbulkdataselect request is done for event: %s/%s in %s' \
              % (i+1, len(events), t22-t11)

    FDSN_serial_parallel(i, events, add_event, Sta_req, input_dics,
                         len_req_fdsn)

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

    FDSN_reporter(i, add_event, events, input_dics, Sta_req, len_sta_ev,
                  req_type, t_wave_1)

# ##################### FDSN_serial_parallel ##################################


def FDSN_serial_parallel(i, events, add_event, Sta_req, input_dics,
                         len_req_fdsn):
    """
    FDSN serial/parallel request
    """
    dic = {}
    print '\nFDSN-Event: %s/%s -- %s' % (i+1, len(events), add_event[i])

    client_fdsn = Client_fdsn(base_url=input_dics['fdsn_base_url'],
                              user=input_dics['fdsn_user'],
                              password=input_dics['fdsn_pass'])
    if input_dics['req_parallel'] == 'Y':
        print "Parallel request with %s processes.\n" % input_dics['req_np']
        par_jobs = []
        for j in range(len_req_fdsn):
            p = multiprocessing.Process(target=FDSN_download_core,
                                        args=(i, j, dic, len(events),
                                              events, add_event, Sta_req,
                                              input_dics, client_fdsn,))
            par_jobs.append(p)
        sub_par_jobs = []
        for l in range(len(par_jobs)):
            counter = input_dics['req_np']
            while counter >= input_dics['req_np']:
                counter = 0
                for ll in range(len(sub_par_jobs)):
                    if par_jobs[sub_par_jobs[ll]].is_alive():
                        counter += 1
            par_jobs[l].start()
            sub_par_jobs.append(l)

        counter = input_dics['req_np']
        while counter > 0:
            counter = 0
            for ll in range(len(par_jobs)):
                if par_jobs[ll].is_alive():
                    counter += 1
    else:
        for j in range(len_req_fdsn):
            FDSN_download_core(i=i, j=j, dic=dic, len_events=len(events),
                               events=events, add_event=add_event,
                               Sta_req=Sta_req, input_dics=input_dics,
                               client_fdsn=client_fdsn)

    if input_dics['fdsn_bulk'] == 'Y':
        input_dics['waveform'] = 'Y'
        sta_saved_path = glob.glob(os.path.join(add_event[i],
                                                'BH_RAW',
                                                '*.*.*.*'))
        print '\nAdjusting the station_event file...',

        sta_saved_list = []
        for sta_num in range(len(sta_saved_path)):
            sta_saved_list.append(os.path.basename(sta_saved_path[sta_num]))

        sta_ev_new = []
        for line in fileinput.FileInput(
                os.path.join(add_event[i], 'info', 'station_event')):
            line_split = line.split(',')
            if not '%s.%s.%s.%s' \
                    % (line_split[0], line_split[1], line_split[2],
                       line_split[3]) in sta_saved_list:
                pass
            else:
                sta_ev_new.append(line)

        file_staev_open = open(os.path.join(add_event[i], 'info',
                                            'station_event'), 'w')
        file_staev_open.writelines(sta_ev_new)
        file_staev_open.close()
        print 'DONE'

# ##################### FDSN_download_core ##################################


def FDSN_download_core(i, j, dic, len_events, events, add_event,
                       Sta_req, input_dics, client_fdsn):
    """
    Downloading the waveforms, reponse files (StationXML) and metadata
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
            client_fdsn.get_waveforms(Sta_req[j][0], Sta_req[j][1],
                                      Sta_req[j][2], Sta_req[j][3],
                                      t_start, t_end,
                                      filename=os.path.join(add_event[i],
                                                            'BH_RAW',
                                                            '%s.%s.%s.%s'
                                                            % (Sta_req[j][0],
                                                               Sta_req[j][1],
                                                               Sta_req[j][2],
                                                               Sta_req[j][3])))
            print '%ssaving waveform for: %s.%s.%s.%s  ---> DONE' \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        if input_dics['response'] == 'Y':
            dummy = 'Response'
            client_fdsn.get_stations(network=Sta_req[j][0],
                                     station=Sta_req[j][1],
                                     location=Sta_req[j][2],
                                     channel=Sta_req[j][3],
                                     # starttime=t_start, endtime=t_end,
                                     filename=os.path.join(add_event[i],
                                                           'Resp',
                                                           'STXML.%s.%s.%s.%s'
                                                           % (Sta_req[j][0],
                                                              Sta_req[j][1],
                                                              Sta_req[j][2],
                                                              Sta_req[j][3])),
                                     level='response')

            print "%ssaving Response for: %s.%s.%s.%s  ---> DONE" \
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
        syn = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\n' \
              % (dic[j]['net'], dic[j]['sta'],
                 dic[j]['loc'], dic[j]['cha'],
                 dic[j]['latitude'], dic[j]['longitude'],
                 float(dic[j]['elevation']),
                 float(dic[j]['depth']),
                 events[i]['event_id'], events[i]['latitude'],
                 events[i]['longitude'], events[i]['depth'],
                 events[i]['magnitude'], input_dics['fdsn_base_url'])
        Syn_file.writelines(syn)
        Syn_file.close()

        print "%ssaving Metadata for: %s.%s.%s.%s  ---> DONE" \
              % (info_req, Sta_req[j][0], Sta_req[j][1],
                 Sta_req[j][2], Sta_req[j][3])

        t22 = datetime.now()
        if input_dics['time_fdsn'] == 'Y':
            time_fdsn = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_fdsn'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,+,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_fdsn.seconds,
                                                time_fdsn.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()
    except Exception as e:
        t22 = datetime.now()
        if input_dics['time_fdsn'] == 'Y':
            time_fdsn = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_fdsn'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,-,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_fdsn.seconds,
                                                time_fdsn.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()

        if len(Sta_req[j]) != 0:
            print '%s%s---%s.%s.%s.%s' % (info_req, dummy,
                                          Sta_req[j][0],
                                          Sta_req[j][1],
                                          Sta_req[j][2],
                                          Sta_req[j][3])
            ee = 'fdsn -- %s---%s-%s---%s.%s.%s.%s---%s\n' \
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

# ##################### FDSN_bulk_request ##################################


def FDSN_bulk_request(i, add_event, input_dics):
    """
    Send bulk request to FDSN
    """
    print '\nSending bulk request to FDSN: %s' % input_dics['fdsn_base_url']
    client_fdsn = Client_fdsn(base_url=input_dics['fdsn_base_url'],
                              user=input_dics['fdsn_user'],
                              password=input_dics['fdsn_pass'])
    bulk_list_fio = open(os.path.join(add_event[i], 'info',
                                      'bulkdata_list'))
    bulk_list = pickle.load(bulk_list_fio)
    bulk_smgrs = client_fdsn.get_waveforms_bulk(bulk_list)
    print 'Saving the retrieved waveforms...',
    for bulk_st in bulk_smgrs:
        bulk_st.write(os.path.join(add_event[i], 'BH_RAW',
                                   '%s.%s.%s.%s'
                                   % (bulk_st.stats['network'],
                                      bulk_st.stats['station'],
                                      bulk_st.stats['location'],
                                      bulk_st.stats['channel'])),
                      'MSEED')

# ##################### FDSN_reporter ##################################


def FDSN_reporter(i, add_event, events, input_dics, Sta_req, len_sta_ev,
                  req_type, t_wave_1):
    """
    Writing reports for the request
    """
    report = open(os.path.join(add_event[i], 'info', 'report_st'), 'a')
    eventsID = events[i]['event_id']
    report.writelines('<><><><><><><><><><><><><><><><><>\n')
    report.writelines(eventsID + '\n')
    report.writelines('---------------%s---------------\n'
                      % input_dics['fdsn_base_url'])
    report.writelines('---------------%s---------------\n' % input_dics['cha'])
    rep = 'FDSN-Available stations for channel %s and for event-%s: %s\n' \
          % (input_dics['cha'], i, len(Sta_req))
    report.writelines(rep)
    rep = 'FDSN-%s stations for channel %s and for event-%s: %s\n' \
          % (req_type, input_dics['cha'], i, len_sta_ev)
    report.writelines(rep)
    report.writelines('----------------------------------\n')

    t_wave = datetime.now() - t_wave_1

    rep = 'Time for %sing Waveforms from FDSN: %s\n' % (req_type, t_wave)
    report.writelines(rep)
    report.writelines('----------------------------------\n')
    report.close()

    if input_dics['req_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(add_event[i], 'info',
                                                 'report_parallel'), 'a')
        report_parallel_open.writelines(
            '---------------%s---------------\n'
            % input_dics['fdsn_base_url'])
        report_parallel_open.writelines('Request\n')
        if input_dics['fdsn_bulk'] == 'Y':
            report_parallel_open.writelines('Number of Nodes: (bulk) %s\n'
                                            % input_dics['req_np'])
        else:
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
    print 'FDSN for event-%s is Done' % (i+1)
    print 'Total Time: %s' % t_wave
    print "------------------------"


# -------------------------------- TRASH
# parallel_len_req_fdsn = range(0, len_req_fdsn)

# start = 0
# end = len_req_fdsn
# step = (end - start) / input_dics['req_np'] + 1

# jobs = []
# for index in xrange(input_dics['req_np']):
#     starti = start+index*step
#     endi = min(start+(index+1)*step, end)
#     p = multiprocessing.Process(target=FDSN_download_iter,
#                                 args=(i, starti, endi, dic, req_type,
#                                       len(events), events, add_event,
#                                       Sta_req, input_dics, client_fdsn))

#     jobs.append(p)
# for index in range(len(jobs)):
#     jobs[index].start()

# pp_flag = True
# while pp_flag:
#     for proc in jobs:
#         if proc.is_alive():
#             time.sleep(1)
#             pp_flag = True
#             break
#         else:
#             pp_flag = False
#     if not pp_flag:
#         print '\nAll the processes are finished...'

# len_par_grp = [parallel_len_req_fdsn[n:n+input_dics['req_np']] for n in
#                range(0, len(parallel_len_req_fdsn), input_dics['req_np'])]
# # ##################### FDSN_download_iter ##################################
#
#
# def FDSN_download_iter(i, starti, endi, dic, type, len_events, events,
#                        add_event, Sta_req, input, client_fdsn):
#     """
#     This function only iterates over FDSN_download_core,
#     this should be called by another program.
#     """
#     for j in range(starti, endi):
#         FDSN_download_core(i=i, j=j, dic=dic, type=type,
#                            len_events=len_events, events=events,
#                            add_event=add_event, Sta_req=Sta_req,
#                            input=input, client_fdsn=client_fdsn)
