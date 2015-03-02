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
from obspy.core import UTCDateTime, read

from obspyDMT.utils.input_handler import command_parse, read_input_command
from obspyDMT.utils.event_handler import get_Events
from obspyDMT.utils.fdsn_handler import FDSN_network

import os


def test_FDSN_network():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)
    input_dics['min_date'] = '2011-03-01'
    input_dics['max_date'] = '2011-03-20'
    input_dics['min_mag'] = 8.9
    dir_name = int(UTCDateTime.now().timestamp)
    input_dics['datapath'] = 'test_%s' % dir_name

    events = get_Events(input_dics, 'event-based')

    assert len(events) == 1

    input_dics['net'] = 'TA'
    input_dics['sta'] = 'Z3*'
    input_dics['cha'] = 'BHZ'

    FDSN_network(input_dics, events)

    st_raw = read(os.path.join(input_dics['datapath'],
                               '2011-03-01_2011-03-20_8.9_9.9',
                               '20110311_1',
                               'BH_RAW', '*'))
    assert len(st_raw) == 7
