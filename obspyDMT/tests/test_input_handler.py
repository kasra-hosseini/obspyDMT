#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_input_handler.py
#   Purpose:   testing input_handler
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from obspyDMT.utils.input_handler import command_parse, read_input_command


def test_command_parse():
    (options, args, parser) = command_parse()
    assert len(parser.option_groups) == 15


def test_read_input_command():
    (options, args, parser) = command_parse()
    assert len(parser.option_groups[0].option_list) == 3
    assert len(parser.option_groups[1].option_list) == 2
    assert len(parser.option_groups[2].option_list) == 13
    assert len(parser.option_groups[3].option_list) == 3
    assert len(parser.option_groups[4].option_list) == 15
    assert len(parser.option_groups[5].option_list) == 7
    assert len(parser.option_groups[6].option_list) == 5
    assert len(parser.option_groups[7].option_list) == 5
    assert len(parser.option_groups[8].option_list) == 3
    assert len(parser.option_groups[9].option_list) == 14
    assert len(parser.option_groups[10].option_list) == 3
    assert len(parser.option_groups[11].option_list) == 7
    assert len(parser.option_groups[12].option_list) == 17
    assert len(parser.option_groups[13].option_list) == 14
    assert len(parser.option_groups[14].option_list) == 3

    input_dics = read_input_command(parser)
    assert input_dics['water_level'] == 600.0

    return input_dics

def test_kos():
    input_dics = test_read_input_command()
    assert input_dics['water_level'] == 600.1


