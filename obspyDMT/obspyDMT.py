#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  obspyDMT.py
#   Purpose:   obspyDMT main program 
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
#-------------------------------------------------------------------

#-----------------------------------------------------------------------
#----------------Import required Modules (Python and Obspy)-------------
#-----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from __future__ import with_statement
import sys
import os
import math as math
import operator
import fnmatch
import fileinput
import time
import random
import shutil
import pickle
import glob
import ConfigParser
import commands
import subprocess
import tarfile
from datetime import datetime
#import multiprocessing
from lxml import objectify
from optparse import OptionParser
from datetime import datetime

try:
    import pprocess
except Exception, error:
    print "\n**************************"
    print "Unable to import pprocess."
    print "**************************\n"
    
try:
    import smtplib
except Exception, error:
    print "\n********************************************************"
    print "Unable to import smtplib. Sending email is not possible!"
    print "********************************************************\n"
    
global descrip
descrip = []

try:
    from obspy import __version__ as obs_ver
except Exception, error:
    try:
        from obspy.core import __version__ as obs_ver
    except Exception, error:
        print error
        print '------------------------------------------------------'
        print 'Do you have ObsPy properly installed on your computer?'
        print '------------------------------------------------------'
        sys.exit(2)

from obspy.core import read, UTCDateTime
from obspy.signal import seisSim, invsim
from obspy.xseed import Parser

# Required Clients from Obspy will be imported here.
from obspy.neries import Client as Client_neries
from obspy.iris import Client as Client_iris
from obspy.arclink import Client as Client_arclink
    
descrip.append('obspy ver: ' + obs_ver)
try:
    from obspy.core.util import locations2degrees
except Exception, error:
    print "\n*************************************"
    print error
    print "*************************************\n"
    from obspy.taup.taup import locations2degrees
    
import numpy as np
descrip.append('numpy ver: ' + np.__version__)
import scipy
descrip.append('scipy ver: ' + scipy.__version__)
try:
    from matplotlib import __version__ as mat_ver
    import matplotlib.pyplot as plt
    descrip.append('matplotlib ver: ' + mat_ver)
except Exception, error:
    descrip.append('matplotlib: ' + 'not installed' + '\n\n' + \
                    'error:' + '\n' + str(error) + '\n')
try:
    from mpl_toolkits.basemap import __version__ as base_ver
    from mpl_toolkits.basemap import Basemap
    descrip.append('Basemap ver: ' + base_ver)
except Exception, error:
    descrip.append('Basemap: ' + 'not installed' + '\n\n' + \
                    'error:' + '\n' + str(error) + '\n' + \
                    'You could not use the Plot module')

########################################################################
############################# Main Program #############################
########################################################################

def obspyDMT(**kwargs):
    
    """
    obspyDMT: is the function dedicated to the main part of the code.
    """ 
    
    print '\n------------------------------------------------------------' + \
            '---------------------'
    print '\t\t' + 'obspyDMT (ObsPy Data Management Tool)' + '\n'
    print '\t' + 'Automatic tool for Downloading, Processing and Management'
    print '\t\t\t' + 'of Large Seismic Datasets'
    print '\n'
    print ':copyright:'
    print 'The ObsPy Development Team (devs@obspy.org)' + '\n'
    print 'Developed by Kasra Hosseini'
    print 'email: hosseini@geophysik.uni-muenchen.de' + '\n'
    print ':license:'
    print 'GNU General Public License, Version 3'
    print '(http://www.gnu.org/licenses/gpl-3.0-standalone.html)'
    print '------------------------------------------------------------' + \
            '---------------------'
    
    # global variables
    global input, events
       
    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()
    
    # ------------------Read INPUT file (Parameters)--------------------
    if options.type == 'file':
        read_input_file()
    else:
        read_input_command(parser, **kwargs)
   
    # ------------------Getting List of Events/Continuous requests------
    if input['get_events'] == 'Y':
        get_Events(input, request = 'event-based')
    
    if input['get_continuous'] == 'Y':
        get_Events(input, request = 'continuous')
    
    # ------------------Seismicity--------------------------------------
    if input['seismicity'] == 'Y':
        seismicity()
       
    # ------------------IRIS--------------------------------------------
    if input['IRIS'] == 'Y':
        print '\n********************************************************'
        print 'IRIS -- Download waveforms, response files and meta-data'
        print '********************************************************'
        IRIS_network(input)
        
    # ------------------Arclink-----------------------------------------
    if input['ArcLink'] == 'Y':
        print '\n***********************************************************'
        print 'ArcLink -- Download waveforms, response files and meta-data'
        print '***********************************************************'
        ARC_network(input)
                
    # ------------------IRIS-Updating-----------------------------------
    if input['iris_update'] != 'N':
        print '\n*********************'
        print 'IRIS -- Updating Mode'
        print '*********************'
        IRIS_update(input, address = input['iris_update'])

    # ------------------ArcLink-Updating--------------------------------
    if input['arc_update'] != 'N':
        print '\n************************'
        print 'ArcLink -- Updating Mode'
        print '************************'
        ARC_update(input, address = input['arc_update'])
    
    # ------------------IRIS-instrument---------------------------------
    if input['iris_ic'] != 'N' or input['iris_ic_auto'] == 'Y':
        print '\n*****************************'
        print 'IRIS -- Instrument Correction'
        print '*****************************'
        IRIS_ARC_IC(input, clients = 'iris')
    
    # ------------------Arclink-instrument------------------------------
    if input['arc_ic'] != 'N' or input['arc_ic_auto'] == 'Y':
        print '\n********************************'
        print 'ArcLink -- Instrument Correction'
        print '********************************'
        IRIS_ARC_IC(input, clients = 'arc')
    
    # ------------------IRIS-merge--------------------------------------    
    if input['iris_merge'] != 'N' or input['iris_merge_auto'] == 'Y':
        print '\n*****************************'
        print 'IRIS -- Merging the waveforms'
        print '*****************************'
        IRIS_ARC_merge(input, clients = 'iris')
    
    # ------------------ArcLink-merge-----------------------------------    
    if input['arc_merge'] != 'N' or input['arc_merge_auto'] == 'Y':
        print '\n********************************'
        print 'ArcLink -- Merging the waveforms'
        print '********************************'
        IRIS_ARC_merge(input, clients = 'arc')
    
    # ------------------PLOT--------------------------------------------    
    for i in ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray', 'plot_ray_gmt', \
                'plot_epi', 'plot_dt']:
        if input[i] != 'N':
            print '\n********'
            print 'Plotting'
            print '********'
            if input['plot_all'] == 'Y' or input['plot_iris'] == 'Y':
                PLOT(input, clients = 'iris')
            if input['plot_arc'] == 'Y':
                PLOT(input, clients = 'arc')
    
    # ------------------Email-------------------------------------------    
    if input['email'] != 'N':
        print '\n*********************************************'
        print 'Sending email to the following email-address:'
        print input['email']
        print '*********************************************'
        send_email()

########################################################################
###################### Functions are defined here ######################
########################################################################
    
###################### command_parse ###################################

def command_parse():
    """
    Parsing command-line options.
    """
    # create command line option parser
    parser = OptionParser("%prog [options]")
    # configure command line options
    # action=".." tells OptionsParser what to save:
    # store_true saves bool TRUE,
    # store_false saves bool FALSE, store saves string; into the variable
    # given with dest="var"
    # * you need to provide every possible option here.
    
    helpmsg = "show the obspyDMT version and exit"
    parser.add_option("--version", action="store_true",
                      dest="version", help=helpmsg)
    
    helpmsg = "check all the dependencies and their installed versions " + \
                                        "on the local machine and exit"
    parser.add_option("--check", action="store_true",
                      dest="check", help=helpmsg)
    
    helpmsg = "Run a quick tour!"
    parser.add_option("--tour", action="store_true",
                      dest="tour", help=helpmsg)
    
    helpmsg = "type of the input ('command' or 'file') to be read by " + \
                "obspyDMT. Please note that for \"--type 'file'\" an " + \
                "external file ('INPUT.cfg') should exist in the same " + \
                "directory as obspyDMT.py [Default: command] "
    parser.add_option("--type", action="store",
                      dest="type", help=helpmsg)
    
    helpmsg = "if the datapath is found deleting it before running obspyDMT."
    parser.add_option("--reset", action="store_true",
                      dest="reset", help=helpmsg)
    
    helpmsg = "the path where obspyDMT will store the data " + \
                                        "[Default: './obspyDMT-data']"
    parser.add_option("--datapath", action="store",
                      dest="datapath", help=helpmsg)
    
    helpmsg = "start time, syntax: Y-M-D-H-M-S (eg: " + \
                "'2010-01-01-00-00-00') or just Y-M-D [Default: 10 days ago]"
    parser.add_option("--min_date", action="store",
                      dest="min_date", help=helpmsg)
    
    helpmsg = "end time, syntax: Y-M-D-H-M-S (eg: " + \
                "'2011-01-01-00-00-00') or just Y-M-D [Default: 5 days ago]"
    parser.add_option("--max_date", action="store",
                      dest="max_date", help=helpmsg)
    
    helpmsg = "event catalog (EMSC or IRIS). " + \
                "[Default: 'EMSC']"
    parser.add_option("--event_catalog", action="store",
                      dest="event_catalog", help=helpmsg)
    
    helpmsg = "magnitude type. Some common types (there are many) " + \
                "include 'Ml' (local/Richter magnitude), " + \
                "'Ms' (surface magnitude), 'mb' (body wave magnitude), " + \
                "'Mw' (moment magnitude). [Default: 'Mw']"
    parser.add_option("--mag_type", action="store",
                      dest="mag_type", help=helpmsg)
    
    helpmsg = "minimum magnitude. [Default: 5.5]"
    parser.add_option("--min_mag", action="store",
                      dest="min_mag", help=helpmsg)
    
    helpmsg = "maximum magnitude. [Default: 9.9]"
    parser.add_option("--max_mag", action="store",
                      dest="max_mag", help=helpmsg)

    helpmsg = "minimum depth. [Default: +10.0 (above the surface!)]"
    parser.add_option("--min_depth", action="store",
                      dest="min_depth", help=helpmsg)
    
    helpmsg = "maximum depth. [Default: -6000.0]"
    parser.add_option("--max_depth", action="store",
                      dest="max_depth", help=helpmsg)
                      
    helpmsg = "search for all the events within the defined rectangle, " + \
                "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax> " + \
                "[Default: -180.0/+180.0/-90.0/+90.0]"
    parser.add_option("--event_rect", action="store", dest="event_rect",
                        help=helpmsg)
    
    helpmsg = "search for all the events within the defined " + \
                "circle, syntax: <lon>/<lat>/<rmin>/<rmax>. " + \
                "May not be used together with rectangular " + \
                "bounding box event restrictions (event_rect). " + \
                "[currently just IRIS support this option]"
    parser.add_option("--event_circle", action="store",
                      dest="event_circle", help=helpmsg)
    
    helpmsg = "maximum number of events to be requested. [Default: 2500]"
    parser.add_option("--max_result", action="store",
                      dest="max_result", help=helpmsg)
    
    helpmsg = "Just retrieve the event information and create an event archive."
    parser.add_option("--event_info", action="store_true",
                      dest="event_info", help=helpmsg)
    
    helpmsg = "Create a seismicity map according to the event and " + \
                "location specifications."
    parser.add_option("--seismicity", action="store_true",
                      dest="seismicity", help=helpmsg)
    
    helpmsg = "event-based request (please refer to the tutorial). [Default: 'Y']"
    parser.add_option("--get_events", action="store",
                      dest="get_events", help=helpmsg)
    
    helpmsg = "continuous request (please refer to the tutorial)."
    parser.add_option("--continuous", action="store_true",
                      dest="get_continuous", help=helpmsg)
    
    helpmsg = "time interval for dividing the continuous request. " + \
                "[Default: 86400 sec (1 day)]"
    parser.add_option("--interval", action="store",
                      dest="interval", help=helpmsg)
    
    helpmsg = "Parallel waveform/response/paz request"
    parser.add_option("--req_parallel", action="store_true",
                      dest="req_parallel", help=helpmsg)
    
    helpmsg = "Number of processors to be used in --req_parallel. [Default: 4]"
    parser.add_option("--req_np", action="store",
                        dest="req_np", help=helpmsg)
    
    helpmsg = "using the IRIS bulkdataselect Web service. Since this " + \
                "method returns multiple channels of time series data " + \
                "for specified time ranges in one request, it speeds up " + \
                "the waveform retrieving approximately by a factor of " + \
                "two. [RECOMMENDED]"
    parser.add_option("--iris_bulk", action="store_true",
                      dest="iris_bulk", help=helpmsg)
    
    helpmsg = "retrieve the waveform. [Default: 'Y']"
    parser.add_option("--waveform", action="store",
                      dest="waveform", help=helpmsg)
    
    helpmsg = "retrieve the response file. [Default: 'Y']"
    parser.add_option("--response", action="store",
                      dest="response", help=helpmsg)
    
    helpmsg = "retrieve the PAZ."
    parser.add_option("--paz", action="store_true",
                      dest="paz", help=helpmsg)
    
    helpmsg = "send request (waveform/response) to IRIS. [Default: 'Y']"
    parser.add_option("--iris", action="store",
                      dest="IRIS", help=helpmsg)
    
    helpmsg = "send request (waveform/response) to ArcLink. [Default: 'Y']"
    parser.add_option("--arc", action="store",
                      dest="ArcLink", help=helpmsg)
    
    helpmsg = "send request (waveform) to NERIES if ArcLink fails. [Default: 'N']"
    parser.add_option("--neries", action="store_true",
                      dest="NERIES", help=helpmsg)
                 
    helpmsg = "SAC format for saving the waveforms. Station location " + \
                "(stla and stlo), station elevation (stel), " + \
                "station depth (stdp), event location (evla and evlo), " + \
                "event depth (evdp) and event magnitude (mag) " + \
                "will be stored in the SAC headers. [Default: 'Y'] "
    parser.add_option("--SAC", action="store",
                      dest="SAC", help=helpmsg)
    
    helpmsg = "MSEED format for saving the waveforms."
    parser.add_option("--mseed", action="store_true",
                      dest="mseed", help=helpmsg)
    
    helpmsg = "generate a data-time file for an IRIS request. " + \
                "This file shows the required time for each request " + \
                "and the stored data in the folder."
    parser.add_option("--time_iris", action="store_true",
                      dest="time_iris", help=helpmsg)
    
    helpmsg = "generate a data-time file for an ArcLink request. " + \
                "This file shows the required time for each request " + \
                "and the stored data in the folder."
    parser.add_option("--time_arc", action="store_true",
                      dest="time_arc", help=helpmsg)
    
    helpmsg = "time parameter in seconds which determines how close " + \
                "the time series data (waveform) will be cropped " + \
                "before the origin time of the event. Default: 0.0 seconds."
    parser.add_option("--preset", action="store",
                      dest="preset", help=helpmsg)
    
    helpmsg = "time parameter in seconds which determines how close " + \
                "the time series data (waveform) will be cropped " + \
                "after the origin time of the event. Default: 1800.0 seconds."
    parser.add_option("--offset", action="store",
                      dest="offset", help=helpmsg)
    
    helpmsg = "identity code restriction, syntax: net.sta.loc.cha " + \
                "(eg: TA.*.*.BHZ to search for all BHZ channels in " + \
                "TA network). [Default: *.*.*.*]"
    parser.add_option("--identity", action="store", dest="identity",
                        help=helpmsg)
    
    helpmsg = "network code. [Default: *]"
    parser.add_option("--net", action="store",
                      dest="net", help=helpmsg)
    
    helpmsg = "station code. [Default: *]"
    parser.add_option("--sta", action="store",
                      dest="sta", help=helpmsg)
    
    helpmsg = "location code. [Default: *]"
    parser.add_option("--loc", action="store",
                      dest="loc", help=helpmsg)
    
    helpmsg = "channel code. [Default: *]"
    parser.add_option("--cha", action="store",
                      dest="cha", help=helpmsg)
       
    helpmsg = "search for all the stations within the defined " + \
                "rectangle, GMT syntax: " + \
                "<lonmin>/<lonmax>/<latmin>/<latmax>. May not be " + \
                "used together with circular bounding box station " + \
                "restrictions (station_circle) " + \
                "[Default: -180.0/+180.0/-90.0/+90.0]"
    parser.add_option("--station_rect", action="store", 
                      dest="station_rect", help=helpmsg)
    
    helpmsg = "search for all the stations within the defined " + \
                "circle, syntax: <lon>/<lat>/<rmin>/<rmax>. " + \
                "May not be used together with rectangular " + \
                "bounding box station restrictions (station_rect)." + \
                " Currently, ArcLink does not support this option!"
    parser.add_option("--station_circle", action="store",
                      dest="station_circle", help=helpmsg)
   
    helpmsg = "test the program for the desired number of requests, " + \
                "eg: '--test 10' will test the program for 10 requests. " + \
                "[Default: 'N']"
    parser.add_option("--test", action="store",
                      dest="test", help=helpmsg)
    
    helpmsg = "update the specified folder for IRIS, syntax: " + \
                "--iris_update address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--iris_update", action="store",
                      dest="iris_update", help=helpmsg)
    
    helpmsg = "update the specified folder for ArcLink, syntax: " + \
                "--arc_update address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--arc_update", action="store",
                      dest="arc_update", help=helpmsg)
    
    helpmsg = "update the specified folder for both IRIS and ArcLink, " + \
                "syntax: --update_all address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--update_all", action="store",
                      dest="update_all", help=helpmsg)
    
    helpmsg = "apply instrument correction to the specified folder " + \
                "for the downloaded waveforms from IRIS, " + \
                "syntax: --iris_ic address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--iris_ic", action="store",
                        dest="iris_ic", help=helpmsg)
    
    helpmsg = "apply instrument correction to the specified folder " + \
                "for the downloaded waveforms from ArcLink, " + \
                "syntax: --arc_ic address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--arc_ic", action="store",
                        dest="arc_ic", help=helpmsg)
                        
    helpmsg = "apply instrument correction automatically after " + \
                "downloading the waveforms from IRIS. [Default: 'Y']"
    parser.add_option("--iris_ic_auto", action="store",
                        dest="iris_ic_auto", help=helpmsg)
    
    helpmsg = "apply instrument correction automatically after " + \
                "downloading the waveforms from ArcLink. [Default: 'Y']"
    parser.add_option("--arc_ic_auto", action="store",
                        dest="arc_ic_auto", help=helpmsg)
    
    helpmsg = "apply instrument correction to the specified folder " + \
                "for all the waveforms (IRIS and ArcLink), " + \
                "syntax: --ic_all address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--ic_all", action="store",
                        dest="ic_all", help=helpmsg)
    
    helpmsg = "do not apply instrument correction automatically. " + \
                "This is equivalent to: \"--iris_ic_auto N --arc_ic_auto N\""
    parser.add_option("--ic_no", action="store_true",
                        dest="ic_no", help=helpmsg)
    
    helpmsg = "Parallel Instrument Correction. "
    parser.add_option("--ic_parallel", action="store_true",
                        dest="ic_parallel", help=helpmsg)
    
    helpmsg = "Number of processors to be used in --ic_parallel. [Default: 20]"
    parser.add_option("--ic_np", action="store",
                        dest="ic_np", help=helpmsg)
    
    helpmsg = "Instrument Correction (full response), using obspy modules"
    parser.add_option("--ic_obspy_full", action="store",
                      dest="ic_obspy_full", help=helpmsg)
    
    helpmsg = "Instrument Correction (full response), using SAC"
    parser.add_option("--ic_sac_full", action="store_true",
                      dest="ic_sac_full", help=helpmsg)
    
    helpmsg = "Instrument Correction (Poles And Zeros), " + \
                "using SAC (for IRIS) and obspy (for ArcLink)"
    parser.add_option("--ic_paz", action="store_true",
                      dest="ic_paz", help=helpmsg)
    
    helpmsg = "apply a bandpass filter to the data trace before " + \
                "deconvolution ('None' if you do not need pre_filter), " + \
                "syntax: '(f1,f2,f3,f4)' which are the four corner " + \
                "frequencies of a cosine taper, one between f2 and f3 " + \
                "and tapers to zero for f1 < f < f2 and f3 < f < f4. " + \
                "[Default: '(0.008, 0.012, 3.0, 4.0)']"
    parser.add_option("--pre_filt", action="store",
                      dest="pre_filt", help=helpmsg)
    
    helpmsg = "correct the raw waveforms for DIS (m), VEL (m/s) or " + \
                "ACC (m/s^2). [Default: DIS]"
    parser.add_option("--corr_unit", action="store",
                      dest="corr_unit", help=helpmsg)
    
    helpmsg = "compress the raw-waveform files after applying " + \
                "instrument correction."
    parser.add_option("--zip_w", action="store_true",
                        dest="zip_w", help=helpmsg)
    
    helpmsg = "compress the response files after applying " + \
                "instrument correction."
    parser.add_option("--zip_r", action="store_true",
                        dest="zip_r", help=helpmsg)
    
    helpmsg = "merge the IRIS waveforms in the specified folder, " + \
                "syntax: --iris_merge address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--iris_merge", action="store",
                        dest="iris_merge", help=helpmsg)
    
    helpmsg = "merge the ArcLink waveforms in the specified folder, " + \
                "syntax: --arc_merge address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--arc_merge", action="store",
                        dest="arc_merge", help=helpmsg)
    
    helpmsg = "merge automatically after downloading the waveforms " + \
                "from IRIS. [Default: 'Y']"
    parser.add_option("--iris_merge_auto", action="store",
                        dest="iris_merge_auto", help=helpmsg)
    
    helpmsg = "merge automatically after downloading the waveforms " + \
                "from ArcLink. [Default: 'Y']"
    parser.add_option("--arc_merge_auto", action="store",
                        dest="arc_merge_auto", help=helpmsg)
    
    helpmsg = "merge all waveforms (IRIS and ArcLink) in the " + \
                "specified folder, syntax: --merge_all " + \
                "address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--merge_all", action="store",
                      dest="merge_all", help=helpmsg)
        
    helpmsg = "do not merge automatically. This is equivalent " + \
                "to: \"--iris_merge_auto N --arc_merge_auto N\""
    parser.add_option("--merge_no", action="store_true",
                      dest="merge_no", help=helpmsg)
    
    helpmsg = "merge 'raw' or 'corrected' waveforms. [Default: 'raw']"
    parser.add_option("--merge_type", action="store",
                        dest="merge_type", help=helpmsg)
    
    helpmsg = "plot waveforms downloaded from IRIS."
    parser.add_option("--plot_iris", action="store_true",
                      dest="plot_iris", help=helpmsg)
    
    helpmsg = "plot waveforms downloaded from ArcLink."
    parser.add_option("--plot_arc", action="store_true",
                      dest="plot_arc", help=helpmsg)
    
    helpmsg = "plot all waveforms (IRIS and ArcLink). [Default: 'Y']"
    parser.add_option("--plot_all", action="store",
                      dest="plot_all", help=helpmsg)
    
    helpmsg = "plot 'raw' or 'corrected' waveforms. [Default: 'raw']"
    parser.add_option("--plot_type", action="store",
                        dest="plot_type", help=helpmsg)
    
    helpmsg = "plot all the events, stations and ray path between them " + \
                "found in the specified folder, " + \
                "syntax: --plot_ray_gmt address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--plot_ray_gmt", action="store",
                      dest="plot_ray_gmt", help=helpmsg)
    
    helpmsg = "plot all the events found in the specified folder, " + \
                "syntax: --plot_ev address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--plot_ev", action="store",
                      dest="plot_ev", help=helpmsg)
                      
    helpmsg = "plot all the stations found in the specified folder, " + \
                "syntax: --plot_sta address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--plot_sta", action="store",
                      dest="plot_sta", help=helpmsg)
                      
    helpmsg = "plot both all the stations and all the events found " + \
                "in the specified folder, syntax: --plot_se " + \
                "address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--plot_se", action="store",
                      dest="plot_se", help=helpmsg)
                      
    helpmsg = "plot the ray coverage for all the station-event " + \
                "pairs found in the specified folder, syntax: " + \
                "--plot_ray address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--plot_ray", action="store",
                      dest="plot_ray", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" for all the " + \
                "waveforms found in the specified folder, " + \
                "syntax: --plot_epi address_of_the_target_folder. " + \
                "[Default: 'N']"
    parser.add_option("--plot_epi", action="store",
                      dest="plot_epi", help=helpmsg)
                      
    helpmsg = "plot \"epicentral distance-time\" (refer to " + \
                "'--plot_epi') for all the waveforms with " + \
                "epicentral-distance >= min_epi. [Default: 0.0]"
    parser.add_option("--min_epi", action="store",
                      dest="min_epi", help=helpmsg)
    
    helpmsg = "plot \"epicentral distance-time\" (refer to " + \
                "'--plot_epi') for all the waveforms with " + \
                "epicentral-distance <= max_epi. [Default: 180.0]"
    parser.add_option("--max_epi", action="store",
                      dest="max_epi", help=helpmsg)
    
    helpmsg = "plot \"Data(MB)-Time(Sec)\" -- ATTENTION: " + \
                "\"time_iris\" and/or \"time_arc\" should exist in the " + \
                "\"info\" folder [refer to " + \
                "\"time_iris\" and \"time_arc\" options] " + \
                "[Default: 'N']"
    parser.add_option("--plot_dt", action="store",
                      dest="plot_dt", help=helpmsg)
    
    helpmsg = "the path where obspyDMT will store " + \
                "the plots [Default: '.' (the same directory " + \
                "as obspyDMT.py)]"
    parser.add_option("--plot_save", action="store",
                      dest="plot_save", help=helpmsg)
    
    helpmsg = "format of the plots saved on the local machine " + \
                "[Default: 'png']"
    parser.add_option("--plot_format", action="store",
                      dest="plot_format", help=helpmsg)
    
    helpmsg = "send an email to the specified email-address after " + \
                "completing the job, syntax: --email " + \
                "email_address. [Default: 'N']"
    parser.add_option("--email", action="store",
                      dest="email", help=helpmsg)
    
    # parse command line options
    (options, args) = parser.parse_args()
    
    return options, args, parser

