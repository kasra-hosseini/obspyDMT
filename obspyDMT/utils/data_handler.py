#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  data_handler.py
#   Purpose:   handling data (waveform/response) in obspyDMT
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
import numpy as np
try:
    from obspy.clients.fdsn import Client as Client_fdsn
except Exception, e:
    from obspy.fdsn import Client as Client_fdsn
try:
    from obspy.clients.arclink import Client as Client_arclink
except Exception, e:
    from obspy.arclink import Client as Client_arclink
try:
    from obspy.geodetics.base import gps2dist_azimuth as gps2DistAzimuth
except Exception, e:
    try:
        from obspy.geodetics import gps2DistAzimuth
    except Exception, e:
        from obspy.core.util import gps2DistAzimuth
import os
import pickle

from utility_codes import calculate_time_phase, getFolderSize

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### get_data ###############################


def get_data(stas_avail, event, input_dics):
    """
    get the waveform/response from FDSN and ArcLink
    :param stas_avail:
    :param event:
    :param input_dics:
    :return:
    """
    t_wave_1 = datetime.now()

    req_clients = np.unique(stas_avail[:, -1])
    print "Number of all requested data sources: %s" % len(req_clients)
    print req_clients

    if input_dics['test']:
        stas_avail = stas_avail[0:input_dics['test_num']]

    if input_dics['req_parallel']:
        par_jobs = []
        for req_cli in req_clients:
            st_avail = stas_avail[stas_avail[:, -1] == req_cli]
            if not req_cli.lower() in ['arclink']:
                p = multiprocessing.Process(target=fdsn_waveform,
                                            args=(st_avail, event,
                                                  input_dics, req_cli))
                par_jobs.append(p)
            elif req_cli.lower() == 'arclink':
                p = multiprocessing.Process(target=arc_waveform,
                                            args=(st_avail, event,
                                                  input_dics, req_cli))
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
            st_avail = stas_avail[stas_avail[:, -1] == req_cli]
            if not req_cli.lower() in ['arclink']:
                fdsn_waveform(st_avail, event, input_dics, req_cli)
            elif req_cli.lower() == 'arclink':
                arc_waveform(st_avail, event, input_dics, req_cli)

    print "\n==================="
    print "DONE with Event: %s" % event['event_id']
    print "Time: %s" % (datetime.now() - t_wave_1)
    print "==================="

# ##################### fdsn_waveform ###############################


def fdsn_waveform(stas_avail, event, input_dics, req_cli):
    """
    Gets Waveforms, StationXML files and meta-data from FDSN
    :param stas_avail:
    :param event:
    :param input_dics:
    :param req_cli:
    :return:
    """
    period = '{0:s}_{1:s}'.format(
        input_dics['min_date'].split('T')[0],
        input_dics['max_date'].split('T')[0])
    eventpath = os.path.join(input_dics['datapath'], period)
    target_path = os.path.join(eventpath, event['event_id'])

    if input_dics['bulk']:
        try:
            fdsn_bulk_request(target_path, req_cli, input_dics)
        except Exception as e:
            print 'WARNING: %s' % e
        print 'DONE'

        # Following parameter is set to 'N' to avoid
        # retrieving the waveforms twice
        # When using bulk requests, waveforms are retreived in bulk
        # but not response/StationXML files and not metadata
        input_dics['waveform'] = False
        print '%s bulkdataselect request is done for event: %s' \
              % (req_cli, target_path)

    fdsn_serial_parallel(stas_avail, event, input_dics, target_path, req_cli)

# ##################### fdsn_serial_parallel ##################################


