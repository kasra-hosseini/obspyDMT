#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_input_handler.py
#   Purpose:   testing input_handler
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
import os
from obspy.core import UTCDateTime

from obspyDMT.utils.input_handler import command_parse, read_input_command

# ##################### test_command_parse ##################################


def test_command_parse():
    (options, args, parser) = command_parse()
    assert len(parser.option_groups) == 15

# ##################### test_read_input_command ###############################


def test_read_input_command():
    (options, args, parser) = command_parse()

    assert len(parser.option_groups[0].option_list) == 3
    assert len(parser.option_groups[1].option_list) == 2
    assert len(parser.option_groups[2].option_list) == 4
    assert len(parser.option_groups[3].option_list) == 14
    assert len(parser.option_groups[4].option_list) == 8
    assert len(parser.option_groups[5].option_list) == 7
    assert len(parser.option_groups[6].option_list) == 5
    assert len(parser.option_groups[7].option_list) == 6
    assert len(parser.option_groups[8].option_list) == 11
    assert len(parser.option_groups[9].option_list) == 1
    assert len(parser.option_groups[10].option_list) == 7
    assert len(parser.option_groups[11].option_list) == 6
    assert len(parser.option_groups[12].option_list) == 17
    assert len(parser.option_groups[13].option_list) == 13
    assert len(parser.option_groups[14].option_list) == 3

    input_dics = read_input_command(parser)

    return input_dics

# ##################### test_default_inputs ###############################


def test_default_inputs():
    input_dics = test_read_input_command()

    assert os.path.basename(input_dics['datapath']) == 'obspydmt-data'
    assert input_dics['event_based'] is True
    assert input_dics['data_source'] == ['IRIS']
    assert input_dics['waveform'] is True 
    assert input_dics['response'] is True
    assert input_dics['dir_select'] is False
    assert input_dics['list_stas'] is False
    assert input_dics['min_epi'] is False 
    assert input_dics['max_epi'] is False
    assert input_dics['min_azi'] is False 
    assert input_dics['max_azi'] is False
    assert input_dics['test'] is False
    assert (UTCDateTime(input_dics['max_date']) -
            UTCDateTime(input_dics['min_date']) > (60 * 60 * 24 * 365 * 45))
    assert input_dics['preset'] ==  0.0 
    assert input_dics['offset'] == 1800.0
    assert input_dics['waveform_format'] is False
    assert input_dics['resample_method'] == 'lanczos'
    assert input_dics['sampling_rate'] is False
    assert input_dics['net'] == '*'
    assert input_dics['sta'] == '*'
    assert input_dics['loc'] == '*'
    assert input_dics['cha'] == '*'
    assert input_dics['lat_cba'] is None
    assert input_dics['lon_cba'] is None
    assert input_dics['mr_cba'] is None
    assert input_dics['Mr_cba'] is None
    assert input_dics['mlat_rbb'] is None
    assert input_dics['Mlat_rbb'] is None
    assert input_dics['mlon_rbb'] is None
    assert input_dics['Mlon_rbb'] is None
    assert input_dics['req_np'] == 4
    assert input_dics['process_np'] == 4
    assert input_dics['username_fdsn'] is None
    assert input_dics['password_fdsn'] is None
    assert input_dics['username_arclink'] == 'test@obspy.org'
    assert input_dics['password_arclink'] is ''
    assert input_dics['host_arclink'] == 'webdc.eu'
    assert input_dics['port_arclink'] == 18002
    assert input_dics['event_catalog'] == 'LOCAL'
    assert input_dics['min_depth'] == -10.0
    assert input_dics['max_depth'] == +6000.0
    assert input_dics['min_mag'] == 3.0
    assert input_dics['max_mag'] == 10.
    assert input_dics['mag_type'] is None
    assert input_dics['evlatmin'] is None
    assert input_dics['evlatmax'] is None
    assert input_dics['evlonmin'] is None
    assert input_dics['evlonmax'] is None
    assert input_dics['evlat'] is None
    assert input_dics['evlon'] is None
    assert input_dics['evradmin'] is None
    assert input_dics['evradmax'] is None
    assert input_dics['interval'] == 3600*24
    assert input_dics['pre_process'] == 'process_unit'
    assert input_dics['select_data'] is False
    assert input_dics['corr_unit'] == 'DIS'
    assert input_dics['pre_filt'] == '(0.008, 0.012, 3.0, 4.0)'
    assert input_dics['water_level'] == 600.0
    assert input_dics['plot_dir_name'] == 'raw'
    assert input_dics['plot_save'] is False 
    assert input_dics['plot_format'] is False
    assert input_dics['show_no_plot'] is None
    assert input_dics['plot_lon0'] == 180
    assert input_dics['plot_style'] == 'simple'
    assert input_dics['plotxml_date'] is False
    assert input_dics['plotxml_start_stage'] == 1
    assert input_dics['plotxml_end_stage'] == 100
    assert input_dics['plotxml_min_freq'] == 0.01
    assert input_dics['plotxml_percentage'] == 80
    assert input_dics['plotxml_phase_threshold'] == 10.
    assert input_dics['plotxml_output'] == 'VEL'
    assert input_dics['email'] is False
    assert input_dics['arc_avai_timeout'] == 40
    assert input_dics['arc_wave_timeout'] == 2

# ##################### test_tour ###############################


def test_tour():
    input_dics = test_read_input_command()

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

    from obspyDMT import obspyDMT
    input_dics = obspyDMT.dmt_core(input_dics)

    from glob import glob
    assert len(glob('./dmt_tour_dir/*')) == 2
    assert len(glob('./dmt_tour_dir/20110311_054623.a/processed/*')) == 13
    assert len(glob('./dmt_tour_dir/20110311_054623.a/raw/*')) == 13
    assert len(glob('./dmt_tour_dir/20110311_054623.a/resp/*')) == 13
    assert len(glob('./dmt_tour_dir/20110311_054623.a/info/*')) >= 8

    import shutil
    shutil.rmtree('./dmt_tour_dir')
    shutil.rmtree('./obspydmt-data')
