#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  instrument_handler.py
#   Purpose:   handling instrument correction in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from datetime import datetime
import fnmatch
import multiprocessing
from obspy.core import read
from obspy import read_inventory
try:
    from obspy.io.xseed import Parser
except Exception, e:
    from obspy.xseed import Parser
import os
import sys

from event_handler import quake_info
from resample_handler import resample_trace
from utility_codes import read_station_event, check_par_jobs

# ##################### FDSN_ARC_IC #####################################


def FDSN_ARC_IC(input_dics, clients):
    """
    Call "inst_correct" function based on the request.
    Group the stations that have been retrieved from specific client
    Grouping is necessary in applying the instrument correction correctly
    (different clients are treated differently)
    :param input_dics:
    :param clients:
    :return:
    """
    print '\n*****************************'
    print '%s -- Instrument Correction' % clients
    print '*****************************'
    # Following two if-conditions create address to which
    # instrument correction should be applied
    # Please note that these two conditions can not happen at the same time
    address = None
    if clients == 'arc':
        clients_name = 'arc'
    else:
        clients_name = 'fdsn'
    if input_dics[clients_name + '_ic_auto'] == 'Y':
        period = '{0:s}_{1:s}'.\
            format(input_dics['min_date'].split('T')[0],
                   input_dics['max_date'].split('T')[0])
        address = os.path.join(input_dics['datapath'], period)

    if input_dics['fdsn_update'] != 'N':
        address = os.path.join(input_dics['datapath'])

    if input_dics['arc_update'] != 'N':
        address = os.path.join(input_dics['datapath'])

    if input_dics[clients_name + '_ic'] != 'N':
        address = input_dics[clients_name + '_ic']

    events, address_events = quake_info(address, 'info')

    for i in range(len(events)):
        sta_ev = read_station_event(address_events[i])
        ls_saved_stas_tmp = []
        for s_ev in sta_ev[0]:
            if clients.lower() == 'all_fdsn':
                if not s_ev[13].lower() == 'arc':
                    station_id = '%s.%s.%s.%s' % (s_ev[0], s_ev[1],
                                                  s_ev[2], s_ev[3])
                    ls_saved_stas_tmp.append(
                        os.path.join(address_events[i], 'BH_RAW', station_id))
            elif clients.lower() == s_ev[13].lower():
                station_id = '%s.%s.%s.%s' % (s_ev[0], s_ev[1],
                                              s_ev[2], s_ev[3])
                ls_saved_stas_tmp.append(
                    os.path.join(address_events[i], 'BH_RAW', station_id))

        if input_dics['net'].startswith('_'):
            net_pat = '*'
        else:
            net_pat = input_dics['net']

        ls_saved_stas = []
        for net_iter in net_pat.split(','):
            for sta_iter in input_dics['sta'].split(','):
                for loc_iter in input_dics['loc'].split(','):
                    for cha_iter in input_dics['cha'].split(','):
                        pattern_sta = '%s.%s.%s.%s' % (net_iter, sta_iter,
                                                       loc_iter, cha_iter)
                        for saved_sta in ls_saved_stas_tmp:
                            if fnmatch.fnmatch(os.path.basename(saved_sta),
                                               pattern_sta):
                                ls_saved_stas.append(saved_sta)

        if len(ls_saved_stas) != 0:
            print '\nevent: %s/%s -- %s\n' % (i+1, len(events), clients)
            inst_correct(input_dics, ls_saved_stas, address_events[i], clients)
        else:
            print "There is no station in the directory to correct!"
            print "Address: %s" % address_events[i]
    # pass address for using in create_tar_file
    return address

# ##################### inst_correct ###############################


def inst_correct(input_dics, ls_saved_stas, address, clients):
    """
    Apply Instrument Coorection on all available stations in the folder

    Instrument Correction has three main steps:
        1) RTR: remove the trend
        2) tapering
        3) pre-filtering and deconvolution of Resp file from Raw counts

    Remove the instrument type by deconvolution using spectral division.
    :param input_dics:
    :param ls_saved_stas:
    :param address:
    :param clients:
    :return:
    """
    t_inst_1 = datetime.now()

    if not input_dics['corr_unit'] in ['DIS', 'VEL', 'ACC']:
        sys.exit('ERROR: %s can not be recognized.\n'
                 'Available options: DIS, VEL, ACC' % input_dics['corr_unit'])
    if input_dics['corr_unit'] == 'DIS':
        BH_file = 'BH'
    else:
        BH_file = 'BH_' + input_dics['corr_unit']

    try:
        os.makedirs(os.path.join(address, BH_file))
    except Exception as e:
        print "\nWARNING: can not create %s" % os.path.join(address, BH_file)
        print "%s\n" % e
        pass

    ic_serial_parallel(input_dics, ls_saved_stas, clients, address, BH_file)
    t_inst_2 = datetime.now()

    if input_dics['ic_parallel'] == 'Y':
        ic_reporter(input_dics, address, clients, ls_saved_stas, t_inst_1,
                    t_inst_2)

    print '\nTime for instrument correction of %s channels: %s' \
          % (len(ls_saved_stas), t_inst_2-t_inst_1)

