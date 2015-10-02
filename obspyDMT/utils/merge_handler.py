#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  merge_handler.py
#   Purpose:   handling merging mode in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import fnmatch
from obspy.core import read
import os

from event_handler import quake_info
from utility_codes import read_station_event

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### FDSN_ARC_merge ##################################


def FDSN_ARC_merge(input_dics, clients):
    """
    Call "merge_stream" function that merges the retrieved waveforms in
    continuous request
    :param input_dics:
    :param clients:
    :return:
    """
    print '\n*****************************'
    print '%s -- Merging the waveforms' % clients
    print '*****************************'
    # Following two if-conditions create address to which merging
    # should be applied
    # Please note that these two conditions can not happen at the same time
    address = None
    network_name = None
    BH_file = None
    if clients == 'arc':
        clients_name = 'arc'
    else:
        clients_name = 'fdsn'
    if input_dics[clients_name + '_merge_auto'] == 'Y':
        period = '{0:s}_{1:s}'.\
            format(input_dics['min_date'].split('T')[0],
                   input_dics['max_date'].split('T')[0])
        address = os.path.join(input_dics['datapath'], period)

    if input_dics[clients_name + '_merge'] != 'N':
        address = input_dics[clients_name + '_merge']

    events, address_events = quake_info(address, 'info')

    ls_saved_stas_tmp = []
    for i in range(len(events)):
        sta_ev = read_station_event(address_events[i])
        # initialize some parameters which will be used later in merge_stream
        for s_ev in sta_ev[0]:
            if input_dics[clients_name + '_merge_auto'] == 'Y':
                if clients == s_ev[13]:
                    network, network_name, BH_file = \
                        init_merging(input_dics, s_ev[0])
                    station_id = '%s.%s.%s.%s' % (network, s_ev[1],
                                                  s_ev[2], s_ev[3])
                    ls_saved_stas_tmp.append(
                        os.path.join(address_events[i], BH_file, station_id))

            else:
                network, network_name, BH_file = \
                    init_merging(input_dics, s_ev[0])
                station_id = '%s.%s.%s.%s' % (network, s_ev[1],
                                              s_ev[2], s_ev[3])
                ls_saved_stas_tmp.append(
                    os.path.join(address_events[i], BH_file, station_id))

    if not input_dics['net'].startswith('_'):
        pattern_sta = '%s.%s.%s.%s' % (input_dics['net'], input_dics['sta'],
                                       input_dics['loc'], input_dics['cha'])
    else:
        pattern_sta = '*.%s.%s.%s' % (input_dics['sta'], input_dics['loc'],
                                      input_dics['cha'])

    ls_saved_stas = []
    for saved_sta in ls_saved_stas_tmp:
        if fnmatch.fnmatch(os.path.basename(saved_sta), pattern_sta):
            ls_saved_stas.append(saved_sta)

    if len(ls_saved_stas) != 0:
        saved_stations_names = []
        for ls_saved_sta in ls_saved_stas:
            saved_stations_names.append(os.path.basename(ls_saved_sta))
        ls_sta = list(set(saved_stations_names))

        ls_address = []
        for add_ev in address_events:
            ls_address.append(os.path.join(add_ev, BH_file))
        print 'Merging the waveforms...'
        merge_stream(input_dics=input_dics, ls_address=ls_address,
                     ls_sta=ls_sta, network_name=network_name)
        print 'Finish merging the waveforms'
    else:
        print "\nThere is no waveform to merge!"

# ##################### merge_stream ####################################


