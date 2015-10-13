#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  local_handler.py
#   Purpose:   handling local processings/plottings in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import multiprocessing
import numpy as np
import os
from obspy.core import read
from scipy import signal

from .utility_codes import read_station_event, locate, check_par_jobs
from .data_handler import update_sta_ev_file

# ############### POTENTIAL
# if input_dics['resample_raw']:
#     print '\nResample RAW traces to %sHz...' % input_dics['resample_raw'],
#     resample_all(i=i, address_events=add_event,
#                  des_sr=input_dics['resample_raw'],
#                  resample_method=input_dics['resample_method'])
#     print 'DONE'
# if input_dics['SAC'] == 'Y':
#     print '\nConverting the MSEED files to SAC...',
#     writesac_all(i=i, address_events=add_event)
#     print 'DONE'

# ###################### process_data #############


def process_data(input_dics, event):
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
    update_sta_ev_file(target_path)
    sta_ev_arr = np.loadtxt(os.path.join(target_path, 'info', 'station_event'),
                            delimiter=',', dtype='object')
    if len(sta_ev_arr) > 0:
        process_serial_parallel(sta_ev_arr, input_dics, target_path)
    else:
        print("[LOCAL] No station to process!")
    import ipdb; ipdb.set_trace()

# ###################### process_serial_parallel #############


def process_serial_parallel(sta_ev_arr, input_dics, target_path):
    """
    Unit for running the process core in parallel or in serial
    :param sta_ev_arr:
    :param input_dics:
    :return:
    """

    if input_dics['parallel_process']:
        start = 0
        end = len(sta_ev_arr)
        step = (end - start) / input_dics['process_np'] + 1

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

# ###################### process_core_iterate #############


def process_core_iterate(sta_ev_arr, input_dics, target_path, starti, endi):
    for i in range(starti, endi):
        staev_ar = sta_ev_arr[i]
        station_id = '%s.%s.%s.%s' % (staev_ar[0], staev_ar[1],
                                      staev_ar[2], staev_ar[3])
        tr_add = os.path.join(target_path, 'BH_RAW', station_id)
        if len(staev_ar) > 10:
            data_source = staev_ar[13]
        else:
            data_source = staev_ar[9]
        from utils.process_func.process_unit import process_unit
        process_unit(tr_add, target_path, staev_ar, data_source, input_dics)

# ###################### zerophase_chebychev_lowpass_filter #############


def zerophase_chebychev_lowpass_filter(trace, freqmax):
    """
    Custom Chebychev type two zerophase lowpass filter useful for
    decimation filtering.
    This filter is stable up to a reduction in frequency with a factor of
    10. If more reduction is desired, simply decimate in steps.
    Partly based on a filter in ObsPy.
    :param trace: The trace to be filtered.
    :param freqmax: The desired lowpass frequency.
    Will be replaced once ObsPy has a proper decimation filter.

    This code is from LASIF repository (Lion Krischer).
    """
    # rp - maximum ripple of passband, rs - attenuation of stopband
    rp, rs, order = 1, 96, 1e99
    ws = freqmax / (trace.stats.sampling_rate * 0.5) # stop band frequency
    wp = ws # pass band frequency

    while True:
        if order <= 12:
            break
        wp *= 0.99
        order, wn = signal.cheb2ord(wp, ws, rp, rs, analog=0)

    b, a = signal.cheby2(order, rs, wn, btype="low", analog=0, output="ba")

    # Apply twice to get rid of the phase distortion.
    trace.data = signal.filtfilt(b, a, trace.data)

# ###################### decimate_trace #############


def decimate_trace(tr, dt):
    """
    Decimate ObsPy Trace (tr) with dt as delta (1/sampling_rate).

    This code is from LASIF repository (Lion Krischer) with some
    minor modifications.
    """
    while True:
        decimation_factor = int(dt / tr.stats.delta)
        # Decimate in steps for large sample rate reductions.
        if decimation_factor > 5:
            decimation_factor = 5
        if decimation_factor > 1:
            new_nyquist = tr.stats.sampling_rate / 2.0 / decimation_factor
            zerophase_chebychev_lowpass_filter(tr, new_nyquist)
            tr.decimate(factor=decimation_factor, no_filter=True)
        else:
            return tr

# ##################### resample_all ####################################


def resample_all(i, address_events, des_sr, resample_method='decimate'):
    """
    resample all the traces based on the selected sampling rate
    :param i:
    :param address_events:
    :param des_sr:
    :param lancz_a:
    :return:
    """
    sta_ev = read_station_event(address_events[i])
    ls_saved_stas = []

    for j in range(len(sta_ev[0])):
        station_id = '%s.%s.%s.%s' % (sta_ev[0][j][0],
                                      sta_ev[0][j][1],
                                      sta_ev[0][j][2],
                                      sta_ev[0][j][3])
        ls_saved_stas.append(os.path.join(address_events[i],
                                          'BH_RAW', station_id))
    for j in range(len(sta_ev[0])):
        try:
            st = read(ls_saved_stas[j])
            if len(st) > 1:
                print("\n=== WARNING:")
                print("%s" % ls_saved_stas[j])
                print("probably has some gaps!")
                print("It will be merged (fill_value=0).")
                print("\nFor more information refer to:")
                print("%s" % os.path.join(address_events[i], 'info',
                                          'waveform_gap.txt'))
                print("which contains all the waveforms with gap.")

                st.merge(method=1, fill_value=0, interpolation_samples=0)
                gap_fio = open(os.path.join(address_events[i], 'info',
                                            'waveform_gap.txt'), 'a+')
                gap_msg = '%s.%s.%s.%s\t%s\n' % (sta_ev[0][j][0],
                                                 sta_ev[0][j][1],
                                                 sta_ev[0][j][2],
                                                 sta_ev[0][j][3],
                                                 'resampling')
                gap_fio.writelines(gap_msg)
                gap_fio.close()
            tr = st[0]
            # resample
            if resample_method.lower() == 'decimate':
                tr = decimate_trace(tr, dt=1./des_sr)
            tr.write(ls_saved_stas[j], format='MSEED')

        except Exception as e:
            print('\nWARNING: %s' % e)
            print(ls_saved_stas[j])
            print('------------------')

# ##################### resample_trace ####################################


def resample_trace(tr, des_sr, resample_method='decimate'):
    """
    resample one trace based on the selected sampling rate
    :param tr:
    :param des_sr:
    :param resample_method:
    :return:
    """
    try:
        # resample
        if resample_method.lower() == 'decimate':
            tr = decimate_trace(tr, dt=1./des_sr)
        return tr
    except Exception as e:
        print('\nWARNING: %s' % e)
        print('------------------')