def fdsn_serial_parallel(stas_avail, event, input_dics, target_path, req_cli):
    """
    Retrieving data from FDSN
    :param stas_avail:
    :param event:
    :param input_dics:
    :param target_path:
    :param req_cli:
    :return:
    """
    print '\nEvent: %s' % target_path

    client_fdsn = Client_fdsn(base_url=req_cli,
                              user=input_dics['username'],
                              password=input_dics['password'])

    if input_dics['req_parallel']:
        if input_dics['password']:
            num_req_np = 1
        else:
            num_req_np = input_dics['req_np']
        par_jobs = []
        for st_avail in stas_avail:
            p = multiprocessing.Process(target=fdsn_download_core,
                                        args=(st_avail, event,
                                              input_dics, target_path,
                                              client_fdsn, req_cli))
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
        for st_avail in stas_avail:
            fdsn_download_core(st_avail, event, input_dics, target_path,
                               client_fdsn, req_cli)

    update_sta_ev_file(target_path)

    if input_dics['bulk']:
        input_dics['waveform'] = True
        sta_saved_path = glob.glob(os.path.join(target_path, 'BH_RAW',
                                                '*.*.*.*'))
        print '\nAdjusting the station_event file...',

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
                       client_fdsn, req_cli):
    """
    Downloading the waveforms, reponse files (StationXML) and metadata
    This program should be normally called by some higher-level functions
    :param st_avail:
    :param event:
    :param input_dics:
    :param target_path:
    :param client_fdsn:
    :param req_cli:
    :return:
    """
    dummy = 'Initializing'
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
            if not os.path.isfile(os.path.join(target_path, 'BH_RAW', st_id)):
                client_fdsn.get_waveforms(st_avail[0], st_avail[1],
                                          st_avail[2], st_avail[3],
                                          t_start, t_end,
                                          filename=os.path.join(target_path,
                                                                'BH_RAW',
                                                                st_id))
                identifier += 10
                print '%s -- saving waveform for: %s  ---> DONE' \
                      % (req_cli, st_id)
            else:
                identifier += 1

        if input_dics['response']:
            dummy = 'response'
            if not os.path.isfile(os.path.join(target_path, 'Resp',
                                               'STXML.' + st_id)):
                if not os.path.isfile(os.path.join(target_path, 'Resp',
                                                   'DATALESS.' + st_id)):
                    client_fdsn.get_stations(network=st_avail[0],
                                             station=st_avail[1],
                                             location=st_avail[2],
                                             channel=st_avail[3],
                                             starttime=t_start, endtime=t_end,
                                             filename=os.path.join(
                                                 target_path, 'Resp',
                                                 'STXML.%s' % st_id),
                                             level='response')
                identifier += 100
                print "%s -- saving response for: %s  ---> DONE" \
                      % (req_cli, st_id)
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
                 event['event_id'], event['latitude'],
                 event['longitude'], event['depth'],
                 event['magnitude'], req_cli, identifier)
        syn_file.writelines(syn)
        syn_file.close()

        print "%s -- saving metadata for: %s  ---> DONE" % (req_cli, st_id)

        t22 = datetime.now()
        if input_dics['time_get_data']:
            time_fdsn = t22 - t11
            time_file = open(os.path.join(target_path, 'info',
                                          'time_get_data'), 'a')
            size = getFolderSize(os.path.join(target_path))
            ti = '%s,%s,%s,%s,%s,%s,%s,+,%s,\n' % (st_avail[0],
                                                   st_avail[1],
                                                   st_avail[2],
                                                   st_avail[3],
                                                   time_fdsn.seconds,
                                                   time_fdsn.microseconds,
                                                   size/(1024.**2),
                                                   req_cli)
            time_file.writelines(ti)
            time_file.close()
    except Exception as error:
        t22 = datetime.now()
        if input_dics['time_get_data']:
            time_fdsn = t22 - t11
            time_file = open(os.path.join(target_path, 'info',
                                          'time_get_data'), 'a')
            size = getFolderSize(os.path.join(target_path))
            ti = '%s,%s,%s,%s,%s,%s,%s,-,%s\n' % (st_avail[0],
                                                  st_avail[1],
                                                  st_avail[2],
                                                  st_avail[3],
                                                  time_fdsn.seconds,
                                                  time_fdsn.microseconds,
                                                  size/(1024.**2),
                                                  req_cli)
            time_file.writelines(ti)
            time_file.close()

        if len(st_avail) > 0:
            ee = '%s -- %s -- %s -- %s\n' % (req_cli, dummy, st_id, error)
        else:
            ee = '%s: There is no available station for this event.' % req_cli
        Exception_file = open(os.path.join(target_path,
                                           'info', 'exception'), 'a')
        Exception_file.writelines(ee)
        Exception_file.close()

