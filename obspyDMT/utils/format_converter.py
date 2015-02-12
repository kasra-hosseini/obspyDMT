#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  format_converter.py
#   Purpose:   helping functions for converting seismic data format
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import os
from obspy.core import read

from utility_codes import read_station_event

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### writesac_all ####################################


def writesac_all(i, address_events):
    """
    Change the format of a trace to SAC and fill in the header information
    :param i:
    :param address_events:
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
            st[0].write(ls_saved_stas[j], format='SAC')
            tr = read(ls_saved_stas[j])[0]
            if sta_ev[0][j][4]:
                tr.stats.sac.stla = float(sta_ev[0][j][4])
            if sta_ev[0][j][5]:
                tr.stats.sac.stlo = float(sta_ev[0][j][5])
            if sta_ev[0][j][6]:
                tr.stats.sac.stel = float(sta_ev[0][j][6])
            if sta_ev[0][j][7]:
                tr.stats.sac.stdp = float(sta_ev[0][j][7])

            if sta_ev[0][j][9]:
                tr.stats.sac.evla = float(sta_ev[0][j][9])
            if sta_ev[0][j][10]:
                tr.stats.sac.evlo = float(sta_ev[0][j][10])
            if sta_ev[0][j][11]:
                tr.stats.sac.evdp = float(sta_ev[0][j][11])
            if sta_ev[0][j][12]:
                tr.stats.sac.mag = float(sta_ev[0][j][12])

            tr.write(ls_saved_stas[j], format='SAC')

        except Exception as e:
            print '\nWARNING: %s' % e
            print ls_saved_stas[j]
            print '------------------'

# ##################### writesac ########################################


def writesac(address_st, sta_info, ev_info):
    """
    Change the format of a trace to SAC and fill in the header information
    :param address_st:
    :param sta_info:
    :param ev_info:
    :return:
    """

    st = read(address_st)
    st[0].write(address_st, format='SAC')
    st = read(address_st)

    if sta_info['latitude']:
        st[0].stats.sac.stla = sta_info['latitude']
    if sta_info['longitude']:
        st[0].stats.sac.stlo = sta_info['longitude']
    if sta_info['elevation']:
        st[0].stats.sac.stel = sta_info['elevation']
    if sta_info['depth']:
        st[0].stats.sac.stdp = sta_info['depth']

    if ev_info['latitude']:
        st[0].stats.sac.evla = ev_info['latitude']
    if ev_info['longitude']:
        st[0].stats.sac.evlo = ev_info['longitude']
    if ev_info['depth']:
        st[0].stats.sac.evdp = ev_info['depth']
    if ev_info['magnitude']:
        st[0].stats.sac.mag = ev_info['magnitude']

    st[0].write(address_st, format='SAC')
