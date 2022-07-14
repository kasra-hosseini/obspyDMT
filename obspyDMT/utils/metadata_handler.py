#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  metadata_handler.py
#   Purpose:   handling metadata in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from __future__ import print_function
import copy
from datetime import datetime
from glob import glob
import numpy as np
from obspy import UTCDateTime
try:
    from obspy.clients.fdsn import Client as Client_fdsn
except:
    from obspy.fdsn import Client as Client_fdsn
try:
    from obspy.clients.fdsn import RoutingClient
except:
    print("[WARNING] RoutingClient could not be imported.")
try:
    from obspy.geodetics import locations2degrees
except:
    from obspy.core.util import locations2degrees
import os
import pickle

from .utility_codes import create_folders_files
from .utility_codes import print_data_sources
from .utility_codes import read_list_stas, calculate_time_phase
from .utility_codes import read_station_event

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# ###################### get_metadata ####################################


def get_metadata(input_dics, event, info_avail):
    """
    retrieve meta-data information.
    :param input_dics:
    :param event:
    :param info_avail:
    :return:
    """
    print('\n=============')
    print('metadata mode')
    print('=============')

    eventpath = os.path.join(input_dics['datapath'])

    t_1 = datetime.now()
    print('initializing files and directories...', end='')
    create_folders_files(event, eventpath, input_dics)
    print('DONE')

    target_path = os.path.join(eventpath, event['event_id'])

    stas_all = []
    if not input_dics['list_stas']:
        stas_cli = []
        for cl in range(len(input_dics['data_source'])):
            try:
                stas_cli = fdsn_available(input_dics, cl,
                                          event, target_path)
            except Exception as exp:
                print('\nERROR: %s is not implemented! \n%s' \
                      % (input_dics['data_source'][cl], exp))
                print_data_sources()
            # put all the available stations together
            for st_fdarc in stas_cli:
                if len(st_fdarc) == 0:
                    continue
                elif len(st_fdarc) == 1:
                    stas_all.append([st_fdarc])
                else:
                    stas_all.append(st_fdarc)
    else:
        stas_all = read_list_stas(input_dics['list_stas'],
                                  input_dics['normal_mode_syn'],
                                  input_dics['specfem3D'])
        if input_dics['bulk']:
            fdsn_create_bulk_list(target_path, input_dics,
                                  stas_all, event)

    stas_arr = np.array(stas_all)
    np.save(os.path.join(target_path, 'info', 'availability'), stas_arr)

    avail_add_all = os.path.join(target_path, 'info', 'availability.txt')
    avail_fi = open(avail_add_all, 'ab')
    np.savetxt(avail_fi, stas_arr, delimiter=',', fmt='%s')
    avail_fi.close()

    saved_avail = np.loadtxt(avail_add_all, delimiter=',',
                             dtype=bytes, ndmin=2).astype(str)
    saved_avail = saved_avail.astype(object)
    unique_avail = []
    if len(saved_avail) >= 1:
        unique_avail = unique_rows_avail(saved_avail)
        avail_fi = open(avail_add_all, 'wb')
        np.savetxt(avail_fi, unique_avail, delimiter=',', fmt='%s')
        avail_fi.close()

    avail_add_cur = os.path.join(
        target_path, 'info', 'availability_%05i.txt'
                             % len(glob(os.path.join(target_path,
                                                     'info',
                                                     'availab*.txt'))))
    avail_fi = open(avail_add_cur, 'wb')
    np.savetxt(avail_fi, stas_arr, delimiter=',', fmt='%s')
    avail_fi.close()

    saved_avail = np.loadtxt(avail_add_cur, delimiter=',',
                             dtype=bytes, ndmin=2).astype(str)
    saved_avail = saved_avail.astype(object)
    unique_avail = []
    if len(saved_avail) >= 1:
        unique_avail = unique_rows_avail(saved_avail)
        avail_fi = open(avail_add_cur, 'wb')
        np.savetxt(avail_fi, unique_avail, delimiter=',', fmt='%s')
        avail_fi.close()

    # XXX remove duplications
    # if (not input_dics['force_waveform']) \
    #         and (not input_dics['force_response']):
    #     stas_update = rm_duplicate(stas_all, target_path)
    #     stas_arr_update = np.array(stas_update)
    # else:
    stas_arr_update = np.array(unique_avail)

    if not input_dics['bulk']:
        print('\navailability for event: %s ---> DONE' % info_avail)
    else:
        print('\nbulkfile for event: %s ---> DONE' % info_avail)

    print('Time for checking the availability: %s' \
          % (datetime.now() - t_1))

    return stas_arr_update

# ##################### unique_rows_avail ##################################


def unique_rows_avail(av):
    """
    unique (row-wise) the availability array
    :param av:
    :return:
    """
    av_hash = av[:, 0] + '#' + av[:, 1] + '#' + av[:, 2] + '#' +\
              av[:, 3] + '#' + av[:, 8]
    av_hash_unique, av_indx = np.unique(av_hash, return_index=True)
    return av[av_indx]

# ##################### fdsn_available ##################################