# ##################### fdsn_bulk_request ##################################


def fdsn_bulk_request(target_path, req_cli, input_dics):
    """
    Send bulk request to FDSN
    :param target_path:
    :param req_cli:
    :param input_dics:
    :return:
    """
    print '\nSending bulk request to: %s' % req_cli
    client_fdsn = Client_fdsn(base_url=req_cli,
                              user=input_dics['username'],
                              password=input_dics['password'])
    bulk_list_fio = open(os.path.join(target_path, 'info',
                                      'bulkdata_list_%s' % req_cli))
    bulk_list = pickle.load(bulk_list_fio)
    bulk_smgrs = client_fdsn.get_waveforms_bulk(bulk_list)
    print 'Saving the retrieved waveforms...',
    for bulk_st in bulk_smgrs:
        bulk_st.write(os.path.join(target_path, 'BH_RAW',
                                   '%s.%s.%s.%s'
                                   % (bulk_st.stats['network'],
                                      bulk_st.stats['station'],
                                      bulk_st.stats['location'],
                                      bulk_st.stats['channel'])),
                      'MSEED')

# ##################### arc_waveform ###############################


def arc_waveform(stas_avail, event, input_dics, req_cli):
    """
    Gets Waveforms, StationXML files and meta-data from FDSN
    :param stas_avail:
    :param event:
    :param input_dics:
    :param req_cli:
    :return:
    """
    t_wave_1 = datetime.now()

    period = '{0:s}_{1:s}'.format(
        input_dics['min_date'].split('T')[0],
        input_dics['max_date'].split('T')[0])
    eventpath = os.path.join(input_dics['datapath'], period)
    target_path = os.path.join(eventpath, event['event_id'])

    arc_serial_parallel(stas_avail, event, input_dics, target_path, req_cli)

# ##################### arc_serial_parallel ##################################


def arc_serial_parallel(stas_avail, event, input_dics, target_path, req_cli):
    """
    Retrieving data from ArcLink
    """
    print '\nEvent: %s' % target_path

    client_arclink = Client_arclink(user='test@obspy.org',
                                    timeout=input_dics['arc_wave_timeout'])

    if input_dics['req_parallel']:
        par_jobs = []
        for st_avail in stas_avail:
            p = multiprocessing.Process(target=arc_download_core,
                                        args=(st_avail, event,
                                              input_dics, target_path,
                                              client_arclink, req_cli))
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
        for st_avail in stas_avail:
            arc_download_core(st_avail, event, input_dics, target_path,
                              client_arclink, req_cli)

# ##################### arc_download_core ##################################


