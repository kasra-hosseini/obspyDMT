#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  obspyDMT.py
#   Purpose:   obspyDMT main program 
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
import sys
import time

from utils.event_handler import get_Events, create_tar_file
from utils.arclink_handler import ARC_network
from utils.fdsn_handler import FDSN_network
from utils.input_handler import command_parse, read_input_command
from utils.instrument_handler import FDSN_ARC_IC
from utils.merge_handler import FDSN_ARC_merge
from utils.plotting_tools import plot_xml_response, seismicity, plot_tools
from utils.update_handler import FDSN_update, ARC_update
from utils.utility_codes import header_printer, send_email, goodbye_printer

# ##################### obspyDMT ##################################


def obspyDMT(**kwargs):
    """
    obspyDMT: is the function dedicated to the main part of the code.
    It organizes all the sub-main functions used in obspyDMT
    """
    header_printer()
    # initializing variables:
    events = None
    create_tar_file_address = None
    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()
    # ------------------Read INPUT file (Parameters)--------------------
    input_dics = read_input_command(parser, **kwargs)
    # ------------------plot stationxml files--------------------
    if input_dics['plotxml_dir']:
        plot_xml_response(input_dics)
    # ------------------Getting List of Events/Continuous requests------
    if input_dics['get_events'] == 'Y':
        events = get_Events(input_dics, request='event-based')
        if events == 0:
            return
    if input_dics['get_continuous'] == 'Y':
        events = get_Events(input_dics, request='continuous')
    # ------------------Seismicity--------------------------------------
    if input_dics['seismicity'] == 'Y':
        seismicity(input_dics, events)
    # ------------------FDSN--------------------------------------------
    if input_dics['FDSN'] == 'Y':
        FDSN_network(input_dics, events)
    # ------------------Arclink-----------------------------------------
    if input_dics['ArcLink'] == 'Y':
        ARC_network(input_dics, events)
    # ------------------FDSN-Updating-----------------------------------
    if input_dics['fdsn_update'] != 'N':
        FDSN_update(input_dics, address=input_dics['fdsn_update'])
    # ------------------ArcLink-Updating--------------------------------
    if input_dics['arc_update'] != 'N':
        ARC_update(input_dics, address=input_dics['arc_update'])
    # ------------------FDSN-instrument---------------------------------
    if input_dics['fdsn_ic'] != 'N' or input_dics['fdsn_ic_auto'] == 'Y':
        create_tar_file_address = FDSN_ARC_IC(
            input_dics, clients=input_dics['fdsn_base_url'])
    # ------------------Arclink-instrument------------------------------
    if input_dics['arc_ic'] != 'N' or input_dics['arc_ic_auto'] == 'Y':
        create_tar_file_address = FDSN_ARC_IC(input_dics, clients='arc')
    # ------------------FDSN-merge--------------------------------------
    if input_dics['fdsn_merge'] != 'N' or input_dics['fdsn_merge_auto'] == 'Y':
        FDSN_ARC_merge(input_dics, clients=input_dics['fdsn_base_url'])
    # ------------------ArcLink-merge-----------------------------------
    if input_dics['arc_merge'] != 'N' or input_dics['arc_merge_auto'] == 'Y':
        FDSN_ARC_merge(input_dics, clients='arc')
    # ------------------plot_tools--------------------------------------------
    ls_plot_options = ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray',
                       'plot_ray_gmt', 'plot_epi', 'plot_dt']
    for plt_opt in ls_plot_options:
        if input_dics[plt_opt] != 'N':
            print 'Plotting %s' % plt_opt
            if input_dics['plot_all'] == 'Y' or input_dics['plot_fdsn'] == 'Y':
                plot_tools(input_dics, clients=input_dics['fdsn_base_url'])
            if input_dics['plot_arc'] == 'Y':
                plot_tools(input_dics, clients='arc')
    if input_dics['plot_all_events']:
        raw_input('\nPress enter to continue ..\n')
    # ------------------Compressing-------------------------------------------
    if create_tar_file_address:
        if input_dics['zip_w'] == 'Y' or input_dics['zip_r'] == 'Y':
            create_tar_file(input_dics, address=create_tar_file_address)
    # ------------------Email-------------------------------------------
    if input_dics['email'] != 'N':
        send_email(input_dics)
    return input_dics

########################################################################
########################################################################
########################################################################


def main():
    t1_pro = time.time()
    # Run the main program
    input_dics = obspyDMT()
    goodbye_printer(input_dics, t1_pro)
    # pass the return of main to the command line.
    sys.exit()

if __name__ == "__main__":
    main()