def fdsn_available(input_dics, cl, event, target_path):
    """
    check the availablity of FDSN stations
    :param input_dics:
    :param cl:
    :param event:
    :param target_path:
    :return:
    """
    print("check the availability: %s" % input_dics['data_source'][cl])

    if input_dics['username_fdsn']:
        include_restricted = True
    else:
        include_restricted = None

    sta_fdsn = []
    try:
        if input_dics['data_source'][cl].lower() in ["iris-federator", "eida-routing"]:
            client_fdsn = RoutingClient(input_dics['data_source'][cl].lower())

            available = client_fdsn.get_stations(
                network=input_dics['net'],
                station=input_dics['sta'],
                location=input_dics['loc'],
                channel=input_dics['cha'],
                starttime=event['t1'],
                endtime=event['t2'],
                level='channel')

        else:
            client_fdsn = Client_fdsn(
                base_url=input_dics['data_source'][cl].upper(),
                user=input_dics['username_fdsn'],
                password=input_dics['password_fdsn'])

            available = client_fdsn.get_stations(
                network=input_dics['net'],
                station=input_dics['sta'],
                location=input_dics['loc'],
                channel=input_dics['cha'],
                starttime=event['t1'],
                endtime=event['t2'],
                latitude=input_dics['lat_cba'],
                longitude=input_dics['lon_cba'],
                minradius=input_dics['mr_cba'],
                maxradius=input_dics['Mr_cba'],
                minlatitude=input_dics['mlat_rbb'],
                maxlatitude=input_dics['Mlat_rbb'],
                minlongitude=input_dics['mlon_rbb'],
                maxlongitude=input_dics['Mlon_rbb'],
                includerestricted=include_restricted,
                level='channel')

        for network in available.networks:
            for station in network:
                for channel in station:
                    st_id = '%s_%s_%s_%s' % (network.code,
                                             station.code,
                                             channel.location_code,
                                             channel.code)
                    sta_fdsn.append([network.code, station.code,
                                     channel.location_code, channel.code,
                                     channel.latitude, channel.longitude,
                                     channel.elevation, channel.depth,
                                     input_dics['data_source'][cl], st_id,
                                     channel.azimuth, channel.dip])

        if input_dics['bulk']:
            print('creating a list for bulk request...')
            bulk_list = []
            for bulk_sta in sta_fdsn:
                if input_dics['cut_time_phase']:
                    t_start, t_end = calculate_time_phase(event, bulk_sta)
                else:
                    t_start = event['t1']
                    t_end = event['t2']
                bulk_list.append((bulk_sta[0], bulk_sta[1], bulk_sta[2],
                                  bulk_sta[3], t_start, t_end))

            bulk_list_fio = open(os.path.join(
                target_path, 'info',
                'bulkdata_list_%s' % input_dics['data_source'][cl]), 'ab+')
            pickle.dump(bulk_list, bulk_list_fio, protocol=2)
            bulk_list_fio.close()

    except Exception as error:
        exc_file = open(os.path.join(target_path, 'info', 'exception'), 'at+')
        ee = 'availability -- %s -- %s\n' % (input_dics['data_source'][cl],
                                             error)
        exc_file.writelines(ee)
        exc_file.close()
        print('ERROR: %s' % ee)
        return []

    if len(sta_fdsn) == 0:
        sta_fdsn = []
    sta_fdsn.sort()
    return sta_fdsn


# ##################### fdsn_create_bulk_list ###############################


def fdsn_create_bulk_list(target_path, input_dics, stas_all, event):
    """
    create bulkdata_list in case of --list_stas flag
    :param target_path:
    :param input_dics:
    :param stas_all:
    :param event:
    :return:
    """
    print('creating a list for bulk request...')
    bulk_list = []
    for bulk_sta in stas_all:
        if input_dics['cut_time_phase']:
            t_start, t_end = calculate_time_phase(event, bulk_sta)
        else:
            t_start = event['t1']
            t_end = event['t2']
        bulk_list.append((bulk_sta[0], bulk_sta[1], bulk_sta[2],
                          bulk_sta[3], t_start, t_end))

    bulk_list_fio = open(os.path.join(target_path, 'info',
                                      'bulkdata_list_local'), 'ab+')
    pickle.dump(bulk_list, bulk_list_fio, protocol=2)
    bulk_list_fio.close()

# ##################### rm_duplicate ####################################


def rm_duplicate(all_sta_avail, address):
    """
    read already retrieved channels, compare them with the availability,
    remove the duplications and give back the remainings
    """
    id_avai_stas = []
    for sta in all_sta_avail:
        if sta[2] == '--' or sta[2] == '  ':
            sta[2] = ''
        id_avai_stas.append('%s#%s#%s#%s#%s#%s#%s#%s#%s#%s'
                            % (sta[0], sta[1], sta[2], sta[3],
                               sta[4], sta[5], sta[6], sta[7],
                               sta[8], sta[9]))

    sta_ev_saved = read_station_event(address)

    id_all_saved_stas = []
    for saved_sta in sta_ev_saved[0]:
        id_all_saved_stas.append('%s#%s#%s#%s' % (saved_sta[0], saved_sta[1],
                                                  saved_sta[2], saved_sta[3]))

    stas_update = copy.deepcopy(id_avai_stas)
    del_num = []
    for saved_sta in id_all_saved_stas:
        for j in range(len(stas_update)):
            if saved_sta in stas_update[j]:
                del_num.append(j)

    del_num.sort(reverse=True)
    for dn in del_num:
        del stas_update[dn]

    for i in range(len(stas_update)):
        stas_update[i] = stas_update[i].split('#')

    stas_update.sort()
    print('------------------------------------------')
    print('Info:')
    print('Number of all saved stations:     %s' % len(id_all_saved_stas))
    print('Number of all available stations: %s' % len(id_avai_stas))
    print('Number of stations to update for: %s' % len(stas_update))
    print('------------------------------------------')

    return stas_update
