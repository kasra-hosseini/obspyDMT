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
    assert len(parser.option_groups[2].option_list) == 13
    assert len(parser.option_groups[3].option_list) == 3
    assert len(parser.option_groups[4].option_list) == 15
    assert len(parser.option_groups[5].option_list) == 7
    assert len(parser.option_groups[6].option_list) == 8
    assert len(parser.option_groups[7].option_list) == 5
    assert len(parser.option_groups[8].option_list) == 3
    assert len(parser.option_groups[9].option_list) == 14
    assert len(parser.option_groups[10].option_list) == 3
    assert len(parser.option_groups[11].option_list) == 7
    assert len(parser.option_groups[12].option_list) == 19
    assert len(parser.option_groups[13].option_list) == 13
    assert len(parser.option_groups[14].option_list) == 3

    input_dics = read_input_command(parser)
    assert input_dics['water_level'] == 600.0

    return input_dics

# ##################### test_default_inputs ###############################


def test_default_inputs():
    input_dics = test_read_input_command()
    assert os.path.basename(input_dics['datapath']) == 'obspyDMT-data'
    assert (UTCDateTime(input_dics['max_date']) -
            UTCDateTime(input_dics['min_date']) < (60 * 60 * 24 * 5 + 1))
    assert (UTCDateTime(input_dics['max_date']) -
            UTCDateTime(input_dics['min_date']) > (60 * 60 * 24 * 5 - 1))
    assert input_dics['event_url'] == 'IRIS'
    assert input_dics['event_catalog'] is None
    assert input_dics['mag_type'] is None
    assert input_dics['min_mag'] == 5.5
    assert input_dics['max_mag'] == 9.9
    assert input_dics['min_depth'] == -10.0
    assert input_dics['max_depth'] == 6000.0
    assert input_dics['get_events'] == 'Y'
    assert input_dics['interval'] == (3600*24.)
    assert input_dics['preset_cont'] == 0 
    assert input_dics['offset_cont'] == 0
    assert input_dics['req_np'] == 4
    assert input_dics['list_stas'] is False
    assert input_dics['waveform'] == 'Y'
    assert input_dics['response'] == 'Y'
    assert input_dics['FDSN'] == 'Y'
    assert input_dics['ArcLink'] == 'N'
    assert input_dics['fdsn_base_url'] == 'IRIS'
    assert input_dics['fdsn_user'] is None
    assert input_dics['fdsn_pass'] is None
    assert input_dics['arc_avai_timeout'] == 40  
    assert input_dics['arc_wave_timeout'] == 2  
    assert input_dics['SAC'] == 'Y'  
    assert input_dics['preset'] == 0.0   
    assert input_dics['offset'] == 1800.0  
    assert input_dics['net'] == '*'   
    assert input_dics['sta'] == '*'   
    assert input_dics['loc'] == '*'   
    assert input_dics['cha'] == '*'  
    assert input_dics['evlatmin'] is None
    assert input_dics['evlatmax'] is None
    assert input_dics['evlonmin'] is None
    assert input_dics['evlonmax'] is None
    assert input_dics['evlat'] is None
    assert input_dics['evlon'] is None
    assert input_dics['evradmin'] is None
    assert input_dics['evradmax'] is None
    assert input_dics['max_result'] == 2500  
    assert input_dics['depth_bins_seismicity'] == 10  
    assert input_dics['lat_cba'] is None
    assert input_dics['lon_cba'] is None
    assert input_dics['mr_cba'] is None
    assert input_dics['Mr_cba'] is None
    assert input_dics['mlat_rbb'] is None
    assert input_dics['Mlat_rbb'] is None
    assert input_dics['mlon_rbb'] is None
    assert input_dics['Mlon_rbb'] is None
    assert input_dics['test'] is 'N'
    assert input_dics['fdsn_update'] == 'N'   
    assert input_dics['arc_update'] == 'N'   
    assert input_dics['update_all'] == 'N'  
    assert input_dics['email'] == 'N'  
    assert input_dics['ic_all'] == 'N'  
    assert input_dics['fdsn_ic'] == 'N'   
    assert input_dics['fdsn_ic_auto'] == 'Y'  
    assert input_dics['arc_ic'] == 'N'   
    assert input_dics['arc_ic_auto'] == 'N'  
    assert input_dics['ic_np'] == 4  
    assert input_dics['ic_obspy_full'] == 'Y'  
    assert input_dics['pre_filt'] == '(0.008, 0.012, 3.0, 4.0)'  
    assert input_dics['water_level'] == 600.0  
    assert input_dics['corr_unit'] == 'DIS'  
    assert input_dics['merge_all'] == 'N'  
    assert input_dics['fdsn_merge'] == 'N'   
    assert input_dics['fdsn_merge_auto'] == 'N'  
    assert input_dics['merge_type'] == 'raw'  
    assert input_dics['arc_merge'] == 'N'   
    assert input_dics['arc_merge_auto'] == 'N'  
    assert input_dics['plot_all'] == 'Y'  
    assert input_dics['plot_type'] == 'raw'  
    assert input_dics['plot_ev'] is False
    assert input_dics['plot_sta'] is False
    assert input_dics['plot_ray'] is False
    assert input_dics['plot_epi'] is False
    assert input_dics['plot_dt'] is False
    assert input_dics['plot_ray_gmt'] is False
    assert os.path.basename(input_dics['plot_save']) == '.'   
    assert input_dics['plot_format'] == 'png'  
    assert input_dics['min_epi'] == 0.0   
    assert input_dics['max_epi'] == 180.0  
    assert input_dics['plotxml_dir'] is False
    assert input_dics['plotxml_date'] is False
    assert input_dics['plotxml_min_freq'] == 0.01  
    assert input_dics['plotxml_output'] == 'VEL'  
    assert input_dics['plotxml_start_stage'] == 1  
    assert input_dics['plotxml_end_stage'] == 100  
    assert input_dics['plotxml_percentage'] == 80  
    assert input_dics['plotxml_phase_threshold'] == 10.
