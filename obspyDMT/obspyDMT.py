#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  obspyDMT.py
#   Purpose:   obspyDMT main program 
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
import sys
import time

from .utils.data_handler import get_data
from .utils.event_handler import get_time_window
from .utils.input_handler import command_parse, read_input_command
from .utils.local_handler import process_data, plot_unit, event_filter
from .utils.metadata_handler import get_metadata
from .utils.plotxml_handler import plot_xml_response
from .utils.utility_codes import header_printer, goodbye_printer
from .utils.utility_codes import print_event_catalogs, print_data_sources
from .utils.utility_codes import print_syngine_models
from .utils.utility_codes import send_email

# =============================================================================
# ############################## obspyDMT #####################################
# =============================================================================


def dmt_core(input_dics, **kwargs):
    """
    Main function of obspyDMT toolbox.
    All the sub-main functions are organized and will be called from here.
    :param input_dics:
    :param kwargs:
    :return:
    """
    # ------------------print data sources-------------------------------------
    if input_dics['print_data_sources']:
        print_data_sources()
    # ------------------print event catalogs-----------------------------------
    if input_dics['print_event_catalogs']:
        print_event_catalogs()
    # ------------------print available syngine models-------------------------
    if input_dics['print_syngine_models']:
        print_syngine_models()
    # ------------------plot stationxml files----------------------------------
    if input_dics['plot_stationxml']:
        plot_xml_response(input_dics)
    # ------------------getting list of events/continuous requests-------------
    if input_dics['primary_mode'] in ['meta_data', 'event_based', 'continuous', 'local']:
        # events contains all the information for requested time-window
        # Although we do not have any events in continuous requests,
        # it is still called as events.
        request_ident = input_dics['primary_mode']
        if request_ident == 'meta_data':
            if input_dics['continuous']:
                request_ident = 'continuous'
            else:
                request_ident = 'event_based'
        events = get_time_window(input_dics, request=request_ident)
        events = event_filter(events, input_dics)
        print("\n#Events after filtering: %s" % len(events))
        if len(events) == 0:
            return input_dics
    # ------------------checking the availability------------------------------
    if not input_dics['event_info']:
        for ev in range(len(events)):
            info_event = '%s/%s' % (ev+1, len(events))
            if input_dics['meta_data']:
                stas_avail = get_metadata(input_dics,
                                          events[ev],
                                          info_avail=info_event)
                if not len(stas_avail) > 0:
                    continue
            if input_dics['primary_mode'] in ['event_based', 'continuous']:
                get_data(stas_avail, events[ev], input_dics,
                         info_event=info_event)
    # ------------------processing---------------------------------------------
    # From this section, we do not need to connect to the data sources anymore.
    # This consists of pre_processing and plotting tools.
    if input_dics['pre_process'] or input_dics['select_data']:
        for ev in range(len(events)):
            process_data(input_dics, events[ev])
    # ------------------plotting-----------------------------------------------
    if input_dics['plot']:
        plot_unit(input_dics, events)
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
    # printing the header
    header_printer()
    # ------------------parsing command-line options---------------------------
    (options, args, parser) = command_parse()
    # ------------------create input dictionary--------------------------------
    input_dics = read_input_command(parser)
    # run the main program
    input_dics = dmt_core(input_dics)
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
