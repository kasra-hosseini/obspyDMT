#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_fdsn_handler.py
#   Purpose:   testing fdsn_handler
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import matplotlib.pyplot as plt
import os
from obspy.core import UTCDateTime, read
try:
    from obspy.signal import seisSim
except Exception, e:
    from obspy.signal.invsim import seisSim

from obspyDMT.utils.event_handler import get_Events
from obspyDMT.utils.fdsn_handler import FDSN_network
from obspyDMT.utils.input_handler import command_parse, read_input_command
from obspyDMT.utils.instrument_handler import FDSN_ARC_IC
from obspyDMT.utils.update_handler import FDSN_update

dir_name = int(UTCDateTime.now().timestamp)

# ##################### test_FDSN_network ##################################


def test_FDSN_network():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)
    # Changing the input_dics values for testing
    input_dics['min_date'] = '2011-03-01'
    input_dics['max_date'] = '2011-03-20'
    input_dics['min_mag'] = 8.9
    input_dics['datapath'] = 'test_%s' % dir_name
    input_dics['net'] = 'TA'
    input_dics['sta'] = 'Z3*'
    input_dics['cha'] = 'BHZ'
    input_dics['req_parallel'] = 'Y'
    input_dics['req_np'] = 4

    events = get_Events(input_dics, 'event-based')
    assert len(events) == 1

    FDSN_network(input_dics, events)

    st_raw = read(os.path.join(input_dics['datapath'],
                               '2011-03-01_2011-03-20',
                               '20110311_1',
                               'BH_RAW', '*'))
    assert len(st_raw) == 7

    st_wilber = read(os.path.join('tests', 'fdsn_waveforms', 'TA*'))

    for sta in ['Z35A', 'Z37A', 'Z39A']:
        tr_raw = st_raw.select(station=sta)[0]
        tr_wilber = st_wilber.select(station=sta)[0]
        tr_diff = abs(tr_raw.data - tr_wilber.data)
        assert max(tr_diff) == 0.

# ##################### test_FDSN_ARC_IC ##################################


def test_FDSN_ARC_IC():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)
    # Changing the input_dics values for testing
    input_dics['min_date'] = '2011-03-01'
    input_dics['max_date'] = '2011-03-20'
    input_dics['min_mag'] = 8.9
    input_dics['datapath'] = 'test_%s' % dir_name
    input_dics['net'] = 'TA'
    input_dics['sta'] = 'Z3*'
    input_dics['cha'] = 'BHZ'
    input_dics['req_parallel'] = 'Y'
    input_dics['req_np'] = 4

    FDSN_ARC_IC(input_dics, input_dics['fdsn_base_url'])

    st_cor = read(os.path.join(input_dics['datapath'],
                               '2011-03-01_2011-03-20',
                               '20110311_1',
                               'BH', '*'))
    assert len(st_cor) == 7

    st_wilber = read(os.path.join('tests', 'fdsn_waveforms', 'TA*'))

    paz_35 = {'gain': 5.714000e+08,
              'sensitivity': 6.309070e+08,
              'zeros': (0.0, 0.0, 0.0),
              'poles': (-3.701000e-02+3.701000e-02j,
                        -3.701000e-02-3.701000e-02j,
                        -1.131000e+03+0.000000e+00j,
                        -1.005000e+03+0.000000e+00j,
                        -5.027000e+02+0.000000e+00j)}

    for sta in ['Z35A', 'Z37A', 'Z39A']:
        tr_cor = st_cor.select(station=sta)[0]
        tr_wilber = st_wilber.select(station=sta)[0]
        tr_wilber_corr = tr_wilber.copy()
        tr_wilber_corr.detrend()
        corr_wilber = seisSim(tr_wilber.data,
                              tr_wilber.stats.sampling_rate,
                              paz_remove=paz_35,
                              paz_simulate=None,
                              remove_sensitivity=True,
                              simulate_sensitivity=False,
                              water_level=600.,
                              zero_mean=True,
                              taper=True,
                              taper_fraction=0.05,
                              pre_filt=(0.008, 0.012, 3.0, 4.0),
                              pitsasim=False,
                              sacsim=True)
        tr_wilber_corr.data = corr_wilber
        tr_diff = abs(tr_cor.data - tr_wilber_corr.data)
        # amplitude of the traces is in the order of 1e6 or so
        assert max(tr_diff) < 0.00001

