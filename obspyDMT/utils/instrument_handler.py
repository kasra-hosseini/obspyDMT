#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  instrument_handler.py
#   Purpose:   handling instrument correction in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from obspy import read_inventory
try:
    from obspy.io.xseed import Parser
except:
    from obspy.xseed import Parser
from obspy import __version__ as obspy_ver
import os
from pkg_resources import parse_version

# ##################### instrument_correction #################################


def instrument_correction(tr, target_path, save_path, corr_unit, pre_filt,
                          water_level, zero_mean=True, taper=True,
                          taper_fraction=0.05, remove_trend=True):
    """
    find STXML or DATALESS file for one trace and apply instrument correction
    :param tr:
    :param target_path:
    :param save_path:
    :param corr_unit:
    :param pre_filt:
    :param water_level:
    :param zero_mean:
    :param taper:
    :param taper_fraction:
    :param remove_trend:
    :return:
    """
    resp_file = os.path.join(target_path, 'resp', 'DATALESS.%s' % tr.id)
    stxml_file = os.path.join(target_path, 'resp', 'STXML.%s' % tr.id)

    if os.path.isfile(stxml_file):
        tr_corr = obspy_fullresp_stxml(tr, stxml_file, save_path,
                                       corr_unit, pre_filt, water_level,
                                       zero_mean, taper, taper_fraction,
                                       remove_trend,
                                       debug=False, inv_format='stationxml')
    elif os.path.isfile(resp_file) and (parse_version(obspy_ver) >= parse_version('1.1.0')):
        tr_corr = obspy_fullresp_stxml(tr, resp_file, save_path,
                                       corr_unit, pre_filt, water_level,
                                       zero_mean, taper, taper_fraction,
                                       remove_trend,
                                       debug=False)
    elif os.path.isfile(resp_file):
        tr_corr = obspy_fullresp_resp(tr, resp_file, save_path,
                                      corr_unit, pre_filt, water_level,
                                      zero_mean, taper, taper_fraction,
                                      remove_trend,
                                      debug=False)
    else:
        print("%s -- StationXML or Response file does not exist!" % tr.id)
        tr_corr = False
    return tr_corr

# ##################### obspy_fullresp_stxml #################################


def obspy_fullresp_stxml(trace, stxml_file, save_path, unit,
                         bp_filter, water_level, zero_mean, taper,
                         taper_fraction, remove_trend, debug=False, inv_format=False):
    """
    apply instrument correction using StationXML file
    :param trace:
    :param stxml_file:
    :param save_path:
    :param unit:
    :param bp_filter:
    :param water_level:
    :param zero_mean:
    :param taper:
    :param taper_fraction:
    :param remove_trend:
    :param debug:
    :return:
    """
    if 'dis' in unit.lower():
        unit = 'DISP'
    elif 'vel' in unit.lower():
        unit = 'VEL'
    elif 'acc' in unit.lower():
        unit = 'ACC'
    else:
        unit = unit.upper()
    try:
        if debug:
            print(20*'=')
            print('stationXML file: %s' % stxml_file)
            print('tarce: %s' % trace.id)
            print('save path: %s' % save_path)

        # # remove the trend
        # if remove_trend:
        #     trace.detrend('linear')
        if inv_format == 'stationxml':
            inv = read_inventory(stxml_file, format="stationxml")
        else:
            inv = read_inventory(stxml_file)
        trace.attach_response(inv)
        trace.remove_response(output=unit,
                              water_level=water_level,
                              pre_filt=eval(bp_filter),
                              zero_mean=zero_mean,
                              taper=taper,
                              taper_fraction=taper_fraction)

        # Remove the following line to keep the units
        # as it is in the stationXML
        # trace.data *= 1.e9

        if unit.lower() == 'disp':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print('instrument correction to %s for: %s' % (unit_print, trace.id))

        return trace

    except Exception as error:
        print('[EXCEPTION] %s -- %s' % (trace.id, error))
        return False

# ##################### obspy_fullresp_resp ##################################


def obspy_fullresp_resp(trace, resp_file, save_path, unit,
                        bp_filter, water_level, zero_mean, taper,
                        taper_fraction, remove_trend, debug=False):
    """
    apply instrument correction by using response file
    :param trace:
    :param resp_file:
    :param save_path:
    :param unit:
    :param bp_filter:
    :param water_level:
    :param zero_mean:
    :param taper:
    :param taper_fraction:
    :param remove_trend:
    :param debug:
    :return:
    """
    if 'dis' in unit.lower():
        unit = 'DIS'
    elif 'vel' in unit.lower():
        unit = 'VEL'
    elif 'acc' in unit.lower():
        unit = 'ACC'
    else:
        unit = unit.upper()

    dataless_parser = Parser(resp_file)
    seedresp = {'filename': dataless_parser, 'units': unit}

    if debug:
        print(20*'=')
        print('stationXML file: %s' % resp_file)
        print('tarce: %s' % trace.id)
        print('save path: %s' % save_path)

    # # remove the trend
    # if remove_trend:
    #     trace.detrend('linear')
    try:
        trace.simulate(seedresp=seedresp, paz_remove=None, paz_simulate=None,
                       remove_sensitivity=True, simulate_sensitivity=False,
                       water_level=water_level,
                       zero_mean=zero_mean, taper=taper,
                       taper_fraction=taper_fraction,
                       pre_filt=eval(bp_filter),
                       pitsasim=False, sacsim=True)

        # Remove the following line since we want to keep
        # the units as it is in the stationXML
        # trace.data *= 1.e9

        if unit.lower() == 'dis':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print('instrument correction to %s for: %s' % (unit_print, trace.id))

        return trace

    except Exception as error:
        print('[EXCEPTION] %s -- %s' % (trace.id, error))
        return False
