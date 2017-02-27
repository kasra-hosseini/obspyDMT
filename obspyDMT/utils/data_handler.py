#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  data_handler.py
#   Purpose:   handling data (waveform/response) in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from datetime import datetime
import fileinput
import glob
import multiprocessing
import numpy as np
try:
    from obspy.clients.fdsn import Client as Client_fdsn
except:
    from obspy.fdsn import Client as Client_fdsn
try:
    from obspy.clients.arclink import Client as Client_arclink
except:
    from obspy.arclink import Client as Client_arclink
try:
    from obspy.geodetics.base import gps2dist_azimuth as gps2DistAzimuth
except:
    try:
        from obspy.geodetics import gps2DistAzimuth
    except:
        from obspy.core.util import gps2DistAzimuth
import os
import pickle

from utility_codes import calculate_time_phase, getFolderSize

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### get_data ###############################


def get_data(stas_avail, event, input_dics, info_event):
    """
    get the waveform/response from FDSN and ArcLink
    :param stas_avail:
    :param event:
    :param input_dics:
    :param info_event:
    :return:
    """
    t_wave_1 = datetime.now()

    req_clients = np.unique(stas_avail[:, 8])
    print "[INFO] requested data sources:"
    for req_c in req_clients:
        print req_c,
    print '\n'

    if input_dics['test']:
        stas_avail = stas_avail[0:input_dics['test_num']]

    if input_dics['req_parallel']:
        par_jobs = []
        for req_cli in req_clients:
            st_avail = stas_avail[stas_avail[:, 8] == req_cli]
            if not req_cli.lower() in ['arclink']:
                p = multiprocessing.Process(target=fdsn_waveform,
                                            args=(st_avail, event,
                                                  input_dics, req_cli,
                                                  info_event))
                par_jobs.append(p)
            elif req_cli.lower() == 'arclink':
                p = multiprocessing.Process(target=arc_waveform,
                                            args=(st_avail, event,
                                                  input_dics, req_cli,
                                                  info_event))
                par_jobs.append(p)

        sub_par_jobs = []
        for l in range(len(par_jobs)):
            counter = len(req_clients)
            while counter >= len(req_clients):
                counter = 0
                for ll in range(len(sub_par_jobs)):
                    if par_jobs[sub_par_jobs[ll]].is_alive():
                        counter += 1
            par_jobs[l].start()
            sub_par_jobs.append(l)

        counter = len(req_clients)
        while counter > 0:
            counter = 0
            for ll in range(len(par_jobs)):
                if par_jobs[ll].is_alive():
                    counter += 1
    else:
        for req_cli in req_clients:
            st_avail = stas_avail[stas_avail[:, 8] == req_cli]
            if not req_cli.lower() in ['arclink']:
                fdsn_waveform(st_avail, event, input_dics, req_cli, info_event)
            elif req_cli.lower() == 'arclink':
                arc_waveform(st_avail, event, input_dics, req_cli, info_event)

    print "\n========================"
    print "DONE with Event: %s" % event['event_id']
    print "Time: %s" % (datetime.now() - t_wave_1)
    print "========================"

# ##################### fdsn_waveform ###############################


def fdsn_waveform(stas_avail, event, input_dics, req_cli, info_event):
    """
    get Waveforms, StationXML files and meta-data from FDSN
    :param stas_avail:
    :param event:
    :param input_dics:
    :param req_cli:
    :param info_event:
    :return:
    """
    eventpath = os.path.join(input_dics['datapath'])
    target_path = os.path.join(eventpath, event['event_id'])

    if input_dics['bulk']:
        try:
            fdsn_bulk_request(target_path, req_cli, input_dics)
        except Exception as error:
            print '[WARNING] %s' % error
        print 'DONE'

        # Following parameter is set to 'N' to avoid
        # retrieving the waveforms twice
        # When using bulk requests, waveforms are retreived in bulk
        # but not response/StationXML files and not metadata
        input_dics['waveform'] = False
        print '%s bulkdataselect request is done for event: %s' \
              % (req_cli, target_path)

    fdsn_serial_parallel(stas_avail, event, input_dics, target_path,
                         req_cli, info_event)

# ##################### fdsn_serial_parallel ##################################