# ##################### test_FDSN_update ##################################


def test_FDSN_update():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)
    # Changing the input_dics values for testing
    input_dics['min_date'] = '2011-03-01'
    input_dics['max_date'] = '2011-03-20'
    input_dics['min_mag'] = 8.9
    input_dics['datapath'] = 'test_%s' % dir_name
    input_dics['net'] = 'TA'
    input_dics['sta'] = 'T40A'
    input_dics['cha'] = 'BHZ'
    input_dics['req_parallel'] = 'N'
    input_dics['ic_parallel'] = 'Y'
    input_dics['ic_np'] = 4

    input_dics['fdsn_update'] = input_dics['datapath']

    FDSN_update(input_dics, address=input_dics['fdsn_update'])

    FDSN_ARC_IC(input_dics, input_dics['fdsn_base_url'])

    st_cor = read(os.path.join(input_dics['datapath'],
                               '2011-03-01_2011-03-20',
                               '20110311_1',
                               'BH', '*'))
    assert len(st_cor) == 8

    st_wilber = read(os.path.join('tests', 'fdsn_waveforms', 'TA*'))

    paz_t40 = {'gain': 3.484620e+17,
               'sensitivity': 6.271920e+08,
               'zeros': (+0.000000e+00+0.000000e+00j,
                         +0.000000e+00+0.000000e+00j,
                         +0.000000e+00+0.000000e+00j,
                         -4.631000e+02+4.305000e+02j,
                         -4.631000e+02-4.305000e+02j,
                         -1.766000e+02+0.000000e+00j,
                         -1.515000e+01+0.000000e+00j),
               'poles': (-1.330000e+04+0.000000e+00j,
                         -1.053000e+04+1.005000e+04j,
                         -1.053000e+04-1.005000e+04j,
                         -5.203000e+02+0.000000e+00j,
                         -3.748000e+02+0.000000e+00j,
                         -9.734000e+01+4.007000e+02j,
                         -9.734000e+01-4.007000e+02j,
                         -1.564000e+01+0.000000e+00j,
                         -3.700000e-02+3.700000e-02j,
                         -3.700000e-02-3.700000e-02j,
                         -2.551000e+02+0.000000e+00j)}

    paz_35 = {'gain': 5.714000e+08,
              'sensitivity': 6.309070e+08,
              'zeros': (0.0, 0.0, 0.0),
              'poles': (-3.701000e-02+3.701000e-02j,
                        -3.701000e-02-3.701000e-02j,
                        -1.131000e+03+0.000000e+00j,
                        -1.005000e+03+0.000000e+00j,
                        -5.027000e+02+0.000000e+00j)}

    for sta in ['T40A', 'Z35A', 'Z37A', 'Z39A']:
        if sta not in ['T40A']:
            paz_req = paz_35
        else:
            paz_req = paz_t40
        tr_cor = st_cor.select(station=sta)[0]
        tr_wilber = st_wilber.select(station=sta)[0]
        tr_wilber_corr = tr_wilber.copy()
        tr_wilber_corr.detrend()
        corr_wilber = seisSim(tr_wilber.data,
                              tr_wilber.stats.sampling_rate,
                              paz_remove=paz_req,
                              paz_simulate=None,
                              remove_sensitivity=True,
                              simulate_sensitivity=False,
                              water_level=600.,
                              zero_mean=True,
                              taper=True,
                              taper_fraction=0.05,
                              pre_filt=(0.008, 0.012, 3.0, 4.0),
                              pitsasim=False,
                              sacsim=True)
        tr_wilber_corr.data = corr_wilber
        tr_diff = abs(tr_cor.data - tr_wilber_corr.data)
        plt.figure()
        plt.clf()
        plt.subplot(2, 1, 1)
        plt.plot(tr_cor.data, 'b')
        plt.plot(tr_wilber_corr.data, 'r')
        plt.subplot(2, 1, 2)
        plt.plot(tr_diff)
        plt.savefig(os.path.join(input_dics['datapath'], '%s.png' % sta), format='png')
        # amplitude of the traces is in the order of 1e13 or so
        assert max(tr_diff) < 0.00001