###################### read_input_command ##############################

def read_input_command(parser, **kwargs):
    """
    Create input object (dictionary) based on command-line options.
    The default values are as "input" object (below) 
    [same in INPUT-default.cfg]
    """
    global input, descrip
    
    # Defining the default values. 
    # Each of these values could be changed:
    # 1. By changing the 'INPUT.cfg' file (if you use 
    # "'./obspyDMT.py --type file'")
    # 2. By defining the required command-line flag (if you use 
    # "'./obspyDMT.py --type command'")
    input = {   'datapath': 'obspyDMT-data',
                'min_date': str(UTCDateTime() - 60 * 60 * 24 * 10 * 1),
                'max_date': str(UTCDateTime() - 60 * 60 * 24 * 5 * 1),
                'event_catalog': 'EMSC',
                'mag_type': 'Mw',
                'min_mag': 5.5, 'max_mag': 9.9,
                'min_depth': +10.0, 'max_depth': -6000.0,
                'get_events': 'Y',
                'interval': 3600*24,
                'req_np': 4,
                'waveform': 'Y', 'response': 'Y',
                'IRIS': 'Y', 'ArcLink': 'Y',
                'SAC': 'Y',
                'preset': 0.0, 'offset': 1800.0,
                'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
                'evlatmin': None, 'evlatmax': None, 
                'evlonmin': None, 'evlonmax': None,
                'evlat': None, 'evlon': None, 
                'evradmin': None, 'evradmax': None,
                'max_result': 2500,
                'lat_cba': None, 'lon_cba': None, 
                'mr_cba': None, 'Mr_cba': None,
                'mlat_rbb': None, 'Mlat_rbb': None, 
                'mlon_rbb': None, 'Mlon_rbb': None,
                'test': 'N',
                'iris_update': 'N', 'arc_update': 'N', 'update_all': 'N',
                'email': 'N',
                'ic_all': 'N',
                'iris_ic': 'N', 'iris_ic_auto': 'Y',
                'arc_ic': 'N', 'arc_ic_auto': 'Y',
                'ic_np': 20,
                'ic_obspy_full': 'Y',
                'pre_filt': '(0.008, 0.012, 3.0, 4.0)',
                'corr_unit': 'DIS',
                'merge_all': 'N',
                'iris_merge': 'N', 'iris_merge_auto': 'Y',
                'merge_type': 'raw',
                'arc_merge': 'N', 'arc_merge_auto': 'Y',
                'plot_all': 'Y',
                'plot_type': 'raw',
                'plot_ev': 'N', 'plot_sta': 'N', 'plot_se': 'N',
                'plot_ray': 'N', 'plot_epi': 'N', 'plot_dt': 'N',
                'plot_ray_gmt': 'N',
                'plot_save': '.', 'plot_format': 'png',
                'min_epi': 0.0, 'max_epi': 180.0,
            }
    
    # feed input dictionary of defaults into parser object
    parser.set_defaults(**input)
    
    # parse command line options
    (options, args) = parser.parse_args()
    # command line options can now be accessed via options.varname.
    
    # Check if keyword arguments have been passed to the main function from
    # another script and parse here:
    if kwargs:
        # assigning kwargs to entries of OptionParser object
        for arg in kwargs:
            exec("options.%s = kwargs[arg]") % arg
    
    if options.version: 
        print '\t\t' + '*********************************'
        print '\t\t' + '*        obspyDMT version:      *' 
        print '\t\t' + '*' + '\t\t' + '0.4.0' + '\t\t' + '*'
        print '\t\t' + '*********************************'
        print '\n'
        sys.exit(2)
    
    # Check whether it is possible to import all required modules
    if options.check:
        print "*********************************"
        print "Check all the BASIC dependencies:"
        for i in range(0, len(descrip)):
            print descrip[i]
        print "*********************************\n"
        sys.exit(2)
        
    if options.tour:
        print '\n########################################'
        print 'obspyDMT Quick Tour will start in 5 sec!'
        print '########################################\n'
        time.sleep(5)
        options.datapath = './DMT-Tour-Data'
        options.min_date = '2011-03-10'
        options.max_date = '2011-03-12'
        options.min_mag = '8.9'
        options.identity = 'TA.1*.*.BHZ'
        options.event_catalog = 'IRIS'
        options.req_parallel = True
        options.ArcLink = 'N'
    
    # parse datapath (check if given absolute or relative)
    if options.datapath:
        if not os.path.isabs(options.datapath):
            options.datapath = os.path.join(os.getcwd(), options.datapath)
    
    if options.iris_update != 'N':
        if not os.path.isabs(options.iris_update):
            options.iris_update = os.path.join(os.getcwd(), options.iris_update)
    
    if options.arc_update != 'N':
        if not os.path.isabs(options.arc_update):
            options.arc_update = os.path.join(os.getcwd(), options.arc_update)
    
    if options.update_all != 'N':
        if not os.path.isabs(options.update_all):
            options.update_all = os.path.join(os.getcwd(), options.update_all)
    
    if options.iris_ic != 'N':
        if not os.path.isabs(options.iris_ic):
            options.iris_ic = os.path.join(os.getcwd(), options.iris_ic)
    
    if options.arc_ic != 'N':
        if not os.path.isabs(options.arc_ic):
            options.arc_ic = os.path.join(os.getcwd(), options.arc_ic)
    
    if options.ic_all != 'N':
        if not os.path.isabs(options.ic_all):
            options.ic_all = os.path.join(os.getcwd(), options.ic_all)
    
    if options.iris_merge != 'N':
        if not os.path.isabs(options.iris_merge):
            options.iris_merge = os.path.join(os.getcwd(), options.iris_merge)
    
    if options.arc_merge != 'N':
        if not os.path.isabs(options.arc_merge):
            options.arc_merge = os.path.join(os.getcwd(), options.arc_merge)
    
    if options.merge_all != 'N':
        if not os.path.isabs(options.merge_all):
            options.merge_all = os.path.join(os.getcwd(), options.merge_all)
    
    if options.plot_ev != 'N':
        if not os.path.isabs(options.plot_ev):
            options.plot_ev = os.path.join(os.getcwd(), options.plot_ev)
            
    if options.plot_sta != 'N':
        if not os.path.isabs(options.plot_sta):
            options.plot_sta = os.path.join(os.getcwd(), options.plot_sta)
    
    if options.plot_se != 'N':
        if not os.path.isabs(options.plot_se):
            options.plot_se = os.path.join(os.getcwd(), options.plot_se)
    
    if options.plot_ray != 'N':
        if not os.path.isabs(options.plot_ray):
            options.plot_ray = os.path.join(os.getcwd(), options.plot_ray)
    
    if options.plot_ray_gmt != 'N':
        if not os.path.isabs(options.plot_ray_gmt):
            options.plot_ray_gmt = os.path.join(os.getcwd(), options.plot_ray_gmt)
    
    if options.plot_epi != 'N':
        if not os.path.isabs(options.plot_epi):
            options.plot_epi = os.path.join(os.getcwd(), options.plot_epi)
    
    if options.plot_dt != 'N':
        if not os.path.isabs(options.plot_dt):
            options.plot_dt = os.path.join(os.getcwd(), options.plot_dt)
    
    if options.plot_save != 'N':
        if not os.path.isabs(options.plot_save):
            options.plot_save = os.path.join(os.getcwd(), options.plot_save)
        
    # extract min. and max. longitude and latitude if the user has given the
    # coordinates with -r (GMT syntax)
    if options.event_rect:
        try:
            options.event_rect = options.event_rect.split('/')
            if len(options.event_rect) != 4:
                print "Erroneous rectangle given."
                sys.exit(2)
            options.evlonmin = float(options.event_rect[0])
            options.evlonmax = float(options.event_rect[1])
            options.evlatmin = float(options.event_rect[2])
            options.evlatmax = float(options.event_rect[3])
        except:
            print "Erroneous rectangle given."
            sys.exit(2)
    
    # circular event restriction option parsing
    if options.event_circle:
        try:
            options.event_circle = options.event_circle.split('/')
            if len(options.event_circle) != 4:
                print "Erroneous circle given."
                sys.exit(2)
            options.evlon = float(options.event_circle[0])
            options.evlat = float(options.event_circle[1])
            options.evradmin = float(options.event_circle[2])
            options.evradmax = float(options.event_circle[3])
        except:
            print "Erroneous circle given."
            sys.exit(2)
    
    # extract min. and max. longitude and latitude if the user has given the
    # coordinates with -g (GMT syntax)
    if options.station_rect:
        try:
            options.station_rect = options.station_rect.split('/')
            if len(options.station_rect) != 4:
                print "Erroneous rectangle given."
                sys.exit(2)
            options.mlon_rbb = float(options.station_rect[0])
            options.Mlon_rbb = float(options.station_rect[1])
            options.mlat_rbb = float(options.station_rect[2])
            options.Mlat_rbb = float(options.station_rect[3])
        except:
            print "Erroneous rectangle given."
            sys.exit(2)
    
    # circular station restriction option parsing
    if options.station_circle:
        try:
            options.station_circle = options.station_circle.split('/')
            if len(options.station_circle) != 4:
                print "Erroneous circle given."
                sys.exit(2)
            options.lon_cba = float(options.station_circle[0])
            options.lat_cba = float(options.station_circle[1])
            options.mr_cba = float(options.station_circle[2])
            options.Mr_cba = float(options.station_circle[3])
        except:
            print "Erroneous circle given."
            sys.exit(2)
    
    # delete data path if -R or --reset args are given at cmdline
    if options.reset:
        # try-except so we don't get an exception if path doesnt exist
        try:
            shutil.rmtree(options.datapath)
            print '----------------------------------'
            print 'The following folder has been deleted:'
            print str(options.datapath)
            print 'obspyDMT is going to create a new folder...'
            print '----------------------------------'
        except:
            pass
    
    # Extract network, station, location, channel if the user has given an
    # identity code (-i xx.xx.xx.xx)
    if options.identity:
        try:
            options.net, options.sta, options.loc, options.cha = \
                                    options.identity.split('.')
        except:
            print "Erroneous identity code given."
            sys.exit(2)
    
    input['datapath'] = options.datapath
    input['min_date'] = str(UTCDateTime(options.min_date))
    input['max_date'] = str(UTCDateTime(options.max_date))
    input['event_catalog'] = options.event_catalog.upper()
    input['mag_type'] = options.mag_type
    input['min_mag'] = float(options.min_mag)
    input['max_mag'] = float(options.max_mag)
    input['min_depth'] = float(options.min_depth)
    input['max_depth'] = float(options.max_depth)
    input['evlonmin'] = options.evlonmin
    input['evlonmax'] = options.evlonmax
    input['evlatmin'] = options.evlatmin
    input['evlatmax'] = options.evlatmax
    input['evlat'] = options.evlat
    input['evlon'] = options.evlon
    input['evradmax'] = options.evradmax
    input['evradmin'] = options.evradmin
    input['preset'] = float(options.preset)
    input['offset'] = float(options.offset)
    input['max_result'] = int(options.max_result)
    if options.seismicity:
        input['seismicity'] = 'Y'
    else:
        input['seismicity'] = 'N'
    input['get_events'] = options.get_events
    if options.get_continuous:
        input['get_events'] = 'N'
        input['get_continuous'] = 'Y'
    else:
        input['get_continuous'] = 'N'
    input['interval'] = float(options.interval)
    if options.req_parallel: options.req_parallel = 'Y'
    input['req_parallel'] = options.req_parallel
    input['req_np'] = int(options.req_np)
    if options.iris_bulk: options.iris_bulk = 'Y'
    input['iris_bulk'] = options.iris_bulk
    input['waveform'] = options.waveform
    input['response'] = options.response
    if options.paz: options.paz = 'Y'
    input['paz'] = options.paz
    input['SAC'] = options.SAC
    if options.mseed: input['SAC'] = 'N'
    input['IRIS'] = options.IRIS
    input['ArcLink'] = options.ArcLink
    if options.NERIES: options.NERIES = 'Y'
    input['NERIES'] = options.NERIES
    if options.time_iris: options.time_iris = 'Y'
    input['time_iris'] = options.time_iris
    if options.time_arc: options.time_arc = 'Y'
    input['time_arc'] = options.time_arc
    input['net'] = options.net
    input['sta'] = options.sta
    if options.loc == "''":
        input['loc'] = ''
    elif options.loc == '""':
        input['loc'] = ''
    else:
        input['loc'] = options.loc
    input['cha'] = options.cha
    input['lon_cba'] = options.lon_cba
    input['lat_cba'] = options.lat_cba
    input['mr_cba'] = options.mr_cba
    input['Mr_cba'] = options.Mr_cba
    input['mlon_rbb'] = options.mlon_rbb
    input['Mlon_rbb'] = options.Mlon_rbb
    input['mlat_rbb'] = options.mlat_rbb
    input['Mlat_rbb'] = options.Mlat_rbb    
    if options.test != 'N':
        input['test'] = 'Y'
        input['test_num'] = int(options.test)
    input['iris_update'] = options.iris_update
    input['arc_update'] = options.arc_update
    input['update_all'] = options.update_all
    if input['update_all'] != 'N':
        input['iris_update'] = input['update_all']
        input['arc_update'] = input['update_all']
    input['iris_ic'] = options.iris_ic
    input['iris_ic_auto'] = options.iris_ic_auto
    input['arc_ic'] = options.arc_ic
    input['arc_ic_auto'] = options.arc_ic_auto
    input['ic_all'] = options.ic_all
    if input['ic_all'] != 'N':
        input['iris_ic'] = input['ic_all']
        input['arc_ic'] = input['ic_all']
    if options.ic_parallel: options.ic_parallel = 'Y'
    input['ic_parallel'] = options.ic_parallel
    input['ic_np'] = int(options.ic_np)
    input['ic_obspy_full'] = options.ic_obspy_full
    if options.ic_sac_full: options.ic_sac_full = 'Y'
    input['ic_sac_full'] = options.ic_sac_full
    if options.ic_paz: options.ic_paz = 'Y'
    input['ic_paz'] = options.ic_paz
    if input['ic_sac_full'] == 'Y' or input['ic_paz'] == 'Y':
        input['SAC'] = 'Y'
        input['ic_obspy_full'] = 'N'
    input['corr_unit'] = options.corr_unit
    input['pre_filt'] = options.pre_filt
    if options.zip_w: options.zip_w = 'Y'
    input['zip_w'] = options.zip_w
    if options.zip_r: options.zip_r = 'Y'
    input['zip_r'] = options.zip_r
    input['iris_merge'] = options.iris_merge
    input['arc_merge'] = options.arc_merge
    input['merge_all'] = options.merge_all
    if input['merge_all'] != 'N':
        input['iris_merge'] = input['merge_all']
        input['arc_merge'] = input['merge_all']
    input['plot_type'] = options.plot_type
    input['plot_all'] = options.plot_all
    if options.plot_iris: options.plot_iris = 'Y'
    input['plot_iris'] = options.plot_iris
    if options.plot_arc: options.plot_arc = 'Y'
    input['plot_arc'] = options.plot_arc
    input['plot_ev'] = options.plot_ev
    input['plot_sta'] = options.plot_sta
    input['plot_se'] = options.plot_se
    input['plot_ray'] = options.plot_ray
    input['plot_ray_gmt'] = options.plot_ray_gmt
    input['plot_epi'] = options.plot_epi
    input['plot_dt'] = options.plot_dt
    input['min_epi'] = float(options.min_epi)
    input['max_epi'] = float(options.max_epi)
    input['plot_save'] = options.plot_save
    input['plot_format'] = options.plot_format
    input['email'] = options.email
    
    #--------------------------------------------------------
    if input['get_continuous'] == 'N':
        input['iris_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
    else:
        input['iris_merge_auto'] = options.iris_merge_auto
        input['arc_merge_auto'] = options.arc_merge_auto
        input['merge_type'] = options.merge_type
        
    for i in ['iris_update', 'arc_update', 'iris_ic', 'arc_ic', \
                'iris_merge', 'arc_merge', 'plot_se', 'plot_sta', \
                'plot_ev', 'plot_ray', 'plot_ray_gmt', 'plot_epi', \
                'plot_dt']:
        if input[i] != 'N':
            input['datapath'] = input[i]
            input['get_events'] = 'N'
            input['get_continuous'] = 'N'
            input['IRIS'] = 'N'
            input['ArcLink'] = 'N'
            input['iris_ic_auto'] = 'N'
            input['arc_ic_auto'] = 'N'
            input['iris_merge_auto'] = 'N'
            input['arc_merge_auto'] = 'N'
    
    if options.IRIS == 'N':
        input['iris_ic_auto'] = 'N'
        input['iris_merge_auto'] = 'N'
    if options.ArcLink == 'N':
        input['arc_ic_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
    
    if options.ic_no:
        input['iris_ic_auto'] = 'N'
        input['arc_ic_auto'] = 'N'
    
    if options.merge_no:
        input['iris_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
    
    if input['plot_iris'] == 'Y' or input['plot_arc'] == 'Y':
        input['plot_all'] = 'N'
    
    if options.event_info:
        input['IRIS'] = 'N'
        input['ArcLink'] = 'N'
        input['iris_ic_auto'] = 'N'
        input['arc_ic_auto'] = 'N'
        input['iris_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
    
    if options.seismicity:
        input['IRIS'] = 'N'
        input['ArcLink'] = 'N'
        input['iris_ic_auto'] = 'N'
        input['arc_ic_auto'] = 'N'
        input['iris_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
        input['max_result'] = 1000000
     
    if input['req_parallel'] == 'Y' or input['ic_parallel'] == 'Y':
        try:
            import pprocess
        except Exception, error:
            print '***************************************************'
            print 'WARNING:'
            print 'ppross is not installed on your machine!'
            print 'for more info: http://pypi.python.org/pypi/pprocess'
            print '\nobspyDMT will work in Serial mode.'
            print '***************************************************'
            input['req_parallel'] = 'N'; input['ic_parallel'] = 'N'
            
###################### read_input_file #################################

def read_input_file():  
    
    """
    #SHOULD BE CHANGED!
    Read inputs from INPUT.cfg file.
    
    This module will read the INPUT.cfg file which is 
    located in the same folder as obspyDMT.py
    
    Please note that if you choose (nodes = Y) then:
    * min_datetime
    * max_datetime
    * min_magnitude
    * max_magnitude
    will be selected based on INPUT-Periods file.
    """
    
    global input
    
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(os.getcwd(), 'INPUT.cfg'))

    input = {}
    input['datapath'] = config.get('Address_info', 'datapath')
    input['inter_address'] = config.get('Address_info', 'interactive_address')
    input['target_folder'] = config.get('Address_info', 'target_folder')
    input['save_folder'] = config.get('Address_info', 'save_folder')
    
    if not os.path.isabs(input['datapath']):
        input['datapath'] = os.path.join(os.getcwd(), input['datapath'])
    
    if not os.path.isabs(input['inter_address']):
        input['inter_address'] = os.path.join(os.getcwd(), input['inter_address'])
    
    if not os.path.isabs(input['target_folder']):
        input['target_folder'] = os.path.join(os.getcwd(), input['target_folder'])
    
    if not os.path.isabs(input['save_folder']):
        input['save_folder'] = os.path.join(os.getcwd(), input['save_folder'])
        
    
    input['min_date'] = str(eval(config.get('Event_Request', 'min_datetime')))
    input['max_date'] = str(eval(config.get('Event_Request', 'max_datetime')))
    input['min_mag'] = config.getfloat('Event_Request', 'min_magnitude')
    input['max_mag'] = config.getfloat('Event_Request', 'max_magnitude')
    input['min_depth'] = config.getfloat('Event_Request', 'min_depth')
    input['max_depth'] = config.getfloat('Event_Request', 'max_depth')
    input['evlonmin'] = config.getfloat('Event_Request', 'evlonmin')
    input['evlonmax'] = config.getfloat('Event_Request', 'evlonmax')
    input['evlatmin'] = config.getfloat('Event_Request', 'evlatmin')
    input['evlatmax'] = config.getfloat('Event_Request', 'evlatmax')
    input['preset'] = config.getfloat('Event_Request', 'preset')
    input['offset'] = config.getfloat('Event_Request', 'offset')
    input['max_result'] = config.getint('Event_Request', 'max_results')
    
    input['get_events'] = config.get('Request', 'get_events')
    input['input_period'] = config.get('Parallel', 'input_period')
    input['IRIS'] = config.get('Request', 'IRIS')
    input['ArcLink'] = config.get('Request', 'ArcLink')
    input['time_iris'] = config.get('Request', 'time_iris')
    input['time_arc'] = config.get('Request', 'time_arc')
    
    input['nodes'] = config.get('Parallel', 'nodes')

    input['waveform'] = config.get('Request', 'waveform')
    input['response'] = config.get('Request', 'response')
    input['SAC'] = config.get('Request', 'SAC')
    
    input['net'] = config.get('specifications_request', 'network')
    input['sta'] = config.get('specifications_request', 'station')
    
    if config.get('specifications_request', 'location') == "''":
        input['loc'] = ''
    elif config.get('specifications_request', 'location') == '""':
        input['loc'] = ''
    else:
        input['loc'] = config.get('specifications_request', 'location')
    
    input['cha'] = config.get('specifications_request', 'channel')

    if config.get('specifications_request', 'lat') == 'None':
        input['lat_cba'] = None
    else:
        input['lat_cba'] = config.get('specifications_request', 'lat')
        
    if config.get('specifications_request', 'lon') == 'None':
        input['lon_cba'] = None
    else:
        input['lon_cba'] = config.get('specifications_request', 'lon')
    
    if config.get('specifications_request', 'minradius') == 'None':
        input['mr_cba'] = None
    else:
        input['mr_cba'] = config.get('specifications_request', 'minradius')
    
    if config.get('specifications_request', 'maxradius') == 'None':
        input['Mr_cba'] = None
    else:
        input['Mr_cba'] = config.get('specifications_request', 'maxradius')
    
        
    if config.get('specifications_request', 'minlat') == 'None':
        input['mlat_rbb'] = None
    else:
        input['mlat_rbb'] = config.get('specifications_request', 'minlat')
    
    if config.get('specifications_request', 'maxlat') == 'None':
        input['Mlat_rbb'] = None
    else:
        input['Mlat_rbb'] = config.get('specifications_request', 'maxlat')
    
    if config.get('specifications_request', 'minlon') == 'None':
        input['mlon_rbb'] = None
    else:
        input['mlon_rbb'] = config.get('specifications_request', 'minlon')
    
    if config.get('specifications_request', 'maxlon') == 'None':
        input['Mlon_rbb'] = None
    else:
        input['Mlon_rbb'] = config.get('specifications_request', 'maxlon')

    
    input['test'] = config.get('test', 'test')
    input['test_num'] = config.getint('test', 'test_num')
    
    input['update_interactive'] = config.get('update', 'update_interactive')
    input['iris_update'] = config.get('update', 'iris_update')
    input['arc_update'] = config.get('update', 'arc_update')

    input['QC_IRIS'] = config.get('QC', 'QC_IRIS')
    input['QC_ARC'] = config.get('QC', 'QC_ARC')
    
    input['email'] = config.get('email', 'email')
    input['email_address'] = config.get('email', 'email_address')
    
    input['report'] = config.get('report', 'report')
    
    input['corr_unit'] = config.get('instrument_correction', 'corr_unit')
    input['pre_filt'] = config.get('instrument_correction', 'pre_filter')
    
    input['plt_event'] = config.get('ObsPyPT', 'plot_event')
    input['plt_sta'] = config.get('ObsPyPT', 'plot_sta')
    input['plt_ray'] = config.get('ObsPyPT', 'plot_ray')

    input['llcrnrlon'] = config.getfloat('ObsPyPT', 'llcrnrlon')
    input['urcrnrlon'] = config.getfloat('ObsPyPT', 'urcrnrlon')
    input['llcrnrlat'] = config.getfloat('ObsPyPT', 'llcrnrlat')
    input['urcrnrlat'] = config.getfloat('ObsPyPT', 'urcrnrlat')
    
    input['lon_0'] = config.getfloat('ObsPyPT', 'lon_0')
    input['lat_0'] = config.getfloat('ObsPyPT', 'lat_0')

###################### get_Events ######################################

def get_Events(input, request):
    """
    Getting list of events from NERIES
    
    NERIES: a client for the Seismic Data Portal (http://www.seismicportal.eu) 
    which was developed under the European Commission-funded NERIES project. 
    
    The Portal provides a single point of access to diverse, 
    distributed European earthquake data provided in a unique joint 
    initiative by observatories and research institutes in and around Europe.
    """
    t_event_1 = datetime.now()
    global events
    Period = input['min_date'].split('T')[0] + '_' + \
        input['max_date'].split('T')[0] + '_' + \
        str(input['min_mag']) + '_' + str(input['max_mag'])
    eventpath = os.path.join(input['datapath'], Period)
    if os.path.exists(eventpath) == True:
        print '\n\n********************************************************'
        if raw_input('Directory for the requested period already exists:\n' +
            str(eventpath) + '\n\n' + 
            'Options:' + '\n' + 'N: Close the program and try the ' + 
            'updating mode.' + '\n' + 
            'Y: Remove the tree, continue the program ' + 
            'and re-download.\n').upper() == 'Y':
            print '********************************************************'
            shutil.rmtree(eventpath)
            os.makedirs(eventpath)
        
        else:
            print 'EXIT'
            sys.exit()
    else:
        os.makedirs(eventpath)
    events = events_info(request)
    os.makedirs(os.path.join(eventpath, 'EVENTS-INFO'))
    # logging the command line
    input_logger(argus = sys.argv, 
                 address = os.path.join(eventpath, 'EVENTS-INFO', 'logger.txt'),
                 inputs = input)
    len_events = len(events)
    for i in range(0, len_events):
        print "-------------------------------------------------"
        print "Event No:" + " " + str(i+1)
        print "Date Time:" + " " + str(events[i]['datetime'])
        print "Depth:" + " " + str(events[i]['depth'])
        print "Event-ID:" + " " + events[i]['event_id']
        try:
            print "Flynn-Region:" + " " + events[i]['flynn_region']
        except Exception, e:
            print "Flynn-Region:" + " " + "NONE"
        print "Latitude:" + " " + str(events[i]['latitude'])
        print "Longitude:" + " " + str(events[i]['longitude'])
        print "Magnitude:" + " " + str(events[i]['magnitude'])
    print "-------------------------------------------------"
    Event_cat = open(os.path.join(eventpath, 'EVENTS-INFO', 'EVENT-CATALOG'), 'a+')
    Event_cat.writelines(str(Period) + '\n')
    Event_cat.writelines('-------------------------------------' + '\n')
    Event_cat.writelines('Information about the requested Events:' + '\n\n')
    Event_cat.writelines('Number of Events: ' + str(len_events) + '\n')
    Event_cat.writelines('min datetime: ' + str(input['min_date']) + '\n')
    Event_cat.writelines('max datetime: ' + str(input['max_date']) + '\n')
    Event_cat.writelines('min magnitude: ' + str(input['min_mag']) + '\n')
    Event_cat.writelines('max magnitude: ' + str(input['max_mag']) + '\n')
    Event_cat.writelines('min latitude: ' + str(input['evlatmin']) + '\n')
    Event_cat.writelines('max latitude: ' + str(input['evlatmax']) + '\n')
    Event_cat.writelines('min longitude: ' + str(input['evlonmin']) + '\n')
    Event_cat.writelines('max longitude: ' + str(input['evlonmax']) + '\n')
    Event_cat.writelines('min depth: ' + str(input['min_depth']) + '\n')
    Event_cat.writelines('max depth: ' + str(input['max_depth']) + '\n')
    Event_cat.writelines('-------------------------------------' + '\n\n')
    Event_cat.close()
    
    for j in range(0, len_events):
        Event_cat = open(os.path.join(eventpath, 'EVENTS-INFO', 'EVENT-CATALOG'), 'a')
        Event_cat.writelines("Event No: " + str(j) + '\n')
        Event_cat.writelines("Event-ID: " + str(events[j]['event_id']) + '\n')
        Event_cat.writelines("Date Time: " + str(events[j]['datetime']) + '\n')
        Event_cat.writelines("Magnitude: " + str(events[j]['magnitude']) + '\n')
        Event_cat.writelines("Depth: " + str(events[j]['depth']) + '\n')
        Event_cat.writelines("Latitude: " + str(events[j]['latitude']) + '\n')
        Event_cat.writelines("Longitude: " + str(events[j]['longitude']) + '\n')
        
        try:
            Event_cat.writelines("Flynn-Region: " + \
                                str(events[j]['flynn_region']) + '\n')
        except Exception, e:
            Event_cat.writelines("Flynn-Region: " + 'None' + '\n')
        Event_cat.writelines('-------------------------------------' + '\n')
        Event_cat.close()
    Event_file = open(os.path.join(eventpath, 'EVENTS-INFO', 'event_list'), 'a+')
    pickle.dump(events, Event_file)
    Event_file.close()
    print 'Number of events: %s' %(len_events)
    t_event_2 = datetime.now()
    t_event = t_event_2 - t_event_1
    print 'Time for retrieving and saving the event info: %s' %(t_event)
    return events

###################### events_info #####################################

def events_info(request):
    """
    Get the event(s) info for event-based or continuous requests
    """
    global input
    if request == 'event-based':
        if input['evlatmin']==None:
            evlatmin=-90.0;evlatmax=+90.0;evlonmin=-180.0;evlonmax=+180.0
        else:
            evlatmin=input['evlatmin'];evlatmax=input['evlatmax']
            evlonmin=input['evlonmin'];evlonmax=input['evlonmax']
        print 'Event Catalog: ',
        if input['event_catalog'] == 'EMSC':
            print 'EMSC'
            client_neries = Client_neries()
            events = client_neries.getEvents(min_datetime=input['min_date'], \
                max_datetime=input['max_date'], min_magnitude=input['min_mag'], \
                max_magnitude=input['max_mag'], min_latitude=evlatmin, \
                max_latitude=evlatmax, min_longitude=evlonmin, \
                max_longitude=evlonmax, min_depth = input['min_depth'], \
                max_depth=input['max_depth'], magnitude_type=input['mag_type'],
                max_results=input['max_result'])
        elif input['event_catalog'] == 'IRIS':
            try:
                if input['evlat']==None:
                    evlat=0.0;evlon=0.0;evradmax=180.0;evradmin=0.0
                else:
                    evlat=input['evlat'];evlon=input['evlon']
                    evradmax=input['evradmax'];evradmin=input['evradmin']
                print 'IRIS'
                client_iris = Client_iris()
                events_QML = client_iris.getEvents(\
                        minlat=evlatmin,maxlat=evlatmax,\
                        minlon=evlonmin,maxlon=evlonmax,\
                        lat=evlat,lon=evlon,\
                        maxradius=evradmax,minradius=evradmin,\
                        mindepth=-input['min_depth'],maxdepth=-input['max_depth'],\
                        starttime=input['min_date'],endtime=input['max_date'],\
                        minmag=input['min_mag'],maxmag=input['max_mag'],\
                        magtype=input['mag_type'])
                events = []
                for i in range(0, len(events_QML)):
                    event_time = events_QML.events[i].origins[0].time
                    if event_time.month < 10:
                        event_time_month = '0' + str(event_time.month)
                    else:
                        event_time_month = str(event_time.month)
                    if event_time.day < 10:
                        event_time_day = '0' + str(event_time.day)
                    else:
                        event_time_day = str(event_time.day)
                    events.append({\
                        'author': \
                            events_QML.events[i].magnitudes[0].creation_info.author, \
                        'event_id': str(event_time.year) + event_time_month + \
                                     event_time_day + '_' + str(i), \
                        'origin_id': 'NAN', \
                        'longitude': events_QML.events[i].origins[0].longitude, \
                        'latitude': events_QML.events[i].origins[0].latitude, \
                        'datetime': event_time, \
                        'depth': -events_QML.events[i].origins[0].depth, \
                        'magnitude': events_QML.events[i].magnitudes[0].mag, \
                        'magnitude_type': \
                            events_QML.events[i].magnitudes[0].magnitude_type.lower(), \
                        'flynn_region': 'NAN'})
            except Exception, e:
                print 30*'-'
                print e
                print 30*'-'
                events = []
        for i in range(0, len(events)):
            #client_iris.flinnengdahl(lat=-1.196, lon=121.33, rtype="code")
            events[i]['t1'] = events[i]['datetime'] - input['preset']
            events[i]['t2'] = events[i]['datetime'] + input['offset']
    elif request == 'continuous':
        print 'Start identifying the intervals...',
        m_date = UTCDateTime(input['min_date'])
        M_date = UTCDateTime(input['max_date'])
        t_cont = M_date - m_date
        events = []
        if t_cont > input['interval']:
            num_div = int(t_cont/input['interval'])
            t_res = t_cont - num_div*input['interval']
            for i in range(0, num_div):
                events.append({'author': 'NAN', 'event_id': 'continuous' + str(i), \
                            'origin_id': -12345.0, 'longitude': -12345.0, \
                            'datetime': m_date + i*input['interval'], \
                            't1': m_date + i*input['interval'],\
                            't2': m_date + (i+1)*input['interval'] + 60.0,\
                            'depth': -12345.0, 'magnitude': -12345.0, \
                            'magnitude_type': 'NAN', 'latitude': -12345.0, \
                            'flynn_region': 'NAN'})
            events.append({'author': 'NAN', 'event_id': 'continuous' + str(i+1), \
                            'origin_id': -12345.0, 'longitude': -12345.0, \
                            'datetime': m_date + (i+1)*input['interval'], \
                            't1': m_date + (i+1)*input['interval'],\
                            't2': M_date,\
                            'depth': -12345.0, 'magnitude': -12345.0, \
                            'magnitude_type': 'NAN', 'latitude': -12345.0, \
                            'flynn_region': 'NAN'})
        else:
            events.append({'author': 'NAN', 'event_id': 'continuous0', \
                            'origin_id': -12345.0, 'longitude': -12345.0, \
                            'datetime': m_date, \
                            't1': m_date,\
                            't2': M_date,\
                            'depth': -12345.0, 'magnitude': -12345.0, \
                            'magnitude_type': 'NAN', 'latitude': -12345.0, \
                            'flynn_region': 'NAN'})
        print 'DONE'
    return events

###################### input_logger ###################################

def input_logger(argus, address, inputs):
    """
    log the entered command line!
    """
    st_argus = 'Command line:\n-------------\n' 
    for item in argus:
        st_argus += item + ' '
    st_argus += '\n\ninputs:\n-------\n'
    items = []
    for item in inputs:
        items.append(item)
    items.sort()
    for item in items:
        st_argus += str(item) + ': ' + str(inputs[item]) + '\n'
    logger_open = open(address, 'w')
    logger_open.write(st_argus)
    logger_open.close()

###################### seismicity ######################################

def seismicity():
    """
    Create a seismicity map
    """
    global input, events
    print '\n##############'
    print 'Seismicity map'
    print '##############\n'
    if input['evlatmin'] == None:
        input['evlatmin']=-90;input['evlatmax']=+90
        input['evlonmin']=-180;input['evlonmax']=+180
    m = Basemap(projection='cyl',llcrnrlat=input['evlatmin'],\
        urcrnrlat=input['evlatmax'], llcrnrlon=input['evlonmin'],\
        urcrnrlon=input['evlonmax'],resolution='l')
    m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90.,120.,30.))
    m.drawmeridians(np.arange(0.,420.,60.))
    m.drawmapboundary()
    
    # Defining Labels:
    x_ev, y_ev = m(-360, 0)
    m.scatter(x_ev, y_ev, 20, color='red', marker="o", \
                edgecolor="black", zorder=10, label = '0-70km')
    m.scatter(x_ev, y_ev, 20, color='green', marker="o", \
                edgecolor="black", zorder=10, label = '70-300km')
    m.scatter(x_ev, y_ev, 20, color='blue', marker="o", \
                edgecolor="black", zorder=10, label = '300< km')
    
    m.scatter(x_ev, y_ev, 5, color='white', marker="o", \
                edgecolor="black", zorder=10, label = '<=4.0')
    m.scatter(x_ev, y_ev, 20, color='white', marker="o", \
                edgecolor="black", zorder=10, label = '4.0-5.0')
    m.scatter(x_ev, y_ev, 35, color='white', marker="o", \
                edgecolor="black", zorder=10, label = '5.0-6.0')
    m.scatter(x_ev, y_ev, 50, color='white', marker="o", \
                edgecolor="black", zorder=10, label = '6.0<')
    
    for i in range(0, len(events)):
        x_ev, y_ev = m(float(events[i]['longitude']), float(events[i]['latitude']))
        if abs(float(events[i]['depth'])) <= 70.0:
            color = 'red'
        elif 70.0 < abs(float(events[i]['depth'])) <= 300.0:
            color = 'green'
        elif 300.0 < abs(float(events[i]['depth'])) <= 1000.0:
            color = 'blue'
        
        if float(events[i]['magnitude']) <= 4.0:
            size = 5
        elif 4.0 < float(events[i]['magnitude']) <= 5.0:
            size = 20
        elif 5.0 < float(events[i]['magnitude']) <= 6.0:
            size = 35
        elif 6.0 < float(events[i]['magnitude']):
            size = 50
        
        m.scatter(x_ev, y_ev, size,\
                color=color, marker="o", \
                edgecolor="black", zorder=10)
    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
    plt.show()

###################### IRIS_network ####################################

def IRIS_network(input):
    """
    Returns information about what time series data is available 
    at the IRIS DMC for all requested events
    """
    global events
    len_events = len(events)
    Period = input['min_date'].split('T')[0] + '_' + \
                input['max_date'].split('T')[0] + '_' + \
                str(input['min_mag']) + '_' + str(input['max_mag'])
    eventpath = os.path.join(input['datapath'], Period)
    print 'Create folders...',
    create_folders_files(events, eventpath)
    print 'DONE'
    for i in range(0, len_events):
        t_iris_1 = datetime.now()
        target_path = os.path.join(eventpath, events[i]['event_id'])
        Stas_iris = IRIS_available(input, events[i], target_path, event_number = i)
        if input['iris_bulk'] != 'Y':
            print '\nIRIS-Availability for event: ' + str(i+1) + str('/') + \
                                    str(len_events) + '  ---> ' + 'DONE'
        else:
            print '\nIRIS-bulkfile for event: ' + str(i+1) + str('/') + \
                                    str(len_events) + '  ---> ' + 'DONE'
        t_iris_2 = datetime.now()
        t_iris = t_iris_2 - t_iris_1
        print 'Time for checking the availability: ' + str(t_iris)
        if Stas_iris:
            IRIS_waveform(input, Stas_iris, i, type = 'save')
        else:
            'No available station in IRIS for your request!'
            continue

###################### IRIS_available ##################################

def IRIS_available(input, event, target_path, event_number):
    """
    Check the availablity of the IRIS stations
    """
    client_iris = Client_iris()
    Sta_iris = []
    try:       
        available = client_iris.availability(network=input['net'], \
            station=input['sta'], location=input['loc'], \
            channel=input['cha'], \
            starttime=UTCDateTime(event['t1']), \
            endtime=UTCDateTime(event['t2']), \
            lat=input['lat_cba'], \
            lon=input['lon_cba'], minradius=input['mr_cba'], \
            maxradius=input['Mr_cba'], minlat=input['mlat_rbb'], \
            maxlat=input['Mlat_rbb'], minlon=input['mlon_rbb'], \
            maxlon=input['Mlon_rbb'], output='xml')
        Sta_iris = XML_list_avail(xmlfile = available)
        if input['iris_bulk'] == 'Y':
            if os.path.exists(os.path.join(target_path,\
                                    'info', 'bulkdata.txt')):
                print 'bulkdata.txt exists in the directory!'
            else:
                available_bulk = client_iris.availability(network=input['net'], \
                            station=input['sta'], location=input['loc'], \
                            channel=input['cha'], \
                            starttime=UTCDateTime(event['t1']), \
                            endtime=UTCDateTime(event['t2']), \
                            lat=input['lat_cba'], \
                            lon=input['lon_cba'], minradius=input['mr_cba'], \
                            maxradius=input['Mr_cba'], minlat=input['mlat_rbb'], \
                            maxlat=input['Mlat_rbb'], minlon=input['mlon_rbb'], \
                            maxlon=input['Mlon_rbb'], \
                            filename = os.path.join(target_path,\
                                        'info', 'bulkdata.txt'), 
                            output='bulk')
    except Exception, e:
        Exception_file = open(os.path.join(target_path, \
            'info', 'exception'), 'a+')
        ee = 'iris -- Event:' + str(event_number) + '---' + str(e) + '\n'
        Exception_file.writelines(ee)
        Exception_file.close()
        print e
    if len(Sta_iris) == 0:
        Sta_iris.append([])
    return Sta_iris
    
###################### IRIS_waveform ###############################

def IRIS_waveform(input, Sta_req, i, type):
    """
    Gets Waveforms, Response files and meta-data 
    from IRIS DMC based on the requested events...
    """
    t_wave_1 = datetime.now()
    global events
    client_iris = Client_iris()
    add_event = []
    if type == 'save':
        Period = input['min_date'].split('T')[0] + '_' + \
                    input['max_date'].split('T')[0] + '_' + \
                    str(input['min_mag']) + '_' + str(input['max_mag'])
        eventpath = os.path.join(input['datapath'], Period)
        for k in range(0, len(events)):
            add_event.append(os.path.join(eventpath, \
                                        events[k]['event_id'])) 
    elif type == 'update':
        events, add_event = quake_info(input['iris_update'], target = 'info')
    len_events = len(events)
    if input['test'] == 'Y':
        len_req_iris = input['test_num']
    else:   
        len_req_iris = len(Sta_req)

    if input['iris_bulk'] == 'Y':
        t11 = datetime.now()
        bulk_file = os.path.join(add_event[i], 'info', 'bulkdata.txt')
        if input['req_parallel'] == 'Y':
            num_lines=1000; bulk_enum=0; bulk_num_files=1
            bulkfile_new=open(os.path.join(add_event[i], 'info', 'bulk_split_0.txt'), 'wb')
            for line in fileinput.FileInput(os.path.join(add_event[i], 'info', 'bulkdata.txt')):
                bulkfile_new.write(line)
                bulk_enum+=1
                if bulk_enum%num_lines==0:
                    bulkfile_new.close()
                    bulk_num_files+=1
                    bulkfile_new=open(os.path.join(add_event[i], 'info', \
                                       "bulk_split_%d.txt"%(bulk_enum/num_lines)), 'wb')
            bulkfile_new.close()
            
            print '\nbulkdataselect request is sent for event ' + \
                                    str(i+1) + '/' + str(len_events)
            parallel_results = pprocess.Map(limit=2, reuse=1)
            parallel_job = parallel_results.manage(pprocess.MakeReusable(bulk_download_core))
            for bulk_num in range(0, bulk_num_files):
                parallel_job(os.path.join(add_event[i], 'info', \
                        "bulk_split_%d.txt"%(bulk_num)), add_event[i])
            parallel_results.finish()
            if input['response'] == 'N':
                input['req_parallel'] = 'N'
                bulk_parallel_tmp_flag = True
                   
        else:
            print '\nbulkdataselect request is sent for event: ' + \
                                    str(i+1) + '/' + str(len_events)
            bulk_st = client_iris.bulkdataselect(bulk_file)
            print 'Saving the retrieved waveforms...',
            for m in range(0, len(bulk_st)):
                bulk_st_info = bulk_st[m].stats
                bulk_st[m].write(os.path.join(add_event[i], 'BH_RAW', \
                    bulk_st_info['network'] + '.' + \
                    bulk_st_info['station'] + '.' + \
                    bulk_st_info['location'] + '.' + \
                    bulk_st_info['channel']), 'MSEED')
            print 'DONE'
        input['waveform'] = 'N'
        t22 = datetime.now()
        print '\nbulkdataselect request is done for event: %s/%s in %s' \
                                    %(i+1, len_events, t22-t11)
    
    dic = {}                
    print '\nIRIS-Event: %s/%s' %(i+1, len_events)
    if input['req_parallel'] == 'Y':
        print "Parallel request with %s processes.\n" %(input['req_np'])
        parallel_results = pprocess.Map(limit=input['req_np'], reuse=1)
        parallel_job = parallel_results.manage(pprocess.MakeReusable(IRIS_download_core))
        for j in range(0, len_req_iris):
            parallel_job(i = i, j = j, dic = dic, type = type, \
                            len_events = len_events, \
                            events = events, add_event = add_event, \
                            Sta_req = Sta_req, input = input)
        parallel_results.finish()
    else:
        for j in range(0, len_req_iris):
            IRIS_download_core(i = i, j = j, dic = dic, type = type, \
                                len_events = len_events, \
                                events = events, add_event = add_event, \
                                Sta_req = Sta_req, input = input)
    try:
        if bulk_parallel_tmp_flag:
            input['req_parallel'] = 'Y'
    except:
        pass
   
    if input['iris_bulk'] == 'Y':
        input['waveform'] = 'Y'
        sta_saved_path = glob.glob(os.path.join(add_event[i], 'BH_RAW', '*.*.*.*'))
        print '\nAdjusting the station_event file...',
        sta_saved_list = []
        sta_ev_new = []
        for sta_num in range(0, len(sta_saved_path)):
            sta_saved_list.append(sta_saved_path[sta_num].split('/')[-1])
        for line in fileinput.FileInput(os.path.join(add_event[i], 'info', 'station_event')):
            if not line.split(',')[0]+'.'+line.split(',')[1]+'.'+line.split(',')[2]+'.'+line.split(',')[3] in \
                        sta_saved_list:
                pass
            else:
                sta_ev_new.append(line)
        file_staev_open = open(os.path.join(add_event[i], 'info', 'station_event'), 'w')
        file_staev_open.writelines(sta_ev_new)
        file_staev_open.close()
        print 'DONE'
    if input['SAC'] == 'Y':
        print '\nConverting the MSEED files to SAC...',
        writesac_all(i = i, events = events, address_events = add_event)
        print 'DONE'
   
    #len_sta_ev_open=open(os.path.join(add_event[i], 'info', 'station_event'), 'r')
    #len_sta_ev=len(len_sta_ev_open.readlines())
    len_sta_ev=[]
    Report = open(os.path.join(add_event[i], 'info', 'report_st'), 'a')
    eventsID = events[i]['event_id']
    Report.writelines('<><><><><><><><><><><><><><><><><>' + '\n')
    Report.writelines(eventsID + '\n')
    Report.writelines('---------------IRIS---------------' + '\n')
    Report.writelines('---------------' + input['cha'] + '---------------' + '\n')
    rep = 'IRIS-Available stations for channel ' + input['cha'] + \
            ' and for event' + '-' + str(i) + ': ' + str(len(Sta_req)) + '\n'
    Report.writelines(rep)
    rep = 'IRIS-' + type + ' stations for channel ' + input['cha'] + \
            ' and for event' + '-' + str(i) + ':     ' + str(len_sta_ev) + '\n'
    Report.writelines(rep)
    Report.writelines('----------------------------------' + '\n')
        
    t_wave_2 = datetime.now()
    t_wave = t_wave_2 - t_wave_1
        
    rep = "Time for " + type + "ing Waveforms from IRIS: " + str(t_wave) + '\n'
    Report.writelines(rep)
    Report.writelines('----------------------------------' + '\n')
    Report.close()
    
    if input['req_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(add_event[i], \
                                    'info', 'report_parallel'), 'a')
        report_parallel_open.writelines(\
            '---------------IRIS---------------' + '\n')
        report_parallel_open.writelines(\
            'Request' + '\n')
        if input['iris_bulk'] == 'Y':
            report_parallel_open.writelines(\
                'Number of Nodes: 2' + '\n')
        else:
            report_parallel_open.writelines(\
                'Number of Nodes: ' + str(input['req_np']) + '\n')

        size = getFolderSize(os.path.join(add_event[i])) 
        ti = str(t_wave.seconds) + ',' + str(t_wave.microseconds) \
                + ',' + str(size/(1024.**2)) + ',+,\n'
                
        report_parallel_open.writelines(\
            'Total Time     : ' + str(t_wave) + '\n')
        report_parallel_open.writelines(ti)
        report_parallel_open.close()
        
    print "\n------------------------"
    print 'IRIS for event-' + str(i+1) + ' is Done'
    print 'Total Time: %s' %(t_wave)
    print "------------------------"

###################### bulk_download_core ##################################

def bulk_download_core(bulk_file, add_event):
    
    client_iris = Client_iris()
    print "Send bulkdatarequest for: %s" %(bulk_file)
    bulk_st=client_iris.bulkdataselect(bulk_file)
    print "* bulkdataselect request for %s ... DONE" %(bulk_file.split('/')[-1])
    print '* Saving the retrieved waveforms of '+bulk_file.split('/')[-1]+'...',
    for m in range(0, len(bulk_st)):
        bulk_st_info = bulk_st[m].stats
        bulk_st[m].write(os.path.join(add_event,
            'BH_RAW', bulk_st_info['network'] + '.' +
            bulk_st_info['station'] + '.' +
            bulk_st_info['location'] + '.' +
            bulk_st_info['channel']), 'MSEED')
    print 'DONE'

###################### IRIS_download_core ##################################

def IRIS_download_core(i, j, dic, type, len_events, events, add_event, Sta_req, input):
    
    try:
        dummy = 'Initializing'
        client_iris = Client_iris()
        t11 = datetime.now()
        if Sta_req[j][2] == '--' or Sta_req[j][2] == '  ':
                Sta_req[j][2] = ''
        info_req = '['+str(i+1)+'/'+str(len_events)+'-'+\
                    str(j+1)+'/'+str(len(Sta_req))+'-'+input['cha']+'] ' 

        if input['waveform'] == 'Y':                    
            dummy = 'Waveform'
            client_iris.saveWaveform(os.path.join(add_event[i], 'BH_RAW', \
                Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3]), \
                Sta_req[j][0], Sta_req[j][1], \
                Sta_req[j][2], Sta_req[j][3], \
                events[i]['t1'], events[i]['t2'])
            print str(info_req) + "Saving Waveform for: " + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"  
        
        if input['response'] == 'Y':
            dummy = 'Response'
            client_iris.saveResponse(os.path.join(add_event[i], \
                'Resp', 'RESP' + '.' + \
                Sta_req[j][0] +  '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3]), \
                Sta_req[j][0], Sta_req[j][1], \
                Sta_req[j][2], Sta_req[j][3], \
                events[i]['t1'], events[i]['t2'])
            print str(info_req) + "Saving Response for: " + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"   
        
        if input['paz'] == 'Y':                    
            dummy = 'PAZ'
            client_iris.sacpz(Sta_req[j][0], Sta_req[j][1], \
                Sta_req[j][2], Sta_req[j][3], \
                events[i]['t1'], events[i]['t2'], \
                filename = os.path.join(add_event[i], 'Resp', \
                'PAZ' + '.' + Sta_req[j][0] + '.' + \
                Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + \
                Sta_req[j][3] + '.' + 'full'))
            print str(info_req) + "Saving PAZ for     : " + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"
        
        dummy = 'Meta-data'
        dic[j] ={'info': Sta_req[j][0] + '.' + Sta_req[j][1] + \
            '.' + Sta_req[j][2] + '.' + Sta_req[j][3], \
            'net': Sta_req[j][0], 'sta': Sta_req[j][1], \
            'latitude': Sta_req[j][4], 'longitude': Sta_req[j][5], \
            'loc': Sta_req[j][2], 'cha': Sta_req[j][3], \
            'elevation': Sta_req[j][6], 'depth': 0}
        Syn_file = open(os.path.join(add_event[i], 'info', \
                                'station_event'), 'a')
        syn = dic[j]['net'] + ',' + dic[j]['sta'] + ',' + \
                dic[j]['loc'] + ',' + dic[j]['cha'] + ',' + \
                dic[j]['latitude'] + ',' + dic[j]['longitude'] + \
                ',' + dic[j]['elevation'] + ',' + '0' + ',' + \
                events[i]['event_id'] + ',' + str(events[i]['latitude']) \
                + ',' + str(events[i]['longitude']) + ',' + \
                str(events[i]['depth']) + ',' + \
                str(events[i]['magnitude']) + ',' + 'iris' + ',' + '\n'
        Syn_file.writelines(syn)
        Syn_file.close()
        '''
        if input['SAC'] == 'Y':
            writesac(address_st = os.path.join(add_event[i], 'BH_RAW', \
                Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3]), \
                sta_info = dic[j], ev_info = events[i])
        '''
        print str(info_req) + "Saving Metadata for: " + Sta_req[j][0] + \
            '.' + Sta_req[j][1] + '.' + \
            Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"
        
        t22 = datetime.now()
        if input['time_iris'] == 'Y':
            time_iris = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info', \
                'time_iris'), 'a')
            size = getFolderSize(os.path.join(add_event[i])) 
            print size/(1024.**2)
            ti = Sta_req[j][0] + ',' + Sta_req[j][1] + ',' + \
                Sta_req[j][2] + ',' + Sta_req[j][3] + ',' + \
                str(time_iris.seconds) + ',' + str(time_iris.microseconds) \
                + ',' + str(size/(1024.**2)) + ',+,\n'
            time_file.writelines(ti)
            time_file.close()
    except Exception, e:    
        t22 = datetime.now()
        if input['time_iris'] == 'Y':
            time_iris = t22 - t11
            time_file = open(os.path.join(add_event[i], \
                            'info', 'time_iris'), 'a')
            size = getFolderSize(os.path.join(add_event[i])) 
            print size/(1024.**2)
            ti = Sta_req[j][0] + ',' + Sta_req[j][1] + ',' + \
                Sta_req[j][2] + ',' + Sta_req[j][3] + ',' + \
                str(time_iris.seconds) + ',' + \
                str(time_iris.microseconds) + ',' + \
                str(size/(1024.**2)) + ',-,\n'
            time_file.writelines(ti)
            time_file.close()
        
        if len(Sta_req[j]) != 0: 
            print str(info_req) + dummy + '---' + Sta_req[j][0] + '.' + Sta_req[j][1] + \
                            '.' +Sta_req[j][2] + '.' + Sta_req[j][3]
            ee = 'iris -- ' + dummy + '---' + str(i) + '-' + str(j) + '---' + \
                    Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                    Sta_req[j][2] + '.' + Sta_req[j][3] + \
                    '---' + str(e) + '\n'
        elif len(Sta_req[j]) == 0:
            ee = 'There is no available station for this event.'
        Exception_file = open(os.path.join(add_event[i], \
                        'info', 'exception'), 'a')
        Exception_file.writelines(ee)
        Exception_file.close()
        print e

###################### Arclink_network #################################

def ARC_network(input):
    
    """
    Returns information about what time series data is available 
    at the ArcLink nodes for all requested events
    """
    
    global events
    
    len_events = len(events)
    Period = input['min_date'].split('T')[0] + '_' + \
                input['max_date'].split('T')[0] + '_' + \
                str(input['min_mag']) + '_' + str(input['max_mag'])
    eventpath = os.path.join(input['datapath'], Period)
    
    if input['IRIS'] != 'Y':
        print 'Create folders...',
        create_folders_files(events, eventpath)
        print 'DONE'
    for i in range(0, len_events):
        t_arc_1 = datetime.now()
        Stas_arc = ARC_available(input, events[i], eventpath, event_number = i)
        print '\nArcLink-Availability for event: ' + str(i+1) + str('/') + \
                                    str(len_events) + '  --->' + 'DONE'
        t_arc_2 = datetime.now()
        t_arc_21 = t_arc_2 - t_arc_1
        print 'Time for checking the availability: ' + str(t_arc_21)
        
        if Stas_arc:
            ARC_waveform(input, Stas_arc, i, type = 'save')
        else:
            'No available station in ArcLink for your request!'

###################### ARC_available ###################################

def ARC_available(input, event, target_path, event_number):
    
    """
    Check the availablity of the ArcLink stations
    """
    
    client_arclink = Client_arclink()
    Sta_arc = []
    try:
        inventories = client_arclink.getInventory(network=input['net'], \
            station=input['sta'], location=input['loc'], \
            channel=input['cha'], \
            starttime=UTCDateTime(event['datetime'])-10, \
            endtime=UTCDateTime(event['datetime'])+10, \
            instruments=False, route=True, sensortype='', \
            min_latitude=None, max_latitude=None, \
            min_longitude=None, max_longitude=None, \
            restricted=False, permanent=None, modified_after=None)
        for j in inventories.keys():
            netsta = j.split('.') 
            if len(netsta) == 4:
                sta = netsta[0] + '.' + netsta[1]
                if inventories[sta]['depth'] == None:
                    inventories[sta]['depth'] = 0.0
                if input['mlat_rbb']==None:
                    mlatrbb=-90.0;Mlatrbb=+90.0 
                    mlonrbb=-180.0;Mlonrbb=+180.0
                else:
                    mlatrbb=input['mlat_rbb']
                    Mlatrbb=input['Mlat_rbb']
                    mlonrbb=input['mlon_rbb'] 
                    Mlonrbb=input['Mlon_rbb'] 
                if mlatrbb <= inventories[sta]['latitude'] <= Mlatrbb and \
                    mlonrbb <= inventories[sta]['longitude'] <= Mlonrbb:
                    Sta_arc.append([netsta[0], netsta[1], netsta[2], netsta[3],\
                            inventories[sta]['latitude'], inventories[sta]['longitude'],\
                            inventories[sta]['elevation'], inventories[sta]['depth']])
                
        if len(Sta_arc) == 0:
            Sta_arc.append([])
        Sta_arc.sort()
    except Exception, e:
        Exception_file = open(os.path.join(target_path, \
            'info', 'exception'), 'a+')
        ee = 'arclink -- Event:' + str(event_number) + '---' + str(e) + '\n'
        Exception_file.writelines(ee)
        Exception_file.close()
        print e
    
    return Sta_arc

###################### Arclink_waveform ############################

def ARC_waveform(input, Sta_req, i, type):
    """
    Gets Waveforms, Response files and meta-data 
    from ArcLink based on the requested events...
    """
    t_wave_1 = datetime.now()
    global events
    client_arclink = Client_arclink()
    client_neries = Client_neries(user='test@obspy.org')
    add_event = []
    if type == 'save':
        Period = input['min_date'].split('T')[0] + '_' + \
                    input['max_date'].split('T')[0] + '_' + \
                    str(input['min_mag']) + '_' + str(input['max_mag'])
        eventpath = os.path.join(input['datapath'], Period)
        for k in range(0, len(events)):
            add_event.append(os.path.join(eventpath, \
                                        events[k]['event_id']))  
    elif type == 'update':
        events, add_event = quake_info(input['arc_update'], target = 'info')
    len_events = len(events)
    if input['test'] == 'Y':
        len_req_arc = input['test_num']
    else:    
        len_req_arc = len(Sta_req)       
    dic = {}
    print '\nArcLink-Event: %s/%s' %(i+1, len_events)
    if input['req_parallel'] == 'Y':
        print "Parallel request with %s processes.\n" %(input['req_np'])
        parallel_results = pprocess.Map(limit=input['req_np'], reuse=1)
        parallel_job = \
            parallel_results.manage(pprocess.MakeReusable(ARC_download_core))
        for j in range(0, len_req_arc):
            parallel_job(i = i, j = j, dic = dic, type = type, \
                            len_events = len_events, \
                            events = events, add_event = add_event, \
                            Sta_req = Sta_req, input = input)
        parallel_results.finish()
    else:
        for j in range(0, len_req_arc):
            ARC_download_core(i = i, j = j, dic = dic, type = type, \
                            len_events = len_events, \
                            events = events, add_event = add_event, \
                            Sta_req = Sta_req, input = input)
    if input['SAC'] == 'Y':
        print '\nConverting the MSEED files to SAC...',
        writesac_all(i = i, events = events, address_events = add_event)
        print 'DONE'
    Report = open(os.path.join(add_event[i], 'info', 'report_st'), 'a')
    eventsID = events[i]['event_id']
    Report.writelines('<><><><><><><><><><><><><><><><><>' + '\n')
    Report.writelines(eventsID + '\n')
    Report.writelines('---------------ARC---------------' + '\n')
    Report.writelines('---------------' + input['cha'] + '---------------' + '\n')
    rep = 'ARC-Available stations for channel ' + input['cha'] + \
                ' and for event' + '-' + str(i) + ': ' + str(len(Sta_req)) + '\n'
    Report.writelines(rep)
    rep = 'ARC-' + type + ' stations for channel ' + \
            input['cha'] + ' and for event' + '-' + \
            str(i) + ':     ' + str(len(dic)) + '\n'
    Report.writelines(rep)
    Report.writelines('----------------------------------' + '\n')
    t_wave_2 = datetime.now()
    t_wave = t_wave_2 - t_wave_1
    rep = "Time for " + type + "ing Waveforms from ArcLink: " + str(t_wave) + '\n'
    Report.writelines(rep)
    Report.writelines('----------------------------------' + '\n')
    Report.close()
    if input['req_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(add_event[i], \
                                    'info', 'report_parallel'), 'a')
        report_parallel_open.writelines(\
            '---------------ARC---------------' + '\n')
        report_parallel_open.writelines(\
            'Request' + '\n')
        report_parallel_open.writelines(\
            'Number of Nodes: ' + str(input['req_np']) + '\n')
        size = getFolderSize(os.path.join(add_event[i])) 
        ti = str(t_wave.seconds) + ',' + str(t_wave.microseconds) \
                + ',' + str(size/(1024.**2)) + ',+,\n'
        report_parallel_open.writelines(\
            'Total Time     : ' + str(t_wave) + '\n')
        report_parallel_open.writelines(ti)
        report_parallel_open.close()
    
    print "\n------------------------"
    print 'ArcLink for event-' + str(i+1) + ' is Done'
    print 'Total Time: %s' %(t_wave)
    print "------------------------"

###################### ARC_download_core ###############################

def ARC_download_core(i, j, dic, type, len_events, events, add_event, Sta_req, input):
 
    try:
        dummy = 'Initializing'
        client_arclink = Client_arclink()
        t11 = datetime.now()
        info_req = '['+str(i+1)+'/'+str(len_events)+'-'+\
                    str(j+1)+'/'+str(len(Sta_req))+'-'+input['cha']+'] ' 
        if input['waveform'] == 'Y':
            dummy = 'Waveform'
            try:
                client_arclink.saveWaveform(os.path.join(add_event[i], \
                    'BH_RAW', \
                    Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                    Sta_req[j][2] + '.' + Sta_req[j][3]), \
                    Sta_req[j][0], Sta_req[j][1], \
                    Sta_req[j][2], Sta_req[j][3], \
                    events[i]['t1'], events[i]['t2'])
            except Exception, e: 
                print e
                if input['NERIES'] == 'Y':
                    print "\nWaveform is not available in ArcLink, trying NERIES!\n"
                    client_neries.saveWaveform(os.path.join(add_event[i], \
                        'BH_RAW', \
                        Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                        Sta_req[j][2] + '.' + Sta_req[j][3]), \
                        Sta_req[j][0], Sta_req[j][1], \
                        Sta_req[j][2], Sta_req[j][3], \
                        events[i]['t1'], events[i]['t2'])
            check_file = open(os.path.join(add_event[i], 'BH_RAW', \
                Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3]))
            check_file.close()
            print str(info_req) + "Saving Waveform for: " + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"  
        
        if input['response'] == 'Y':
            dummy = 'Response'
            client_arclink.saveResponse(os.path.join(add_event[i], \
                'Resp', 'RESP' + \
                '.' + Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3]), \
                Sta_req[j][0], Sta_req[j][1], \
                Sta_req[j][2], Sta_req[j][3], \
                events[i]['t1'], events[i]['t2'])
            sp = Parser(os.path.join(add_event[i], \
                'Resp', 'RESP' + '.' + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3]))
            sp.writeRESP(os.path.join(add_event[i], 'Resp'))
            print str(info_req) + "Saving Response for: " + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"
        
        if input['paz'] == 'Y':                    
            dummy = 'PAZ'
            paz_arc = client_arclink.getPAZ(\
                Sta_req[j][0], Sta_req[j][1], \
                Sta_req[j][2], Sta_req[j][3], \
                time = events[i]['t1'])
            paz_file = open(\
                os.path.join(add_event[i], 'Resp', 'PAZ' + '.' + \
                Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + \
                Sta_req[j][3] + '.' + 'paz'), 'w')
            pickle.dump(paz_arc, paz_file)
            paz_file.close()
            print str(info_req) + "Saving PAZ for     : " + Sta_req[j][0] + \
                '.' + Sta_req[j][1] + '.' + \
                Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"
        
        dummy = 'Meta-data'
        dic[j] ={'info': Sta_req[j][0] + '.' + Sta_req[j][1] + \
            '.' + Sta_req[j][2] + '.' + Sta_req[j][3], \
            'net': Sta_req[j][0], 'sta': Sta_req[j][1], \
            'latitude': Sta_req[j][4], 'longitude': Sta_req[j][5], \
            'loc': Sta_req[j][2], 'cha': Sta_req[j][3], \
            'elevation': Sta_req[j][6], 'depth': Sta_req[j][7]}
        Syn_file = open(os.path.join(add_event[i], \
                            'info', 'station_event'), 'a')
        syn = Sta_req[j][0] + ',' + Sta_req[j][1] + ',' + \
            Sta_req[j][2] + ',' + Sta_req[j][3] + ',' + \
            str(Sta_req[j][4]) + ',' + str(Sta_req[j][5]) + \
            ',' + str(Sta_req[j][6]) + ',' + \
            str(Sta_req[j][7]) + ',' + events[i]['event_id'] + \
            ',' + str(events[i]['latitude']) \
             + ',' + str(events[i]['longitude']) + ',' + \
             str(events[i]['depth']) + ',' + \
             str(events[i]['magnitude']) + ',' + 'arc' + ',' + '\n'
        Syn_file.writelines(syn)
        Syn_file.close()
        '''
        if input['SAC'] == 'Y':
            writesac(address_st = os.path.join(add_event[i], 'BH_RAW', \
                    Sta_req[j][0] +  '.' + Sta_req[j][1] + \
                    '.' + Sta_req[j][2] + '.' + Sta_req[j][3]), \
                    sta_info = dic[j], ev_info = events[i])
        '''
        print str(info_req) + "Saving Station  for: " + Sta_req[j][0] + '.' + \
            Sta_req[j][1] + '.' + \
            Sta_req[j][2] + '.' + Sta_req[j][3] + "  ---> DONE"
        t22 = datetime.now()
        if input['time_arc'] == 'Y':
            time_arc = t22 - t11
            time_file = open(os.path.join(add_event[i], \
                            'info', 'time_arc'), 'a+')
            size = getFolderSize(os.path.join(add_event[i]))
            print size/(1024.**2)
            ti = Sta_req[j][0] + ',' + Sta_req[j][1] + ',' + \
                Sta_req[j][2] + ',' + Sta_req[j][3] + ',' + \
                str(time_arc.seconds) + ',' + \
                str(time_arc.microseconds) + ',' + \
                str(size/(1024.**2)) + ',+,\n'
            time_file.writelines(ti)
            time_file.close()
        
    except Exception, e:    
        t22 = datetime.now()
        if input['time_arc'] == 'Y':
            time_arc = t22 - t11
            time_file = open(os.path.join(add_event[i], \
                            'info', 'time_arc'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            print size/(1024.**2)
            ti = Sta_req[j][0] + ',' + Sta_req[j][1] + ',' + \
                Sta_req[j][2] + ',' + Sta_req[j][3] + ',' + \
                str(time_arc.seconds) + ',' + \
                str(time_arc.microseconds) + ',' + \
                str(size/(1024.**2)) + ',-,\n'
            time_file.writelines(ti)
            time_file.close()
        
        if len(Sta_req[j]) != 0: 
            print str(info_req) + dummy + '---' + Sta_req[j][0] + '.' + Sta_req[j][1] + \
                            '.' +Sta_req[j][2] + '.' + Sta_req[j][3]
            ee = 'arclink -- ' + dummy + '---' + str(i) + '-' + str(j) + '---' + \
                        Sta_req[j][0] + '.' + Sta_req[j][1] + '.' + \
                        Sta_req[j][2] + '.' + Sta_req[j][3] + \
                        '---' + str(e) + '\n'
        elif len(Sta_req[j]) == 0:
            ee = 'There is no available station for this event.'
        Exception_file = open(os.path.join(add_event[i], \
                        'info', 'exception'), 'a')
        Exception_file.writelines(ee)
        Exception_file.close()
        print e

###################### IRIS_update #####################################
    
def IRIS_update(input, address):
    
    """
    Initialize folders and required stations for IRIS update requests
    """
    
    t_update_1 = datetime.now()
    client_iris = Client_iris()
    events, address_events = quake_info(address, 'info')
    len_events = len(events)
    for i in range(0, len_events):
        target_path = address_events
        Stas_iris = IRIS_available(input, events[i], target_path[i], event_number = i)
        if input['iris_bulk'] != 'Y':
            print '\nIRIS-Availability for event: ' + str(i+1) + str('/') + \
                                    str(len_events) + '  ---> ' + 'DONE'
        else:
            print 'IRIS-bulkfile for event    : ' + str(i+1) + str('/') + \
                                    str(len_events) + '  ---> ' + 'DONE'
        if Stas_iris != [[]]:
            Stas_req = rm_duplicate(Stas_iris, \
                            address = os.path.join(address_events[i]))
        else:
            Stas_req = [[]]
            print '------------------------------------------'
            print 'There is no available station!'
            print '------------------------------------------'
        if not os.path.isdir(os.path.join(address_events[i], 'BH_RAW')):
            os.makedirs(os.path.join(address_events[i], 'BH_RAW'))
        if Stas_req:
            IRIS_waveform(input, Stas_req, i, type = 'update')
        else:
            'No available station in IRIS for your request!'
            continue

###################### ARC_update ######################################
    
def ARC_update(input, address):
    
    """
    Initialize folders and required stations for ARC update requests
    """
    
    t_update_1 = datetime.now()
    client_arclink = Client_arclink()
    events, address_events = quake_info(address, 'info')
    len_events = len(events)
    for i in range(0, len_events):
        target_path = address_events
        Stas_arc = ARC_available(input, events[i], target_path[i], event_number = i)
        print '\nArcLink-Availability for event: ' + str(i+1) + str('/') + \
                                    str(len_events) + '  --->' + 'DONE'
        
        if Stas_arc != [[]]:
            Stas_req = rm_duplicate(Stas_arc, \
                            address = os.path.join(address_events[i]))
        else:
            Stas_req = [[]]
            print '------------------------------------------'
            print 'There is no available station!'
            print '------------------------------------------'
        if not os.path.isdir(os.path.join(address_events[i], 'BH_RAW')):
            os.makedirs(os.path.join(address_events[i], 'BH_RAW'))
        if Stas_req:
            ARC_waveform(input, Stas_req, i, type = 'update')
        else:
            'No available station in ArcLink for your request!'
            continue
    
###################### IRIS_ARC_IC #####################################

def IRIS_ARC_IC(input, clients):
    
    """
    Call "inst_correct" function based on the channel request.
    """
    
    if input[clients + '_ic_auto'] == 'Y':
        global events        
        Period = input['min_date'].split('T')[0] + '_' + \
                    input['max_date'].split('T')[0] + '_' + \
                    str(input['min_mag']) + '_' + str(input['max_mag'])
        eventpath = os.path.join(input['datapath'], Period)
        address = eventpath
    elif input[clients + '_ic'] != 'N':
        address = input[clients + '_ic']
    
    events, address_events = quake_info(address, 'info')

    for i in range(0, len(events)):
        sta_ev = read_station_event(address_events[i])
        ls_saved_stas_tmp = []
        ls_saved_stas = []
        
        for j in range(0, len(sta_ev[0])):
            if clients == sta_ev[0][j][13]:
                station_id = sta_ev[0][j][0] + '.' + sta_ev[0][j][1] + '.' + \
                             sta_ev[0][j][2] + '.' + sta_ev[0][j][3]
                ls_saved_stas_tmp.append(os.path.join(address_events[i], 'BH_RAW',\
                                        station_id))
        
        pattern_sta = input['net'] + '.' + input['sta'] + '.' + \
                        input['loc'] + '.' + input['cha']
        
        for k in range(0, len(ls_saved_stas_tmp)):
            if fnmatch.fnmatch(ls_saved_stas_tmp[k].split('/')[-1], pattern_sta):
                ls_saved_stas.append(ls_saved_stas_tmp[k])
        
        if len(ls_saved_stas) != 0:        
            print '\nevent: ' + str(i+1) + '/' + str(len(events)) + \
                                             ' -- ' + clients + '\n'
            inst_correct(input, ls_saved_stas, address_events[i], clients) 
        else:
            print "There is no station in the folder to correct!"

###################### inst_correct ###############################
    
def inst_correct(input, ls_saved_stas, address, clients):
    
    """
    Apply Instrument Coorection on all available stations in the folder
    This scrips uses 'seisSim' from obspy.signal for this reason
    
    Instrument Correction has three main steps:
        1) RTR: remove the trend
        2) tapering
        3) pre-filtering and deconvolution of Resp file from Raw counts
        
    Remove the instrument type by deconvolution using spectral division.
    """
    
    t_inst_1 = datetime.now()
    
    if input['corr_unit'] == 'DIS':
        BH_file = 'BH'
    else:
        BH_file = 'BH_' + input['corr_unit']
    
    try:
        os.makedirs(os.path.join(address, BH_file))
    except Exception, e:
        pass
    
    if input['ic_parallel'] == 'Y':
       
        print '\nParallel Instrument Correction with %s processes.\n' %(input['ic_np'])
        #!! Still do not know which one is the best: 
        #parallel_results = pprocess.Queue(limit=input['req_np'])
        #parallel_job = parallel_results.manage(pprocess.MakeParallel(IC_core))
        #parallel_results = pprocess.Map(limit=input['req_np'], continuous=1)
        #parallel_job = parallel_results.manage(pprocess.MakeParallel(IC_core))
        parallel_results = pprocess.Map(limit=input['ic_np'], reuse=1)
        parallel_job = parallel_results.manage(pprocess.MakeReusable(IC_core))
        for i in range(0, len(ls_saved_stas)):
            parallel_job(ls_saved_stas = ls_saved_stas[i], \
                    clients = clients, address = address, \
                    BH_file = BH_file, \
                    inform = clients + ' -- ' + \
                    str(i+1) + '/' + str(len(ls_saved_stas)))

        parallel_results.finish()
    else:
        for i in range(0, len(ls_saved_stas)):
            IC_core(ls_saved_stas = ls_saved_stas[i], \
                    clients = clients, address = address, \
                    BH_file = BH_file, \
                    inform = clients + ' -- ' + \
                    str(i+1) + '/' + str(len(ls_saved_stas)))
    
    # ---------Creating Tar files (Response files)
    if input['zip_w'] == 'Y':
        print '\nCompressing Raw files...',
        path = os.path.join(address, 'BH_RAW')
        tar_file = os.path.join(path, 'BH_RAW.tar')
        files = '*.*.*.*'
        compress_gzip(path = path, tar_file = tar_file, files = files)
        print 'DONE'
    # ---------Creating Tar files (Response files)
    if input['zip_r'] == 'Y':
        print '\nCompressing Resp files...',
        path = os.path.join(address, 'Resp')
        tar_file = os.path.join(path, 'Resp.tar')
        files = '*.*.*.*'
        compress_gzip(path = path, tar_file = tar_file, files = files)
        print 'DONE'
    
    t_inst_2 = datetime.now()
    if input['ic_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(address, \
                                    'info', 'report_parallel'), 'a')
        report_parallel_open.writelines(\
            '---------------' + clients.upper() + '---------------' + '\n')
        report_parallel_open.writelines(\
            'Instrument Correction' + '\n')
        report_parallel_open.writelines(\
            'Number of Nodes: ' + str(input['ic_np']) + '\n')
        report_parallel_open.writelines(\
            'Number of Stas : ' + str(len(ls_saved_stas)) + '\n')
        report_parallel_open.writelines(\
            'Total Time     : ' + str(t_inst_2 - t_inst_1) + '\n')
    print '\nTime for Instrument Correction of ' + \
            str(len(ls_saved_stas))+' stations: %s' %(t_inst_2-t_inst_1)

###################### IC_core #########################################

def IC_core(ls_saved_stas, clients, address, BH_file, inform):
    
    global input
    
    try:
        
        if input['ic_obspy_full'] == 'Y':
            # Removing the trend
            rt_c = RTR(stream = ls_saved_stas, degree = 2)
            tr = read(ls_saved_stas)[0]
            tr.data = rt_c
            
            # Tapering
            taper = invsim.cosTaper(len(tr.data))
            tr.data *= taper
            
            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
                                        ls_saved_stas.split('/')[-1])
            
            obspy_fullresp(trace = tr, resp_file = resp_file, \
                Address = os.path.join(address, BH_file), unit = input['corr_unit'], \
                BP_filter = input['pre_filt'], inform = inform)
        
        if input['ic_sac_full'] == 'Y':
            
            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
                                        ls_saved_stas.split('/')[-1])
        
            SAC_fullresp(trace = ls_saved_stas, resp_file = resp_file, \
                address = address, BH_file = BH_file, unit = input['corr_unit'], \
                BP_filter = input['pre_filt'], inform = inform)
        
        if input['ic_paz'] == 'Y':
            """
            paz_file = os.path.join(address, 'Resp', 'PAZ' + '.' + \
                                ls_saved_stas.split('/')[-1] + '.' + 'full')
            
            SAC_PAZ(trace = ls_saved_stas, paz_file = paz_file, \
                address = address, BH_file = BH_file, unit = input['corr_unit'], \
                BP_filter = input['pre_filt'], inform = inform)
            """
            """ 
            rt_c = RTR(stream = ls_saved_stas, degree = 2)
            tr = read(ls_saved_stas)[0]
            tr.data = rt_c
            
            # Tapering
            taper = invsim.cosTaper(len(tr.data))
            tr.data *= taper
            
            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
                                        ls_saved_stas.split('/')[-1])
        
            obspy_PAZ(trace = tr, resp_file = resp_file, \
                Address = os.path.join(address, BH_file), \
                clients = clients, unit = input['corr_unit'], \
                BP_filter = input['pre_filt'], inform = inform)
            """
            
            if clients == 'iris':
                paz_file = os.path.join(address, 'Resp', 'PAZ' + '.' + \
                                ls_saved_stas.split('/')[-1] + '.' + 'full')
 
                SAC_PAZ(trace = ls_saved_stas, paz_file = paz_file, \
                    address = address, BH_file = BH_file, unit = input['corr_unit'], \
                    BP_filter = input['pre_filt'], inform = inform)
            
            if clients == 'arc':
                rt_c = RTR(stream = ls_saved_stas, degree = 2)
                tr = read(ls_saved_stas)[0]
                tr.data = rt_c
                
                # Tapering
                taper = invsim.cosTaper(len(tr.data))
                tr.data *= taper
                
                resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
                                            ls_saved_stas.split('/')[-1])
            
                obspy_PAZ(trace = tr, resp_file = resp_file, \
                    Address = os.path.join(address, BH_file), \
                    clients = clients, unit = input['corr_unit'], \
                    BP_filter = input['pre_filt'], inform = inform)
            
                """
                rt_c = RTR(stream = ls_saved_stas, degree = 2)
                tr = read(ls_saved_stas)[0]
                tr.data = rt_c
                
                # Tapering
                taper = invsim.cosTaper(len(tr.data))
                tr.data *= taper
                
                paz_file_open = open(os.path.join(address, 'Resp', 'PAZ' + '.' + \
                                ls_saved_stas.split('/')[-1] + '.' + 'paz'))
                paz_file = pickle.load(paz_file_open)
                
                paz_dic = {\
                'poles': paz_file['poles'], \
                'zeros': paz_file['zeros'], \
                'gain': paz_file['gain']}
                
                obspy_PAZ(trace = tr, paz_dic = paz_dic, \
                    Address = os.path.join(address, BH_file), unit = input['corr_unit'], \
                    BP_filter = input['pre_filt'], inform = inform)
                """
            
    except Exception, e:
        print e

###################### RTR #############################################

def RTR(stream, degree = 2):
    
    """
    Remove the trend by Fitting a linear function to the trace 
    with least squares and subtracting it
    """
    
    raw_f = read(stream)

    t = []
    b0 = 0
    inc = []
    
    b = raw_f[0].stats['starttime']

    for i in range(0, raw_f[0].stats['npts']):
        inc.append(b0)
        b0 = b0+1.0/raw_f[0].stats['sampling_rate'] 
        b0 = round(b0, 4)
        
    A = np.vander(inc, degree)
    (coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, raw_f[0].data)
    
    f = np.poly1d(coeffs)
    y_est = f(inc)
    rt_c = raw_f[0].data-y_est
    
    return rt_c

###################### obspy_fullresp #######################################

def obspy_fullresp(trace, resp_file, Address, unit = 'DIS', \
            BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):

    date = trace.stats['starttime']
    seedresp = {'filename':resp_file,'date':date,'units':unit}
    
    try:
        
        trace.data = seisSim(data = trace.data, \
            samp_rate = trace.stats.sampling_rate,paz_remove=None, \
            paz_simulate = None, remove_sensitivity=True, \
            simulate_sensitivity = False, water_level = 600.0, \
            zero_mean = True, taper = False, pre_filt=eval(BP_filter), \
            seedresp=seedresp, pitsasim=False, sacsim = True)
        
        trace.data *= 1.e9
        trace_identity = trace.stats['station'] + '.' + \
                trace.stats['location'] + '.' + trace.stats['channel']
        trace.write(os.path.join(Address, unit.lower() + '.' + \
                                        trace_identity), format = 'SAC')
        
        if unit.lower() == 'dis':
            unit_print = 'displacement'
        if unit.lower() == 'vel':
            unit_print = 'velocity'
        if unit.lower() == 'acc':
            unit_print = 'acceleration'

        print inform + ' -- Instrument Correction to ' + unit_print + \
                                            ' for: ' + trace_identity 
        
    except Exception, e:
        print inform + ' -- ' + str(e)

###################### SAC_fullresp ####################################

def SAC_fullresp(trace, resp_file, address, BH_file = 'BH', unit = 'DIS', \
                    BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
    
    """
    This script runs SAC program for instrument correction
    Instrument Correction will be done for all waveforms in the BH_RAW folder
    Response files will be loaded from Resp folder

    Instrument Correction has three main steps:
    1) RTR: remove the trend
    2) tapering
    3) pre-filtering and deconvolution of Resp file from Raw counts
    """
    
    try:
        
        trace_info = trace.split('/')[-1].split('.')
        
        if unit.lower() == 'dis':
            unit_sac = 'NONE'
        if unit.lower() == 'vel':
            unit_sac = 'VEL'
        if unit.lower() == 'acc':
            unit_sac = 'ACC'
        
        BP_filter_tuple = eval(BP_filter)
        freqlim = str(BP_filter_tuple[0]) + ' ' +  str(BP_filter_tuple[1]) \
                    + ' ' + str(BP_filter_tuple[2]) + ' ' + \
                    str(BP_filter_tuple[3])
        
        pwd = commands.getoutput('pwd')
        os.chdir(os.path.join(address, BH_file))
        
        p = subprocess.Popen(['sac'],
                             stdout = subprocess.PIPE,
                             stdin  = subprocess.PIPE,
                             stderr = subprocess.STDOUT )
                             
        s = \
        'setbb resp ../Resp/' + resp_file.split('/')[-1] + '\n' + \
        'read ../BH_RAW/' + trace.split('/')[-1] + '\n' + \
        'rtrend' + '\n' + \
        'taper' + '\n' + \
        'rmean' + '\n' + \
        'trans from evalresp fname %resp to ' + unit_sac + ' freqlim ' + freqlim + '\n' + \
        'write ' + unit.lower() + '.' + trace_info[1] + '.' + trace_info[2] + \
                                            '.' + trace_info[3] + '\n' + \
        'quit\n'
        
        out = p.communicate(s)
        print out[0]
        os.chdir(pwd)
                            
        if unit.lower() == 'dis':
            unit_print = 'displacement'
        if unit.lower() == 'vel':
            unit_print = 'velocity'
        if unit.lower() == 'acc':
            unit_print = 'acceleration'

        print inform + ' -- Instrument Correction to ' + unit_print + \
                        ' for: ' + trace_info[0] + '.' + trace_info[1] + \
                        '.' + trace_info[2] + '.' + trace_info[3] 
        print "-----------------------------------"
                                            
    except Exception, e:
        print inform + ' -- ' + str(e)

###################### readRESP ########################################

def readRESP(resp_file, unit):

    resp_open = open(resp_file)
    resp_read = resp_open.readlines()
    
    check_resp = []
    
    for resp_line in resp_read:
        if "velocity in meters per second" in resp_line.lower() or \
            "velocity in meters/second" in resp_line.lower() or \
            "m/s -" in resp_line.lower():
            check_resp.append('M/S')
        
        elif "m/s**2 - acceleration" in resp_line.lower():
            check_resp.append('M/S**2')
    
    if check_resp == []:
        print '\n***************************************************************'
        print 'The response file is not in the right dimension (M/S) or (M/S**2)'
        print 'This could cause problems in the instrument correction.'
        print 'Please check the response file:'
        print resp_file
        print '*****************************************************************'
        sys.exit()
    
    gain_num = []
    A0_num = []
    poles_num = []
    poles = []
    zeros = []
    zeros_num = []
    #if clients == 'iris':
    if resp_read[0].find('obspy.xseed') == -1:
        for i in range(0, len(resp_read)):
            if resp_read[i].find('B058F04') != -1:  
                gain_num.append(i)
            if resp_read[i].find('B053F07') != -1:  
                A0_num.append(i)
            if resp_read[i].find('B053F10-13') != -1:  
                zeros_num.append(i)
            if resp_read[i].find('B053F15-18') != -1:  
                poles_num.append(i)
                
    #elif clients == 'arc':
    elif resp_read[0].find('obspy.xseed') != -1:
        for i in range(0, len(resp_read)):
            if resp_read[i].find('B058F04') != -1:  
                gain_num.append(i)
            if resp_read[i].find('B043F08') != -1:  
                A0_num.append(i)
            if resp_read[i].find('B043F11-14') != -1:  
                zeros_num.append(i)
            if resp_read[i].find('B043F16-19') != -1:  
                poles_num.append(i)
        
    list_sensitivity = resp_read[gain_num[-1]].split('\n')[0].split(' ')
    list_new_sensitivity = [x for x in list_sensitivity if x]
    sensitivity = eval(list_new_sensitivity[-1])
    
    list_A0 = resp_read[A0_num[0]].split('\n')[0].split(' ')
    list_new_A0 = [x for x in list_A0 if x]
    A0 = eval(list_new_A0[-1])

    
    for i in range(0, len(poles_num)):
        
        list_poles = resp_read[poles_num[i]].split('\n')[0].split(' ')
        list_new_poles = [x for x in list_poles if x]
        
        poles_r = eval(list_new_poles[-4])
        poles_i = eval(list_new_poles[-3])
        poles.append(complex(poles_r, poles_i))
    
    for i in range(0, len(zeros_num)):
        
        list_zeros = resp_read[zeros_num[i]].split('\n')[0].split(' ')
        list_new_zeros = [x for x in list_zeros if x]
        
        zeros_r = eval(list_new_zeros[-4])
        zeros_i = eval(list_new_zeros[-3])
        zeros.append(complex(zeros_r, zeros_i))
            
    if check_resp[0] == 'M/S':
        if unit.lower() == 'dis':
            zeros.append(0j)
        #if unit.lower() == 'vel':
        #    zeros = [0j, 0j]
        #if unit.lower() == 'acc':
        #    zeros = [0j]
    elif check_resp[0] == 'M/S**2':
        if unit.lower() == 'dis':
            zeros.append(0j)
            zeros.append(0j)
    
    paz = {\
    'poles': poles,
    'zeros': zeros,
    'gain': A0,
    'sensitivity': sensitivity\
    }
 
    return paz

###################### obspy_PAZ #######################################

def obspy_PAZ(trace, resp_file, Address, clients, unit = 'DIS', \
            BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
    
    try:
        
        paz = readRESP(resp_file, unit)
        
        trace.data = seisSim(data = trace.data, \
            samp_rate = trace.stats.sampling_rate,paz_remove=paz, \
            paz_simulate = None, remove_sensitivity=True, \
            simulate_sensitivity = False, water_level = 600.0, \
            zero_mean = True, taper = False, pre_filt=eval(BP_filter), \
            seedresp=None, pitsasim=False, sacsim = True)
        
        trace.data *= 1.e9
        
        trace_identity = trace.stats['station'] + '.' + \
                trace.stats['location'] + '.' + trace.stats['channel']
        trace.write(os.path.join(Address, unit.lower() + '.' + \
                                        trace_identity), format = 'SAC')
        
        if unit.lower() == 'dis':
            unit_print = 'displacement'
        if unit.lower() == 'vel':
            unit_print = 'velocity'
        if unit.lower() == 'acc':
            unit_print = 'acceleration'

        print inform + ' -- Instrument Correction to ' + unit_print + \
                                            ' for: ' + trace_identity 
        
    except Exception, e:
        print inform + ' -- ' + str(e)

###################### SAC_PAZ #########################################

def SAC_PAZ(trace, paz_file, address, BH_file = 'BH', unit = 'DIS', \
                    BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
    
    """
    This script runs SAC program for instrument correction (PAZ)
    Instrument Correction will be done for all waveforms in the BH_RAW folder
    PAZ files will be loaded from Resp folder

    Instrument Correction has three main steps:
    1) RTR: remove the trend
    2) tapering
    3) pre-filtering and deconvolution of PAZ from Raw counts
    """
    
    try:
        
        trace_info = trace.split('/')[-1].split('.')
        
        if unit.lower() == 'dis':
            unit_sac = 'NONE'
        if unit.lower() == 'vel':
            unit_sac = 'VEL'
        if unit.lower() == 'acc':
            unit_sac = 'ACC'
        
        BP_filter_tuple = eval(BP_filter)
        freqlim = str(BP_filter_tuple[0]) + ' ' +  str(BP_filter_tuple[1]) \
                    + ' ' + str(BP_filter_tuple[2]) + ' ' + \
                    str(BP_filter_tuple[3])
        
        pwd = commands.getoutput('pwd')
        os.chdir(os.path.join(address, BH_file))
        
        p = subprocess.Popen(['sac'],
                             stdout = subprocess.PIPE,
                             stdin  = subprocess.PIPE,
                             stderr = subprocess.STDOUT )
                             
        s = \
        'setbb pzfile ../Resp/' + paz_file.split('/')[-1] + '\n' + \
        'read ../BH_RAW/' + trace.split('/')[-1] + '\n' + \
        'rtrend' + '\n' + \
        'taper' + '\n' + \
        'rmean' + '\n' + \
        'trans from polezero s %pzfile to ' + unit_sac + ' freqlim ' + freqlim + '\n' + \
        'MUL 1.0e9' + '\n' + \
        'write ' + unit.lower() + '.' + trace_info[1] + '.' + trace_info[2] + \
                                            '.' + trace_info[3] + '\n' + \
        'quit\n'
        
        out = p.communicate(s)
        print out[0]
        os.chdir(pwd)
                            
        if unit.lower() == 'dis':
            unit_print = 'displacement'
        if unit.lower() == 'vel':
            unit_print = 'velocity'
        if unit.lower() == 'acc':
            unit_print = 'acceleration'

        print inform + ' -- Instrument Correction to ' + unit_print + \
                        ' for: ' + trace_info[0] + '.' + trace_info[1] + \
                        '.' + trace_info[2] + '.' + trace_info[3] 
                                            
    except Exception, e:
        print inform + ' -- ' + str(e)
"""
###################### obspy_PAZ #######################################

def obspy_PAZ(trace, paz_dic, Address, unit = 'DIS', \
            BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
    
    date = trace.stats['starttime']
    
    try:
        
        trace.data = seisSim(data = trace.data, \
            samp_rate = trace.stats.sampling_rate,paz_remove=paz_dic, \
            paz_simulate = None, remove_sensitivity=False, \
            simulate_sensitivity = False, water_level = 600.0, \
            zero_mean = True, taper = False, pre_filt=eval(BP_filter), \
            seedresp=None, pitsasim=False, sacsim = False)
        
        trace_identity = trace.stats['station'] + '.' + \
                trace.stats['location'] + '.' + trace.stats['channel']
        trace.write(os.path.join(Address, unit.lower() + '.' + \
                                        trace_identity), format = 'SAC')
        
        if unit.lower() == 'dis':
            unit_print = 'displacement'
        if unit.lower() == 'vel':
            unit_print = 'velocity'
        if unit.lower() == 'acc':
            unit_print = 'acceleration'

        print inform + ' -- Instrument Correction to ' + unit_print + \
                                            ' for: ' + trace_identity 
        
    except Exception, e:
        print inform + ' -- ' + str(e)
"""
###################### IRIS_ARC_merge ##################################

def IRIS_ARC_merge(input, clients):
    
    """
    Call "merge_stream" function
    """

    if input[clients + '_merge_auto'] == 'Y':
        global events        
        Period = input['min_date'].split('T')[0] + '_' + \
                    input['max_date'].split('T')[0] + '_' + \
                    str(input['min_mag']) + '_' + str(input['max_mag'])
        eventpath = os.path.join(input['datapath'], Period)
        address = eventpath
    elif input[clients + '_merge'] != 'N':
        address = input[clients + '_merge']
        
    events, address_events = quake_info(address, 'info')
    ls_saved_stas_tmp = []
    ls_saved_stas = []
    for i in range(0, len(events)):
        sta_ev = read_station_event(address_events[i])
        for j in range(0, len(sta_ev[0])):
            if clients == sta_ev[0][j][13]:
                
                if input['merge_type'] == 'raw':
                    BH_file = 'BH_RAW'
                    network = sta_ev[0][j][0]
                    network_name = 'raw'
                elif input['merge_type'] == 'corrected':
                    if input['corr_unit'] == 'DIS':
                        BH_file = 'BH'
                        network = 'dis'
                        network_name = 'dis'
                    elif input['corr_unit'] == 'VEL':
                        BH_file = 'BH_' + input['corr_unit']
                        network = 'vel'
                        network_name = 'vel'
                    elif input['corr_unit'] == 'ACC':
                        BH_file = 'BH_' + input['corr_unit']
                        network = 'acc'
                        network_name = 'acc'
                        
                station_id = network + '.' + sta_ev[0][j][1] + '.' + \
                             sta_ev[0][j][2] + '.' + sta_ev[0][j][3]
                ls_saved_stas_tmp.append(os.path.join(address_events[i], BH_file,\
                                        station_id))
    pattern_sta = input['net'] + '.' + input['sta'] + '.' + \
                    input['loc'] + '.' + input['cha']
    for k in range(0, len(ls_saved_stas_tmp)):
        if fnmatch.fnmatch(ls_saved_stas_tmp[k].split('/')[-1], pattern_sta):
            ls_saved_stas.append(ls_saved_stas_tmp[k])
    
    if len(ls_saved_stas) != 0:
        ls_saved_stations = []
        ls_address = []
        for i in range(0, len(ls_saved_stas)):
            ls_saved_stations.append(ls_saved_stas[i].split('/')[-1])
        ls_sta = list(set(ls_saved_stations))
        for i in range(0, len(address_events)):
            ls_address.append(os.path.join(address_events[i], BH_file))
        print 'Merging the waveforms...'
        merge_stream(ls_address = ls_address, ls_sta = ls_sta, \
                                                    network_name = network_name)
        print 'DONE'
    else:
        print "\nThere is no waveform to merege! Please check your folders!"

###################### merge_stream ####################################

def merge_stream(ls_address, ls_sta, network_name):
    
    global input
    
    address = os.path.dirname(os.path.dirname(ls_address[0]))
    try:
        os.makedirs(os.path.join(address, 'MERGED' + '-' + network_name))
    except Exception, e:
        pass
    
    for i in range(0, len(ls_sta)):
        for j in range(0, len(ls_address)):
            if os.path.isfile(os.path.join(ls_address[j], ls_sta[i])):
                st = read(os.path.join(ls_address[j], ls_sta[i]))
                for k in range(j+1, len(ls_address)):
                    try:
                        st.append(read(os.path.join(ls_address[k], \
                                                        ls_sta[i]))[0])
                    except Exception, e:
                        print e

                st.merge(method=1, fill_value='latest', interpolation_samples=0)
                trace = st[0]
                trace_identity = trace.stats['network'] + '.' + \
                        trace.stats['station'] + '.' + \
                        trace.stats['location'] + '.' + trace.stats['channel']
                st.write(os.path.join(address, 'MERGED' + '-' + network_name, \
                                        trace_identity), format = 'SAC')     
                break

###################### PLOT ############################################

def PLOT(input, clients):
    
    """
    Plotting tools
    """
    
    for i in ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray', 
                'plot_ray_gmt', 'plot_epi', 'plot_dt']:
        if input[i] != 'N':
            events, address_events = quake_info(input[i], 'info')
    
    ls_saved_stas = []
    ls_add_stas = []
    
    for k in ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray', 'plot_ray_gmt', \
                'plot_epi']:
        if input[k] != 'N':
            for i in range(0, len(events)):
                
                ls_saved_stas_tmp = []
                ls_add_stas_tmp = []
                sta_ev = read_station_event(address_events[i])
                
                for j in range(0, len(sta_ev[0])):
                    
                    if input['plot_type'] == 'raw':
                        BH_file = 'BH_RAW'
                        network = sta_ev[0][j][0]
                    elif input['plot_type'] == 'corrected':
                        if input['corr_unit'] == 'DIS':
                            BH_file = 'BH'
                            network = 'dis'
                        elif input['corr_unit'] == 'VEL':
                            BH_file = 'BH_' + input['corr_unit']
                            network = 'vel'
                        elif input['corr_unit'] == 'ACC':
                            BH_file = 'BH_' + input['corr_unit']
                            network = 'acc'
                            
                    station_id = network + ',' + sta_ev[0][j][1] + ',' + \
                         sta_ev[0][j][2] + ',' + sta_ev[0][j][3] + ',' + \
                         sta_ev[0][j][4] + ',' + sta_ev[0][j][5] + ',' + \
                         sta_ev[0][j][6] + ',' + sta_ev[0][j][7] + ',' + \
                         sta_ev[0][j][8] + ',' + sta_ev[0][j][9] + ',' + \
                         sta_ev[0][j][10] + ',' + sta_ev[0][j][11] + ',' + \
                         sta_ev[0][j][12] + ',' + sta_ev[0][j][13]

                    if input['plot_all'] != 'Y':
                        if clients == sta_ev[0][j][13]:
                            ls_saved_stas_tmp.append(station_id)
                            ls_add_stas_tmp.append(\
                                        os.path.join(address_events[i], \
                                        BH_file, network + '.' + \
                                        sta_ev[0][j][1] + '.' + \
                                        sta_ev[0][j][2] + '.' + \
                                        sta_ev[0][j][3]))
                    elif input['plot_all'] == 'Y':
                        ls_saved_stas_tmp.append(station_id)
                        ls_add_stas_tmp.append(\
                                os.path.join(address_events[i], \
                                BH_file, network + '.' + \
                                sta_ev[0][j][1] + '.' + \
                                sta_ev[0][j][2] + '.' + \
                                sta_ev[0][j][3]))
                
                ls_saved_stas.append(ls_saved_stas_tmp)
                ls_add_stas.append(ls_add_stas_tmp)
            
            for i in range(0, len(ls_saved_stas)):
                for j in range(0, len(ls_saved_stas[i])):
                    ls_saved_stas[i][j] = ls_saved_stas[i][j].split(',')
    
    for i in ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray']:
        if input[i] != 'N':
            plot_se_ray(input, ls_saved_stas)
    
    if input['plot_ray_gmt'] != 'N':
        plot_ray_gmt(input, ls_saved_stas)
    
    if input['plot_epi'] != 'N':
        plot_epi(input, ls_add_stas, ls_saved_stas)
    
    if input['plot_dt'] != 'N':
        plot_dt(input, address_events)
    
###################### plot_se_ray #####################################

def plot_se_ray(input, ls_saved_stas):
    
    """
    Plot: station, event, both and ray path
    """

    plt.clf()
    
    #import ipdb; ipdb.set_trace()
    m = Basemap(projection='aeqd', lon_0=-100, lat_0=40, \
                                                resolution='c')
    m.drawcoastlines()
    #m.fillcontinents()
    m.drawparallels(np.arange(-90.,120.,30.))
    m.drawmeridians(np.arange(0.,420.,60.))
    m.drawmapboundary()
    
    pattern_sta = input['sta'] + '.' + input['loc'] + '.' + input['cha']
    for i in range(0, len(ls_saved_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*int(100.*(i+1)/len(ls_saved_stas)),
                                                100.*(i+1)/len(ls_saved_stas)))
        sys.stdout.flush()
        ls_stas = ls_saved_stas[i]
        
        if input['evlatmin']==None:
            input['evlatmin']=-90
            input['evlatmax']=+90
            input['evlonmin']=-180
            input['evlonmax']=+180
        if input['plot_se'] != 'N' or input['plot_ev'] != 'N' or \
                            input['plot_ray'] != 'N':   
            if not input['evlatmin']<=float(ls_stas[0][9])<=input['evlatmax'] or \
               not input['evlonmin']<=float(ls_stas[0][10])<=input['evlonmax'] or \
               not input['max_depth']<=float(ls_stas[0][11])<=input['min_depth'] or \
               not input['min_mag']<=float(ls_stas[0][12])<=input['max_mag']:
                continue
        if input['plot_se'] != 'N' or input['plot_ev'] != 'N' or \
                            input['plot_ray'] != 'N':   
            x_ev, y_ev = m(float(ls_stas[0][10]), \
                           float(ls_stas[0][9]))
            m.scatter(x_ev, y_ev, \
                        math.log(float(ls_stas[0][12])) ** 6, \
                        color="red", marker="o", \
                        edgecolor="black", zorder=10)
        
        for j in range(0, len(ls_stas)):
            try:           
                
                station_name = ls_stas[j][1] + '.' + ls_stas[j][2] + \
                            '.' + ls_stas[j][3]
                station_ID = ls_stas[j][0] + '.' + station_name

                if not fnmatch.fnmatch(station_name, pattern_sta):
                    continue
                if input['mlat_rbb']==None:
                    input['mlat_rbb']=-90.0 
                    input['Mlat_rbb']=+90.0 
                    input['mlon_rbb']=-180.0 
                    input['Mlon_rbb']=+180.0 
                if not input['mlat_rbb']<=float(ls_stas[j][4])<=input['Mlat_rbb'] or \
                   not input['mlon_rbb']<=float(ls_stas[j][5])<=input['Mlon_rbb']:
                    continue
                st_lat = float(ls_stas[j][4])
                st_lon = float(ls_stas[j][5])
                ev_lat = float(ls_stas[j][9])
                ev_lon = float(ls_stas[j][10])
                ev_mag = float(ls_stas[j][12])

                if input['plot_ray'] != 'N':
                    m.drawgreatcircle(ev_lon, ev_lat, st_lon, st_lat, \
                                    alpha = 0.1)
                        
                if input['plot_se'] != 'N' or \
                                input['plot_sta'] != 'N' or \
                                input['plot_ray'] != 'N':
                    x_sta, y_sta = m(st_lon, st_lat)
                    m.scatter(x_sta, y_sta, 20, color='blue', marker="o", \
                                            edgecolor="black", zorder=10)
            
            except Exception, e:
                print e
                pass
                
    print '\nSaving the plot in the following address:'
    print input['plot_save'] + 'plot.' + input['plot_format']
    plt.savefig(os.path.join(input['plot_save'], 'plot.' + \
                                                input['plot_format']))

###################### plot_ray_gmt ####################################

def plot_ray_gmt(input, ls_saved_stas):
    
    """
    Plot: stations, events and ray paths for the specified directory
    using GMT
    """
    #import ipdb; ipdb.set_trace()
    evsta_info_open = open(os.path.join(input['plot_save'], 'evsta_info.txt'), 'w')
    evsta_plot_open = open(os.path.join(input['plot_save'], 'evsta_plot.txt'), 'w')
    ev_plot_open = open(os.path.join(input['plot_save'], 'ev_plot.txt'), 'w')
    sta_plot_open = open(os.path.join(input['plot_save'], 'sta_plot.txt'), 'w')
    
    ls_sta = []
    
    for i in range(0, len(ls_saved_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*int(100.*(i+1)/len(ls_saved_stas)),
                                                100.*(i+1)/len(ls_saved_stas)))
        sys.stdout.flush()
        ls_stas = ls_saved_stas[i]
        if input['evlatmin']==None:
            input['evlatmin']=-90
            input['evlatmax']=+90
            input['evlonmin']=-180
            input['evlonmax']=+180
        if not input['evlatmin']<=float(ls_stas[0][9])<=input['evlatmax'] or \
           not input['evlonmin']<=float(ls_stas[0][10])<=input['evlonmax'] or \
           not input['max_depth']<=float(ls_stas[0][11])<=input['min_depth'] or \
           not input['min_mag']<=float(ls_stas[0][12])<=input['max_mag']:
            continue
        ev_plot_open.writelines(str(round(float(ls_stas[0][10]), 5)) + ' ' + \
                                str(round(float(ls_stas[0][9]), 5)) + ' ' + \
                                '\n')
        pattern_sta = input['sta'] + '.' + input['loc'] + '.' + input['cha']
        
        for j in range(0, len(ls_stas)):
            
            station_name = ls_stas[j][1] + '.' + ls_stas[j][2] + \
                                '.' + ls_stas[j][3]
            station_ID = ls_stas[j][0] + '.' + station_name
            
            
            if not fnmatch.fnmatch(station_name, pattern_sta):
                continue
            if input['mlat_rbb']==None:
                    input['mlat_rbb']=-90.0 
                    input['Mlat_rbb']=+90.0 
                    input['mlon_rbb']=-180.0 
                    input['Mlon_rbb']=+180.0 
            if not input['mlat_rbb']<=float(ls_stas[j][4])<=input['Mlat_rbb'] or \
               not input['mlon_rbb']<=float(ls_stas[j][5])<=input['Mlon_rbb']:
                continue
            
            evsta_info_open.writelines(ls_stas[j][8] + ' , ' + station_ID + ' , \n')
    
            evsta_plot_open.writelines(\
                '> -G' + str(int(random.random()*256)) + '/' + \
                str(int(random.random()*256)) + '/' + str(int(random.random()*256)) + '\n' + \
                str(round(float(ls_stas[j][10]), 5)) + ' ' + \
                str(round(float(ls_stas[j][9]), 5)) + ' ' + \
                str(random.random()) + ' ' + \
                '\n' + \
                str(round(float(ls_stas[j][5]), 5)) + ' ' + \
                str(round(float(ls_stas[j][4]), 5)) + ' ' + \
                str(random.random()) + ' ' + \
                '\n')
            
            if ls_sta == [] or not station_ID in ls_sta[:][0]:
                ls_sta.append([station_ID, \
                    [str(round(float(ls_stas[j][4]), 5)), \
                     str(round(float(ls_stas[j][5]), 5))]])
    
    for k in range(0, len(ls_sta)):
        sta_plot_open.writelines(\
                str(round(float(ls_sta[k][1][1]), 5)) + ' ' + \
                str(round(float(ls_sta[k][1][0]), 5)) + ' ' + \
                '\n')
    
    evsta_info_open.close()
    evsta_plot_open.close()
    ev_plot_open.close()
    sta_plot_open.close()    
    
    pwd_str = os.getcwd()
    
    os.chdir(input['plot_save'])
    
    os.system('psbasemap -Rd -JK180/9i -B45g30 -K > output.ps')
    os.system('pscoast -Rd -JK180/9i -B45g30:."World-wide Ray Path Coverage": -Dc -A1000 -Glightgray -Wthinnest -t20 -O -K >> output.ps')
    
    os.system('psxy ./evsta_plot.txt -JK180/9i -Rd -O -K -t100 >> output.ps')
    os.system('psxy ./sta_plot.txt -JK180/9i -Rd -Si0.14c -Gblue -O -K >> output.ps')
    os.system('psxy ./ev_plot.txt -JK180/9i -Rd -Sa0.28c -Gred -O >> output.ps')
        
    os.system('ps2raster output.ps -A -P -Tf')
    
    os.system('mv output.ps plot.ps')
    os.system('mv output.pdf plot.pdf')
    
    os.system('xdg-open plot.pdf')
    
    os.chdir(pwd_str)
    
###################### plot_epi ########################################

def plot_epi(input, ls_add_stas, ls_saved_stas):
    
    """
    Plot: Epicentral distance-Time
    """
            
    plt.clf()
    
    for target in range(0, len(ls_add_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*int(100.*(target+1)/len(ls_add_stas)),
                                                100.*(target+1)/len(ls_add_stas)))
        sys.stdout.flush()
        for i in range(0, len(ls_add_stas[target])):
            try:
                tr = read(ls_add_stas[target][i])[0]
                tr.normalize()
                dist = locations2degrees(float(ls_saved_stas[target][i][9]), \
                            float(ls_saved_stas[target][i][10]), \
                            float(ls_saved_stas[target][i][4]), \
                            float(ls_saved_stas[target][i][5]))
                if input['min_epi'] <= dist <= input['max_epi']:
                    x = range(0, len(tr.data))
                    for i in range(0, len(x)):
                        x[i] = x[i]/float(tr.stats['sampling_rate'])
                    plt.plot(x, tr.data + dist, color = 'black')
            except Exception, e:
                print e
                pass
            plt.xlabel('Time (sec)')
            plt.ylabel('Epicentral distance (deg)')
    print '\nSaving the plot in the following address:'
    print input['plot_save'] + 'plot.' + input['plot_format']
    plt.savefig(os.path.join(input['plot_save'], 'plot.' + \
                                                input['plot_format']))

###################### plot_dt #########################################

def plot_dt(input, address_events):
    
    """
    Plot: Data(MB)-Time(Sec)
    """
            
    for i in range(0, len(address_events)):
        for client in ['time_iris', 'time_arc']:
            print address_events[i]
            if os.path.isfile(os.path.join(address_events[i], 'info', client)):
                plt.clf()
                dt_open = open(os.path.join(address_events[i], \
                                            'info', client))
                dt_read = dt_open.readlines()
                for j in range(0, len(dt_read)):
                    dt_read[j] = dt_read[j].split(',')
                
                time_single = 0
                succ = 0; fail = 0
                MB_all = []; time_all = []
                for k in range(0, len(dt_read)):
                    time_single += eval(dt_read[k][4]) + eval(dt_read[k][5])/(1024.**2)
                    time_all.append(time_single)
                    MB_single = eval(dt_read[k][6])
                    MB_all.append(MB_single)
                    if dt_read[k][7] == '+':
                        single_succ = plt.scatter(time_single, MB_single, s = 1, \
                                    c = 'b', edgecolors = 'b', marker = 'o', \
                                    label = 'Serial (successful)')
                        succ += 1
                    elif dt_read[k][7] == '-':
                        single_fail = plt.scatter(time_single, MB_single, s = 1, \
                                    c = 'r', edgecolors = 'r', marker = 'o', \
                                    label = 'Serial (failed)')
                        fail += 1
                
                if input['req_parallel'] == 'Y':
                    rep_par_open = open(os.path.join(address_events[i], \
                                                    'info', 'report_parallel'))
                    rep_par_read = rep_par_open.readlines()
                    time_parallel = eval(rep_par_read[4].split(',')[0]) + \
                                    eval(rep_par_read[4].split(',')[1])/(1024.**2)
                    MB_parallel = eval(rep_par_read[4].split(',')[2])
                    trans_rate_parallel = MB_parallel/time_parallel*60
                    parallel_succ = plt.scatter(time_parallel, MB_parallel, s = 30, \
                                    c = 'r', edgecolors = 'r', marker = 'o', \
                                    label = 'Parallel')
                
                time_array = np.array(time_all)
                MB_array = np.array(MB_all)
                
                poly = np.poly1d(np.polyfit(time_array, MB_array, 1))
                time_poly = np.linspace(0, time_all[-1], len(time_all))
                plt.plot(time_array, poly(time_array), 'k--')
                
                trans_rate = (poly(time_array[-1])-poly(time_array[0]))/ \
                                        (time_array[-1]-time_array[0])*60
                
                plt.xlabel('Time (sec)', size = 'large', weight = 'bold')
                plt.ylabel('Stored Data (MB)', size = 'large', weight = 'bold')
                plt.xticks(size = 'large', weight = 'bold')
                plt.yticks(size = 'large', weight = 'bold')
                
                plt.title(client.split('_')[1].upper() + '\n' + \
                            'All: ' + str(succ + fail) + '--' + \
                            'Succ: ' + str(succ) + ' ' + '(' + \
                            str(round(float(succ)/(succ + fail)*100., 1)) + '%)' + \
                            '-' + \
                            'Fail: ' + str(fail) + ' ' + '(' + \
                            str(round(float(fail)/(succ + fail)*100., 1)) + '%)' + \
                            '--' + \
                             str(round(trans_rate, 2)) + 'MB/min', size = 'x-large')
                """
                plt.title(client.split('_')[1].upper() + '\n' + \
                             'Serial: ' + str(round(trans_rate, 2)) + 'MB/min -- ' + \
                             'Parallel: ' + str(round(trans_rate_parallel, 2)) + 'MB/min', \
                             size = 'large', weight = 'bold')
                """
                
                if input['req_parallel'] == 'Y':
                    plt.legend([single_succ, parallel_succ], \
                            ['Serial', 'Parallel'], loc=4)
                
                plt.savefig(os.path.join(address_events[i], 'info', \
                            'Data-Time_' + client.split('_')[1] + \
                            '.' + input['plot_format']))
            
###################### XML_list_avail ##################################

def XML_list_avail(xmlfile):
    
    """
    This module changes the XML file got from availability to a list
    """
    
    sta_obj = objectify.XML(xmlfile)
    sta_req = []

    for i in range(0, len(sta_obj.Station)):
        
        station = sta_obj.Station[i]
        net = station.get('net_code')
        sta = station.get('sta_code')
        
        lat = str(station.Lat)
        lon = str(station.Lon)
        ele = str(station.Elevation)
        
        for j in range(0, len(station.Channel)):
            cha = station.Channel[j].get('chan_code')
            loc = station.Channel[j].get('loc_code')
            
            sta_req.append([net, sta, loc, cha, lat, lon, ele])
    
    return sta_req

###################### create_folders_files ############################

def create_folders_files(events, eventpath):
    
    """
    Create required folders and files in the event folder(s)
    """
    
    len_events = len(events)
    
    for i in range(0, len_events):
        if os.path.exists(os.path.join(eventpath, events[i]['event_id'])) == True:
            
            if raw_input('Folder for -- the requested Period (min/max) ' + \
            'and Magnitude (min/max) -- exists in your directory.' + '\n\n' + \
            'You could either close the program and try updating your ' + \
            'folder OR remove the tree, continue the program and download again.' + \
            '\n' + 'Do you want to continue? (Y/N)' + '\n').upper() == 'Y':
                print '-------------------------------------------------------------'
                shutil.rmtree(os.path.join(eventpath, events[i]['event_id']))
            
            else:
                print '------------------------------------------------'
                print 'So...you decided to update your folder...Ciao'
                print '------------------------------------------------'
                sys.exit()

    for i in range(0, len_events):
        try:
            os.makedirs(os.path.join(eventpath, events[i]['event_id'], 'BH_RAW'))
            os.makedirs(os.path.join(eventpath, events[i]['event_id'], 'Resp'))
            os.makedirs(os.path.join(eventpath, events[i]['event_id'], 'info'))
        except Exception, e:
            pass
    
    for i in range(0, len_events):
        Report = open(os.path.join(eventpath, events[i]['event_id'], \
            'info', 'report_st'), 'a+')
        Report.close()
    
    
    for i in range(0, len_events):
        Exception_file = open(os.path.join(eventpath, events[i]['event_id'], \
            'info', 'exception'), 'a+')
        eventsID = events[i]['event_id']
        Exception_file.writelines('\n' + eventsID + '\n')
        
        Syn_file = open(os.path.join(eventpath, events[i]['event_id'], \
            'info', 'station_event'), 'a+')
        Syn_file.close()
        
    for i in range(0, len_events):
        quake_file = open(os.path.join(eventpath, events[i]['event_id'],\
                            'info', 'quake'), 'a+')
        
        quake_file.writelines(repr(events[i]['datetime'].year).rjust(15)\
                + repr(events[i]['datetime'].julday).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['datetime'].hour).rjust(15)\
                + repr(events[i]['datetime'].minute).rjust(15) + \
                repr(events[i]['datetime'].second).rjust(15) + \
                repr(events[i]['datetime'].microsecond).rjust(15) + '\n')
        
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % events[i]['latitude'])) + '%.5f' \
                % events[i]['latitude'] + \
                ' '*(15 - len('%.5f' % events[i]['longitude'])) + '%.5f' \
                % events[i]['longitude'] + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % abs(events[i]['depth']))) + '%.5f' \
                % abs(events[i]['depth']) + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % abs(events[i]['magnitude']))) + '%.5f' \
                % abs(events[i]['magnitude']) + '\n')
        quake_file.writelines(\
                ' '*(15 - len(events[i]['event_id'])) + \
                        events[i]['event_id'] + '-' + '\n')
        
        quake_file.writelines(repr(events[i]['t1'].year).rjust(15)\
                + repr(events[i]['t1'].julday).rjust(15) \
                + repr(events[i]['t1'].month).rjust(15) \
                + repr(events[i]['t1'].day).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['t1'].hour).rjust(15)\
                + repr(events[i]['t1'].minute).rjust(15) + \
                repr(events[i]['t1'].second).rjust(15) + \
                repr(events[i]['t1'].microsecond).rjust(15) + '\n')
        
        quake_file.writelines(repr(events[i]['t2'].year).rjust(15)\
                + repr(events[i]['t2'].julday).rjust(15) \
                + repr(events[i]['t2'].month).rjust(15) \
                + repr(events[i]['t2'].day).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['t2'].hour).rjust(15)\
                + repr(events[i]['t2'].minute).rjust(15) + \
                repr(events[i]['t2'].second).rjust(15) + \
                repr(events[i]['t2'].microsecond).rjust(15) + '\n')

