#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  update_handler.py
#   Purpose:   handling update mode in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import copy
from datetime import datetime
import os

from arclink_handler import ARC_available, ARC_waveform
from event_handler import quake_info
from fdsn_handler import FDSN_available, FDSN_waveform
from utility_codes import read_station_event, read_list_stas

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### FDSN_update #####################################


def FDSN_update(input_dics, address):
    """
    Initialize directories and pass the required stations
    (removing the duplications) for FDSN update requests
    :param input_dics:
    :param address:
    :return:
    """
    print '\n*********************'
    print 'FDSN -- Updating Mode'
    print '*********************'
    t_update_1 = datetime.now()

    events, address_events = quake_info(address, 'info')

    for i in range(len(events)):
        if not input_dics['list_stas']:
            Stas_fdsn = FDSN_available(input_dics, events[i],
                                       address_events[i], event_number=i)
        else:
            Stas_fdsn = read_list_stas(input_dics['list_stas'],
                                       input_dics['normal_mode_syn'],
                                       input_dics['specfem3D'])

        if input_dics['fdsn_bulk'] != 'Y':
            print '\n%s-Availability for event: %s/%s ---> DONE' \
                  % (input_dics['fdsn_base_url'], i+1, len(events))
        else:
            print '\nFDSN-bulkfile for event: %s/%s ---> DONE' \
                  % (i+1, len(events))

        if Stas_fdsn != [[]]:
            Stas_req = rm_duplicate(Stas_fdsn,
                                    address=os.path.join(address_events[i]))
        else:
            Stas_req = None
            print '------------------------------'
            print 'There is no available station!'
            print '------------------------------'

        if not os.path.isdir(os.path.join(address_events[i], 'BH_RAW')):
            os.makedirs(os.path.join(address_events[i], 'BH_RAW'))

        if Stas_req:
            FDSN_waveform(input_dics, events, Stas_req, i, req_type='update')
        else:
            print '\nNo available station in %s for your request!' \
                  % input_dics['fdsn_base_url']
            print 'Check the next event...'
            continue

    print '\nTotal time for updating FDSN: %s' % (datetime.now() - t_update_1)

# ##################### ARC_update ######################################


def ARC_update(input_dics, address):
    """
    Initialize directories and pass the required stations
    (removing the duplications) for ArcLink update requests
    :param input_dics:
    :param address:
    :return:
    """
    print '\n************************'
    print 'ArcLink -- Updating Mode'
    print '************************'
    t_update_1 = datetime.now()

    events, address_events = quake_info(address, 'info')

    for i in range(len(events)):
        if not input_dics['list_stas']:
            Stas_arc = ARC_available(input_dics, events[i],
                                     address_events[i], event_number=i)
        else:
            Stas_arc = read_list_stas(input_dics['list_stas'],
                                      input_dics['normal_mode_syn'],
                                      input_dics['specfem3D'])

        print '\nArcLink-Availability for event: %s/%s ---> DONE' \
              % (i+1, len(events))

        if Stas_arc != [[]]:
            Stas_req = rm_duplicate(Stas_arc,
                                    address=os.path.join(address_events[i]))
        else:
            Stas_req = None
            print '------------------------------'
            print 'There is no available station!'
            print '------------------------------'

        if not os.path.isdir(os.path.join(address_events[i], 'BH_RAW')):
            os.makedirs(os.path.join(address_events[i], 'BH_RAW'))

        if Stas_req:
            ARC_waveform(input_dics, events, Stas_req, i, req_type='update')
        else:
            print '\nNo available station in ArcLink for your request!'
            print 'Check the next event...'
            continue

    print '\nTotal time for updating ArcLink: %s' \
          % (datetime.now() - t_update_1)

# ##################### rm_duplicate ####################################


def rm_duplicate(all_sta_avail, address):
    """
    remove duplicates and give back the required list for updating
    """

    id_avai_stas = []
    for sta in all_sta_avail:
        if sta[2] == '--' or sta[2] == '  ':
            sta[2] = ''
        if len(sta) == 7:
            id_avai_stas.append('%s_%s_%s_%s_%s_%s_%s'
                                % (sta[0], sta[1], sta[2], sta[3],
                                   sta[4], sta[5], sta[6]))
        elif len(sta) == 8:
            id_avai_stas.append('%s_%s_%s_%s_%s_%s_%s_%s'
                                % (sta[0], sta[1], sta[2], sta[3],
                                   sta[4], sta[5], sta[6], sta[7]))

    sta_ev_saved = read_station_event(address)

    id_all_saved_stas = []
    for saved_sta in sta_ev_saved[0]:
        id_all_saved_stas.append('%s_%s_%s_%s' % (saved_sta[0], saved_sta[1],
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
        stas_update[i] = stas_update[i].split('_')

    stas_update.sort()
    print '------------------------------------------'
    print 'Info:'
    print 'Number of all saved stations:     %s' % len(id_all_saved_stas)
    print 'Number of all available stations: %s' % len(id_avai_stas)
    print 'Number of stations to update for: %s' % len(stas_update)
    print '------------------------------------------'

    return stas_update
