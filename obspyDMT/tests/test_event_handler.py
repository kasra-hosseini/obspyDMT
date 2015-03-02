#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_event_handler.py
#   Purpose:   testing event_handler
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from obspy.core import UTCDateTime

from obspyDMT.utils.input_handler import command_parse, read_input_command
from obspyDMT.utils.event_handler import gcmt_catalog, events_info

# ##################### test_gmt_catalog ##################################


def test_gmt_catalog():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)
    # Changing the input_dics values for testing
    input_dics['min_date'] = UTCDateTime('2011-03-01')
    input_dics['max_date'] = UTCDateTime('2011-03-20')
    input_dics['min_mag'] = 8.9

    evlatmin = input_dics['evlatmin']
    evlatmax = input_dics['evlatmax']
    evlonmin = input_dics['evlonmin']
    evlonmax = input_dics['evlonmax']

    evlat = input_dics['evlat']
    evlon = input_dics['evlon']
    evradmax = input_dics['evradmax']
    evradmin = input_dics['evradmin']

    events_QML = \
        gcmt_catalog(input_dics['min_date'],
                     input_dics['max_date'],
                     evlatmin, evlatmax, evlonmin, evlonmax,
                     evlat, evlon, evradmin, evradmax,
                     input_dics['min_depth'],
                     input_dics['max_depth'],
                     input_dics['min_mag'],
                     input_dics['max_mag'])
    assert events_QML[0].preferred_origin().latitude == 37.520
    assert events_QML[0].preferred_origin().longitude == 143.050
    assert events_QML[0].preferred_origin().depth == 20000.

# ##################### test_continuous ##################################


def test_continuous():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)
    # Changing the input_dics values for testing
    input_dics['min_date'] = UTCDateTime('2011-03-01')
    input_dics['max_date'] = UTCDateTime('2011-03-20')

    events, events_QML, successful_read = events_info(input_dics, 'continuous')
    assert len(events) == 19

    input_dics['min_date'] = UTCDateTime('2011-03-01-10-00-00')
    input_dics['max_date'] = UTCDateTime('2011-03-01-13-00-00')
    input_dics['interval'] = 1000.

    events, events_QML, successful_read = events_info(input_dics, 'continuous')
    assert len(events) == 11
