#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_process_unit.py
#   Purpose:   testing process_unit 
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


def test_process_unit():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)

    input_dics['datapath'] = './event_based_dir'
    input_dics['min_date'] = '2014-01-01'
    input_dics['max_date'] = '2015-01-01'
    input_dics['min_mag'] = '7.5'
    input_dics['identity'] = 'II.*.00.BHZ'
    input_dics['event_catalog'] = 'NEIC_USGS'
    input_dics['data_source'] = ['IRIS']
    input_dics['req_parallel'] = True
    input_dics['instrument_correction'] = True
    input_dics['net'] = 'II'
    input_dics['sta'] = '*'
    input_dics['loc'] = '00'
    input_dics['cha'] = 'BHZ'
    input_dics['preset'] = 100
    input_dics['offset'] = 1800
    input_dics['process_np'] = 4
    input_dics['resample_method'] = 'lanczos'
    input_dics['sampling_rate'] = 2.0

    from obspyDMT import obspyDMT
    input_dics = obspyDMT.dmt_core(input_dics)

    from glob import glob
    assert len(glob('./event_based_dir/*')) == 6
    assert len(glob('./event_based_dir/20140401_234647.a/*')) == 4 
    assert len(glob('./event_based_dir/20140403_024313.a/*')) == 4 
    assert len(glob('./event_based_dir/20140412_201439.a/*')) == 4 
    assert len(glob('./event_based_dir/20140419_132800.a/*')) == 4 
    assert len(glob('./event_based_dir/20140623_205309.a/*')) == 4 

    from obspy import read
    tr_process = read('./event_based_dir/20140401_234647.a/processed/*')[0]
    assert (tr_process.stats.sampling_rate - input_dics['sampling_rate']) < 1e-2

    import shutil
    shutil.rmtree('./obspydmt-data')
    shutil.rmtree('./event_based_dir')
