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
from obspy.fdsn import Client as Client_fdsn

from obspyDMT.utils.input_handler import command_parse, read_input_command
from obspyDMT.utils.event_handler import events_info

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

    client_fdsn = Client_fdsn(base_url=input_dics['event_url'])
    events_QML = client_fdsn.get_events(
        minlatitude=evlatmin,
        maxlatitude=evlatmax,
        minlongitude=evlonmin,
        maxlongitude=evlonmax,
        latitude=evlat,
        longitude=evlon,
        maxradius=evradmax,
        minradius=evradmin,
        mindepth=input_dics['min_depth'],
        maxdepth=input_dics['max_depth'],
        starttime=input_dics['min_date'],
        endtime=input_dics['max_date'],
        minmagnitude=input_dics['min_mag'],
        maxmagnitude=input_dics['max_mag'],
        orderby='time',
        catalog=input_dics['event_catalog'],
        magnitudetype=input_dics['mag_type'])

    assert events_QML[0].preferred_origin().latitude == 38.2963
    assert events_QML[0].preferred_origin().longitude == 142.498
    assert events_QML[0].preferred_origin().depth == 19700.0

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