def fdsn_serial_parallel(stas_avail, event, input_dics, target_path,
                         req_cli, info_event):
    """
    retrieving data from FDSN
    :param stas_avail:
    :param event:
    :param input_dics:
    :param target_path:
    :param req_cli:
    :param info_event:
    :return:
    """
    print '%s -- event: %s' % (req_cli, target_path)

    client_fdsn = Client_fdsn(base_url=req_cli,
                              user=input_dics['username'],
                              password=input_dics['password'])
                              #debug=True)

    if input_dics['req_parallel']:
        if input_dics['password']:
            print "[INFO] Restricted data from %s" % req_cli
            print "[WARNING] parallel retrieving is now possible!"
            print "[WARNING] serial retrieving is activated!"
            # num_req_np = 1
            num_req_np = input_dics['req_np']
        else:
            num_req_np = input_dics['req_np']
        par_jobs = []
        st_counter = 0
        for st_avail in stas_avail:
            st_counter += 1
            info_station = '[%s-%s/%s]' % (info_event, st_counter,
                                           len(stas_avail))
            p = multiprocessing.Process(target=fdsn_download_core,
                                        args=(st_avail, event,
                                              input_dics, target_path,
                                              client_fdsn, req_cli,
                                              info_station))
            par_jobs.append(p)

        sub_par_jobs = []
        for l in range(len(par_jobs)):
            counter = num_req_np
            while counter >= num_req_np:
                counter = 0
                for ll in range(len(sub_par_jobs)):
                    if par_jobs[sub_par_jobs[ll]].is_alive():
                        counter += 1
            par_jobs[l].start()
            sub_par_jobs.append(l)

        counter = num_req_np
        while counter > 0:
            counter = 0
            for ll in range(len(par_jobs)):
                if par_jobs[ll].is_alive():
                    counter += 1
    else:
        st_counter = 0
        for st_avail in stas_avail:
            st_counter += 1
            info_station = '[%s-%s/%s]' % (info_event, st_counter,
                                           len(stas_avail))
            fdsn_download_core(st_avail, event, input_dics, target_path,
                               client_fdsn, req_cli, info_station)

    update_sta_ev_file(target_path)

    if input_dics['bulk']:
        input_dics['waveform'] = True
        sta_saved_path = glob.glob(os.path.join(target_path, 'raw', '*.*.*.*'))
        print '\n[INFO] adjusting the station_event file for bulk request...',

        sta_saved_list = []
        for sta_num in range(len(sta_saved_path)):
            sta_saved_list.append(os.path.basename(sta_saved_path[sta_num]))

        sta_ev_new = []
        for line in fileinput.FileInput(
                os.path.join(target_path, 'info', 'station_event')):
            line_split = line.split(',')
            if not '%s.%s.%s.%s' \
                    % (line_split[0], line_split[1], line_split[2],
                       line_split[3]) in sta_saved_list:
                pass
            else:
                sta_ev_new.append(line)

        file_staev_open = open(os.path.join(target_path, 'info',
                                            'station_event'), 'w')
        file_staev_open.writelines(sta_ev_new)
        file_staev_open.close()
        print 'DONE'

# ##################### fdsn_download_core ##################################


