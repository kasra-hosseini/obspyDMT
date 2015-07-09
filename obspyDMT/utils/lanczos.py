#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Wrappers using ctypes around fortran code for Lanczos resampling

:copyright:
    Martin van Driel (Martin@vanDriel.de), 2014
:license:
    GNU Lesser General Public License, Version 3 [non-commercial/academic use]
    (http://www.gnu.org/copyleft/lgpl.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
from scipy import signal
import ctypes as C

from .helpers import load_lib

lib = load_lib()


def lanczos_resamp(si, dt_old, dt_new, a):
    """
    Lanczos resampling, see http://en.wikipedia.org/wiki/Lanczos_resampling
    In contrast to frequency domain sinc resampling it allows for arbitrary
    sampling rates but due to the finite support of the kernel is a lot faster
    then sinc resampling in time domain (linear instead of quadratic scaling
    with the number of samples). For large a, converges towards sinc
    resampling. If used for downsampling, make sure to apply a lowpass
    filter first.

    Parameters:
    si      -- input signal
    dt_old  -- sampling of the input sampling
    dt_new  -- desired sampling
    a       -- width of the kernel
    """
    if a < 2:
        raise ValueError("Width of Lanzcos kernel must be at least 2.")

    si = np.require(si, dtype=np.float64, requirements=["F_CONTIGUOUS"])
    n_old = len(si)
    n_new = int(n_old * dt_old / dt_new)
    dt = dt_new / dt_old

    so = np.zeros(n_new, dtype="float64", order="F")

    lib.lanczos_resamp(
        si.ctypes.data_as(C.POINTER(C.c_double)),
        C.c_int(n_old),
        so.ctypes.data_as(C.POINTER(C.c_double)),
        C.c_int(n_new),
        C.c_double(dt),
        C.c_int(a))

    return so


def lanczos_kern(x, a):
    """
    Lanczos kernel L_a(x), see http://en.wikipedia.org/wiki/Lanczos_resampling
    """
    kern = C.c_double(0.0)
    lib.lanczos_kern(
        C.c_double(x),
        C.c_int(a),
        C.byref(kern))

    return kern.value


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