###################### writesac_all ####################################

def writesac_all(i, events, address_events):
    
    sta_ev = read_station_event(address_events[i])
    ls_saved_stas = []
    
    for j in range(0, len(sta_ev[0])):
        station_id = sta_ev[0][j][0] + '.' + sta_ev[0][j][1] + '.' + \
                     sta_ev[0][j][2] + '.' + sta_ev[0][j][3]
        ls_saved_stas.append(os.path.join(address_events[i], 'BH_RAW',\
                                station_id))
    for j in range(0, len(sta_ev[0])):
        try:
            st = read(ls_saved_stas[j])
            st[0].write(ls_saved_stas[j], format = 'SAC')
            tr = read(ls_saved_stas[j])[0]
            if sta_ev[0][j][4] != None:
                tr.stats['sac']['stla'] = float(sta_ev[0][j][4])
            if sta_ev[0][j][5] != None:
                tr.stats['sac']['stlo'] = float(sta_ev[0][j][5])
            if sta_ev[0][j][6] != None:
                tr.stats['sac']['stel'] = float(sta_ev[0][j][6])
            if sta_ev[0][j][7] != None:
                tr.stats['sac']['stdp'] = float(sta_ev[0][j][7])
            
            if sta_ev[0][j][9] != None:
                tr.stats['sac']['evla'] = float(sta_ev[0][j][9])
            if sta_ev[0][j][10] != None:
                tr.stats['sac']['evlo'] = float(sta_ev[0][j][10])
            if sta_ev[0][j][11] != None:
                tr.stats['sac']['evdp'] = float(sta_ev[0][j][11])
            if sta_ev[0][j][12] != None:
                tr.stats['sac']['mag'] = float(sta_ev[0][j][12])
            
            tr.write(ls_saved_stas[j], format = 'SAC')
        except Exception, e:
            print '\n'
            print e
            print ls_saved_stas[j]
            print '------------------'
            