def fdsn_download_core(st_avail, event, input_dics, target_path,
                       client_fdsn, req_cli, info_station):
    """
    downloading the waveforms, reponse files (StationXML) and metadata
    this function should be normally called by some higher-level functions
    :param st_avail:
    :param event:
    :param input_dics:
    :param target_path:
    :param client_fdsn:
    :param req_cli:
    :param info_station:
    :return:
    """
    dummy = 'initializing'

    t11 = datetime.now()
    identifier = 0
    st_id = '%s.%s.%s.%s' % (st_avail[0], st_avail[1],
                             st_avail[2], st_avail[3])
    try:
        if st_avail[2] == '--' or st_avail[2] == '  ':
                st_avail[2] = ''

        if input_dics['cut_time_phase']:
            t_start, t_end = calculate_time_phase(event, st_avail)
        else:
            t_start = event['t1']
            t_end = event['t2']

        if input_dics['min_azi'] or input_dics['max_azi'] or \
                input_dics['min_epi'] or input_dics['max_epi']:
            dist, azi, bazi = gps2DistAzimuth(event['latitude'],
                                              event['longitude'],
                                              float(st_avail[4]),
                                              float(st_avail[5]))
            epi_dist = dist/111.194/1000.
            if input_dics['min_epi']:
                if epi_dist < input_dics['min_epi']:
                    raise Exception('%s out of epi range: %s'
                                    % (st_id, epi_dist))
            if input_dics['max_epi']:
                if epi_dist > input_dics['max_epi']:
                    raise Exception('%s out of epi range: %s'
                                    % (st_id, epi_dist))
            if input_dics['min_azi']:
                if azi < input_dics['min_azi']:
                    raise Exception('%s outo f Azimuth range: %s'
                                    % (st_id, azi))
            if input_dics['max_azi']:
                if azi > input_dics['max_azi']:
                    raise Exception('%s out of Azimuth range: %s'
                                    % (st_id, azi))

        if input_dics['waveform']:
            dummy = 'waveform'
            if (not os.path.isfile(os.path.join(target_path, 'raw', st_id)))\
                    or input_dics['force_waveform']:
                client_fdsn.get_waveforms(st_avail[0], st_avail[1],
                                          st_avail[2], st_avail[3],
                                          t_start, t_end,
                                          filename=os.path.join(target_path,
                                                                'raw',
                                                                st_id))
                identifier += 10
                print '%s -- %s -- saving waveform for: %s  ---> DONE' \
                      % (info_station, req_cli, st_id)
            else:
                identifier += 1

        if input_dics['response']:
            dummy = 'response'
            if (not os.path.isfile(os.path.join(target_path, 'resp',
                                                'STXML.' + st_id))) \
                or (not os.path.isfile(os.path.join(target_path, 'resp',
                                                    'DATALESS.' + st_id))) \
                    or input_dics['force_response']:
                client_fdsn.get_stations(network=st_avail[0],
                                         station=st_avail[1],
                                         location=st_avail[2],
                                         channel=st_avail[3],
                                         starttime=t_start, endtime=t_end,
                                         filename=os.path.join(
                                             target_path, 'resp',
                                             'STXML.%s' % st_id),
                                         level='response')
                identifier += 100
                print "%s -- %s -- saving response for: %s  ---> DONE" \
                      % (info_station, req_cli, st_id)
            else:
                identifier += 1

        if identifier in [0, 2, 10, 11, 100]:
            raise Exception("CODE: %s will not be registered! (666)"
                            % identifier)

        dummy = 'meta-data'
        syn_file = open(os.path.join(target_path, 'info',
                                     'station_event'), 'a')
        syn = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\n' \
              % (st_avail[0], st_avail[1],
                 st_avail[2], st_avail[3],
                 st_avail[4], st_avail[5],
                 float(st_avail[6]),
                 float(st_avail[7]),
                 req_cli,
                 event['event_id'], event['latitude'],
                 event['longitude'], event['depth'],
                 event['magnitude'], identifier)
        syn_file.writelines(syn)
        syn_file.close()

        print "%s -- %s -- saving metadata for: %s  ---> DONE" \
              % (info_station, req_cli, st_id)

        t22 = datetime.now()
    except Exception as error:
        t22 = datetime.now()
        if len(st_avail) > 0:
            ee = '%s -- %s -- %s -- %s\n' % (req_cli, dummy, st_id, error)
        else:
            ee = '%s: There is no available station for this event.' % req_cli
        Exception_file = open(os.path.join(target_path,
                                           'info', 'exception'), 'a+')
        Exception_file.writelines(ee)
        Exception_file.close()

# ##################### fdsn_bulk_request ##################################


def fdsn_bulk_request(target_path, req_cli, input_dics):
    """
    send bulk request to FDSN
    :param target_path:
    :param req_cli:
    :param input_dics:
    :return:
    """
    print '\n[INFO] sending bulk request to: %s' % req_cli

    client_fdsn = Client_fdsn(base_url=req_cli,
                              user=input_dics['username'],
                              password=input_dics['password'])

    bulk_list_fio = open(os.path.join(target_path, 'info',
                                      'bulkdata_list_%s' % req_cli))
    bulk_list = pickle.load(bulk_list_fio)
    bulk_smgrs = client_fdsn.get_waveforms_bulk(bulk_list)
    print '[INFO] saving the retrieved waveforms from %s...' % req_cli
    for bulk_st in bulk_smgrs:
        bulk_st.write(os.path.join(target_path, 'raw', '%s.%s.%s.%s'
                                   % (bulk_st.stats['network'],
                                      bulk_st.stats['station'],
                                      bulk_st.stats['location'],
                                      bulk_st.stats['channel'])),
                      'MSEED')

# ##################### arc_waveform ###############################


def arc_waveform(stas_avail, event, input_dics, req_cli, info_event):
    """
    get Waveforms, StationXML files and meta-data from ArcLink
    :param stas_avail:
    :param event:
    :param input_dics:
    :param req_cli:
    :param info_event:
    :return:
    """
    eventpath = os.path.join(input_dics['datapath'])
    target_path = os.path.join(eventpath, event['event_id'])

    arc_serial_parallel(stas_avail, event, input_dics, target_path,
                        req_cli, info_event)

