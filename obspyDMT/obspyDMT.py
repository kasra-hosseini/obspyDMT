#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  obspyDMT.py
#   Purpose:   obspyDMT main program 
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
import sys
import time

from utils.data_handler import get_data
from utils.event_handler import get_time_window
from utils.input_handler import command_parse, read_input_command
from utils.local_handler import process_data, plot_unit
from utils.metadata_handler import get_metadata
from utils.plotxml_handler import plot_xml_response
from utils.utility_codes import header_printer, goodbye_printer
from utils.utility_codes import print_event_catalogs, print_data_sources
from utils.utility_codes import send_email

# =============================================================================
# ############################## obspyDMT #####################################
# =============================================================================


def obspyDMT(**kwargs):
    """
    Main function of obspyDMT toolbox.
    All the sub-main functions are organized and will be called from here.
    :param kwargs:
    :return:
    """
    # printing the header
    header_printer()
    # initializing variables:
    events = None
    # ------------------parsing command-line options---------------------------
    (options, args, parser) = command_parse()
    # ------------------create input dictionary--------------------------------
    input_dics = read_input_command(parser, **kwargs)
    # ------------------print data sources-------------------------------------
    if input_dics['print_data_sources']:
        print_data_sources()
    # ------------------print event catalogs-----------------------------------
    if input_dics['print_event_catalogs']:
        print_event_catalogs()
    # ------------------plot stationxml files----------------------------------
    if input_dics['plot_stationxml']:
        plot_xml_response(input_dics)
    # ------------------getting list of events/continuous requests-------------
    if input_dics['primary_mode'] in ['event_based', 'continuous', 'local']:
        # events contains all the information for requested time-window
        # Although we do not have any events in continuous requests,
        # it is still called as events.
        events = get_time_window(input_dics,
                                 request=input_dics['primary_mode'])
        if events == 0:
            return input_dics
    # ------------------checking the availability------------------------------
    for ev in range(len(events)):
        if input_dics['meta_data']:
            stas_avail = get_metadata(input_dics,
                                      events[ev],
                                      info_avail='%s/%s' % (ev+1, len(events)))
            if not len(stas_avail) > 0:
                continue
        if input_dics['primary_mode'] in ['event_based', 'continuous']:
            get_data(stas_avail, events[ev], input_dics)
    # ------------------processing---------------------------------------------
    # From this section, we do not need to connect to the data sources anymore.
    # This consists of pre_processing and plotting tools.
    # XXX remaining:
    # XXX custom functions to be applied to all the data ---> SAC, ...
    # XXX choose one station at each grid point or distance
    if input_dics['pre_process']:
        for ev in range(len(events)):
            process_data(input_dics, events[ev])
    # ------------------plotting-----------------------------------------------
    if input_dics['plot']:
        plot_unit(input_dics, events)
    # ------------------compressing--------------------------------------------
    # XXX a for loop over all events and compress the BH_RAW
    # if input_dics['zip_w'] == 'Y' or input_dics['zip_r'] == 'Y':
    # create_tar_file(input_dics, address=create_tar_file_address)
    # ------------------email--------------------------------------------------
    if input_dics['email']:
        send_email(input_dics)
    # ------------------exit the program---------------------------------------
    return input_dics

# =============================================================================
###############################################################################
# =============================================================================


def main():
    t1_pro = time.time()
    # run the main program
    input_dics = obspyDMT()
    # print goodbye message and exit
    goodbye_printer(input_dics, t1_pro)
    # pass the return of main to the command line.
    sys.exit()

    # =========================================================================
    # ------------------debugging----------------------------------------------
    # =========================================================================
    # For debugging purposes:
    # from pycallgraph import PyCallGraph
    # from pycallgraph.output import GraphvizOutput
    # t1_pro = time.time()
    # graphviz = GraphvizOutput()
    # graphviz.output_file = 'profile_%s.png' % int(t1_pro)
    # with PyCallGraph(output=graphviz):
    #     # Run the main program
    #     input_dics = obspyDMT()
    #     goodbye_printer(input_dics, t1_pro)
    #     # pass the return of main to the command line.
    #     sys.exit()

if __name__ == "__main__":
    main()