###################### writesac ########################################

def writesac(address_st, sta_info, ev_info):
    
    st = read(address_st)
    st[0].write(address_st, format = 'SAC')
    st = read(address_st)
    
    if sta_info['latitude'] != None:
        st[0].stats['sac']['stla'] = sta_info['latitude']
    if sta_info['longitude'] != None:
        st[0].stats['sac']['stlo'] = sta_info['longitude']
    if sta_info['elevation'] != None:
        st[0].stats['sac']['stel'] = sta_info['elevation']
    if sta_info['depth'] != None:
        st[0].stats['sac']['stdp'] = sta_info['depth']
    
    if ev_info['latitude'] != None:
        st[0].stats['sac']['evla'] = ev_info['latitude']    
    if ev_info['longitude'] != None:
        st[0].stats['sac']['evlo'] = ev_info['longitude']   
    if ev_info['depth'] != None:
        st[0].stats['sac']['evdp'] = ev_info['depth']
    if ev_info['magnitude'] != None:
        st[0].stats['sac']['mag'] = ev_info['magnitude']
        
    st[0].write(address_st, format = 'SAC')

###################### rm_duplicate ####################################

def rm_duplicate(Sta_all, address):
    
    """
    remove duplicates and give back the required list for updating
    """
        
    sta_all = []
    saved = []
        
    for i in Sta_all:
        if i[2] == '--' or i[2] == '  ':
            i[2] = ''
        for j in range(0, len(i)):
            if i[j] != str(i[j]):
                i[j] = str(i[j]) 
        if len(i) == 7:
            sta_all.append(str(i[0] + '_' + i[1] + '_' + i[2] + '_' + \
                            i[3] + '_' + i[4] + '_' + i[5] + '_' + i[6]))
        elif len(i) == 8:
            sta_all.append(str(i[0] + '_' + i[1] + '_' + i[2] + '_' + \
                            i[3] + '_' + i[4] + '_' + i[5] + '_' + i[6]\
                             + '_' + i[7]))
                            
    sta_ev = read_station_event(address)
    ls_saved_stas = sta_ev[0]
    
    for i in range(0, len(ls_saved_stas)):
        sta_info = ls_saved_stas[i]
        saved.append(sta_info[0] + '_' + sta_info[1] + '_' + \
                            sta_info[2] + '_' + sta_info[3])
    
    Stas_req = sta_all
    
    len_all_sta = len(sta_all)
    num = []
    for i in range(0, len(saved)):
        for j in range(0, len(Stas_req)):
            if saved[i] in Stas_req[j]:
                num.append(j)

    num.sort(reverse=True)
    for i in num:
        del Stas_req[i]  
    
    for m in range(0, len(Stas_req)):
        Stas_req[m] = Stas_req[m].split('_')
    
    Stas_req.sort()
    
    print '------------------------------------------'
    print 'Info:'
    print 'Number of all saved stations:     ' + str(len(saved))
    print 'Number of all available stations: ' + str(len_all_sta)
    print 'Number of stations to update for: ' + str(len(Stas_req))
    print '------------------------------------------'
    
    return Stas_req

