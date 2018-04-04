#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  resample_handler.py
#   Purpose:   handling resampling in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from scipy import signal

# ###################### zerophase_chebychev_lowpass_filter ###################


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
    # stop band frequency
    ws = freqmax / (trace.stats.sampling_rate * 0.5)
    # pass band frequency
    wp = ws

    while True:
        if order <= 12:
            break
        wp *= 0.99
        order, wn = signal.cheb2ord(wp, ws, rp, rs, analog=0)

    b, a = signal.cheby2(order, rs, wn, btype="low", analog=0, output="ba")

    # Apply twice to get rid of the phase distortion.
    trace.data = signal.filtfilt(b, a, trace.data)

# ###################### resample_trace #######################################


def resample_trace(tr, dt, method, lanczos_a=20):
    """
    resample ObsPy Trace (tr) with dt as delta (1/sampling_rate).

    This code is from LASIF repository (Lion Krischer) with some
    minor modifications.
    :param tr:
    :param dt:
    :param method:
    :param lanczos_a:
    :return:
    """
    while True:
        if method == 'decimate':
            decimation_factor = int(dt / tr.stats.delta)
        elif method == 'lanczos':
            decimation_factor = float(dt) / tr.stats.delta
        # decimate in steps for large sample rate reductions.
        if decimation_factor > 5:
            decimation_factor = 5
        if decimation_factor > 1:
            new_nyquist = tr.stats.sampling_rate / 2.0 / decimation_factor
            zerophase_chebychev_lowpass_filter(tr, new_nyquist)
            if method == 'decimate':
                tr.decimate(factor=decimation_factor, no_filter=True)
            elif method == 'lanczos':
                current_sr = float(tr.stats.sampling_rate)
                tr.interpolate(method='lanczos',
                               sampling_rate=current_sr/decimation_factor,
                               a=lanczos_a)
        else:
            return tr

# ##################### resample_trace ####################################


def resample_unit(tr, des_sr, resample_method='decimate'):
    """
    resample one trace based on the selected sampling rate
    :param tr:
    :param des_sr:
    :param resample_method:
    :return:
    """
    try:
        if resample_method.lower() == 'decimate':
            tr = resample_trace(tr, dt=1./des_sr, method='decimate')
        elif resample_method.lower() == 'lanczos':
            try:
                from obspy.signal.interpolation import lanczos_interpolation
                tr = resample_trace(tr, dt=1./des_sr, method='lanczos')
            except:
                tr = resample_trace(tr, dt=1./des_sr, method='decimate')
        return tr
    except Exception as error:
        print('[WARNING] resampling of %s: %s' % (tr.id, error))