def arc_download_core(st_avail, event, input_dics, target_path,
                      client_arclink, req_cli):
    """
    Downloading the waveforms, reponse files (StationXML) and metadata
    This program should be normally called by some higher-level functions
    """
    dummy = 'Initializing'
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
            if not os.path.isfile(os.path.join(target_path, 'BH_RAW', st_id)):
                client_arclink.saveWaveform(os.path.join(target_path,
                                                         'BH_RAW', st_id),
                                            st_avail[0], st_avail[1],
                                            st_avail[2], st_avail[3],
                                            t_start, t_end)
                identifier += 10
                print '%s -- saving waveform for: %s  ---> DONE' \
                      % (req_cli, st_id)
            else:
                identifier += 1

        if input_dics['response']:
            dummy = 'response'
            if not os.path.isfile(os.path.join(target_path, 'Resp',
                                               'STXML.' + st_id)):
                if not os.path.isfile(os.path.join(target_path, 'Resp',
                                                   'DATALESS.' + st_id)):
                    client_arclink.saveResponse(
                        os.path.join(target_path, 'Resp',
                                     'DATALESS.%s' % st_id),
                        st_avail[0], st_avail[1], st_avail[2], st_avail[3],
                        t_start, t_end)
                identifier += 100
                print "%s -- saving response for: %s  ---> DONE" \
                      % (req_cli, st_id)
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
                 event['event_id'], event['latitude'],
                 event['longitude'], event['depth'],
                 event['magnitude'], req_cli, identifier)
        syn_file.writelines(syn)
        syn_file.close()

        print "%s -- saving Metadata for: %s  ---> DONE" % (req_cli, st_id)

        t22 = datetime.now()
        if input_dics['time_get_data']:
            time_fdsn = t22 - t11
            time_file = open(os.path.join(target_path, 'info',
                                          'time_get_data'), 'a')
            size = getFolderSize(os.path.join(target_path))
            ti = '%s,%s,%s,%s,%s,%s,%s,+,%s,\n' % (st_avail[0],
                                                   st_avail[1],
                                                   st_avail[2],
                                                   st_avail[3],
                                                   time_fdsn.seconds,
                                                   time_fdsn.microseconds,
                                                   size/(1024.**2),
                                                   req_cli)
            time_file.writelines(ti)
            time_file.close()
    except Exception as error:
        t22 = datetime.now()
        if input_dics['time_get_data']:
            time_fdsn = t22 - t11
            time_file = open(os.path.join(target_path, 'info',
                                          'time_get_data'), 'a')
            size = getFolderSize(os.path.join(target_path))
            ti = '%s,%s,%s,%s,%s,%s,%s,-,%s,\n' % (st_avail[0],
                                                   st_avail[1],
                                                   st_avail[2],
                                                   st_avail[3],
                                                   time_fdsn.seconds,
                                                   time_fdsn.microseconds,
                                                   size/(1024.**2),
                                                   req_cli)
            time_file.writelines(ti)
            time_file.close()

        if len(st_avail) != 0:
            ee = '%s -- %s -- %s -- %s\n' % (req_cli, dummy, st_id, error)
        else:
            ee = '%s: There is no available station for this event.' % req_cli
        Exception_file = open(os.path.join(target_path,
                                           'info', 'exception'), 'a')
        Exception_file.writelines(ee)
        Exception_file.close()

# ##################### update_sta_ev_file ##################################


def update_sta_ev_file(target_path):
    """
    Update the station event file based on already stored waveforms
    """
    sta_ev_add = os.path.join(target_path, 'info', 'station_event')
    if os.path.isfile(sta_ev_add):
        sta_ev_fi = np.loadtxt(sta_ev_add, delimiter=',', dtype='object')
        if len(sta_ev_fi) > 0:
            sta_ev_names = sta_ev_fi[:, 0] + '.' + sta_ev_fi[:, 1] + '.' + \
                           sta_ev_fi[:, 2] + '.' + sta_ev_fi[:, 3]
            sta_saved_path = glob.glob(
                os.path.join(target_path, 'BH_RAW', '*.*.*.*'))
            sta_saved_path.sort()
            sta_sorted = []
            for sta_sav_abs in sta_saved_path:
                try:
                    sta_sav = os.path.basename(sta_sav_abs)
                    sta_indx = np.where(sta_ev_names == sta_sav)[0][-1]
                    sta_sorted.append(sta_ev_fi[sta_indx])
                except Exception, e:
                    continue
            np.savetxt(sta_ev_add, sta_sorted, delimiter=',', fmt='%s')
    else:
        print "[DATA] Can not find: %s" % sta_ev_add
        avail_arr = np.loadtxt(os.path.join(target_path, 'info',
                                            'availability.txt'),
                               delimiter=',', dtype='object')
        sta_ev_names = avail_arr[:, 0] + '.' + avail_arr[:, 1] + '.' + \
                       avail_arr[:, 2] + '.' + avail_arr[:, 3]
        sta_saved_path = glob.glob(
            os.path.join(target_path, 'BH_RAW', '*.*.*.*'))
        sta_saved_path.sort()
        sta_sorted = []
        for sta_sav_abs in sta_saved_path:
            try:
                sta_sav = os.path.basename(sta_sav_abs)
                sta_indx = np.where(sta_ev_names == sta_sav)[0][-1]
                sta_sorted.append(avail_arr[sta_indx])
            except Exception, e:
                continue
        np.savetxt(sta_ev_add, sta_sorted, delimiter=',', fmt='%s')

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