###################### read_station_event ##############################

def read_station_event(address):
    
    """
    Reads the station_event file ("info" folder)
    """
    
    if address.split('/')[-1].split('.') == ['info']:
        target_add = [address]
    elif locate(address, 'info'):
        target_add = locate(address, 'info')
    else:
        print 'Error: There is no "info" folder in the address.'
    
    sta_ev = []
    
    for k in range(0, len(target_add)):
        sta_ev_tmp = []
        
        if os.path.isfile(os.path.join(target_add[k], 'station_event')):
            sta_file_open = open(os.path.join(target_add[k],\
                                                    'station_event'), 'r')
        else:
            create_station_event(address = target_add[k])
            sta_file_open = open(os.path.join(target_add[k],\
                                                    'station_event'), 'r')
        sta_file = sta_file_open.readlines()
        for i in sta_file:
            sta_ev_tmp.append(i.split(','))
        sta_ev.append(sta_ev_tmp)
    
    return sta_ev

###################### create_station_event ############################

def create_station_event(address):
    
    """
    Creates the station_event file ("info" folder)
    """
    
    print '====================================='
    print 'station_event could not be found'
    print 'Start Creating the station_event file'
    print '====================================='
    
    event_address = os.path.dirname(address)
    if os.path.isdir(os.path.join(event_address, 'BH_RAW')):
        sta_address = os.path.join(event_address, 'BH_RAW')
    elif os.path.isdir(os.path.join(event_address, 'BH')):
        sta_address = os.path.join(event_address, 'BH')
    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))
    
    print len(ls_stas)
    for i in range(0, len(ls_stas)):
        print i,
        sta_file_open = open(os.path.join(address, 'station_event'), 'a')
        
        try:
            sta = read(ls_stas[i])[0]
        except Exception, e:
            print e
            print 'could not read the waveform data'
        
        sta_stats = sta.stats
        
        try:
            sta_info = sta_stats.network + ',' + sta_stats.station + ',' + \
                        sta_stats.location + ',' + sta_stats.channel + ',' + \
                        str(sta_stats.sac.stla) + ',' + str(sta_stats.sac.stlo) + ',' + \
                        str(sta_stats.sac.stel) + ',' + str(sta_stats.sac.stdp) + ',' + \
                        event_address.split('/')[-1] + ',' + \
                        str(sta_stats.sac.evla) + ',' + str(sta_stats.sac.evlo) + ',' + \
                        str(sta_stats.sac.evdp) + ',' + str(sta_stats.sac.mag) + ',' + \
                        'iris' + ',' + '\n'
        except Exception, e:
            print e
            sta_info = sta_stats.network + ',' + sta_stats.station + ',' + \
                        sta_stats.location + ',' + sta_stats.channel + ',' + \
                        str(-12345.0) + ',' + str(-12345.0) + ',' + \
                        str(-12345.0) + ',' + str(-12345.0) + ',' + \
                        event_address.split('/')[-1] + ',' + \
                        str(-12345.0) + ',' + str(-12345.0) + ',' + \
                        str(-12345.0) + ',' + str(-12345.0) + ',' + \
                        'iris' + ',' + '\n'
        
        sta_file_open.writelines(sta_info)
        sta_file_open.close()
    
    print '\n--------------------------'
        