# ##################### arc_serial_parallel ##################################


def arc_serial_parallel(stas_avail, event, input_dics, target_path,
                        req_cli, info_event):
    """
    retrieving data from ArcLink
    :param stas_avail:
    :param event:
    :param input_dics:
    :param target_path:
    :param req_cli:
    :param info_event:
    :return:
    """
    print '%s -- event: %s' % (req_cli, target_path)

    client_arclink = Client_arclink(user='test@obspy.org',
                                    timeout=input_dics['arc_wave_timeout'])

    if input_dics['req_parallel']:
        par_jobs = []
        st_counter = 0
        for st_avail in stas_avail:
            st_counter += 1
            info_station = '[%s-%s/%s]' % (info_event, st_counter,
                                           len(stas_avail))
            p = multiprocessing.Process(target=arc_download_core,
                                        args=(st_avail, event,
                                              input_dics, target_path,
                                              client_arclink, req_cli,
                                              info_station))
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
        st_counter = 0
        for st_avail in stas_avail:
            st_counter += 1
            info_station = '[%s-%s/%s]' % (info_event, st_counter,
                                           len(stas_avail))
            arc_download_core(st_avail, event, input_dics, target_path,
                              client_arclink, req_cli, info_station)

# ##################### arc_download_core ##################################


def arc_download_core(st_avail, event, input_dics, target_path,
                      client_arclink, req_cli, info_station):
    """
    downloading the waveforms, reponse files (StationXML) and metadata
    this function should be normally called by some higher-level functions
    :param st_avail:
    :param event:
    :param input_dics:
    :param target_path:
    :param client_arclink:
    :param req_cli:
    :param info_station:
    :return:
    """
    dummy = 'initializing'

    t11 = datetime.now()
    identifier = 0
    st_id = '%s.%s.%s.%s' % (st_avail[0], st_avail[1],
                             st_avail[2], st_avail[3])
    try:
        if st_avail[2] == '--' or st_avail[2] == '  ':
                st_avail[2] = ''

        if input_dics['cut_time_phase']:
            t_start, t_end = calculate_time_phase(event, st_avail)
        else:
            t_start = event['t1']
            t_end = event['t2']

        if input_dics['min_azi'] or input_dics['max_azi'] or \
                input_dics['min_epi'] or input_dics['max_epi']:
            dist, azi, bazi = gps2DistAzimuth(event['latitude'],
                                              event['longitude'],
                                              float(st_avail[4]),
                                              float(st_avail[5]))
            epi_dist = dist/111.194/1000.
            if input_dics['min_epi']:
                if epi_dist < input_dics['min_epi']:
                    raise Exception('%s out of epi range: %s'
                                    % (st_id, epi_dist))
            if input_dics['max_epi']:
                if epi_dist > input_dics['max_epi']:
                    raise Exception('%s out of epi range: %s'
                                    % (st_id, epi_dist))
            if input_dics['min_azi']:
                if azi < input_dics['min_azi']:
                    raise Exception('%s outo f Azimuth range: %s'
                                    % (st_id, azi))
            if input_dics['max_azi']:
                if azi > input_dics['max_azi']:
                    raise Exception('%s out of Azimuth range: %s'
                                    % (st_id, azi))

        if input_dics['waveform']:
            dummy = 'waveform'
            if (not os.path.isfile(os.path.join(target_path, 'raw', st_id))) \
                    or input_dics['force_waveform']:
                client_arclink.saveWaveform(os.path.join(target_path,
                                                         'raw', st_id),
                                            st_avail[0], st_avail[1],
                                            st_avail[2], st_avail[3],
                                            t_start, t_end)
                identifier += 10
                print '%s -- %s -- saving waveform for: %s  ---> DONE' \
                      % (info_station, req_cli, st_id)
            else:
                identifier += 1

        if input_dics['response']:
            dummy = 'response'
            if (not os.path.isfile(os.path.join(target_path, 'resp',
                                                'STXML.' + st_id))) \
                or (not os.path.isfile(os.path.join(target_path, 'resp',
                                                    'DATALESS.' + st_id))) \
                    or input_dics['force_response']:
                client_arclink.saveResponse(
                    os.path.join(target_path, 'resp',
                                 'DATALESS.%s' % st_id),
                    st_avail[0], st_avail[1], st_avail[2], st_avail[3],
                    t_start, t_end)
                identifier += 100
                print "%s -- %s -- saving response for: %s  ---> DONE" \
                      % (info_station, req_cli, st_id)
            else:
                identifier += 1

        if identifier in [0, 2, 10, 11, 100]:
            raise Exception("CODE: %s will not be registered! (666)"
                            % identifier)

        dummy = 'meta-data'
        syn_file = open(os.path.join(target_path, 'info',
                                     'station_event'), 'a')
        syn = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\n' \
              % (st_avail[0], st_avail[1],
                 st_avail[2], st_avail[3],
                 st_avail[4], st_avail[5],
                 float(st_avail[6]),
                 float(st_avail[7]),
                 req_cli,
                 event['event_id'], event['latitude'],
                 event['longitude'], event['depth'],
                 event['magnitude'], identifier)
        syn_file.writelines(syn)
        syn_file.close()

        print "%s -- %s -- saving Metadata for: %s  ---> DONE" \
              % (info_station, req_cli, st_id)

        t22 = datetime.now()
    except Exception as error:
        t22 = datetime.now()

        if len(st_avail) != 0:
            ee = '%s -- %s -- %s -- %s\n' % (req_cli, dummy, st_id, error)
        else:
            ee = '%s: There is no available station for this event.' % req_cli
        Exception_file = open(os.path.join(target_path,
                                           'info', 'exception'), 'a+')
        Exception_file.writelines(ee)
        Exception_file.close()