# ##################### ic_serial_parallel ###################################


def ic_serial_parallel(input_dics, ls_saved_stas, clients, address, BH_file):
    """
    instrument correction in serial/parallel
    :param input_dics:
    :param ls_saved_stas:
    :param clients:
    :param address:
    :param BH_file:
    :return:
    """

    if input_dics['ic_parallel'] == 'Y':
        print '\nParallel instrument correction with %s processes.\n' \
              % input_dics['ic_np']

        start = 0
        end = len(ls_saved_stas)
        step = (end - start) / input_dics['ic_np'] + 1

        jobs = []
        for index in xrange(input_dics['ic_np']):
            starti = start + index * step
            endi = min(start + (index + 1) * step, end)
            print starti, endi
            p = multiprocessing.Process(target=IC_core_iterate,
                                        args=(input_dics, ls_saved_stas,
                                              clients, address, BH_file,
                                              starti, endi))
            jobs.append(p)
        for i in range(len(jobs)):
            jobs[i].start()
        check_par_jobs(jobs)

    else:
        for i in range(len(ls_saved_stas)):
            IC_core(input_dics=input_dics, ls_saved_sta=ls_saved_stas[i],
                    clients=clients, address=address, BH_file=BH_file,
                    inform='%s -- %s/%s' % (clients, i+1, len(ls_saved_stas)))

# ##################### IC_core_iterate ######################################


def IC_core_iterate(input_dics, ls_saved_stas, clients, address, BH_file,
                    starti, endi):
    """
    Simple iterator over IC_core Designed to be used for
    parallel instrument correction
    :param input_dics:
    :param ls_saved_stas:
    :param clients:
    :param address:
    :param BH_file:
    :param starti:
    :param endi:
    :return:
    """
    for i in range(starti, endi):
        IC_core(input_dics=input_dics, ls_saved_sta=ls_saved_stas[i],
                clients=clients, address=address, BH_file=BH_file,
                inform='%s -- %s/%s' % (clients, i+1, len(ls_saved_stas)))

# ##################### IC_core #########################################


def IC_core(input_dics, ls_saved_sta, clients, address, BH_file, inform):
    """
    Function that prepare the waveforms for instrument correction and
    divert the program to the right instrument correction function!
    :param input_dics:
    :param ls_saved_sta:
    :param clients:
    :param address:
    :param BH_file:
    :param inform:
    :return:
    """
    try:
        if input_dics['ic_obspy_full'] == 'Y':
            st = read(ls_saved_sta)
            if len(st) > 1:
                print "\n=== WARNING:"
                print "%s" % ls_saved_sta
                print "probably has some gaps!"
                print "It will be merged (fill_value=0)."
                print "\nFor more information refer to:"
                print "%s" % os.path.join(address, 'info',
                                          'waveform_gap.txt')
                print "which contains all the waveforms with gap."

                st.merge(method=1, fill_value=0, interpolation_samples=0)
                gap_fio = open(os.path.join(address, 'info',
                                            'waveform_gap.txt'), 'a+')
                gap_msg = '%s.%s.%s.%s\t%s\n' % (st[0].stats.network,
                                                 st[0].stats.station,
                                                 st[0].stats.location,
                                                 st[0].stats.channel,
                                                 'instrument_correction')
                gap_fio.writelines(gap_msg)
                gap_fio.close()
            tr = st[0]
            if clients.lower() != 'arc':
                stxml_file = \
                    os.path.join(address, 'Resp',
                                 'STXML.%s' % os.path.basename(ls_saved_sta))
                obspy_fullresp_STXML(input_dics=input_dics, trace=tr,
                                     stxml_file=stxml_file,
                                     Address=os.path.join(address, BH_file),
                                     unit=input_dics['corr_unit'],
                                     BP_filter=input_dics['pre_filt'],
                                     inform=inform)
            else:
                resp_file = \
                    os.path.join(address, 'Resp',
                                 'DATALESS.%s'
                                 % os.path.basename(ls_saved_sta))
                obspy_fullresp_RESP(input_dics=input_dics, trace=tr,
                                    resp_file=resp_file,
                                    Address=os.path.join(address, BH_file),
                                    unit=input_dics['corr_unit'],
                                    BP_filter=input_dics['pre_filt'],
                                    inform=inform)
        else:
            sys.exit('ERROR: only ic_obspy_full is implemented for '
                     'instrument correction')
    except Exception as e:
        print e

# ##################### obspy_fullresp_STXML #################################