###################### quake_info ######################################

def quake_info(address, target):
    
    """
    Reads the info in quake file ("info" folder)
    """
    
    events = []
    target_add = locate(address, target)
    
    for k in range(0, len(target_add)):
        if not os.path.isfile(os.path.join(target_add[k], 'quake')):
            print '============================='
            print 'quake file could not be found'
            print 'Start Creating the quake file'
            print '============================='
            quake_create(address_info = target_add[k])
        quake_file_open = open(os.path.join(target_add[k], 'quake'), 'r')
        quake_file = quake_file_open.readlines()

        tmp = []
        
        for i in quake_file:
            for j in i.split():
                try:
                    tmp.append(float(j))
                except ValueError:
                    pass
        
        if len(tmp) < 20:
            print '====================='
            print 'Modify the quake file'
            print '====================='
            quake_modify(quake_item = tmp, address_info = target_add[k])
            
            quake_file_open = open(os.path.join(target_add[k], 'quake'), 'r')
            quake_file = quake_file_open.readlines()

            tmp = []
            
            for i in quake_file:
                for j in i.split():
                    try:
                        tmp.append(float(j))
                    except ValueError:
                        pass

        quake_d = {'year0': int(tmp[0]), 'julday0': int(tmp[1]), \
                'hour0': int(tmp[2]), 'minute0': int(tmp[3]), \
                'second0': int(tmp[4]), 'lat': float(tmp[6]), \
                'lon': float(tmp[7]), 'dp': float(tmp[8]), \
                'mag': float(tmp[9]), \
                'year1': int(tmp[10]), 'julday1': int(tmp[11]), \
                'hour1': int(tmp[14]), 'minute1': int(tmp[15]), \
                'second1': int(tmp[16]), \
                'year2': int(tmp[18]), 'julday2': int(tmp[19]), \
                'hour2': int(tmp[22]), 'minute2': int(tmp[23]), \
                'second2': int(tmp[24]),}
        
        quake_t0 = UTCDateTime(year=quake_d['year0'], julday=quake_d['julday0'], \
                        hour=quake_d['hour0'], minute=quake_d['minute0'], \
                        second=quake_d['second0'])
        quake_t1 = UTCDateTime(year=quake_d['year1'], julday=quake_d['julday1'], \
                        hour=quake_d['hour1'], minute=quake_d['minute1'], \
                        second=quake_d['second1'])
        quake_t2 = UTCDateTime(year=quake_d['year2'], julday=quake_d['julday2'], \
                        hour=quake_d['hour2'], minute=quake_d['minute2'], \
                        second=quake_d['second2'])
        
        events.append({'author': 'NONE', 'datetime': quake_t0,\
                    'depth': quake_d['dp'],
                    'event_id': quake_file[5].split('-')[0].lstrip(),
                    'flynn_region': 'NONE',
                    'latitude': quake_d['lat'],
                    'longitude': quake_d['lon'],
                    'magnitude': quake_d['mag'],
                    'magnitude_type': 'NONE',
                    'origin_id': -12345.0,
                    't1': quake_t1,
                    't2': quake_t2})

    address_event = []
    for i in range(0, len(target_add)):
        address_event.append(os.path.dirname(target_add[i]))
    
    return events, address_event