def merge_stream(input_dics, ls_address, ls_sta, network_name):
    """
    merges the waveforms in continuous requests
    Merging technique: (method=1)
    Discard data of the previous trace assuming the following trace
    contains data with a more correct time value.
    The parameter interpolation_samples specifies the number of samples used
    to linearly interpolate between
    the two traces in order to prevent steps.
    Note that if there are gaps inside, the returned array is still
    a masked array, only if fill_value is set,
    the returned array is a normal array and gaps are filled with fill value.
    No interpolation (interpolation_samples=0):

    Trace 1: AAAAAAAA
    Trace 2:     FFFFFFFF
    1 + 2  : AAAAFFFFFFFF

    :param input_dics:
    :param ls_address:
    :param ls_sta:
    :param network_name:
    :return:
    """
    address = os.path.dirname(os.path.dirname(ls_address[0]))

    try:
        os.makedirs(os.path.join(address, 'MERGED-%s' % network_name))
    except Exception as e:
        print "ERROR in creating a directory in %s" % address
        print e
        pass

    for sta in ls_sta:
        for j in range(len(ls_address)):
            if os.path.isfile(os.path.join(ls_address[j], sta)):
                st = read(os.path.join(ls_address[j], sta))
                for k in range(j+1, len(ls_address)):
                    try:
                        tr_tmp = read(os.path.join(ls_address[k], sta))
                        if len(tr_tmp) > 1:
                            print "\n=== WARNING:"
                            print "%s" % os.path.join(ls_address[k], sta)
                            print "probably has some gaps!"
                            print "It will be merged (fill_value=0)."
                            print "\nFor more information refer to:"
                            print "%s" % os.path.join(ls_address[k],
                                                      os.path.pardir,
                                                      'info',
                                                      'waveform_gap.txt')
                            print "which contains all the waveforms " \
                                  "with gap."

                            tr_tmp.merge(method=1, fill_value=0,
                                         interpolation_samples=0)
                            gap_fio = open(os.path.join(ls_address[k],
                                                        os.path.pardir,
                                                        'info',
                                                        'waveform_gap.txt'),
                                           'a+')
                            gap_msg = '%s.%s.%s.%s\t%s\n' \
                                      % (tr_tmp[0].stats.network,
                                         tr_tmp[0].stats.station,
                                         tr_tmp[0].stats.location,
                                         tr_tmp[0].stats.channel,
                                         'pre-merge')
                            gap_fio.writelines(gap_msg)
                            gap_fio.close()
                        st.append(tr_tmp[0])
                    except Exception as e:
                        print "ERROR: can not append to the trace! \n%s" % e

                try:
                    st.merge(method=1, fill_value=0, interpolation_samples=0)
                    trace = st[0]
                    trace_identity = '%s.%s.%s.%s' % (trace.stats['network'],
                                                      trace.stats['station'],
                                                      trace.stats['location'],
                                                      trace.stats['channel'])
                except Exception as e:
                    print "ERROR in merging: %s" % sta 
                    print e
                    continue

                if input_dics['mseed'] == 'N':
                    st.write(os.path.join(address, 'MERGED-%s'
                                          % network_name, trace_identity),
                             format='SAC')
                else:
                    st.write(os.path.join(address, 'MERGED-%s'
                                          % network_name, trace_identity),
                             format='MSEED')
                break

# ##################### init_merging ####################################


def init_merging(input_dics, net_name):
    """
    Create required variables for merging
    """
    network_name = None
    network = None
    BH_file = None

    if input_dics['merge_type'] == 'raw':
        BH_file = 'BH_RAW'
        network = net_name
        network_name = 'raw'
    elif input_dics['merge_type'] == 'corrected':
        if input_dics['corr_unit'] == 'DIS':
            BH_file = 'BH'
            network = 'dis.%s' % net_name
            network_name = 'dis'
        elif input_dics['corr_unit'] == 'VEL':
            BH_file = 'BH_' + input_dics['corr_unit']
            network = 'vel.%s' % net_name
            network_name = 'vel'
        elif input_dics['corr_unit'] == 'ACC':
            BH_file = 'BH_' + input_dics['corr_unit']
            network = 'acc.%s' % net_name
            network_name = 'acc'
    return network, network_name, BH_file
