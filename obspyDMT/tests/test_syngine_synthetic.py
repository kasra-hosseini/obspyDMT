#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_syngine_synthetic.py
#   Purpose:   testing syngine synthetics 
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from obspyDMT.utils.input_handler import command_parse, read_input_command

# ##################### test_syngine_tour ###############################


def test_syngine_tour():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)

    input_dics['datapath'] = './dmt_tour_dir'
    input_dics['min_date'] = '2011-03-10'
    input_dics['max_date'] = '2011-03-12'
    input_dics['min_mag'] = '8.9'
    input_dics['identity'] = 'TA.1*.*.BHZ'
    input_dics['event_catalog'] = 'IRIS'
    input_dics['req_parallel'] = True
    input_dics['instrument_correction'] = True
    input_dics['net'] = 'TA'
    input_dics['sta'] = '1*'
    input_dics['loc'] = '*'
    input_dics['cha'] = 'BHZ'
    input_dics['syngine'] = True

    from obspyDMT import obspyDMT
    input_dics = obspyDMT.dmt_core(input_dics)

    from glob import glob
    assert len(glob('./dmt_tour_dir/*')) == 2
    assert len(glob('./dmt_tour_dir/20110311_054623.a/raw/*')) > 10
    assert len(glob('./dmt_tour_dir/20110311_054623.a/processed/*')) == len(glob('./dmt_tour_dir/20110311_054623.a/raw/*'))
    assert len(glob('./dmt_tour_dir/20110311_054623.a/syngine_iasp91_2s/*')) > 10
    assert len(glob('./dmt_tour_dir/20110311_054623.a/resp/*')) == len(glob('./dmt_tour_dir/20110311_054623.a/raw/*'))
    assert len(glob('./dmt_tour_dir/20110311_054623.a/info/*')) >= 8

    import shutil
    shutil.rmtree('./dmt_tour_dir')
    shutil.rmtree('./obspydmt-data')