###################### quake_create ####################################

def quake_create(address_info):
            
    """
    if there is not any quake file in the info folder
    then it will be created based on the data available 
    in the BH_RAW or BH file
    """
    
    quake_file = open(os.path.join(address_info, 'quake'), 'w')
    
    address = os.path.normpath(os.path.join(address_info, '..'))
    
    if os.path.isdir(os.path.join(address, 'BH_RAW')):
        sta_address = os.path.join(address, 'BH_RAW')
    #elif os.path.isdir(os.path.join(address, 'BH')):
    else:
        sta_address = os.path.join(address, 'BH')
        
    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))
    
    sta = read(ls_stas[0])[0]
    sta_stats = sta.stats
    
    try:
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15)\
                + repr(sta_stats.starttime.julday).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15)\
                + repr(sta_stats.starttime.minute).rjust(15) + \
                repr(sta_stats.starttime.second).rjust(15) + \
                repr(sta_stats.starttime.microsecond).rjust(15) + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % sta_stats.sac.evla)) + '%.5f' \
                % sta_stats.sac.evla + \
                ' '*(15 - len('%.5f' % sta_stats.sac.evlo)) + '%.5f' \
                % sta_stats.sac.evlo + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % abs(sta_stats.sac.evdp))) + '%.5f' \
                % abs(sta_stats.sac.evdp) + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % abs(sta_stats.sac.mag))) + '%.5f' \
                % abs(sta_stats.sac.mag) + '\n')
        quake_file.writelines(\
                ' '*(15 - len(address.split('/')[-1])) + \
                        address.split('/')[-1] + '-' + '\n')
        
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15)\
                + repr(sta_stats.starttime.julday).rjust(15) \
                + repr(sta_stats.starttime.month).rjust(15) \
                + repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15)\
                + repr(sta_stats.starttime.minute).rjust(15) + \
                repr(sta_stats.starttime.second).rjust(15) + \
                repr(sta_stats.starttime.microsecond).rjust(15) + '\n')
            
        sta_stats_endtime = sta_stats.starttime + sta_stats.npts/sta_stats.sampling_rate

        quake_file.writelines(repr(sta_stats_endtime.year).rjust(15)\
                + repr(sta_stats_endtime.julday).rjust(15) \
                + repr(sta_stats_endtime.month).rjust(15) \
                + repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats_endtime.hour).rjust(15)\
                + repr(sta_stats_endtime.minute).rjust(15) + \
                repr(sta_stats_endtime.second).rjust(15) + \
                repr(sta_stats_endtime.microsecond).rjust(15) + '\n')
                
    except Exception, e:
        print e
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15)\
                + repr(sta_stats.starttime.julday).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15)\
                + repr(sta_stats.starttime.minute).rjust(15) + \
                repr(sta_stats.starttime.second).rjust(15) + \
                repr(sta_stats.starttime.microsecond).rjust(15) + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % 0.0)) + '%.5f' \
                % 0.0 + \
                ' '*(15 - len('%.5f' % 0.0)) + '%.5f' \
                % 0.0 + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % abs(-12345.0))) + '%.5f' \
                % abs(-12345.0) + '\n')
        quake_file.writelines(\
                ' '*(15 - len('%.5f' % abs(-12345.0))) + '%.5f' \
                % abs(-12345.0) + '\n')
        quake_file.writelines(\
                ' '*(15 - len(address.split('/')[-1])) + \
                        address.split('/')[-1] + '-' + '\n')
        
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15)\
                + repr(sta_stats.starttime.julday).rjust(15) \
                + repr(sta_stats.starttime.month).rjust(15) \
                + repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15)\
                + repr(sta_stats.starttime.minute).rjust(15) + \
                repr(sta_stats.starttime.second).rjust(15) + \
                repr(sta_stats.starttime.microsecond).rjust(15) + '\n')
            
        sta_stats_endtime = sta_stats.starttime + sta_stats.npts/sta_stats.sampling_rate

        quake_file.writelines(repr(sta_stats_endtime.year).rjust(15)\
                + repr(sta_stats_endtime.julday).rjust(15) \
                + repr(sta_stats_endtime.month).rjust(15) \
                + repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats_endtime.hour).rjust(15)\
                + repr(sta_stats_endtime.minute).rjust(15) + \
                repr(sta_stats_endtime.second).rjust(15) + \
                repr(sta_stats_endtime.microsecond).rjust(15) + '\n')
    quake_file.close()