# ##################### update_sta_ev_file ##################################


def update_sta_ev_file(target_path):
    """
    update the station_event file based on already stored waveforms
    """
    sta_ev_add = os.path.join(target_path, 'info', 'station_event')
    if os.path.isfile(sta_ev_add):
        sta_ev_fi = np.loadtxt(sta_ev_add, delimiter=',', dtype='object')
        if len(sta_ev_fi) > 0:
            if len(np.shape(sta_ev_fi)) == 1:
                sta_ev_fi = np.reshape(sta_ev_fi, [1, len(sta_ev_fi)])
            sta_ev_names = sta_ev_fi[:, 0] + '.' + sta_ev_fi[:, 1] + '.' + \
                           sta_ev_fi[:, 2] + '.' + sta_ev_fi[:, 3]

            sta_saved_path = glob.glob(
                os.path.join(target_path, 'raw', '*.*.*.*'))
            sta_saved_path.sort()
            sta_sorted = []
            for sta_sav_abs in sta_saved_path:
                try:
                    sta_sav = os.path.basename(sta_sav_abs)
                    sta_indx = np.where(sta_ev_names == sta_sav)[0][-1]
                    sta_sorted.append(sta_ev_fi[sta_indx])
                except:
                    continue
            np.savetxt(sta_ev_add, sta_sorted, delimiter=',', fmt='%s')
    else:
        print "[INFO] can not find: %s" % sta_ev_add
        avail_arr = np.loadtxt(os.path.join(target_path, 'info',
                                            'availability.txt'),
                               delimiter=',', dtype='object')
        sta_ev_names = avail_arr[:, 0] + '.' + avail_arr[:, 1] + '.' + \
                       avail_arr[:, 2] + '.' + avail_arr[:, 3]

        sta_saved_path = glob.glob(
            os.path.join(target_path, 'raw', '*.*.*.*'))
        sta_saved_path.sort()
        sta_sorted = []
        for sta_sav_abs in sta_saved_path:
            try:
                sta_sav = os.path.basename(sta_sav_abs)
                sta_indx = np.where(sta_ev_names == sta_sav)[0][-1]
                sta_sorted.append(avail_arr[sta_indx])
            except:
                continue
        np.savetxt(sta_ev_add, sta_sorted[:, :-1], delimiter=',', fmt='%s')

# -------------------------------- TRASH

# to shuffle the stations, we do not need it anymore as we
# parallelize it over the data-sources as well
# all_sta = []
# for req_cli in req_clients:
#     all_sta.append(stas_avail[stas_avail[:, -1] == req_cli])
# all_sta = np.array(list(roundrobin(all_sta)))

# from itertools import cycle, islice
# def roundrobin(iterables):
#     # Recipe credited to George Sakkis
#     pending = len(iterables)
#     nexts = cycle(iter(it).next for it in iterables)
#     while pending:
#         try:
#             for next in nexts:
#                 yield next()
#         except StopIteration:
#             pending -= 1
#     nexts = cycle(islice(nexts, pending))

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