def obspy_fullresp_STXML(input_dics, trace, stxml_file, Address, unit='DIS',
                         BP_filter=(0.008, 0.012, 3.0, 4.0), inform='N/N'):
    """
    Instrument correction using station_XML --->
    equivalent to full response file steps: detrend, demean, taper, filter,
    deconvolution
    :param input_dics:
    :param trace:
    :param stxml_file:
    :param Address:
    :param unit:
    :param BP_filter:
    :param inform:
    :return:
    """
    try:
        if input_dics['resample_corr']:
            trace = resample_trace(trace,
                                   des_sr=input_dics['resample_corr'],
                                   resample_method=
                                   input_dics['resample_method'])
        trace.detrend('linear')
        # To keep it consistant with obspy.remove_response method!
        if unit.lower() == 'dis':
            unit = 'DISP'
            unit_write = 'dis'
        else:
            unit_write = unit.lower()

        inv = read_inventory(stxml_file, format="stationxml")
        trace.attach_response(inv)
        trace.remove_response(output=unit,
                              water_level=input_dics['water_level'],
                              pre_filt=eval(BP_filter), zero_mean=True,
                              taper=True, taper_fraction=0.05)
        # Remove the following line to keep the units
        # as it is in the stationXML
        # trace.data *= 1.e9

        trace_identity = '%s.%s.%s.%s' % (trace.stats['network'],
                                          trace.stats['station'],
                                          trace.stats['location'],
                                          trace.stats['channel'])
        if input_dics['mseed'] == 'N':
            trace.write(os.path.join(
                Address, '%s.%s' % (unit_write, trace_identity)), format='SAC')
        else:
            trace.write(
                os.path.join(Address, '%s.%s' % (unit_write, trace_identity)),
                format='MSEED')

        if unit.lower() == 'disp':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print '%s -- instrument correction to %s for: %s' \
              % (inform, unit_print, trace_identity)

    except Exception as e:
        print '%s -- %s' % (inform, e)

# ##################### obspy_fullresp_RESP ##################################


def obspy_fullresp_RESP(input_dics, trace, resp_file, Address, unit='DIS',
                        BP_filter=(0.008, 0.012, 3.0, 4.0), inform='N/N'):
    """
    Instrument correction using dataless seed --->
    equivalent to full response file steps: detrend, demean, taper, filter,
    deconvolution
    :param input_dics:
    :param trace:
    :param resp_file:
    :param Address:
    :param unit:
    :param BP_filter:
    :param inform:
    :return:
    """
    dataless_parser = Parser(resp_file)
    seedresp = {'filename': dataless_parser, 'units': unit}

    try:
        if input_dics['resample_corr']:
            trace = resample_trace(trace,
                                   des_sr=input_dics['resample_corr'],
                                   resample_method=
                                   input_dics['resample_method'])
        trace.detrend('linear')
        trace.simulate(seedresp=seedresp, paz_remove=None, paz_simulate=None,
                       remove_sensitivity=True, simulate_sensitivity=False,
                       water_level=input_dics['water_level'],
                       zero_mean=True, taper=True,
                       taper_fraction=0.05, pre_filt=eval(BP_filter),
                       pitsasim=False, sacsim=True)
        # Remove the following line since we want to keep
        # the units as it is in the stationXML
        # trace.data *= 1.e9
        trace_identity = '%s.%s.%s.%s' % (trace.stats['network'],
                                          trace.stats['station'],
                                          trace.stats['location'],
                                          trace.stats['channel'])
        if input_dics['mseed'] == 'N':
            trace.write(os.path.join(Address, '%s.%s' % (unit.lower(),
                                                         trace_identity)),
                        format='SAC')
        else:
            trace.write(os.path.join(Address, '%s.%s' % (unit.lower(),
                                                         trace_identity)),
                        format='MSEED')

        if unit.lower() == 'dis':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print '%s -- instrument correction to %s for: %s' \
              % (inform, unit_print, trace_identity)

    except Exception as e:
        print '%s -- %s' % (inform, e)

# ##################### ic_reporter ##################################


def ic_reporter(input_dics, address, clients, ls_saved_stas, t_inst_1,
                t_inst_2):
    """
    writing log files for instrument correction
    :param input_dics:
    :param address:
    :param clients:
    :param ls_saved_stas:
    :param t_inst_1:
    :param t_inst_2:
    :return:
    """
    report_parallel_open = open(os.path.join(address, 'info',
                                             'report_parallel'), 'a')
    report_parallel_open.writelines('---------------%s---------------\n'
                                    % clients.upper())
    report_parallel_open.writelines('Instrument Correction\n')
    report_parallel_open.writelines('Number of Nodes: %s\n'
                                    % input_dics['ic_np'])
    report_parallel_open.writelines('Number of Stas : %s\n'
                                    % len(ls_saved_stas))
    report_parallel_open.writelines('Total Time     : %s\n'
                                    % (t_inst_2 - t_inst_1))