###################### quake_modify ####################################

def quake_modify(quake_item, address_info):

    """
    if the quake file does not contain all the required parameters
    then it will be modified based on the data available 
    in the BH_RAW or BH file
    """
    
    quake_file_new = open(os.path.join(address_info, 'quake'), 'w')
    
    address = os.path.normpath(os.path.join(address_info, '..'))
    
    if os.path.isdir(os.path.join(address, 'BH_RAW')):
        sta_address = os.path.join(address, 'BH_RAW')
    #elif os.path.isdir(os.path.join(address, 'BH')):
    else:
        sta_address = os.path.join(address, 'BH')
        
    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))
    
    sta = read(ls_stas[0])[0]
    sta_stats = sta.stats
    
    try:
        quake_file_new.writelines(repr(int(quake_item[0])).rjust(15)\
                + repr(int(quake_item[1])).rjust(15) + '\n')
        quake_file_new.writelines(repr(int(quake_item[2])).rjust(15)\
                + repr(int(quake_item[3])).rjust(15) + \
                repr(int(quake_item[4])).rjust(15) + \
                repr(int(quake_item[5])).rjust(15) + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len('%.5f' % quake_item[6])) + '%.5f' \
                % quake_item[6] + \
                ' '*(15 - len('%.5f' % quake_item[7])) + '%.5f' \
                % quake_item[7] + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len('%.5f' % abs(quake_item[8]))) + '%.5f' \
                % abs(quake_item[8]) + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len('%.5f' % abs(sta_stats.sac.mag))) + '%.5f' \
                % abs(sta_stats.sac.mag) + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len(address.split('/')[-1])) + \
                        address.split('/')[-1] + '-' + '\n')
        
        quake_file_new.writelines(repr(sta_stats.starttime.year).rjust(15)\
                + repr(sta_stats.starttime.julday).rjust(15) \
                + repr(sta_stats.starttime.month).rjust(15) \
                + repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats.starttime.hour).rjust(15)\
                + repr(sta_stats.starttime.minute).rjust(15) + \
                repr(sta_stats.starttime.second).rjust(15) + \
                repr(sta_stats.starttime.microsecond).rjust(15) + '\n')
            
        sta_stats_endtime = sta_stats.starttime + sta_stats.npts/sta_stats.sampling_rate

        quake_file_new.writelines(repr(sta_stats_endtime.year).rjust(15)\
                + repr(sta_stats_endtime.julday).rjust(15) \
                + repr(sta_stats_endtime.month).rjust(15) \
                + repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats_endtime.hour).rjust(15)\
                + repr(sta_stats_endtime.minute).rjust(15) + \
                repr(sta_stats_endtime.second).rjust(15) + \
                repr(sta_stats_endtime.microsecond).rjust(15) + '\n')
                
    except Exception, e:
        print e
        quake_file_new.writelines(repr(int(quake_item[0])).rjust(15)\
                + repr(int(quake_item[1])).rjust(15) + '\n')
        quake_file_new.writelines(repr(int(quake_item[2])).rjust(15)\
                + repr(int(quake_item[3])).rjust(15) + \
                repr(int(quake_item[4])).rjust(15) + \
                repr(int(quake_item[5])).rjust(15) + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len('%.5f' % quake_item[6])) + '%.5f' \
                % quake_item[6] + \
                ' '*(15 - len('%.5f' % quake_item[7])) + '%.5f' \
                % quake_item[7] + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len('%.5f' % abs(quake_item[8]))) + '%.5f' \
                % abs(quake_item[8]) + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len('%.5f' % abs(-12345.0))) + '%.5f' \
                % abs(-12345.0) + '\n')
        quake_file_new.writelines(\
                ' '*(15 - len(address.split('/')[-1])) + \
                        address.split('/')[-1] + '-' + '\n')
        
        quake_file_new.writelines(repr(sta_stats.starttime.year).rjust(15)\
                + repr(sta_stats.starttime.julday).rjust(15) \
                + repr(sta_stats.starttime.month).rjust(15) \
                + repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats.starttime.hour).rjust(15)\
                + repr(sta_stats.starttime.minute).rjust(15) + \
                repr(sta_stats.starttime.second).rjust(15) + \
                repr(sta_stats.starttime.microsecond).rjust(15) + '\n')
            
        sta_stats_endtime = sta_stats.starttime + sta_stats.npts/sta_stats.sampling_rate

        quake_file_new.writelines(repr(sta_stats_endtime.year).rjust(15)\
                + repr(sta_stats_endtime.julday).rjust(15) \
                + repr(sta_stats_endtime.month).rjust(15) \
                + repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats_endtime.hour).rjust(15)\
                + repr(sta_stats_endtime.minute).rjust(15) + \
                repr(sta_stats_endtime.second).rjust(15) + \
                repr(sta_stats_endtime.microsecond).rjust(15) + '\n')
    quake_file_new.close()
    
###################### compress_gzip ###################################

def compress_gzip(path, tar_file, files):
            
    tar = tarfile.open(tar_file, "w:gz")
    os.chdir(path)
    
    for infile in glob.glob( os.path.join(path, files) ):
        
        print '------------------------------------'
        print 'Compressing:'
        print infile
        
        tar.add(infile.split('/')[-1])
        os.remove(infile)
    
    tar.close()

###################### send_email ######################################

def send_email():
    
    """
    Sending email to the specified "email" address
    """ 
    
    global input, t1_pro, t1_str
    
    t2_pro = time.time()
    t2_str = datetime.now()
    t_pro = t2_pro - t1_pro
    
    fromaddr = 'obspyDMT'
    toaddrs = input['email']
    
    msg = "Request at: \n" + str(t1_str) + "\n\nFinished at \n" + \
            str(t2_str) + "\n\n" + "Total time: " + "\n" + str(t_pro)
    
    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddr, toaddrs, msg)

###################### getFolderSize ###################################

def getFolderSize(folder):

    """
    Returns the size of a folder in bytes.
    """

    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

###################### locate ##########################################

def locate(root = '.', target = 'info'):

    """
    Locates a subdirectory within a directory.
    """
    
    matches = []
    
    for root, dirnames, filenames in os.walk(root):
        for dirnames in fnmatch.filter(dirnames, target):
            matches.append(os.path.join(root, dirnames))
    
    return matches

########################################################################
########################################################################
########################################################################

def main():
    
    global t1_pro, t1_str
    
    t1_pro = time.time()
    t1_str = datetime.now()
    
    status = obspyDMT()
    
    try:
        global input, events
        size = getFolderSize(input['datapath'])
        size /= (1024.**2)
        t_pro = time.time() - t1_pro
        print "\n\n=================================================="
        print "Info:"
        print "* The following folder contains %f MB of data."  % (size)
        print input['datapath']
        print "* Total time %f sec" %(t_pro)
        print "--------------------------------------------------"
        Period = input['min_date'].split('T')[0] + '_' + \
                    input['max_date'].split('T')[0] + '_' + \
                    str(input['min_mag']) + '_' + str(input['max_mag'])
        eventpath = os.path.join(input['datapath'], Period)
                
        len_events = len(events)
        
        address = []
        for i in range(0, len_events):
            address.append(os.path.join(eventpath, events[i]['event_id']))
        if address != []:
            print "* Address of the stored events:"
            for i in range(0, len_events):
                print address[i]
            print "=================================================="
        
    except Exception, e:
        print e
        pass
        print "=================================================="
    # pass the return of main to the command line.
    sys.exit(status)


if __name__ == "__main__":
    main()



# ----------------------------------------------
# TRASH:
#!! Still do not know which one is the best: 
#parallel_results = pprocess.Queue(limit=input['req_np'])
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IRIS_download_core))
#parallel_results = pprocess.Map(limit=input['req_np'])
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IRIS_download_core))
#parallel_results = pprocess.Map(limit=input['req_np'], continuous=1)
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IRIS_download_core))
'''
parallel_len_req_iris = range(0, len_req_iris)
lol = [parallel_len_req_iris[n:n+input['req_np']] for n in range(0, len(parallel_len_req_iris), input['req_np'])]
import ipdb; ipdb.set_trace()
jobs = []
for j in range(0, len_req_iris):
    p = multiprocessing.Process(target=IRIS_download_core,\
                args=(i, j, dic, type, \
                        len_events, \
                        events, add_event, \
                        Sta_req, input,))
    jobs.append(p)

for l in range(0, len(lol)):
    for ll in lol[l]:
        jobs[ll].start()
    jobs[ll].join()
'''


