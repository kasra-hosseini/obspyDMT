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
import copy
from datetime import datetime
import fileinput
import fnmatch
import glob
import math as math
import multiprocessing
from optparse import OptionParser
import os
import pickle
import random
import shutil
import sys
import tarfile
import time

############### obspy modules will be imported here
try:
    from obspy import __version__ as obs_ver
except Exception as error:
    print '---------------------------------------------------'
    print 'Have you properly installed ObsPy on your computer?'
    print 'Error: %s' % error
    print '---------------------------------------------------'
    sys.exit(2)

from obspy import read_inventory
from obspy.core import read, UTCDateTime
from obspy.signal import pazToFreqResp
from obspy.taup import taup
from obspy.xseed import Parser

# Required Clients from Obspy will be imported here.
from obspy.arclink import Client as Client_arclink
from obspy.fdsn import Client as Client_fdsn
############### END obspy modules

try:
    import smtplib
except Exception as error:
    print "\n********************************************************"
    print "Unable to import smtplib. Sending email is not possible!"
    print "Error: %s" % error
    print "********************************************************\n"


############### Fill in descrip list
descrip = ['obspy ver: ' + obs_ver]
try:
    from obspy.core.util import locations2degrees
except Exception as error:
    print "\n*************************************"
    print "ERROR: %s" % error
    print "*************************************\n"

import numpy as np
descrip.append('numpy ver: ' + np.__version__)
import scipy
descrip.append('scipy ver: ' + scipy.__version__)

# Import plotting modules:
try:
    from matplotlib import __version__ as mat_ver
    import matplotlib.pyplot as plt
    descrip.append('matplotlib ver: ' + mat_ver)
except Exception as error:
    descrip.append('matplotlib: not installed\n\nerror:\n%s\n' % error)

try:
    from mpl_toolkits.basemap import __version__ as base_ver
    from mpl_toolkits.basemap import Basemap
    descrip.append('Basemap ver: ' + base_ver)
except Exception as error:
    descrip.append('Basemap: not installed\n\nerror:\n%s\n'
                   'You could not use all the plot options' % error)
############### END Fill in descrip list

########################################################################
############################# Main Program #############################
########################################################################


def obspyDMT(**kwargs):
    """
    obspyDMT: is the function dedicated to the main part of the code.
    It organizes all the sub-main functions used in obspyDMT
    """

    print '\n' + 80*'-'
    print '\t\tobspyDMT (ObsPy Data Management Tool)\n'
    print '\tAutomatic tool for Downloading, Processing and Management'
    print '\t\t\tof Large Seismological Datasets\n'
    print ':copyright:'
    print 'The ObsPy Development Team (devs@obspy.org)\n'
    print 'Developed by Kasra Hosseini'
    print 'email: hosseini@geophysik.uni-muenchen.de\n'
    print ':license:'
    print 'GNU General Public License, Version 3'
    print '(http://www.gnu.org/licenses/gpl-3.0-standalone.html)'
    print 80*'-'

    # ------------------global variables-------------------
    global input, events

    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()

    # ------------------Read INPUT file (Parameters)--------------------
    read_input_command(parser, **kwargs)

    # ------------------plot stationxml files--------------------
    if input['plotxml_dir']:
        plot_xml_response(input)

    # ------------------Getting List of Events/Continuous requests------
    if input['get_events'] == 'Y':
        get_Events(input, request='event-based')

    if input['get_continuous'] == 'Y':
        get_Events(input, request='continuous')

    # ------------------Seismicity--------------------------------------
    if input['seismicity'] == 'Y':
        seismicity()

    # ------------------FDSN--------------------------------------------
    if input['FDSN'] == 'Y':
        print '\n********************************************************'
        print 'FDSN -- Download waveforms, StationXML files and meta-data'
        print '********************************************************'
        FDSN_network(input)

    # ------------------Arclink-----------------------------------------
    if input['ArcLink'] == 'Y':
        print '\n***********************************************************'
        print 'ArcLink -- Download waveforms, response files and meta-data'
        print '***********************************************************'
        ARC_network(input)

    # ------------------FDSN-Updating-----------------------------------
    if input['fdsn_update'] != 'N':
        print '\n*********************'
        print 'FDSN -- Updating Mode'
        print '*********************'
        FDSN_update(input, address=input['fdsn_update'])

    # ------------------ArcLink-Updating--------------------------------
    if input['arc_update'] != 'N':
        print '\n************************'
        print 'ArcLink -- Updating Mode'
        print '************************'
        ARC_update(input, address=input['arc_update'])

    # ------------------FDSN-instrument---------------------------------
    if input['fdsn_ic'] != 'N' or input['fdsn_ic_auto'] == 'Y':
        print '\n*****************************'
        print 'FDSN -- Instrument Correction'
        print '*****************************'
        create_tar_file_address = FDSN_ARC_IC(input,
                                              clients=input['fdsn_base_url'])

    # ------------------Arclink-instrument------------------------------
    if input['arc_ic'] != 'N' or input['arc_ic_auto'] == 'Y':
        print '\n********************************'
        print 'ArcLink -- Instrument Correction'
        print '********************************'
        create_tar_file_address = FDSN_ARC_IC(input, clients='arc')

    # ------------------FDSN-merge--------------------------------------
    if input['fdsn_merge'] != 'N' or input['fdsn_merge_auto'] == 'Y':
        print '\n*****************************'
        print 'FDSN -- Merging the waveforms'
        print '*****************************'
        FDSN_ARC_merge(input, clients=input['fdsn_base_url'])

    # ------------------ArcLink-merge-----------------------------------    
    if input['arc_merge'] != 'N' or input['arc_merge_auto'] == 'Y':
        print '\n********************************'
        print 'ArcLink -- Merging the waveforms'
        print '********************************'
        FDSN_ARC_merge(input, clients='arc')

    # ------------------plot_tools--------------------------------------------
    ls_plot_options = ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray',
                       'plot_ray_gmt', 'plot_epi', 'plot_dt']
    for plt_opt in ls_plot_options:
        if input[plt_opt] != 'N':
            print '\n********'
            print 'Plotting %s' % plt_opt
            print '********'
            if input['plot_all'] == 'Y' or input['plot_fdsn'] == 'Y':
                plot_tools(input, clients=input['fdsn_base_url'])
            if input['plot_arc'] == 'Y':
                plot_tools(input, clients='arc')

    if input['plot_all_events']:
        raw_input('\nPress enter to continue....\n')

    # ------------------Compressing-------------------------------------------
    if input['zip_w'] == 'Y' or input['zip_r'] == 'Y':
        print '\n**************************'
        print 'Start creating tar file(s)'
        print '**************************'
        create_tar_file(input, address=create_tar_file_address)

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

    helpmsg = "check all the dependencies and their installed versions on " \
              "the local machine and exit!"
    parser.add_option("--check", action="store_true",
                      dest="check", help=helpmsg)

    helpmsg = "run a quick tour!"
    parser.add_option("--tour", action="store_true",
                      dest="tour", help=helpmsg)

    helpmsg = "if the datapath is found deleting it before running obspyDMT."
    parser.add_option("--reset", action="store_true",
                      dest="reset", help=helpmsg)

    helpmsg = "the path where obspyDMT will store the data" \
              "[Default: './obspyDMT-data']"
    parser.add_option("--datapath", action="store",
                      dest="datapath", help=helpmsg)

    helpmsg = "consider the first phase arrival (P, Pdiff, PKIKP) to use " \
              "as the reference time, i.e. --min_date and --max_date will " \
              "be calculated from the first phase arrival."
    parser.add_option("--cut_time_phase", action="store_true",
                      dest="cut_time_phase", help=helpmsg)

    helpmsg = "start time, syntax: Y-M-D-H-M-S " \
              "(eg: '2010-01-01-00-00-00') or just " \
              "Y-M-D [Default: 10 days ago]"
    parser.add_option("--min_date", action="store",
                      dest="min_date", help=helpmsg)

    helpmsg = "end time, syntax: Y-M-D-H-M-S " \
              "(eg: '2011-01-01-00-00-00') or just " \
              "Y-M-D [Default: 5 days ago]"
    parser.add_option("--max_date", action="store",
                      dest="max_date", help=helpmsg)

    helpmsg = "event webservice (IRIS or NERIES). [Default: 'IRIS']"
    parser.add_option("--event_url", action="store",
                      dest="event_url", help=helpmsg)

    helpmsg = "event catalog (EMSC, GCMT, NEIC PDE, ISC). [Default: None]"
    parser.add_option("--event_catalog", action="store",
                      dest="event_catalog", help=helpmsg)

    helpmsg = "magnitude type. " \
              "Some common types (there are many) include " \
              "'Ml' (local/Richter magnitude), " \
              "'Ms' (surface magnitude), " \
              "'mb' (body wave magnitude), " \
              "'Mw' (moment magnitude). " \
              "[Default: 'Mw']"
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

    helpmsg = "search for all the events within the defined rectangle, " \
              "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax> " \
              "[Default: -180.0/+180.0/-90.0/+90.0]"
    parser.add_option("--event_rect", action="store",
                      dest="event_rect", help=helpmsg)

    helpmsg = "search for all the events within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "May not be used together with rectangular bounding box " \
              "event restrictions (event_rect)."
    parser.add_option("--event_circle", action="store",
                      dest="event_circle", help=helpmsg)

    helpmsg = "maximum number of events to be requested. [Default: 2500]"
    parser.add_option("--max_result", action="store",
                      dest="max_result", help=helpmsg)

    helpmsg = "just retrieve the event information and " \
              "create an event archive."
    parser.add_option("--event_info", action="store_true",
                      dest="event_info", help=helpmsg)

    helpmsg = "create a seismicity map according to " \
              "the event and location specifications."
    parser.add_option("--seismicity", action="store_true",
                      dest="seismicity", help=helpmsg)

    helpmsg = "Depth bins for plotting the seismicity histrogram. " \
              "[Default: 10]"
    parser.add_option("--depth_bins_seismicity", action="store",
                      dest="depth_bins_seismicity", help=helpmsg)

    helpmsg = "event-based request " \
              "(please refer to the tutorial). [Default: 'Y']"
    parser.add_option("--get_events", action="store",
                      dest="get_events", help=helpmsg)

    helpmsg = "continuous request (please refer to the tutorial)."
    parser.add_option("--continuous", action="store_true",
                      dest="get_continuous", help=helpmsg)

    helpmsg = "time interval for dividing the continuous request. " \
              "[Default: 86400 sec (1 day)]"
    parser.add_option("--interval", action="store",
                      dest="interval", help=helpmsg)

    helpmsg = "preset defined for EACH continuous request, i.e. time before " \
              "EACH interval (refer to '--interval' option) " \
              "in continuous request."
    parser.add_option("--preset_cont", action="store",
                      dest="preset_cont", help=helpmsg)

    helpmsg = "offset defined for EACH continuous request, i.e. time after " \
              "EACH interval (refer to '--interval' option) " \
              "in continuous request."
    parser.add_option("--offset_cont", action="store",
                      dest="offset_cont", help=helpmsg)

    helpmsg = "parallel waveform/response/paz request"
    parser.add_option("--req_parallel", action="store_true",
                      dest="req_parallel", help=helpmsg)

    helpmsg = "number of processors to be used in --req_parallel. [Default: 4]"
    parser.add_option("--req_np", action="store",
                      dest="req_np", help=helpmsg)

    helpmsg = "use a station list instead of checking the availability."
    parser.add_option("--list_stas", action="store",
                      dest="list_stas", help=helpmsg)

    helpmsg = "retrieve synthetic waveforms calculated by normal mode " \
              "summation code. (ShakeMovie project)"
    parser.add_option("--normal_mode_syn", action="store_true",
                      dest="normal_mode_syn", help=helpmsg)

    helpmsg = "retrieve synthetic waveforms of SPECFEM3D."
    parser.add_option("--specfem3D", action="store_true",
                      dest="specfem3D", help=helpmsg)

    helpmsg = "using the FDSN bulkdataselect Web service. " \
              "Since this method returns multiple channels of " \
              "time series data for specified time ranges in one request, " \
              "it speeds up the waveform retrieving approximately by " \
              "a factor of two. [RECOMMENDED]"
    parser.add_option("--fdsn_bulk", action="store_true",
                      dest="fdsn_bulk", help=helpmsg)

    helpmsg = "retrieve the waveform. [Default: 'Y']"
    parser.add_option("--waveform", action="store",
                      dest="waveform", help=helpmsg)

    helpmsg = "retrieve the response file. [Default: 'Y']"
    parser.add_option("--response", action="store",
                      dest="response", help=helpmsg)

    helpmsg = "retrieve the PAZ."
    parser.add_option("--paz", action="store_true",
                      dest="paz", help=helpmsg)

    helpmsg = "base_url for FDSN requests (waveform/response). " \
              "[Default: 'IRIS']"
    parser.add_option("--fdsn_base_url", action="store",
                      dest="fdsn_base_url", help=helpmsg)

    helpmsg = "username for FDSN requests (waveform/response). [Default: None]"
    parser.add_option("--fdsn_user", action="store",
                      dest="fdsn_user", help=helpmsg)

    helpmsg = "password for FDSN requests (waveform/response). [Default: None]"
    parser.add_option("--fdsn_pass", action="store",
                      dest="fdsn_pass", help=helpmsg)

    helpmsg = "send request (waveform/response) to ArcLink. [Default: 'N']"
    parser.add_option("--arc", action="store",
                      dest="ArcLink", help=helpmsg)

    helpmsg = "timeout for sending request (availability) to ArcLink. " \
              "[Default: 40]"
    parser.add_option("--arc_avai_timeout", action="store",
                      dest="arc_avai_timeout", help=helpmsg)

    helpmsg = "timeout for sending request (waveform/response) to ArcLink. " \
              "[Default: 2]"
    parser.add_option("--arc_wave_timeout", action="store",
                      dest="arc_wave_timeout", help=helpmsg)

    helpmsg = "SAC format for saving the waveforms. " \
              "Station location (stla and stlo), " \
              "station elevation (stel), " \
              "station depth (stdp), " \
              "event location (evla and evlo), " \
              "event depth (evdp) and " \
              "event magnitude (mag) " \
              "will be stored in the SAC headers. [Default: 'Y'] "
    parser.add_option("--SAC", action="store",
                      dest="SAC", help=helpmsg)

    helpmsg = "MSEED format for saving the waveforms."
    parser.add_option("--mseed", action="store_true",
                      dest="mseed", help=helpmsg)

    helpmsg = "generate a data-time file for a FDSN request. " \
              "This file shows the required time for each request and " \
              "the stored data in the folder."
    parser.add_option("--time_fdsn", action="store_true",
                      dest="time_fdsn", help=helpmsg)

    helpmsg = "generate a data-time file for an ArcLink request. " \
              "This file shows the required time for each request " \
              "and the stored data in the folder."
    parser.add_option("--time_arc", action="store_true",
                      dest="time_arc", help=helpmsg)

    helpmsg = "time parameter in seconds which determines " \
              "how close the time series data (waveform) will be cropped " \
              "before the origin time of the event. Default: 0.0 seconds."
    parser.add_option("--preset", action="store",
                      dest="preset", help=helpmsg)

    helpmsg = "time parameter in seconds which determines " \
              "how close the time series data (waveform) will be cropped " \
              "after the origin time of the event. Default: 1800.0 seconds."
    parser.add_option("--offset", action="store",
                      dest="offset", help=helpmsg)

    helpmsg = "identity code restriction, syntax: " \
              "net.sta.loc.cha (eg: TA.*.*.BHZ to search for " \
              "all BHZ channels in TA network). [Default: *.*.*.*]"
    parser.add_option("--identity", action="store",
                      dest="identity", help=helpmsg)

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

    helpmsg = "search for all the stations within the defined rectangle, " \
              "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax>. " \
              "May not be used together with circular bounding box station " \
              "restrictions (station_circle) " \
              "[Default: -180.0/+180.0/-90.0/+90.0]"
    parser.add_option("--station_rect", action="store",
                      dest="station_rect", help=helpmsg)

    helpmsg = "search for all the stations within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "May not be used together with rectangular bounding box " \
              "station restrictions (station_rect). Currently, " \
              "ArcLink does not support this option!"
    parser.add_option("--station_circle", action="store",
                      dest="station_circle", help=helpmsg)

    helpmsg = "test the program for the desired number of requests, " \
              "eg: '--test 10' will test the program for 10 " \
              "requests. [Default: 'N']"
    parser.add_option("--test", action="store",
                      dest="test", help=helpmsg)

    helpmsg = "update the specified folder for FDSN, " \
              "syntax: --fdsn_update address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--fdsn_update", action="store",
                      dest="fdsn_update", help=helpmsg)

    helpmsg = "update the specified folder for ArcLink, " \
              "syntax: --arc_update address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--arc_update", action="store",
                      dest="arc_update", help=helpmsg)

    helpmsg = "apply instrument correction to the specified folder for " \
              "downloaded waveforms from FDSN, " \
              "syntax: --fdsn_ic address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--fdsn_ic", action="store",
                      dest="fdsn_ic", help=helpmsg)

    helpmsg = "apply instrument correction to the specified folder for " \
              "downloaded waveforms from ArcLink, " \
              "syntax: --arc_ic address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--arc_ic", action="store",
                      dest="arc_ic", help=helpmsg)

    helpmsg = "apply instrument correction automatically " \
              "after downloading the waveforms from FDSN. [Default: 'Y']"
    parser.add_option("--fdsn_ic_auto", action="store",
                      dest="fdsn_ic_auto", help=helpmsg)

    helpmsg = "apply instrument correction automatically " \
              "after downloading the waveforms from ArcLink. [Default: 'Y']"
    parser.add_option("--arc_ic_auto", action="store",
                      dest="arc_ic_auto", help=helpmsg)

    helpmsg = "apply instrument correction to the specified folder for " \
              "all the waveforms (FDSN and ArcLink), " \
              "syntax: --ic_all address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--ic_all", action="store",
                      dest="ic_all", help=helpmsg)

    helpmsg = "do not apply instrument correction automatically. " \
              "This is equivalent to: \"--fdsn_ic_auto N --arc_ic_auto N\""
    parser.add_option("--ic_no", action="store_true",
                      dest="ic_no", help=helpmsg)

    helpmsg = "parallel Instrument Correction. "
    parser.add_option("--ic_parallel", action="store_true",
                      dest="ic_parallel", help=helpmsg)

    helpmsg = "number of processors to be used in --ic_parallel. [Default: 20]"
    parser.add_option("--ic_np", action="store",
                      dest="ic_np", help=helpmsg)

    helpmsg = "instrument Correction (full response), using obspy modules"
    parser.add_option("--ic_obspy_full", action="store",
                      dest="ic_obspy_full", help=helpmsg)

    helpmsg = "instrument Correction (full response), using SAC"
    parser.add_option("--ic_sac_full", action="store_true",
                      dest="ic_sac_full", help=helpmsg)

    helpmsg = "instrument Correction (Poles And Zeros), " \
              "using SAC (for FDSN) and obspy (for ArcLink)"
    parser.add_option("--ic_paz", action="store_true",
                      dest="ic_paz", help=helpmsg)

    helpmsg = "apply a bandpass filter to the data trace before " \
              "deconvolution ('None' if you do not need pre_filter), " \
              "syntax: '(f1,f2,f3,f4)' which " \
              "are the four corner frequencies " \
              "of a cosine taper, one between f2 and f3 and tapers to zero " \
              "for f1 < f < f2 and f3 < f < f4. " \
              "[Default: '(0.008, 0.012, 3.0, 4.0)']"
    parser.add_option("--pre_filt", action="store",
                      dest="pre_filt", help=helpmsg)

    helpmsg = "correct the raw waveforms for DIS (m), VEL (m/s) or " \
              "ACC (m/s^2). [Default: DIS]"
    parser.add_option("--corr_unit", action="store",
                      dest="corr_unit", help=helpmsg)

    helpmsg = "compress the raw-waveform files after " \
              "applying instrument correction."
    parser.add_option("--zip_w", action="store_true",
                      dest="zip_w", help=helpmsg)

    helpmsg = "compress the response files after " \
              "applying instrument correction."
    parser.add_option("--zip_r", action="store_true",
                      dest="zip_r", help=helpmsg)

    helpmsg = "merge the FDSN waveforms in the specified folder, " \
              "syntax: --fdsn_merge address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--fdsn_merge", action="store",
                      dest="fdsn_merge", help=helpmsg)

    helpmsg = "merge the ArcLink waveforms in the specified folder, " \
              "syntax: --arc_merge address_of_the_target_folder." \
              "[Default: 'N']"
    parser.add_option("--arc_merge", action="store",
                      dest="arc_merge", help=helpmsg)

    helpmsg = "merge automatically after downloading the waveforms " \
              "from FDSN. [Default: 'Y']"
    parser.add_option("--fdsn_merge_auto", action="store",
                      dest="fdsn_merge_auto", help=helpmsg)

    helpmsg = "merge automatically after downloading the waveforms " \
              "from ArcLink. [Default: 'Y']"
    parser.add_option("--arc_merge_auto", action="store",
                      dest="arc_merge_auto", help=helpmsg)

    helpmsg = "merge all waveforms (FDSN and ArcLink) in " \
              "the specified folder, " \
              "syntax: --merge_all address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--merge_all", action="store",
                      dest="merge_all", help=helpmsg)

    helpmsg = "do not merge automatically. This is equivalent to: " \
              "\"--fdsn_merge_auto N --arc_merge_auto N\""
    parser.add_option("--merge_no", action="store_true",
                      dest="merge_no", help=helpmsg)

    helpmsg = "merge 'raw' or 'corrected' waveforms. [Default: 'raw']"
    parser.add_option("--merge_type", action="store",
                      dest="merge_type", help=helpmsg)

    helpmsg = "plot waveforms downloaded from FDSN."
    parser.add_option("--plot_fdsn", action="store_true",
                      dest="plot_fdsn", help=helpmsg)

    helpmsg = "plot waveforms downloaded from ArcLink."
    parser.add_option("--plot_arc", action="store_true",
                      dest="plot_arc", help=helpmsg)

    helpmsg = "plot all waveforms (FDSN and ArcLink). [Default: 'Y']"
    parser.add_option("--plot_all", action="store",
                      dest="plot_all", help=helpmsg)

    helpmsg = "plot 'raw' or 'corrected' waveforms. [Default: 'raw']"
    parser.add_option("--plot_type", action="store",
                      dest="plot_type", help=helpmsg)

    helpmsg = "plot all the events, stations and ray path between them " \
              "found in the specified folder, " \
              "syntax: --plot_ray_gmt address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--plot_ray_gmt", action="store",
                      dest="plot_ray_gmt", help=helpmsg)

    helpmsg = "plot all the events found in the specified folder, " \
              "syntax: --plot_ev address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--plot_ev", action="store",
                      dest="plot_ev", help=helpmsg)

    helpmsg = "plot all the stations found in the specified folder, " \
              "syntax: --plot_sta address_of_the_target_folder. " \
              "[Default: 'N']"
    parser.add_option("--plot_sta", action="store",
                      dest="plot_sta", help=helpmsg)

    helpmsg = "plot both all the stations and all the events found " \
              "in the specified folder, " \
              "syntax: --plot_se address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--plot_se", action="store",
                      dest="plot_se", help=helpmsg)

    helpmsg = "plot the ray coverage for all the station-event pairs " \
              "found in the specified folder, " \
              "syntax: --plot_ray address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--plot_ray", action="store",
                      dest="plot_ray", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" for " \
              "all the waveforms found in the specified folder, " \
              "syntax: --plot_epi address_of_the_target_folder. [Default: 'N']"
    parser.add_option("--plot_epi", action="store",
                      dest="plot_epi", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" (refer to --plot_epi') " \
              "for all the waveforms with " \
              "epicentral-distance >= min_epi. [Default: 0.0]"
    parser.add_option("--min_epi", action="store",
                      dest="min_epi", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" " \
              "(refer to '--plot_epi') for all the waveforms with " \
              "epicentral-distance <= max_epi. [Default: 180.0]"
    parser.add_option("--max_epi", action="store",
                      dest="max_epi", help=helpmsg)

    helpmsg = "plot \"Data(MB)-Time(Sec)\" -- ATTENTION: " \
              "\"time_fdsn\" and/or \"time_arc\" should exist in the " \
              "\"info\" folder [refer to \"time_fdsn\" and " \
              "\"time_arc\" options] [Default: 'N']"
    parser.add_option("--plot_dt", action="store",
                      dest="plot_dt", help=helpmsg)

    helpmsg = "the path where obspyDMT will store the plots " \
              "[Default: '.' (the same directory as obspyDMT.py)]"
    parser.add_option("--plot_save", action="store",
                      dest="plot_save", help=helpmsg)

    helpmsg = "format of the plots saved on the local machine [Default: 'png']"
    parser.add_option("--plot_format", action="store",
                      dest="plot_format", help=helpmsg)

    helpmsg = "send an email to the specified email-address after " \
              "completing the job, syntax: --email email_address. " \
              "[Default: 'N']"
    parser.add_option("--email", action="store",
                      dest="email", help=helpmsg)

    helpmsg = "address of a file/directory that contains StationXML files. " \
              "[Default: False]"
    parser.add_option("--plotxml_dir", action="store",
                      dest="plotxml_dir", help=helpmsg)

    helpmsg = "datetime to be used for plotting the transfer function," \
              "syntax: Y-M-D-H-M-S (eg: '2011-01-01-00-00-00') or just " \
              "Y-M-D. If this is not set, the starting date of the " \
              "stationXML will be used instead!"
    parser.add_option("--plotxml_date", action="store",
                      dest="plotxml_date", help=helpmsg)

    helpmsg = "minimum frequency to be used for plotting the transfer " \
              "function. [Default: 0.01]"
    parser.add_option("--plotxml_min_freq", action="store",
                      dest="plotxml_min_freq", help=helpmsg)

    helpmsg = "output of the transfer function: DISP/VEL. [Default: VEL]"
    parser.add_option("--plotxml_output", action="store",
                      dest="plotxml_output", help=helpmsg)

    helpmsg = "start stage in response file to be considered for plotting " \
              "the transfer function. [Default: 1]"
    parser.add_option("--plotxml_start_stage", action="store",
                      dest="plotxml_start_stage", help=helpmsg)

    helpmsg = "final stage in response file to be considered for plotting " \
              "the transfer function. [Default: 100]"
    parser.add_option("--plotxml_end_stage", action="store",
                      dest="plotxml_end_stage", help=helpmsg)

    helpmsg = "whether or not use unwrap phase in plotting the transfer " \
              "function. [Default: True]"
    parser.add_option("--plotxml_unwrap_phase", action="store_true",
                      dest="plotxml_unwrap_phase", help=helpmsg)

    helpmsg = "percentage of the phase transfer function length to be used " \
              "for checking the difference between different methods, " \
              "e.g. 100 will be the whole transfer function, " \
              "80 means consider the transfer function from min_freq until " \
              "20 percent before the Nyquist frequency. [Default: 80]"
    parser.add_option("--plotxml_percentage", action="store",
                      dest="plotxml_percentage", help=helpmsg)

    helpmsg = "maximum allowable difference between two different methods of" \
              "instrument correction. This only applies to phase " \
              "difference. [Default: 0.1]"
    parser.add_option("--plotxml_phase_threshpld", action="store",
                      dest="plotxml_phase_threshold", help=helpmsg)

    helpmsg = "plot the full response file. [Default: True]"
    parser.add_option("--plotxml_response", action="store_true",
                      dest="plotxml_response", help=helpmsg)

    helpmsg = "plot only stage 1 and 2 of full response file. [Default: False]"
    parser.add_option("--plotxml_plotstage12", action="store_true",
                      dest="plotxml_plotstage12", help=helpmsg)

    helpmsg = "plot PAZ of the response file. [Default: False]"
    parser.add_option("--plotxml_paz", action="store_true",
                      dest="plotxml_paz", help=helpmsg)

    helpmsg = "plot all the stages available in the response file. " \
              "[Default: True]"
    parser.add_option("--plotxml_allstages", action="store_true",
                      dest="plotxml_allstages", help=helpmsg)

    helpmsg = "plot all the stations that have been compared in terms of " \
              "instrument response. [Default: False]"
    parser.add_option("--plotxml_map_compare", action="store_true",
                      dest="plotxml_map_compare", help=helpmsg)

    # parse command line options
    (options, args) = parser.parse_args()

    return options, args, parser

###################### read_input_command ##############################


def read_input_command(parser, **kwargs):
    """
    Create input object (dictionary) based on command-line options.
    The default values are as "input" object (below) 
    """
    global input, descrip

    # Defining the default values. 
    # Each of these values could be changed
    # by defining the required command-line flag (if you use 
    # "'./obspyDMT.py --type command'")
    input = {'datapath': 'obspyDMT-data',
             'min_date': str(UTCDateTime() - 60 * 60 * 24 * 10 * 1),
             'max_date': str(UTCDateTime() - 60 * 60 * 24 * 5 * 1),
             'event_url': 'IRIS',
             'event_catalog': None,
             'mag_type': 'Mw',
             'min_mag': 5.5, 'max_mag': 9.9,
             'min_depth': +10.0, 'max_depth': -6000.0,
             'get_events': 'Y',
             'interval': 3600*24,
             'preset_cont': 0,
             'offset_cont': 0,
             'req_np': 4,
             'list_stas': False,
             'waveform': 'Y', 'response': 'Y',
             'FDSN': 'Y', 'ArcLink': 'N',
             'fdsn_base_url': 'IRIS',
             'fdsn_user': None,
             'fdsn_pass': None,
             'arc_avai_timeout': 40,
             'arc_wave_timeout': 2,
             'neries_timeout': 2,
             'SAC': 'Y',
             'preset': 0.0, 'offset': 1800.0,
             'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
             'evlatmin': None, 'evlatmax': None,
             'evlonmin': None, 'evlonmax': None,
             'evlat': None, 'evlon': None,
             'evradmin': None, 'evradmax': None,
             'max_result': 2500,
             'depth_bins_seismicity': 10,
             'lat_cba': None, 'lon_cba': None,
             'mr_cba': None, 'Mr_cba': None,
             'mlat_rbb': None, 'Mlat_rbb': None,
             'mlon_rbb': None, 'Mlon_rbb': None,
             'test': 'N',
             'fdsn_update': 'N', 'arc_update': 'N', 'update_all': 'N',
             'email': 'N',
             'ic_all': 'N',
             'fdsn_ic': 'N', 'fdsn_ic_auto': 'Y',
             'arc_ic': 'N', 'arc_ic_auto': 'Y',
             'ic_np': 4,
             'ic_obspy_full': 'Y',
             'pre_filt': '(0.008, 0.012, 3.0, 4.0)',
             'corr_unit': 'DIS',
             'merge_all': 'N',
             'fdsn_merge': 'N', 'fdsn_merge_auto': 'Y',
             'merge_type': 'raw',
             'arc_merge': 'N', 'arc_merge_auto': 'Y',
             'plot_all': 'Y',
             'plot_type': 'raw',
             'plot_ev': 'N', 'plot_sta': 'N', 'plot_se': 'N',
             'plot_ray': 'N', 'plot_epi': 'N', 'plot_dt': 'N',
             'plot_ray_gmt': 'N',
             'plot_save': '.', 'plot_format': 'png',
             'min_epi': 0.0, 'max_epi': 180.0,
             'plotxml_dir': False,
             'plotxml_date': False,
             'plotxml_min_freq': 0.01,
             'plotxml_output': 'VEL',
             'plotxml_start_stage': 1,
             'plotxml_end_stage': 100,
             'plotxml_unwrap_phase': True,
             'plotxml_percentage': 80,
             'plotxml_phase_threshold': 0.1,
             'plotxml_response': True,
             'plotxml_plotstage12': False,
             'plotxml_paz': False,
             'plotxml_allstages': True,
             'plotxml_map_compare': False
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
            exec "options.%s = kwargs[arg]" % arg

    if options.version:
        print '\n\t\t' + '*********************************'
        print '\t\t' + '*        obspyDMT version:      *'
        print '\t\t' + '*' + '\t\t' + '0.7.6' + '\t\t' + '*'
        print '\t\t' + '*********************************'
        print '\n'
        sys.exit(2)

    # Check whether it is possible to import all required modules
    if options.check:
        print "*********************************"
        print "Check all the BASIC dependencies:"
        for i in range(len(descrip)):
            print descrip[i]
        print "*********************************\n"
        sys.exit(2)

    if options.tour:
        print '\n########################################'
        print 'obspyDMT Quick Tour will start in 2 sec!'
        print '########################################\n'
        time.sleep(2)
        options.datapath = './dmt-tour-data'
        options.min_date = '2011-03-10'
        options.max_date = '2011-03-12'
        options.min_mag = '8.9'
        options.identity = 'TA.1*.*.BHZ'
        options.event_url = 'IRIS'
        options.event_catalog = None
        options.req_parallel = True
        options.ArcLink = 'N'

    #############Parse paths and make sure that they are all absolute path
    if options.datapath and not os.path.isabs(options.datapath):
        options.datapath = os.path.join(os.getcwd(), options.datapath)

    if options.fdsn_update != 'N' and not os.path.isabs(options.fdsn_update):
        options.fdsn_update = os.path.join(os.getcwd(), options.fdsn_update)

    if options.arc_update != 'N' and not os.path.isabs(options.arc_update):
        options.arc_update = os.path.join(os.getcwd(), options.arc_update)

    if options.update_all != 'N' and not os.path.isabs(options.update_all):
        options.update_all = os.path.join(os.getcwd(), options.update_all)

    if options.fdsn_ic != 'N' and not os.path.isabs(options.fdsn_ic):
        options.fdsn_ic = os.path.join(os.getcwd(), options.fdsn_ic)

    if options.arc_ic != 'N' and not os.path.isabs(options.arc_ic):
        options.arc_ic = os.path.join(os.getcwd(), options.arc_ic)

    if options.ic_all != 'N' and not os.path.isabs(options.ic_all):
        options.ic_all = os.path.join(os.getcwd(), options.ic_all)

    if options.fdsn_merge != 'N' and not os.path.isabs(options.fdsn_merge):
        options.fdsn_merge = os.path.join(os.getcwd(), options.fdsn_merge)

    if options.arc_merge != 'N' and not os.path.isabs(options.arc_merge):
        options.arc_merge = os.path.join(os.getcwd(), options.arc_merge)

    if options.merge_all != 'N' and not os.path.isabs(options.merge_all):
        options.merge_all = os.path.join(os.getcwd(), options.merge_all)

    if options.plot_ev != 'N' and not os.path.isabs(options.plot_ev):
        options.plot_ev = os.path.join(os.getcwd(), options.plot_ev)

    if options.plot_sta != 'N' and not os.path.isabs(options.plot_sta):
        options.plot_sta = os.path.join(os.getcwd(), options.plot_sta)

    if options.plot_se != 'N' and not os.path.isabs(options.plot_se):
        options.plot_se = os.path.join(os.getcwd(), options.plot_se)

    if options.plot_ray != 'N' and not os.path.isabs(options.plot_ray):
        options.plot_ray = os.path.join(os.getcwd(), options.plot_ray)

    if options.plot_ray_gmt != 'N' and not os.path.isabs(options.plot_ray_gmt):
        options.plot_ray_gmt = os.path.join(os.getcwd(), options.plot_ray_gmt)

    if options.plot_epi != 'N' and not os.path.isabs(options.plot_epi):
        options.plot_epi = os.path.join(os.getcwd(), options.plot_epi)

    if options.plot_dt != 'N' and not os.path.isabs(options.plot_dt):
        options.plot_dt = os.path.join(os.getcwd(), options.plot_dt)

    if options.plot_save != 'N' and not os.path.isabs(options.plot_save):
        options.plot_save = os.path.join(os.getcwd(), options.plot_save)

    if options.plotxml_dir and not os.path.isabs(options.plotxml_dir):
        options.plotxml_dir = os.path.join(os.getcwd(), options.plotxml_dir)
    #############END Parse paths

    # extract min. and max. longitude and latitude for event
    # if the user has given the coordinates with -r (GMT syntax)
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
        except Exception, e:
            print "Erroneous rectangle given: %s" % e
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
        except Exception, e:
            print "Erroneous circle given: %s" % e
            sys.exit(2)

    # extract min. and max. longitude and latitude for station
    # if the user has given the coordinates with -g (GMT syntax)
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
        except Exception, e:
            print "Erroneous rectangle given: %s" % e
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
        except Exception, e:
            print "Erroneous circle given: %s" % e
            sys.exit(2)

    # delete data path if -R or --reset args are given at cmdline
    if options.reset:
        # try-except so we don't get an exception if path doesnt exist
        try:
            shutil.rmtree(options.datapath)
            print '\n-------------------------------'
            print 'Delete the following directory:'
            print str(options.datapath)
            print 'obspyDMT is going to re-create it...'
            print '-------------------------------\n\n'
        except Exception, e:
            print "Warning: can not remove the following directory: %s" % e
            pass

    # Extract network, station, location, channel if the user has given an
    # identity code (-i xx.xx.xx.xx)
    if options.identity:
        try:
            options.net, options.sta, options.loc, options.cha = \
                options.identity.split('.')
        except Exception, e:
            print "Erroneous identity code given: %s" % e
            sys.exit(2)

    input['plotxml_dir'] = options.plotxml_dir
    if options.plotxml_date:
        input['plotxml_date'] = UTCDateTime(options.plotxml_date)
    else:
        input['plotxml_date'] = options.plotxml_date
    input['plotxml_min_freq'] = float(options.plotxml_min_freq)
    input['plotxml_output'] = options.plotxml_output
    input['plotxml_start_stage'] = int(options.plotxml_start_stage)
    input['plotxml_end_stage'] = int(options.plotxml_end_stage)
    input['plotxml_unwrap_phase'] = options.plotxml_unwrap_phase
    input['plotxml_percentage'] = float(options.plotxml_percentage)
    input['plotxml_phase_threshold'] = float(options.plotxml_phase_threshold)
    input['plotxml_response'] = options.plotxml_response
    input['plotxml_plotstage12'] = options.plotxml_plotstage12
    input['plotxml_paz'] = options.plotxml_paz
    input['plotxml_allstages'] = options.plotxml_allstages
    input['plotxml_map_compare'] = options.plotxml_map_compare

    input['datapath'] = options.datapath
    if options.cut_time_phase:
        input['cut_time_phase'] = True
    else:
        input['cut_time_phase'] = False
    input['min_date'] = str(UTCDateTime(options.min_date))
    input['max_date'] = str(UTCDateTime(options.max_date))
    input['event_url'] = options.event_url.upper()
    if options.event_catalog:
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
    input['depth_bins_seismicity'] = int(options.depth_bins_seismicity)
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
    input['preset_cont'] = float(options.preset_cont)
    input['offset_cont'] = float(options.offset_cont)
    if options.req_parallel:
        options.req_parallel = 'Y'
    input['req_parallel'] = options.req_parallel
    input['req_np'] = int(options.req_np)
    input['list_stas'] = options.list_stas
    if options.fdsn_bulk:
        options.fdsn_bulk = 'Y'
    input['fdsn_bulk'] = options.fdsn_bulk
    if options.specfem3D:
        options.specfem3D = 'Y'
    input['specfem3D'] = options.specfem3D
    if options.normal_mode_syn:
        options.normal_mode_syn = 'Y'
    input['normal_mode_syn'] = options.normal_mode_syn
    input['waveform'] = options.waveform
    input['response'] = options.response
    if options.paz:
        options.paz = 'Y'
    input['paz'] = options.paz
    input['SAC'] = options.SAC
    if options.mseed:
        input['SAC'] = 'N'
        input['mseed'] = 'Y'
    else:
        input['mseed'] = 'N'
    input['FDSN'] = options.FDSN
    input['fdsn_base_url'] = options.fdsn_base_url
    input['fdsn_user'] = options.fdsn_user
    input['fdsn_pass'] = options.fdsn_pass
    input['ArcLink'] = options.ArcLink

    input['arc_avai_timeout'] = float(options.arc_avai_timeout)
    input['arc_wave_timeout'] = float(options.arc_wave_timeout)
    input['neries_timeout'] = float(options.neries_timeout)

    if options.time_fdsn:
        options.time_fdsn = 'Y'
    input['time_fdsn'] = options.time_fdsn
    if options.time_arc:
        options.time_arc = 'Y'
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
    input['fdsn_update'] = options.fdsn_update
    input['arc_update'] = options.arc_update
    input['update_all'] = options.update_all
    if input['update_all'] != 'N':
        input['fdsn_update'] = input['update_all']
        input['arc_update'] = input['update_all']
    input['fdsn_ic'] = options.fdsn_ic
    input['fdsn_ic_auto'] = options.fdsn_ic_auto
    input['arc_ic'] = options.arc_ic
    input['arc_ic_auto'] = options.arc_ic_auto
    input['ic_all'] = options.ic_all
    if input['ic_all'] != 'N':
        input['fdsn_ic'] = input['ic_all']
        input['arc_ic'] = input['ic_all']
    if options.ic_parallel:
        options.ic_parallel = 'Y'
    input['ic_parallel'] = options.ic_parallel
    input['ic_np'] = int(options.ic_np)
    input['ic_obspy_full'] = options.ic_obspy_full
    if options.ic_sac_full:
        options.ic_sac_full = 'Y'
    input['ic_sac_full'] = options.ic_sac_full
    if options.ic_paz:
        options.ic_paz = 'Y'
    input['ic_paz'] = options.ic_paz
    if input['ic_sac_full'] == 'Y' or input['ic_paz'] == 'Y':
        input['SAC'] = 'Y'
        input['ic_obspy_full'] = 'N'
    input['corr_unit'] = options.corr_unit
    input['pre_filt'] = options.pre_filt
    if options.zip_w:
        options.zip_w = 'Y'
    input['zip_w'] = options.zip_w
    if options.zip_r:
        options.zip_r = 'Y'
    input['zip_r'] = options.zip_r
    input['fdsn_merge'] = options.fdsn_merge
    input['arc_merge'] = options.arc_merge
    input['merge_all'] = options.merge_all
    if input['merge_all'] != 'N':
        input['fdsn_merge'] = input['merge_all']
        input['arc_merge'] = input['merge_all']
    input['plot_type'] = options.plot_type
    input['plot_all'] = options.plot_all
    if options.plot_fdsn:
        options.plot_fdsn = 'Y'
    input['plot_fdsn'] = options.plot_fdsn
    if options.plot_arc:
        options.plot_arc = 'Y'
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

    #--------------Changing relevant options for some specific options
    if input['get_continuous'] == 'N':
        input['fdsn_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
    else:
        input['fdsn_merge_auto'] = options.fdsn_merge_auto
        input['arc_merge_auto'] = options.arc_merge_auto
        input['merge_type'] = options.merge_type

    for opts in ['fdsn_update', 'arc_update', 'fdsn_ic', 'arc_ic',
                 'fdsn_merge', 'arc_merge',
                 'plot_se', 'plot_sta', 'plot_ev', 'plot_ray',
                 'plot_ray_gmt', 'plot_epi', 'plot_dt']:
        if input[opts] != 'N':
            input['datapath'] = input[opts]
            input['get_events'] = 'N'
            input['get_continuous'] = 'N'
            input['FDSN'] = 'N'
            input['ArcLink'] = 'N'
            input['fdsn_ic_auto'] = 'N'
            input['arc_ic_auto'] = 'N'
            input['fdsn_merge_auto'] = 'N'
            input['arc_merge_auto'] = 'N'

    if options.event_info:
        input['FDSN'] = 'N'
        input['ArcLink'] = 'N'
        input['fdsn_ic_auto'] = 'N'
        input['arc_ic_auto'] = 'N'
        input['fdsn_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
        input['plot_all_events'] = True
    else:
        input['plot_all_events'] = False

    if options.seismicity:
        input['FDSN'] = 'N'
        input['ArcLink'] = 'N'
        input['fdsn_ic_auto'] = 'N'
        input['arc_ic_auto'] = 'N'
        input['fdsn_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'
        input['max_result'] = 1000000

    if options.FDSN == 'N':
        input['fdsn_ic_auto'] = 'N'
        input['fdsn_merge_auto'] = 'N'

    if options.ArcLink == 'N':
        input['arc_ic_auto'] = 'N'
        input['arc_merge_auto'] = 'N'

    if options.ic_no:
        input['fdsn_ic_auto'] = 'N'
        input['arc_ic_auto'] = 'N'

    if options.merge_no:
        input['fdsn_merge_auto'] = 'N'
        input['arc_merge_auto'] = 'N'

    if input['plot_fdsn'] == 'Y' or input['plot_arc'] == 'Y':
        input['plot_all'] = 'N'

    # Create a priority list (for all requested clients)
    # For the moment, we just support: FDSN and ArcLink, but it should be
    # easily extendable!
    input['priority_clients'] = []
    for cli in ['FDSN', 'ArcLink']:
        if input[cli] == 'Y':
            input['priority_clients'].append(cli)

###################### plot_xml_response ###############################


def plot_xml_response(input):
    """
    This function plots the response file of stationXML file(s)
    It has several modes such as:
    plotting all the stages
    plotting full response file
    plotting selected stages
    plotting only PAZ
    :param input:
    :return:
    """

    print '[INFO] plotting StationXML file/files in: %s' % input['plotxml_dir']
    print '[INFO] stationxml_plots dir will be created!'

    # Assgin the input parameters to the running parameters in this function:
    stxml_dir = input['plotxml_dir']
    plotxml_datetime = input['plotxml_date']
    min_freq = input['plotxml_min_freq']
    output = input['plotxml_output']
    start_stage = input['plotxml_start_stage']
    end_stage = input['plotxml_end_stage']
    unwrap_phase = input['plotxml_unwrap_phase']
    percentage = input['plotxml_percentage']/100.
    threshold = input['plotxml_phase_threshold']
    plot_response = input['plotxml_response']
    plotstage12 = input['plotxml_plotstage12']
    plotpaz = input['plotxml_paz']
    plotallstages = input['plotxml_allstages']
    plot_map_compare = input['plotxml_map_compare']

    if os.path.isfile(stxml_dir):
        addxml_all = glob.glob(os.path.join(stxml_dir))
    elif os.path.isdir(stxml_dir):
        addxml_all = glob.glob(os.path.join(stxml_dir, 'STXML.*'))
    else:
        sys.exit('[ERROR] wrong address: %s' % stxml_dir)

    lat_good = []
    lon_good = []
    lat_bad = []
    lon_bad = []
    for addxml in addxml_all:
        try:
            xml_inv = read_inventory(addxml, format='stationXML')
            cha_name = xml_inv.get_contents()['channels'][0]
            if plotxml_datetime:
                cha_date = plotxml_datetime
            else:
                print '[INFO] plotxml_date has not been set, the start_date ' \
                      'of stationXML file will be used instead!'
                cha_date = xml_inv.networks[0][0][0].start_date

            xml_response = xml_inv.get_response(cha_name, cha_date)
            for stage in xml_response.response_stages[::-1]:
                if (stage.decimation_input_sample_rate is not None
                        and stage.decimation_factor is not None):
                    sampling_rate = (stage.decimation_input_sample_rate /
                                     stage.decimation_factor)
                    break

            t_samp = 1.0 / sampling_rate
            nyquist = sampling_rate / 2.0
            nfft = int(sampling_rate / min_freq)

            if plotallstages:
                plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft,
                                       min_freq, output,
                                       start_stage, end_stage, unwrap_phase,
                                       cha_name)

            try:
                cpx_response, freq = xml_response.get_evalresp_response(
                    t_samp=t_samp, nfft=nfft, output=output,
                    start_stage=start_stage, end_stage=end_stage)
                cpx_paz, freq = xml_response.get_evalresp_response(
                    t_samp=t_samp, nfft=nfft, output=output, start_stage=1,
                    end_stage=2)
            except:
                continue

            paz = convert_xml_paz(xml_response, output)

            h, f = pazToFreqResp(paz['poles'], paz['zeros'], paz['gain'],
                                 1./sampling_rate, nfft, freq=True)

            phase_resp = np.angle(cpx_response)
            if unwrap_phase:
                phase_resp = np.unwrap(phase_resp)
            phase_paz = np.angle(cpx_paz)
            if unwrap_phase:
                phase_paz = np.unwrap(phase_paz)

            if plot_response:
                if not os.path.isdir('./stationxml_plots'):
                    print '[INFO] creating stationxml_plots directory...',
                    os.mkdir('./stationxml_plots')
                    print 'DONE'
                plt.close()
                plt.ion()
                plt.figure(figsize=(20, 10))
                plt.suptitle(cha_name, size=24, weight='bold')
                plt.subplot(2, 2, 1)
                plt.loglog(freq, abs(cpx_response), color='blue',
                           lw=3, label='full-resp')
                if plotstage12:
                    plt.loglog(freq, abs(cpx_paz), ls='--', color='black',
                               lw=3, label='Stage1,2')
                if plotpaz:
                    plt.loglog(f, abs(h)*paz['sensitivity'], color='red',
                               lw=3, label='PAZ')
                plt.axvline(nyquist, ls="--", color='blue', lw=3)
                plt.ylabel('Amplitude', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.ylim(ymax=max(abs(cpx_response))+10e9)
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()

                plt.subplot(2, 2, 3)
                plt.semilogx(freq, phase_resp, color='blue',
                             lw=3, label='full-resp')
                if plotstage12:
                    plt.semilogx(freq, phase_paz, ls='--', color='black',
                                 lw=3, label='Stage1,2')
                if plotpaz:
                    plt.semilogx(f, np.angle(h), color='red',
                                 lw=3, label='PAZ')
                plt.axvline(nyquist, ls="--", color='blue', lw=3)
                plt.xlabel('Frequency [Hz]', size=24, weight='bold')
                plt.ylabel('Phase [rad]', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()

                plt.subplot(2, 2, 2)
                if plotstage12:
                    plt.loglog(freq, abs(abs(cpx_response) - abs(cpx_paz)),
                               '--', color='black', lw=3,
                               label='|full-resp - Stage1,2|')

                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                if plotpaz:
                    plt.loglog(f, abs(abs(cpx_response) -
                                      abs(h)*paz['sensitivity']),
                               color='red', lw=3, label='|full-resp - PAZ|')
                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                plt.ylabel('Amplitude Difference', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.ylim(ymax=max(abs(cpx_response))+10e9)
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()

                plt.subplot(2, 2, 4)
                if plotstage12:
                    plt.semilogx(freq, abs(phase_resp - phase_paz),
                                 color='black', ls='--', lw=3,
                                 label='|full-resp - Stage1,2|')
                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                if plotpaz:
                    plt.semilogx(freq, abs(phase_resp - np.angle(h)),
                                 color='red', lw=3,
                                 label='|full-resp - PAZ|')
                    plt.axvline(nyquist, ls="--", color='blue', lw=3)
                    plt.axvline(percentage*nyquist, ls="--",
                                color='blue', lw=3)
                plt.xlabel('Frequency [Hz]', size=24, weight='bold')
                plt.ylabel('Phase Difference [rad]', size=24, weight='bold')
                plt.xticks(size=18, weight='bold')
                plt.yticks(size=18, weight='bold')
                plt.xlim(xmin=min_freq, xmax=nyquist+5)
                plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
                plt.grid()
                plt.savefig(os.path.join('stationxml_plots', cha_name + '.png'))

            #compare = abs(phase[:int(0.8*len(phase))] -
            #              np.angle(h[:int(0.8*len(phase))]))
            #if len(compare[compare>0.1]) > 0:
            #    lat_red.append(xml_inv.get_coordinates(cha_name)['latitude'])
            #    lon_red.append(xml_inv.get_coordinates(cha_name)['longitude'])
            #    print cha_name
            #    print paz
            #else:
            #    lat_blue.append(xml_inv.get_coordinates(cha_name)['latitude'])
            #    lon_blue.append(xml_inv.get_coordinates(cha_name)['longitude'])

            compare = abs(phase_resp[:int(percentage*len(phase_resp))] -
                          phase_paz[:int(percentage*len(phase_paz))])
            if len(compare[compare > threshold]) > 0:
                lat_bad.append(xml_inv.get_coordinates(cha_name)['latitude'])
                lon_bad.append(xml_inv.get_coordinates(cha_name)['longitude'])
                print cha_name
            else:
                lat_good.append(xml_inv.get_coordinates(cha_name)['latitude'])
                lon_good.append(xml_inv.get_coordinates(cha_name)['longitude'])
        except Exception, e:
            print 'Exception: %s' % e

    if plot_map_compare:
        m = Basemap(projection='cyl', lon_0=0, lat_0=0, resolution='l')
        #m.drawcoastlines()
        m.fillcontinents()
        m.drawparallels(np.arange(-90., 120., 30.))
        m.drawmeridians(np.arange(0., 420., 60.))
        m.drawmapboundary()

        x_bad, y_bad = m(lon_bad, lat_bad)
        m.scatter(x_bad, y_bad, 100, color='red', marker="v",
                  edgecolor=None, zorder=10)

        x_good, y_good = m(lon_good, lat_good)
        m.scatter(x_good, y_good, 100, color='blue', marker="v",
                  edgecolor=None, zorder=10)
        plt.show()
    sys.exit('[EXIT] obspyDMT finished normally...')

###################### plot_xml_plotallstages ##########################


def plot_xml_plotallstages(xml_response, t_samp, nyquist, nfft, min_freq,
                           output, start_stage, end_stage, unwrap_phase,
                           cha_name):
    """
    plot all the stages in a StationXML file.
    This is controlled by start_stage and end_stage
    :param xml_response:
    :param t_samp:
    :param nyquist:
    :param nfft:
    :param min_freq:
    :param output:
    :param start_stage:
    :param end_stage:
    :param unwrap_phase:
    :param cha_name:
    :return:
    """

    if not os.path.isdir('./stationxml_plots'):
        print '[INFO] creating stationxml_plots directory...',
        os.mkdir('./stationxml_plots')
        print 'DONE'
    plt.close()
    plt.ion()
    plt.figure(figsize=(20, 10))
    plt.suptitle(cha_name, size=24, weight='bold')
    for i in range(start_stage, end_stage+1):
        try:
            cpx_response, freq = xml_response.get_evalresp_response(
                t_samp=t_samp, nfft=nfft, output=output,
                start_stage=i, end_stage=i)
        except:
            continue
    
        try:
            inp = xml_response.response_stages[i].input_units
        except Exception, e:
            inp = ''
        try:
            out = xml_response.response_stages[i].output_units
        except Exception, e:
            out = ''
    
        phase_resp = np.angle(cpx_response)
        if unwrap_phase:
            phase_resp = np.unwrap(phase_resp)
    
        plt.subplot(2, 1, 1)
        plt.loglog(freq, abs(cpx_response), lw=3,
                   label='%s (%s->%s)' % (i, inp, out))
        plt.axvline(nyquist, ls="--", color='blue', lw=3)
        plt.ylabel('Amplitude', size=24, weight='bold')
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.xlim(xmin=min_freq, xmax=nyquist+5)
        plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.semilogx(freq, phase_resp, lw=3,
                     label='%s (%s->%s)' % (i, inp, out))
        plt.axvline(nyquist, ls="--", color='blue', lw=3)
        plt.xlabel('Frequency [Hz]', size=24, weight='bold')
        plt.ylabel('Phase [rad]', size=24, weight='bold')
        plt.xticks(size=18, weight='bold')
        plt.yticks(size=18, weight='bold')
        plt.xlim(xmin=min_freq, xmax=nyquist+5)
        plt.legend(loc=0, prop={'size': 18, 'weight': 'bold'})
        plt.grid()
    plt.savefig(os.path.join('stationxml_plots',
                             '%s_stages.png' % cha_name))

###################### convert_xml_paz ######################################


def convert_xml_paz(xml_response, output):
    """
    convert Stationxml file into PAZ dictionary
    :param xml_response:
    :param output:
    :return: paz
    """
    gain_arr = []
    normalization_factor = []
    poles = []
    zeros = []
    for resp_stage in xml_response.response_stages:
        gain_arr.append(resp_stage.stage_gain)
        try:
            normalization_factor.append(
                resp_stage.normalization_factor)
        except Exception as e:
            pass
        try:
            poles.append(resp_stage.poles)
            zeros.append(resp_stage.zeros)
        except Exception as e:
            pass

    paz = {}
    paz['poles'] = poles[0]
    if output.lower() == 'disp':
        zeros[0].append(0j)
    if output.lower() == 'acc':
        sys.exit('%s output has not implemented!' % output)
    paz['zeros'] = zeros[0]
    paz['gain'] = np.prod(np.array(normalization_factor))
    paz['sensitivity'] = np.prod(np.array(gain_arr))
    return paz

###################### get_Events ######################################


def get_Events(input, request):
    """
    Getting list of events from IRIS or NERIES...
    """
    global events

    t_event_1 = datetime.now()
    period = '{0:s}_{1:s}_{2:s}_{3:s}'.format(input['min_date'].split('T')[0],
                                              input['max_date'].split('T')[0],
                                              str(input['min_mag']),
                                              str(input['max_mag']))
    eventpath = os.path.join(input['datapath'], period)
    if os.path.exists(eventpath):
        print '\n\n********************************************************'
        if raw_input('Directory for the requested period already exists:'
                     '\n%s\n\nOptions:\nN: Close the program and try '
                     'the updating mode.\nY: Remove the tree, continue the '
                     'program and re-download.\n' % eventpath).upper() == 'Y':
            print '********************************************************'
            shutil.rmtree(eventpath)
            os.makedirs(eventpath)
        else:
            sys.exit('Exit the program...')
    else:
        os.makedirs(eventpath)

    # request can be 'event-based' or continuous
    events = events_info(request)

    os.makedirs(os.path.join(eventpath, 'EVENTS-INFO'))
    # logging the command line
    input_logger(argus=sys.argv,
                 address=os.path.join(eventpath, 'EVENTS-INFO', 'logger.txt'),
                 inputs=input)

    for i in range(len(events)):
        print "-------------------------------------------------"
        print "Event No: %s" % (i+1)
        print "Date Time: %s" % events[i]['datetime']
        print "Catalog: %s" % events[i]['author']
        print "Depth: %s" % events[i]['depth']
        print "Event-ID: %s" % events[i]['event_id']
        try:
            print "Flynn-Region: %s" % events[i]['flynn_region']
        except Exception, e:
            print "Flynn-Region: NONE"
        print "Latitude: %s" % events[i]['latitude']
        print "Longitude: %s" % events[i]['longitude']
        print "Magnitude: %s" % events[i]['magnitude']
    print "-------------------------------------------------"

    Event_cat = open(os.path.join(eventpath, 'EVENTS-INFO',
                                  'EVENT-CATALOG'), 'a+')
    Event_cat.writelines(str(period) + '\n')
    Event_cat.writelines('-------------------------------------' + '\n')
    Event_cat.writelines('Information about the requested Events:' + '\n\n')
    Event_cat.writelines('Number of Events: %s\n' % len(events))
    Event_cat.writelines('min datetime: %s\n' % input['min_date'])
    Event_cat.writelines('max datetime: %s\n' % input['max_date'])
    Event_cat.writelines('min magnitude: %s\n' % input['min_mag'])
    Event_cat.writelines('max magnitude: %s\n' % input['max_mag'])
    Event_cat.writelines('min latitude: %s\n' % input['evlatmin'])
    Event_cat.writelines('max latitude: %s\n' % input['evlatmax'])
    Event_cat.writelines('min longitude: %s\n' % input['evlonmin'])
    Event_cat.writelines('max longitude: %s\n' % input['evlonmax'])
    Event_cat.writelines('min depth: %s\n' % input['min_depth'])
    Event_cat.writelines('max depth: %s\n' % input['max_depth'])
    Event_cat.writelines('-------------------------------------' + '\n\n')
    Event_cat.close()

    for i in range(len(events)):
        Event_cat = open(os.path.join(eventpath, 'EVENTS-INFO',
                                      'EVENT-CATALOG'), 'a')
        Event_cat.writelines("Event No: %s\n" % i)
        Event_cat.writelines("Catalog: %s\n" % events[i]['author'])
        Event_cat.writelines("Event-ID: %s\n" % events[i]['event_id'])
        Event_cat.writelines("Date Time: %s\n" % events[i]['datetime'])
        Event_cat.writelines("Magnitude: %s\n" % events[i]['magnitude'])
        Event_cat.writelines("Depth: %s\n" % events[i]['depth'])
        Event_cat.writelines("Latitude: %s\n" % events[i]['latitude'])
        Event_cat.writelines("Longitude: %s\n" % events[i]['longitude'])
        try:
            Event_cat.writelines("Flynn-Region: %s\n"
                                 % events[i]['flynn_region'])
        except Exception:
            Event_cat.writelines("Flynn-Region: None\n")
        Event_cat.writelines('-------------------------------------' + '\n')
        Event_cat.close()
    Event_file = open(os.path.join(eventpath, 'EVENTS-INFO',
                                   'event_list'), 'a+')
    pickle.dump(events, Event_file)
    Event_file.close()

    print 'Number of events: %s' % len(events)
    print 'Time for retrieving and saving the event info: %s' \
          % (datetime.now() - t_event_1)
    return events

###################### events_info #####################################


def events_info(request):
    """
    Get the event(s) info for event-based or continuous requests
    """
    global input

    if request == 'event-based':
        print 'Event(s) are based on: ',

        try:
            print input['event_url']
            print input['event_catalog']

            evlatmin = input['evlatmin']
            evlatmax = input['evlatmax']
            evlonmin = input['evlonmin']
            evlonmax = input['evlonmax']

            evlat = input['evlat']
            evlon = input['evlon']
            evradmax = input['evradmax']
            evradmin = input['evradmin']

            client_fdsn = Client_fdsn(base_url=input['event_url'])
            events_QML = client_fdsn.get_events(minlatitude=evlatmin,
                                                maxlatitude=evlatmax,
                                                minlongitude=evlonmin,
                                                maxlongitude=evlonmax,
                                                latitude=evlat,
                                                longitude=evlon,
                                                maxradius=evradmax,
                                                minradius=evradmin,
                                                mindepth=-input['min_depth'],
                                                maxdepth=-input['max_depth'],
                                                starttime=input['min_date'],
                                                endtime=input['max_date'],
                                                minmagnitude=input['min_mag'],
                                                maxmagnitude=input['max_mag'],
                                                orderby='time',
                                                catalog=input['event_catalog'],
                                                magnitudetype=
                                                input['mag_type'])

            if input['plot_all_events']:
                plt.ion()
                events_QML.plot()

            events = []
            for i in range(len(events_QML)):
                event_time = events_QML.events[i].preferred_origin().time or \
                             events_QML.events[i].origins[0].time
                if event_time.month < 10:
                    event_time_month = '0' + str(event_time.month)
                else:
                    event_time_month = str(event_time.month)
                if event_time.day < 10:
                    event_time_day = '0' + str(event_time.day)
                else:
                    event_time_day = str(event_time.day)

                events.append({'author': events_QML.events[i].preferred_magnitude().creation_info.author or
                                         events_QML.events[i].magnitudes[0].creation_info.author,
                               'event_id': str(event_time.year) + event_time_month + event_time_day + '_' + str(i),
                               'origin_id': events_QML.events[i].preferred_origin_id or
                                            events_QML.events[i].origins[0].resource_id.resource_id,
                               'longitude': events_QML.events[i].preferred_origin().longitude or
                                            events_QML.events[i].origins[0].longitude,
                               'latitude': events_QML.events[i].preferred_origin().latitude or
                                           events_QML.events[i].origins[0].latitude,
                               'datetime': event_time,
                               'depth': -events_QML.events[i].preferred_origin().depth/1000. or
                                        -events_QML.events[i].origins[0].depth/1000.,
                               'magnitude': events_QML.events[i].preferred_magnitude().mag or
                                            events_QML.events[i].magnitudes[0].mag,
                               'magnitude_type': events_QML.events[i].preferred_magnitude().magnitude_type.lower() or
                                                 events_QML.events[i].magnitudes[0].magnitude_type.lower(),
                               'flynn_region': 'NAN'})

        except Exception as e:
            print 30*'-'
            print 'No event found with the requested criteria!'
            print 'ERROR: %s' % e
            print 30*'-'
            events = []

        for i in range(len(events)):
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
            # residual time is: (has not been used here)
            #t_res = t_cont - num_div*input['interval']
            for i in range(num_div):
                cont_dir_name = (len(str(num_div)) - len(str(i)))*'0' + str(i)
                events.append({'author': 'NAN',
                               'event_id': 'continuous' + cont_dir_name,
                               'origin_id': -12345.0,
                               'longitude': -12345.0, 'latitude': -12345.0,
                               'datetime': m_date + i*input['interval'],
                               't1': m_date + i*input['interval'] +
                                     input['preset_cont'],
                               't2': m_date + (i+1)*input['interval'] +
                                     input['offset_cont'],
                               'depth': -12345.0, 'magnitude': -12345.0,
                               'magnitude_type': 'NAN',
                               'flynn_region': 'NAN'})
            cont_dir_name = (len(str(num_div)) - len(str(i+1)))*'0' + str(i+1)
            events.append({'author': 'NAN',
                           'event_id': 'continuous' + cont_dir_name,
                           'origin_id': -12345.0,
                           'longitude': -12345.0, 'latitude': -12345.0,
                           'datetime': m_date + (i+1)*input['interval'],
                           't1': m_date + (i+1)*input['interval'] +
                                 input['preset_cont'],
                           't2': M_date,
                           'depth': -12345.0, 'magnitude': -12345.0,
                           'magnitude_type': 'NAN',
                           'flynn_region': 'NAN'})
        else:
            events.append({'author': 'NAN', 'event_id': 'continuous0',
                           'origin_id': -12345.0,
                           'longitude': -12345.0, 'latitude': -12345.0,
                           'datetime': m_date,
                           't1': m_date, 't2': M_date,
                           'depth': -12345.0, 'magnitude': -12345.0,
                           'magnitude_type': 'NAN', 'flynn_region': 'NAN'})
        print 'DONE'
    return events

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
        input['evlatmin'] = -90
        input['evlatmax'] = +90
        input['evlonmin'] = -180
        input['evlonmax'] = +180

    # Set-up the map
    m = Basemap(projection='cyl', llcrnrlat=input['evlatmin'],
                urcrnrlat=input['evlatmax'], llcrnrlon=input['evlonmin'],
                urcrnrlon=input['evlonmax'], resolution='l')
    #m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90., 120., 30.))
    m.drawmeridians(np.arange(0., 420., 60.))
    m.drawmapboundary()

    # Defining Labels:
    x_ev, y_ev = m(-360, 0)
    m.scatter(x_ev, y_ev, 20, color='red', marker="o",
              edgecolor="black", zorder=10, label='0-70km')
    m.scatter(x_ev, y_ev, 20, color='green', marker="o",
              edgecolor="black", zorder=10, label='70-300km')
    m.scatter(x_ev, y_ev, 20, color='blue', marker="o",
              edgecolor="black", zorder=10, label='300< km')

    m.scatter(x_ev, y_ev, 5, color='white', marker="o",
              edgecolor="black", zorder=10, label='<=4.0')
    m.scatter(x_ev, y_ev, 20, color='white', marker="o",
              edgecolor="black", zorder=10, label='4.0-5.0')
    m.scatter(x_ev, y_ev, 35, color='white', marker="o",
              edgecolor="black", zorder=10, label='5.0-6.0')
    m.scatter(x_ev, y_ev, 50, color='white', marker="o",
              edgecolor="black", zorder=10, label='6.0<')

    ev_dp_all = []
    ev_mag_all = []
    ev_info_ar = np.array([])
    for ev in events:
        x_ev, y_ev = m(float(ev['longitude']), float(ev['latitude']))
        ev_dp_all.append(abs(float(ev['depth'])))
        ev_mag_all.append(abs(float(ev['magnitude'])))
        if abs(float(ev['depth'])) <= 70.0:
            color = 'red'
        elif 70.0 < abs(float(ev['depth'])) <= 300.0:
            color = 'green'
        elif 300.0 < abs(float(ev['depth'])) <= 1000.0:
            color = 'blue'

        if float(ev['magnitude']) <= 4.0:
            size = 10
        elif 4.0 < float(ev['magnitude']) <= 5.0:
            size = 40
        elif 5.0 < float(ev['magnitude']) <= 6.0:
            size = 70
        elif 6.0 < float(ev['magnitude']):
            size = 100
        if np.size(ev_info_ar) < 1:
            ev_info_ar = np.append(ev_info_ar, 
                [float(ev['depth']), float(x_ev), float(y_ev), size, color])
        else:
            ev_info_ar = np.vstack((ev_info_ar, 
                [float(ev['depth']), float(x_ev), float(y_ev), size, color]))
    ev_info_ar = sorted(ev_info_ar, key=lambda ev_info_ar: float(ev_info_ar[0]))
    
    for ev in ev_info_ar[::-1]:
        m.scatter(float(ev[1]), float(ev[2]), float(ev[3]), color=ev[4], marker="o",
                  edgecolor=None, zorder=10)

    plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)

    plt.figure()
    plt.hist(ev_dp_all, input['depth_bins_seismicity'], 
            facecolor='green', alpha=0.75, log=True,
            histtype='stepfilled')
    plt.xlabel('Depth', size=24, weight='bold')
    plt.ylabel('#Events (log)', size=24, weight='bold')
    plt.yscale('log')
    plt.xticks(size=18, weight='bold')
    plt.yticks(size=18, weight='bold')
    plt.tight_layout()
    
    plt.figure()
    plt.hist(ev_mag_all, 
            bins=np.linspace(int(input['min_mag']), 
                int(input['max_mag']), 
                int(input['max_mag'])-int(input['min_mag'])+1), 
        facecolor='green', alpha=0.75, log=True,
        histtype='stepfilled')
    plt.xlabel('Magnitude', size=24, weight='bold')
    plt.ylabel('#Events (log)', size=24, weight='bold')
    plt.yscale('log')
    plt.xticks(size=18, weight='bold')
    plt.yticks(size=18, weight='bold')
    plt.tight_layout()

    plt.show()
                
###################### FDSN_network ####################################
                
                
def FDSN_network(input):
    """         
    Returns information about what time series data is available
        at the requested FDSN web-service for all requested events
    """         
    global events
                
    period = '{0:s}_{1:s}_{2:s}_{3:s}'.format(input['min_date'].split('T')[0],
                                              input['max_date'].split('T')[0],
                                              str(input['min_mag']),
                                              str(input['max_mag']))
    eventpath = os.path.join(input['datapath'], period)
                
    print 'Create folders...',
    create_folders_files(events, eventpath)
    print 'DONE'

    for i in range(len(events)):
        t_fdsn_1 = datetime.now()
        target_path = os.path.join(eventpath, events[i]['event_id'])

        if not input['list_stas']:
            Stas_fdsn = FDSN_available(input, events[i],
                                       target_path, event_number=i)
        else:
            Stas_fdsn = read_list_stas(input['list_stas'],
                                       input['normal_mode_syn'],
                                       input['specfem3D'])

        if input['fdsn_bulk'] != 'Y':
            print '\nFDSN-Availability for event: %s/%s ---> DONE' \
                  % (i+1, len(events))
        else:
            print '\nFDSN-bulkfile for event: %s/%s ---> DONE' \
                  % (i+1, len(events))

        print 'Time for checking the availability: %s' \
              % (datetime.now() - t_fdsn_1)

        if Stas_fdsn != [[]]:
            FDSN_waveform(input, Stas_fdsn, i, type='save')
        else:
            print 'No available station in FDSN for your request and ' \
                  'for event %s!' % i
            continue

###################### FDSN_available ##################################


def FDSN_available(input, event, target_path, event_number):
    """
    Check the availablity of FDSN stations
    """

    print "Check the availablity of FDSN stations"
    client_fdsn = Client_fdsn(base_url=input['fdsn_base_url'],
                              user=input['fdsn_user'],
                              password=input['fdsn_pass'])
    Sta_fdsn = []

    try:
        available = client_fdsn.get_stations(network=input['net'],
                                             station=input['sta'],
                                             location=input['loc'],
                                             channel=input['cha'],
                                             starttime=
                                             UTCDateTime(event['t1']),
                                             endtime=UTCDateTime(event['t2']),
                                             latitude=input['lat_cba'],
                                             longitude=input['lon_cba'],
                                             minradius=input['mr_cba'],
                                             maxradius=input['Mr_cba'],
                                             minlatitude=input['mlat_rbb'],
                                             maxlatitude=input['Mlat_rbb'],
                                             minlongitude=input['mlon_rbb'],
                                             maxlongitude=input['Mlon_rbb'],
                                             level='channel')

        Sta_fdsn = []
        for network in available.networks:
            for station in network:
                for channel in station:
                    Sta_fdsn.append([network.code, station.code,
                                     channel.location_code, channel.code,
                                     channel.latitude, channel.longitude,
                                     channel.elevation, channel.depth])
        if input['fdsn_bulk'] == 'Y':
            if os.path.exists(os.path.join(target_path, 'info',
                                           'bulkdata.txt')):
                print 'bulkdata.txt exists in the directory!'
            else:
                print 'Start creating a list for bulk request'
                bulk_list = []
                for bulk_sta in Sta_fdsn:
                    if input['cut_time_phase']:
                        t_start, t_end = calculate_time_phase(event, bulk_sta)
                    else:
                        t_start = event['t1']
                        t_end = event['t2']
                    bulk_list.append((bulk_sta[0], bulk_sta[1], bulk_sta[2],
                                      bulk_sta[3], t_start, t_end))

                bulk_list_fio = open(os.path.join(target_path, 'info',
                                                  'bulkdata_list'), 'a+')
                pickle.dump(bulk_list, bulk_list_fio)
                bulk_list_fio.close()
    except Exception as e:
        exc_file = open(os.path.join(target_path, 'info', 'exception'), 'a+')
        ee = 'fdsn -- Event: %s --- %s\n' % (event_number, e)
        exc_file.writelines(ee)
        exc_file.close()
        print 'ERROR: %s' % ee

    if len(Sta_fdsn) == 0:
        Sta_fdsn.append([])
    Sta_fdsn.sort()
    return Sta_fdsn

###################### read_list_stas ##################################


def read_list_stas(add_list, normal_mode_syn, specfem3D):
    """
    read a list of stations instead of checking the availability.
    """

    print '\n---------------------------------'
    print 'INFO:'
    print 'Format of the station list:'
    print 'sta  net  loc  cha  lat  lon  ele'
    print '---------------------------------\n\n'

    list_stas_fio = open(add_list)
    list_stas = list_stas_fio.readlines()
    for sta in range(len(list_stas)):
        if not list_stas[sta].startswith('\n'):
            list_stas[sta] = list_stas[sta].split()
    final_list = []

    if specfem3D == 'Y':
        for sta in range(len(list_stas)):
            for chan in ['MXE', 'MXN', 'MXZ']:
                final_list.append(['SY', list_stas[sta][0],
                                   'S3', chan,
                                   list_stas[sta][2],
                                   list_stas[sta][3],
                                   list_stas[sta][4]])
    elif normal_mode_syn == 'Y':
        for sta in range(len(list_stas)):
            for chan in ['LXE', 'LXN', 'LXZ']:
                final_list.append(['SY', list_stas[sta][0],
                                   'S1', chan,
                                   list_stas[sta][2],
                                   list_stas[sta][3],
                                   list_stas[sta][4]])
    else:
        for sta in range(len(list_stas)):
            #for chan in ['BH1', 'BH2', 'BHE', 'BHN', 'BHZ']:
            final_list.append([list_stas[sta][1], list_stas[sta][0],
                               list_stas[sta][2], list_stas[sta][3],
                               list_stas[sta][4], list_stas[sta][5],
                               list_stas[sta][6]])

    return final_list

###################### FDSN_waveform ###############################


def FDSN_waveform(input, Sta_req, i, type):
    """
    Gets Waveforms, StationXML files and meta-data from FDSN
    """

    t_wave_1 = datetime.now()
    global events

    add_event = []
    if type == 'save':
        period = '{0:s}_{1:s}_{2:s}_{3:s}'.\
            format(input['min_date'].split('T')[0],
                   input['max_date'].split('T')[0],
                   str(input['min_mag']),
                   str(input['max_mag']))
        eventpath = os.path.join(input['datapath'], period)
        for k in range(len(events)):
            add_event.append(os.path.join(eventpath, events[k]['event_id']))
    elif type == 'update':
        events, add_event = quake_info(input['fdsn_update'], target='info')

    if input['test'] == 'Y':
        len_req_fdsn = input['test_num']
    else:
        len_req_fdsn = len(Sta_req)

    if input['fdsn_bulk'] == 'Y':
        try:
            t11 = datetime.now()
            client_fdsn = Client_fdsn(base_url=input['fdsn_base_url'],
                                      user=input['fdsn_user'],
                                      password=input['fdsn_pass'])
            bulk_list_fio = open(os.path.join(add_event[i], 'info',
                                              'bulkdata_list'))
            bulk_list = pickle.load(bulk_list_fio)
            bulk_smgrs = client_fdsn.get_waveforms_bulk(bulk_list)
            print 'Saving the retrieved waveforms...',
            for bulk_st in bulk_smgrs:
                bulk_st.stats = bulk_st.stats
                bulk_st.write(os.path.join(add_event[i], 'BH_RAW',
                                           '%s.%s.%s.%s'
                                           % (bulk_st.stats['network'],
                                              bulk_st.stats['station'],
                                              bulk_st.stats['location'],
                                              bulk_st.stats['channel'])),
                              'MSEED')
        except Exception as e:
            print 'WARNING: %s' % e
        print 'DONE'

        # Following parameter is set to 'N' to avoid
        # retrieving the waveforms twice
        # When using bulk requests, waveforms are retreived in bulk
        # but not response/StationXML files and not metadata
        input['waveform'] = 'N'
        t22 = datetime.now()
        print '\nbulkdataselect request is done for event: %s/%s in %s' \
              % (i+1, len(events), t22-t11)

    dic = {}
    print '\nFDSN-Event: %s/%s' % (i+1, len(events))

    client_fdsn = Client_fdsn(base_url=input['fdsn_base_url'],
                              user=input['fdsn_user'],
                              password=input['fdsn_pass'])
    if input['req_parallel'] == 'Y':
        print "Parallel request with %s processes.\n" % input['req_np']
        
        #parallel_len_req_fdsn = range(0, len_req_fdsn)

        #start = 0
        #end = len_req_fdsn
        #step = (end - start) / input['req_np'] + 1

        #jobs = []
        #for index in xrange(input['req_np']):
        #    starti = start+index*step
        #    endi = min(start+(index+1)*step, end)
        #    p = multiprocessing.Process(target=FDSN_download_iter,
        #                                args=(i, starti, endi, dic, type,
        #                                      len(events), events, add_event,
        #                                      Sta_req, input, client_fdsn))

        #    jobs.append(p)
        #for index in range(len(jobs)):
        #    jobs[index].start()

        #pp_flag = True
        #while pp_flag:
        #    for proc in jobs:
        #        if proc.is_alive():
        #            time.sleep(1)
        #            pp_flag = True
        #            break
        #        else:
        #            pp_flag = False
        #    if not pp_flag:
        #        print '\nAll the processes are finished...'

        #len_par_grp = [parallel_len_req_fdsn[n:n+input['req_np']] for n in
        #               range(0, len(parallel_len_req_fdsn), input['req_np'])]

        par_jobs = []
        for j in range(len_req_fdsn):
            p = multiprocessing.Process(target=FDSN_download_core,
                                        args=(i, j, dic, type, len(events),
                                              events, add_event, Sta_req,
                                              input, client_fdsn,))
            par_jobs.append(p)
        sub_par_jobs = [] 
        for l in range(len(par_jobs)):
            counter = input['req_np']
            while counter >= input['req_np']:
                counter = 0
                for ll in range(len(sub_par_jobs)):
                    if par_jobs[sub_par_jobs[ll]].is_alive():
                        counter += 1
                if not counter == input['req_np']:
                    print 'counter: %s' % counter

            par_jobs[l].start()
            sub_par_jobs.append(l)
            print 'length of sub_pat_jobs: %s' % len(sub_par_jobs)

        counter = input['req_np']
        while counter > 0:
            counter = 0
            for ll in range(len(par_jobs)):
                if par_jobs[ll].is_alive():
                    counter += 1

        #for l in range(len(len_par_grp)):
        #    for ll in len_par_grp[l]:
        #        par_jobs[ll].start()
        #        time.sleep(0.01)
        #    for ll in len_par_grp[l]:
        #        while par_jobs[ll].is_alive():
        #            time.sleep(0.01)

    else:
        for j in range(len_req_fdsn):
            FDSN_download_core(i=i, j=j, dic=dic, type=type,
                               len_events=len(events), events=events,
                               add_event=add_event, Sta_req=Sta_req,
                               input=input, client_fdsn=client_fdsn)

    if input['fdsn_bulk'] == 'Y':
        input['waveform'] = 'Y'
        sta_saved_path = glob.glob(os.path.join(add_event[i],
                                                'BH_RAW',
                                                '*.*.*.*'))
        print '\nAdjusting the station_event file...',

        sta_saved_list = []
        for sta_num in range(len(sta_saved_path)):
            sta_saved_list.append(os.path.basename(sta_saved_path[sta_num]))

        sta_ev_new = []
        for line in fileinput.FileInput(os.path.join(add_event[i], 'info',
                                                     'station_event')):
            if not '%s.%s.%s.%s' % (line.split(',')[0], line.split(',')[1],
                                    line.split(',')[2], line.split(',')[3]) \
                    in sta_saved_list:
                pass
            else:
                sta_ev_new.append(line)

        file_staev_open = open(os.path.join(add_event[i], 'info',
                                            'station_event'), 'w')
        file_staev_open.writelines(sta_ev_new)
        file_staev_open.close()
        print 'DONE'

    if input['SAC'] == 'Y':
        print '\nConverting the MSEED files to SAC...',
        writesac_all(i=i, address_events=add_event)
        print 'DONE'

    try:
        len_sta_ev_open = open(os.path.join(add_event[i],
                                            'info',
                                            'station_event'), 'r')
        len_sta_ev = len(len_sta_ev_open.readlines())
    except Exception as e:
        len_sta_ev = 'Can not open station_event file: %s' \
                     % (os.path.join(add_event[i], 'info', 'station_event'))

    report = open(os.path.join(add_event[i], 'info', 'report_st'), 'a')
    eventsID = events[i]['event_id']
    report.writelines('<><><><><><><><><><><><><><><><><>\n')
    report.writelines(eventsID + '\n')
    report.writelines('---------------FDSN---------------\n')
    report.writelines('---------------%s---------------\n' % input['cha'])
    rep = 'FDSN-Available stations for channel %s and for event-%s: %s\n' \
          % (input['cha'], i, len(Sta_req))
    report.writelines(rep)
    rep = 'FDSN-%s stations for channel %s and for event-%s: %s\n' \
          % (type, input['cha'], i, len_sta_ev)
    report.writelines(rep)
    report.writelines('----------------------------------\n')

    t_wave = datetime.now() - t_wave_1

    rep = 'Time for %sing Waveforms from FDSN: %s\n' % (type, t_wave)
    report.writelines(rep)
    report.writelines('----------------------------------\n')
    report.close()

    if input['req_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(add_event[i], 'info',
                                                 'report_parallel'), 'a')
        report_parallel_open.writelines('---------------FDSN---------------\n')
        report_parallel_open.writelines('Request\n')
        if input['fdsn_bulk'] == 'Y':
            report_parallel_open.writelines('Number of Nodes: (bulk) %s\n'
                                            % input['req_np'])
        else:
            report_parallel_open.writelines('Number of Nodes: %s\n'
                                            % input['req_np'])

        size = getFolderSize(os.path.join(add_event[i]))
        ti = '%s,%s,%s,+,\n' % (t_wave.seconds,
                                t_wave.microseconds,
                                size/(1024.**2))

        report_parallel_open.writelines('Total Time     : %s\n' % t_wave)
        report_parallel_open.writelines(ti)
        report_parallel_open.close()

    print "\n------------------------"
    print 'FDSN for event-%s is Done' % (i+1)
    print 'Total Time: %s' % t_wave
    print "------------------------"

###################### FDSN_download_iter ##################################


def FDSN_download_iter(i, starti, endi, dic, type, len_events, events,
                       add_event, Sta_req, input, client_fdsn):
    """
    This function only iterates over FDSN_download_core,
    this should be called by another program.
    """
    for j in range(starti, endi):
        FDSN_download_core(i=i, j=j, dic=dic, type=type,
                           len_events=len_events, events=events,
                           add_event=add_event, Sta_req=Sta_req,
                           input=input, client_fdsn=client_fdsn)

###################### FDSN_download_core ##################################


def FDSN_download_core(i, j, dic, type, len_events, events,
                       add_event, Sta_req, input, client_fdsn):
    """
    Downloading the waveforms, reponse files (StationXML) and metadata
    This program should be normally called by some higher-level functions
    """

    try:
        dummy = 'Initializing'
        t11 = datetime.now()
        info_req = '[%s/%s-%s/%s-%s] ' % (i+1, len_events, j+1,
                                          len(Sta_req), input['cha'])

        if Sta_req[j][2] == '--' or Sta_req[j][2] == '  ':
                Sta_req[j][2] = ''

        if input['cut_time_phase']:
            t_start, t_end = calculate_time_phase(events[i], Sta_req[j])
        else:
            t_start = events[i]['t1']
            t_end = events[i]['t2']

        if input['waveform'] == 'Y':
            dummy = 'Waveform'
            client_fdsn.get_waveforms(Sta_req[j][0], Sta_req[j][1],
                                      Sta_req[j][2], Sta_req[j][3],
                                      t_start, t_end,
                                      filename=os.path.join(add_event[i],
                                                            'BH_RAW',
                                                            '%s.%s.%s.%s'
                                                            % (Sta_req[j][0],
                                                               Sta_req[j][1],
                                                               Sta_req[j][2],
                                                               Sta_req[j][3])))
            print '%ssaving waveform for %s.%s.%s.%s  ---> DONE' \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        if input['response'] == 'Y':
            dummy = 'Response'
            client_fdsn.get_stations(network=Sta_req[j][0],
                                     station=Sta_req[j][1],
                                     location=Sta_req[j][2],
                                     channel=Sta_req[j][3],
                                     starttime=t_start, endtime=t_end,
                                     filename=
                                     os.path.join(add_event[i], 'Resp',
                                                  'STXML.%s.%s.%s.%s'
                                                  % (Sta_req[j][0],
                                                     Sta_req[j][1],
                                                     Sta_req[j][2],
                                                     Sta_req[j][3])),
                                     level='response')

            print "%ssaving Response for: %s.%s.%s.%s  ---> DONE" \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        dummy = 'Meta-data'
        dic[j] = {'info': '%s.%s.%s.%s' % (Sta_req[j][0], Sta_req[j][1],
                                           Sta_req[j][2], Sta_req[j][3]),
                  'net': Sta_req[j][0],
                  'sta': Sta_req[j][1],
                  'latitude': Sta_req[j][4],
                  'longitude': Sta_req[j][5],
                  'loc': Sta_req[j][2],
                  'cha': Sta_req[j][3],
                  'elevation': Sta_req[j][6],
                  'depth': Sta_req[j][7]}
        Syn_file = open(os.path.join(add_event[i], 'info',
                                     'station_event'), 'a')
        syn = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\n' \
              % (dic[j]['net'], dic[j]['sta'],
                 dic[j]['loc'], dic[j]['cha'],
                 dic[j]['latitude'], dic[j]['longitude'],
                 float(dic[j]['elevation']),
                 float(dic[j]['depth']),
                 events[i]['event_id'], events[i]['latitude'],
                 events[i]['longitude'], events[i]['depth'],
                 events[i]['magnitude'], input['fdsn_base_url'])
        Syn_file.writelines(syn)
        Syn_file.close()

        print "%ssaving Metadata for: %s.%s.%s.%s  ---> DONE" \
              % (info_req, Sta_req[j][0], Sta_req[j][1],
                 Sta_req[j][2], Sta_req[j][3])

        t22 = datetime.now()
        if input['time_fdsn'] == 'Y':
            time_fdsn = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_fdsn'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,+,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_fdsn.seconds,
                                                time_fdsn.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()
    except Exception as e:
        t22 = datetime.now()
        if input['time_fdsn'] == 'Y':
            time_fdsn = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_fdsn'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,-,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_fdsn.seconds,
                                                time_fdsn.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()

        if len(Sta_req[j]) != 0:
            print '%s%s---%s.%s.%s.%s' % (info_req, dummy,
                                          Sta_req[j][0],
                                          Sta_req[j][1],
                                          Sta_req[j][2],
                                          Sta_req[j][3])
            ee = 'fdsn -- %s---%s-%s---%s.%s.%s.%s---%s\n' \
                 % (dummy, i, j,
                    Sta_req[j][0], Sta_req[j][1], Sta_req[j][2],
                    Sta_req[j][3], e)
        elif len(Sta_req[j]) == 0:
            ee = 'There is no available station for this event.'
        Exception_file = open(os.path.join(add_event[i],
                                           'info', 'exception'), 'a')
        Exception_file.writelines(ee)
        Exception_file.close()
        print 'ERROR: %s' % ee

###################### calculate_time_phase ##################################


def calculate_time_phase(event, sta):
    """
    calculate arrival time of the requested phase
    to use in retrieving waveforms.
    """

    ev_lat = event['latitude']
    ev_lon = event['longitude']
    ev_dp = abs(float(event['depth']))
    sta_lat = float(sta[4])
    sta_lon = float(sta[5])
    delta = locations2degrees(ev_lat, ev_lon, sta_lat, sta_lon)
    tt = taup.getTravelTimes(delta, ev_dp)
    phase_list = ['P', 'Pdiff', 'PKIKP']
    flag = False
    for ph in phase_list:
        for i in range(len(tt)):
            if tt[i]['phase_name'] == ph:
                flag = True
                time = tt[i]['time']
                break
            else:
                continue
        if flag:
            print 'Phase: %s' % ph
            break
    t_start = event['t1'] + time
    t_end = event['t2'] + time
    return t_start, t_end

###################### Arclink_network #################################


def ARC_network(input):
    """
    Returns information about what time series data is available
    at the ArcLink nodes for all requested events
    """
    global events

    period = '{0:s}_{1:s}_{2:s}_{3:s}'.format(input['min_date'].split('T')[0],
                                              input['max_date'].split('T')[0],
                                              str(input['min_mag']),
                                              str(input['max_mag']))
    eventpath = os.path.join(input['datapath'], period)

    if input['FDSN'] != 'Y':
        print 'Create folders...',
        create_folders_files(events, eventpath)
        print 'DONE'

    for i in range(len(events)):
        t_arc_1 = datetime.now()
        target_path = os.path.join(eventpath, events[i]['event_id'])

        if not input['list_stas']:
            Stas_arc = ARC_available(input, events[i], target_path,
                                     event_number=i)
        else:
            Stas_arc = read_list_stas(input['list_stas'],
                                      normal_mode_syn='N',
                                      specfem3D='N')

        print '\nArcLink-Availability for event: %s/%s  ---> DONE' \
              % (i+1, len(events))
        print 'Time for checking the availability: %s' \
              % (datetime.now() - t_arc_1)

        if Stas_arc != [[]]:
            ARC_waveform(input, Stas_arc, i, type='save')
        else:
            'No available station in ArcLink for your request!'
            continue

###################### ARC_available ###################################


def ARC_available(input, event, target_path, event_number):
    """
    Check the availability of ArcLink stations
    """

    print "Check the availability of ArcLink stations"
    client_arclink = Client_arclink(user='test@obspy.org',
                                    timeout=input['arc_avai_timeout'])
    Sta_arc = []

    try:
        inventories = client_arclink.getInventory(network=input['net'],
                                                  station=input['sta'],
                                                  location=input['loc'],
                                                  channel=input['cha'],
                                                  starttime=
                                                  UTCDateTime(event['t1']),
                                                  endtime=
                                                  UTCDateTime(event['t2']),
                                                  min_latitude=
                                                  input['mlat_rbb'],
                                                  max_latitude=
                                                  input['Mlat_rbb'],
                                                  min_longitude=
                                                  input['mlon_rbb'],
                                                  max_longitude=
                                                  input['Mlon_rbb'])

        for inv_key in inventories.keys():
            netsta = inv_key.split('.')
            if len(netsta) == 4:
                sta = '%s.%s' % (netsta[0], netsta[1])
                if not inventories[sta]['depth']:
                    inventories[sta]['depth'] = 0.0
                Sta_arc.append([netsta[0], netsta[1], netsta[2], netsta[3],
                                inventories[sta]['latitude'],
                                inventories[sta]['longitude'],
                                inventories[sta]['elevation'],
                                inventories[sta]['depth']])

    except Exception as e:
        exception_file = open(os.path.join(target_path, 'info',
                                           'exception'), 'a+')
        ee = 'arclink -- Event: %s --- %s\n' % (event_number, e)
        exception_file.writelines(ee)
        exception_file.close()
        print 'ERROR: %s' % ee

    if len(Sta_arc) == 0:
        Sta_arc.append([])
    Sta_arc.sort()
    return Sta_arc

###################### Arclink_waveform ############################


def ARC_waveform(input, Sta_req, i, type):
    """
    Gets Waveforms, Response files and meta-data
    from ArcLink based on the requested events...
    """

    t_wave_1 = datetime.now()
    global events

    add_event = []
    if type == 'save':
        period = '{0:s}_{1:s}_{2:s}_{3:s}'.\
            format(input['min_date'].split('T')[0],
                   input['max_date'].split('T')[0],
                   str(input['min_mag']), str(input['max_mag']))
        eventpath = os.path.join(input['datapath'], period)
        for k in range(0, len(events)):
            add_event.append(os.path.join(eventpath, events[k]['event_id']))
    elif type == 'update':
        events, add_event = quake_info(input['arc_update'], target='info')

    if input['test'] == 'Y':
        len_req_arc = input['test_num']
    else:
        len_req_arc = len(Sta_req)

    dic = {}
    print '\nArcLink-Event: %s/%s' % (i+1, len(events))

    if input['req_parallel'] == 'Y':
        print "Parallel request with %s processes.\n" % input['req_np']
        parallel_len_req_arc = range(0, len_req_arc)
        len_par_grp = [parallel_len_req_arc[n:n+input['req_np']] for n in
                       range(0, len(parallel_len_req_arc), input['req_np'])]

        par_jobs = []
        for j in range(len_req_arc):
            p = multiprocessing.Process(target=ARC_download_core,
                                        args=(i, j, dic, type,
                                              len(events), events,
                                              add_event, Sta_req, input,))
            par_jobs.append(p)

        for l in range(len(len_par_grp)):
            for ll in len_par_grp[l]:
                par_jobs[ll].start()
                time.sleep(0.01)
            for ll in len_par_grp[l]:
                while par_jobs[ll].is_alive():
                    time.sleep(0.01)


        #par_jobs = []
        #for j in range(len_req_arc):
        #    p = multiprocessing.Process(target=ARC_download_core,
        #                                args=(i, j, dic, type, len(events),
        #                                      events, add_event, Sta_req,
        #                                      input,))
        #    par_jobs.append(p)
        #sub_par_jobs = [] 
        #for l in range(len(par_jobs)):
        #    counter = input['req_np']
        #    while counter >= input['req_np']:
        #        counter = 0
        #        for ll in range(len(sub_par_jobs)):
        #            if par_jobs[sub_par_jobs[ll]].is_alive():
        #                counter += 1
        #        if not counter == input['req_np']:
        #            print 'counter: %s' % counter

        #    par_jobs[l].start()
        #    sub_par_jobs.append(l)
        #    print 'length of sub_pat_jobs: %s' % len(sub_par_jobs)

        #counter = input['req_np']
        #while counter > 0:
        #    counter = 0
        #    for ll in range(len(par_jobs)):
        #        if par_jobs[ll].is_alive():
        #            counter += 1


    else:
        for j in range(len_req_arc):
            ARC_download_core(i=i, j=j, dic=dic, type=type,
                              len_events=len(events), events=events,
                              add_event=add_event,
                              Sta_req=Sta_req, input=input)
    if input['SAC'] == 'Y':
        print '\nConverting the MSEED files to SAC...',
        writesac_all(i=i, address_events=add_event)
        print 'DONE'

    try:
        len_sta_ev_open = open(os.path.join(add_event[i], 'info',
                                            'station_event'), 'r')
        len_sta_ev = len(len_sta_ev_open.readlines())
    except Exception as e:
        len_sta_ev = 'Can not open station_event file: %s' \
                     % (os.path.join(add_event[i], 'info', 'station_event'))

    report = open(os.path.join(add_event[i], 'info', 'report_st'), 'a')
    eventsID = events[i]['event_id']
    report.writelines('<><><><><><><><><><><><><><><><><>\n')
    report.writelines(eventsID + '\n')
    report.writelines('---------------ARC---------------\n')
    report.writelines('---------------%s---------------\n' % input['cha'])
    rep = 'ARC-Available stations for channel %s and for event-%s: %s\n' \
          % (input['cha'], i, len(Sta_req))
    report.writelines(rep)
    rep = 'ARC-%s stations for channel %s and for event-%s: %s\n' \
          % (type, input['cha'], i, len_sta_ev)
    report.writelines(rep)
    report.writelines('----------------------------------\n')

    t_wave = datetime.now() - t_wave_1

    rep = 'Time for %sing Waveforms from ArcLink: %s\n' % (type, t_wave)
    report.writelines(rep)
    report.writelines('----------------------------------\n')
    report.close()

    if input['req_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(add_event[i],
                                                 'info', 'report_parallel'),
                                    'a')
        report_parallel_open.writelines('---------------ARC---------------\n')
        report_parallel_open.writelines('Request\n')
        report_parallel_open.writelines('Number of Nodes: %s\n'
                                        % input['req_np'])

        size = getFolderSize(os.path.join(add_event[i]))
        ti = '%s,%s,%s,+,\n' % (t_wave.seconds, t_wave.microseconds,
                                size/(1024.**2))

        report_parallel_open.writelines('Total Time     : %s\n' % t_wave)
        report_parallel_open.writelines(ti)
        report_parallel_open.close()

    print "\n------------------------"
    print 'ArcLink for event-%s is Done' % (i+1)
    print 'Total Time: %s' % t_wave
    print "------------------------"

###################### ARC_download_core ###############################


def ARC_download_core(i, j, dic, type, len_events, events,
                      add_event, Sta_req, input):
    """
    Downloading waveforms, response files and metadata
    This program should be normally called by some higher-level functions
    """

    client_arclink = Client_arclink(user='test@obspy.org',
                                    timeout=input['arc_wave_timeout'])

    try:
        dummy = 'Initializing'
        t11 = datetime.now()
        info_req = '[%s/%s-%s/%s-%s] ' % (i+1, len_events, j+1,
                                          len(Sta_req), input['cha'])

        if input['cut_time_phase']:
            t_start, t_end = calculate_time_phase(events[i], Sta_req[j])
        else:
            t_start = events[i]['t1']
            t_end = events[i]['t2']

        if input['waveform'] == 'Y':
            dummy = 'Waveform'
            try:
                client_arclink.saveWaveform(os.path.join(add_event[i],
                                                         'BH_RAW',
                                                         '%s.%s.%s.%s'
                                                         % (Sta_req[j][0],
                                                            Sta_req[j][1],
                                                            Sta_req[j][2],
                                                            Sta_req[j][3])),
                                            Sta_req[j][0], Sta_req[j][1],
                                            Sta_req[j][2], Sta_req[j][3],
                                            t_start, t_end)
            except Exception as e:
                print 'WARNING: %s' % e

            print '%ssaving waveform for %s.%s.%s.%s  ---> DONE' \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        if input['response'] == 'Y':
            dummy = 'Response'
            client_arclink.saveResponse(os.path.join(add_event[i], 'Resp',
                                                     'DATALESS.%s.%s.%s.%s'
                                                     % (Sta_req[j][0],
                                                        Sta_req[j][1],
                                                        Sta_req[j][2],
                                                        Sta_req[j][3])),
                                        Sta_req[j][0], Sta_req[j][1],
                                        Sta_req[j][2], Sta_req[j][3],
                                        t_start, t_end)

            print "%ssaving Response for: %s.%s.%s.%s  ---> DONE" \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        if input['paz'] == 'Y':
            dummy = 'PAZ'
            paz_arc = client_arclink.getPAZ(Sta_req[j][0], Sta_req[j][1],
                                            Sta_req[j][2], Sta_req[j][3],
                                            time=t_start)
            paz_file = open(os.path.join(add_event[i], 'Resp',
                                         'PAZ.%s.%s.%s.%s.paz'
                                         % (Sta_req[j][0], Sta_req[j][1],
                                            Sta_req[j][2], Sta_req[j][3])),
                            'w')
            pickle.dump(paz_arc, paz_file)
            paz_file.close()

            print "%ssaving PAZ for     : %s.%s.%s.%s  ---> DONE" \
                  % (info_req, Sta_req[j][0], Sta_req[j][1],
                     Sta_req[j][2], Sta_req[j][3])

        dummy = 'Meta-data'
        dic[j] = {'info': '%s.%s.%s.%s' % (Sta_req[j][0],
                                           Sta_req[j][1],
                                           Sta_req[j][2],
                                           Sta_req[j][3]),
                  'net': Sta_req[j][0], 'sta': Sta_req[j][1],
                  'latitude': Sta_req[j][4], 'longitude': Sta_req[j][5],
                  'loc': Sta_req[j][2], 'cha': Sta_req[j][3],
                  'elevation': Sta_req[j][6], 'depth': Sta_req[j][7]}
        Syn_file = open(os.path.join(add_event[i], 'info', 'station_event'),
                        'a')
        syn = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,arc,\n' \
              % (Sta_req[j][0], Sta_req[j][1], Sta_req[j][2], Sta_req[j][3],
                 Sta_req[j][4], Sta_req[j][5], float(Sta_req[j][6]),
                 float(Sta_req[j][7]),
                 events[i]['event_id'], events[i]['latitude'],
                 events[i]['longitude'], events[i]['depth'],
                 events[i]['magnitude'])
        Syn_file.writelines(syn)
        Syn_file.close()

        print "%ssaving Metadata for: %s.%s.%s.%s  ---> DONE" \
              % (info_req, Sta_req[j][0], Sta_req[j][1],
                 Sta_req[j][2], Sta_req[j][3])

        t22 = datetime.now()
        if input['time_arc'] == 'Y':
            time_arc = t22 - t11
            time_file = open(os.path.join(add_event[i], 'info',
                                          'time_arc'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))
            ti = '%s,%s,%s,%s,%s,%s,%s,+,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_arc.seconds,
                                                time_arc.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()
    except Exception as e:
        t22 = datetime.now()
        if input['time_arc'] == 'Y':
            time_arc = t22 - t11
            time_file = open(os.path.join(add_event[i],
                                          'info',
                                          'time_arc'), 'a')
            size = getFolderSize(os.path.join(add_event[i]))

            ti = '%s,%s,%s,%s,%s,%s,%s,-,\n' % (Sta_req[j][0],
                                                Sta_req[j][1],
                                                Sta_req[j][2],
                                                Sta_req[j][3],
                                                time_arc.seconds,
                                                time_arc.microseconds,
                                                size/(1024.**2))
            time_file.writelines(ti)
            time_file.close()

        if len(Sta_req[j]) != 0:
            print '%s%s---%s.%s.%s.%s' % (info_req, dummy,
                                          Sta_req[j][0], Sta_req[j][1],
                                          Sta_req[j][2], Sta_req[j][3])
            ee = 'arc -- %s---%s-%s---%s.%s.%s.%s---%s\n' \
                 % (dummy, i, j, Sta_req[j][0], Sta_req[j][1],
                    Sta_req[j][2], Sta_req[j][3], e)
        elif len(Sta_req[j]) == 0:
            ee = 'There is no available station for this event.'
        exception_file = open(os.path.join(add_event[i],
                                           'info', 'exception'), 'a')
        exception_file.writelines(ee)
        exception_file.close()
        print 'ERROR: %s' % ee

###################### FDSN_update #####################################


def FDSN_update(input, address):
    """
    Initialize directories and pass the required stations
    (removing the duplications) for FDSN update requests
    """
    t_update_1 = datetime.now()

    events, address_events = quake_info(address, 'info')

    for i in range(len(events)):
        Stas_fdsn = FDSN_available(input, events[i],
                                   address_events[i],
                                   event_number=i)

        if input['fdsn_bulk'] != 'Y':
            print '\nFDSN-Availability for event: %s/%s ---> DONE' \
                  % (i+1, len(events))
        else:
            print '\nFDSN-bulkfile for event    : %s/%s ---> DONE' \
                  % (i+1, len(events))

        if Stas_fdsn != [[]]:
            Stas_req = rm_duplicate(Stas_fdsn,
                                    address=os.path.join(address_events[i]))
        else:
            Stas_req = None
            print '------------------------------'
            print 'There is no available station!'
            print '------------------------------'

        if not os.path.isdir(os.path.join(address_events[i], 'BH_RAW')):
            os.makedirs(os.path.join(address_events[i], 'BH_RAW'))

        if Stas_req:
            FDSN_waveform(input, Stas_req, i, type='update')
        else:
            print '\nNo available station in FDSN for your request!'
            print 'Check the next event...'
            continue

    print '\nTotal time for updating FDSN: %s' % (datetime.now() - t_update_1)

###################### ARC_update ######################################


def ARC_update(input, address):
    """
    Initialize directories and pass the required stations
    (removing the duplications) for ArcLink update requests
    """
    t_update_1 = datetime.now()

    events, address_events = quake_info(address, 'info')

    for i in range(len(events)):
        Stas_arc = ARC_available(input, events[i],
                                 address_events[i],
                                 event_number=i)

        print '\nArcLink-Availability for event: %s/%s ---> DONE' \
              % (i+1, len(events))

        if Stas_arc != [[]]:
            Stas_req = rm_duplicate(Stas_arc,
                                    address=os.path.join(address_events[i]))
        else:
            Stas_req = None
            print '------------------------------'
            print 'There is no available station!'
            print '------------------------------'

        if not os.path.isdir(os.path.join(address_events[i], 'BH_RAW')):
            os.makedirs(os.path.join(address_events[i], 'BH_RAW'))

        if Stas_req:
            ARC_waveform(input, Stas_req, i, type='update')
        else:
            print '\nNo available station in ArcLink for your request!'
            print 'Check the next event...'
            continue

    print '\nTotal time for updating ArcLink: %s' \
          % (datetime.now() - t_update_1)

###################### FDSN_ARC_IC #####################################


def FDSN_ARC_IC(input, clients):
    """
    Call "inst_correct" function based on the request.
    Group the stations that have been retrieved from specific client
    Grouping is necessary in applying the instrument correction correctly
    (different clients are treated differently)
    """

    # Following two if-conditions create address
    # to which instrument correction should be applied
    # Please note that these two conditions can not happen at the same time
    if clients != 'arc':
        clients_name = 'fdsn'
    else:
        clients_name = 'arc'
    if input[clients_name + '_ic_auto'] == 'Y':
        global events
        period = '{0:s}_{1:s}_{2:s}_{3:s}'.\
            format(input['min_date'].split('T')[0],
                   input['max_date'].split('T')[0],
                   str(input['min_mag']),
                   str(input['max_mag']))
        address = os.path.join(input['datapath'], period)

    if input[clients_name + '_ic'] != 'N':
        address = input[clients_name + '_ic']

    events, address_events = quake_info(address, 'info')

    for i in range(len(events)):

        sta_ev = read_station_event(address_events[i])

        ls_saved_stas_tmp = []
        for sta_e in sta_ev[0]:
            if clients.lower() == 'all_fdsn':
                if not sta_e[13].lower() == 'arc':
                    station_id = '%s.%s.%s.%s' % (sta_e[0], sta_e[1],
                                                  sta_e[2], sta_e[3])
                    ls_saved_stas_tmp.append(
                        os.path.join(address_events[i], 'BH_RAW', station_id))
            elif clients.lower() == sta_e[13].lower():
                station_id = '%s.%s.%s.%s' % (sta_e[0], sta_e[1],
                                              sta_e[2], sta_e[3])
                ls_saved_stas_tmp.append(os.path.join(address_events[i],
                                                      'BH_RAW', station_id))
            else:
                sys.exit('%s does not exist!' % clients)

        if not input['net'].startswith('_'):
            pattern_sta = '%s.%s.%s.%s' % (input['net'], input['sta'],
                                           input['loc'], input['cha'])
        else:
            pattern_sta = '*.%s.%s.%s' % (input['sta'], input['loc'],
                                          input['cha'])

        ls_saved_stas = []
        for saved_sta in ls_saved_stas_tmp:
            if fnmatch.fnmatch(os.path.basename(saved_sta), pattern_sta):
                ls_saved_stas.append(saved_sta)

        if len(ls_saved_stas) != 0:
            print '\nevent: %s/%s -- %s\n' % (i+1, len(events), clients)
            inst_correct(input, ls_saved_stas, address_events[i], clients)
        else:
            print "There is no station in the directory to correct!"
            print "Address: %s" % address_events[i]
    # pass address for using in create_tar_file
    return address

###################### inst_correct ###############################


def inst_correct(input, ls_saved_stas, address, clients):
    """
    Apply Instrument Coorection on all available stations in the folder

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
    except Exception as e:
        print "\nWARNING: can not create %s" % os.path.join(address, BH_file)
        print "%s\n" % e
        pass

    if input['ic_parallel'] == 'Y':
        print '\nParallel instrument correction with %s processes.\n' \
              % input['ic_np']

        start = 0
        end = len(ls_saved_stas)
        step = (end - start) / input['ic_np'] + 1

        jobs = []
        for index in xrange(input['ic_np']):
            starti = start+index*step
            endi = min(start+(index+1)*step, end)
            p = multiprocessing.Process(target=IC_core_iterate,
                                        args=(ls_saved_stas, clients,
                                              address, BH_file, starti, endi))
            jobs.append(p)
        for i in range(len(jobs)):
            jobs[i].start()

        pp_flag = True
        while pp_flag:
            for proc in jobs:
                if proc.is_alive():
                    time.sleep(1)
                    pp_flag = True
                    break
                else:
                    pp_flag = False
            if not pp_flag:
                print '\nAll the processes are finished...'

    else:
        for i in range(len(ls_saved_stas)):
            IC_core(ls_saved_sta=ls_saved_stas[i], clients=clients,
                    address=address, BH_file=BH_file,
                    inform='%s -- %s/%s' % (clients, i+1, len(ls_saved_stas)))

    t_inst_2 = datetime.now()

    if input['ic_parallel'] == 'Y':
        report_parallel_open = open(os.path.join(address, 'info',
                                                 'report_parallel'), 'a')
        report_parallel_open.writelines('---------------%s---------------\n'
                                        % clients.upper())
        report_parallel_open.writelines('Instrument Correction\n')
        report_parallel_open.writelines('Number of Nodes: %s\n'
                                        % input['ic_np'])
        report_parallel_open.writelines('Number of Stas : %s\n'
                                        % len(ls_saved_stas))
        report_parallel_open.writelines('Total Time     : %s\n'
                                        % (t_inst_2 - t_inst_1))
    print '\nTime for instrument correction of %s stations: %s' \
          % (len(ls_saved_stas), t_inst_2-t_inst_1)

###################### IC_core_iterate ########################################


def IC_core_iterate(ls_saved_stas, clients, address, BH_file, starti, endi):
    """
    Simple iterator over IC_core
    Designed to be used for parallel instrument correction
    """
    for i in range(starti, endi):
        IC_core(ls_saved_sta=ls_saved_stas[i], clients=clients,
                address=address, BH_file=BH_file,
                inform='%s -- %s/%s' % (clients, i+1, len(ls_saved_stas)))

###################### IC_core #########################################


def IC_core(ls_saved_sta, clients, address, BH_file, inform):
    """
    Function that prepare the waveforms for instrument correction and
    divert the program to the right instrument correction function!
    """
    global input

    try:
        if input['ic_obspy_full'] == 'Y':
            tr = read(ls_saved_sta)[0]
            if clients.lower() != 'arc':
                stxml_file = \
                    os.path.join(address, 'Resp',
                                 'STXML.%s' % os.path.basename(ls_saved_sta))
                obspy_fullresp_STXML(trace=tr, stxml_file=stxml_file,
                                     Address=os.path.join(address, BH_file),
                                     unit=input['corr_unit'],
                                     BP_filter=input['pre_filt'],
                                     inform=inform)
            else:
                resp_file = os.path.join(
                    address, 'Resp',
                    'DATALESS.%s' % os.path.basename(ls_saved_sta))
                obspy_fullresp_RESP(trace=tr, resp_file=resp_file,
                                    Address=os.path.join(address, BH_file),
                                    unit=input['corr_unit'],
                                    BP_filter=input['pre_filt'],
                                    inform=inform)
    except Exception as e:
        print e

###################### obspy_fullresp_STXML ###################################


def obspy_fullresp_STXML(trace, stxml_file, Address,
                         unit='DIS', BP_filter=(0.008, 0.012, 3.0, 4.0),
                         inform='N/N'):
    """
    Instrument correction using station_XML --->
    equivalent to full response file steps: detrend, demean, taper, filter,
    deconvolution
    """

    try:
        trace.detrend('linear')
        # To keep it consistant with obspy.remove_response method!
        if unit.lower() == 'dis':
            unit = 'DISP'
            unit_write = 'dis'
        else:
            unit_write = unit.lower()

        inv = read_inventory(stxml_file, format="stationxml")
        trace.attach_response(inv)

        #rm_process = multiprocessing.Process(target=trace.remove_response,
        #                                     args=(unit, 600.0,
        #                                           eval(BP_filter),
        #                                           True, True, 0.05))
        #rm_process.start()
        #rm_process.join()

        # comment out the following line because of
        # segmentation fault inside EVAL_RESP
        trace.remove_response(output=unit, water_level=600.0,
                              pre_filt=eval(BP_filter), zero_mean=True,
                              taper=True, taper_fraction=0.05)

        # Remove the following line to keep the units
        # as it is in the stationXML
        #trace.data *= 1.e9

        trace_identity = '%s.%s.%s.%s' % (trace.stats['network'],
                                          trace.stats['station'],
                                          trace.stats['location'],
                                          trace.stats['channel'])
        if input['mseed'] == 'N':
            trace.write(os.path.join(
                Address, '%s.%s' % (unit_write, trace_identity)), format='SAC')
        else:
            trace.write(os.path.join(
                Address, '%s.%s' % (unit_write, trace_identity)),
                        format='MSEED')

        if unit.lower() == 'disp':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print '%s -- instrument correction to %s for: %s' \
              % (inform, unit_print, trace_identity)

    except Exception as e:
        print '%s -- %s' % (inform, e)

###################### obspy_fullresp_RESP ####################################


def obspy_fullresp_RESP(trace, resp_file, Address, unit='DIS',
                        BP_filter=(0.008, 0.012, 3.0, 4.0), inform='N/N'):
    """
    Instrument correction using dataless seed --->
    equivalent to full response file steps: detrend, demean, taper, filter,
    deconvolution
    """
    dataless_parser = Parser(resp_file)
    seedresp = {'filename': dataless_parser, 'units': unit}

    try:
        trace.detrend('linear')
        trace.simulate(seedresp=seedresp, paz_remove=None, paz_simulate=None,
                       remove_sensitivity=True, simulate_sensitivity=False,
                       water_level=600.0, zero_mean=True, taper=True,
                       taper_fraction=0.05, pre_filt=eval(BP_filter),
                       pitsasim=False, sacsim=True)
        # Remove the following line since we want to keep
        # the units as it is in the stationXML
        #trace.data *= 1.e9
        trace_identity = '%s.%s.%s.%s' % (trace.stats['network'],
                                          trace.stats['station'],
                                          trace.stats['location'],
                                          trace.stats['channel'])
        if input['mseed'] == 'N':
            trace.write(os.path.join(
                Address, '%s.%s' % (unit.lower(), trace_identity)),
                        format='SAC')
        else:
            trace.write(os.path.join(
                Address, '%s.%s' % (unit.lower(), trace_identity)),
                        format='MSEED')

        if unit.lower() == 'dis':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print '%s -- instrument correction to %s for: %s' \
              % (inform, unit_print, trace_identity)

    except Exception as e:
        print '%s -- %s' % (inform, e)

###################### FDSN_ARC_merge ##################################


def FDSN_ARC_merge(input, clients):
    """
    Call "merge_stream" function that merges the
    retrieved waveforms in continuous request
    """

    # Following two if-conditions create address
    # to which merging should be applied
    # Please note that these two conditions can not happen at the same time
    if clients != 'arc':
        clients_name = 'fdsn'
    else:
        clients_name = 'arc'
    if input[clients_name + '_merge_auto'] == 'Y':
        global events
        period = '{0:s}_{1:s}_{2:s}_{3:s}'.\
            format(input['min_date'].split('T')[0],
                   input['max_date'].split('T')[0],
                   str(input['min_mag']),
                   str(input['max_mag']))
        address = os.path.join(input['datapath'], period)

    if input[clients_name + '_merge'] != 'N':
        address = input[clients_name + '_merge']

    events, address_events = quake_info(address, 'info')

    ls_saved_stas_tmp = []
    for i in range(len(events)):

        sta_ev = read_station_event(address_events[i])

        # initialize some parameters which will be used later in merge_stream
        for s_ev in sta_ev[0]:
            if input[clients_name + '_merge_auto'] == 'Y':
                if clients == s_ev[13]:
                    if input['merge_type'] == 'raw':
                        BH_file = 'BH_RAW'
                        network = s_ev[0]
                        network_name = 'raw'
                    elif input['merge_type'] == 'corrected':
                        if input['corr_unit'] == 'DIS':
                            BH_file = 'BH'
                            network = 'dis.%s' % s_ev[0]
                            network_name = 'dis'
                        elif input['corr_unit'] == 'VEL':
                            BH_file = 'BH_' + input['corr_unit']
                            network = 'vel.%s' % s_ev[0]
                            network_name = 'vel'
                        elif input['corr_unit'] == 'ACC':
                            BH_file = 'BH_' + input['corr_unit']
                            network = 'acc.%s' % s_ev[0]
                            network_name = 'acc'

                    station_id = '%s.%s.%s.%s' % (network, s_ev[1],
                                                  s_ev[2], s_ev[3])
                    ls_saved_stas_tmp.append(
                        os.path.join(address_events[i], BH_file, station_id))

            else:
                if input['merge_type'] == 'raw':
                    BH_file = 'BH_RAW'
                    network = s_ev[0]
                    network_name = 'raw'
                elif input['merge_type'] == 'corrected':
                    if input['corr_unit'] == 'DIS':
                        BH_file = 'BH'
                        network = 'dis.%s' % s_ev[0]
                        network_name = 'dis'
                    elif input['corr_unit'] == 'VEL':
                        BH_file = 'BH_' + input['corr_unit']
                        network = 'vel.%s' % s_ev[0]
                        network_name = 'vel'
                    elif input['corr_unit'] == 'ACC':
                        BH_file = 'BH_' + input['corr_unit']
                        network = 'acc.%s' % s_ev[0]
                        network_name = 'acc'

                station_id = '%s.%s.%s.%s' % (network, s_ev[1],
                                              s_ev[2], s_ev[3])
                ls_saved_stas_tmp.append(
                    os.path.join(address_events[i], BH_file, station_id))

    if not input['net'].startswith('_'):
        pattern_sta = '%s.%s.%s.%s' % (input['net'], input['sta'],
                                       input['loc'], input['cha'])
    else:
        pattern_sta = '*.%s.%s.%s' % (input['sta'], input['loc'],
                                      input['cha'])

    ls_saved_stas = []
    for saved_sta in ls_saved_stas_tmp:
        if fnmatch.fnmatch(os.path.basename(saved_sta), pattern_sta):
            ls_saved_stas.append(saved_sta)

    if len(ls_saved_stas) != 0:
        saved_stations_names = []
        for ls_saved_sta in ls_saved_stas:
            saved_stations_names.append(os.path.basename(ls_saved_sta))
        ls_sta = list(set(saved_stations_names))

        ls_address = []
        for add_ev in address_events:
            ls_address.append(os.path.join(add_ev, BH_file))
        print 'Merging the waveforms...'
        merge_stream(ls_address=ls_address, ls_sta=ls_sta,
                     network_name=network_name)
        print 'Finish merging the waveforms'
    else:
        print "\nThere is no waveform to merege!"

###################### merge_stream ####################################


def merge_stream(ls_address, ls_sta, network_name):
    """
    merges the waveforms in continuous requests
    Merging technique: (method=1)
    Discard data of the previous trace assuming the following trace
    contains data with a more correct time value.
    The parameter interpolation_samples specifies the number of samples used
    to linearly interpolate between
    the two traces in order to prevent steps.
    Note that if there are gaps inside, the returned array is still
    a masked array, only if fill_value is set,
    the returned array is a normal array and gaps are filled with fill value.
    No interpolation (interpolation_samples=0):

    Trace 1: AAAAAAAA
    Trace 2:     FFFFFFFF
    1 + 2  : AAAAFFFFFFFF
    """
    global input

    address = os.path.dirname(os.path.dirname(ls_address[0]))

    try:
        os.makedirs(os.path.join(address, 'MERGED-%s' % network_name))
    except Exception as e:
        print "ERROR in creating a directory in %s" % address
        print e
        pass

    for sta in ls_sta:
        for j in range(len(ls_address)):
            if os.path.isfile(os.path.join(ls_address[j], sta)):
                st = read(os.path.join(ls_address[j], sta))
                for k in range(j+1, len(ls_address)):
                    try:
                        st.append(read(os.path.join(ls_address[k], sta))[0])
                    except Exception as e:
                        print "ERROR: can not append to the trace! \n%s" % e

                st.merge(method=1, fill_value=0, interpolation_samples=0)
                trace = st[0]
                trace_identity = '%s.%s.%s.%s' % (trace.stats['network'],
                                                  trace.stats['station'],
                                                  trace.stats['location'],
                                                  trace.stats['channel'])
                if input['mseed'] == 'N':
                    st.write(os.path.join(address, 'MERGED-%s'
                                          % network_name, trace_identity),
                             format='SAC')
                else:
                    st.write(os.path.join(address, 'MERGED-%s'
                                          % network_name, trace_identity),
                             format='MSEED')
                break

###################### plot_tools ############################################


def plot_tools(input, clients):
    """
    Plotting tools
    """

    for i in ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray',
              'plot_ray_gmt', 'plot_epi', 'plot_dt']:
        if input[i] != 'N':
            events, address_events = quake_info(input[i], 'info')

    ls_saved_stas = []
    ls_add_stas = []
    for k in ['plot_se', 'plot_sta', 'plot_ev', 'plot_ray',
              'plot_ray_gmt', 'plot_epi']:
        if input[k] != 'N':
            for i in range(len(events)):
                ls_saved_stas_tmp = []
                ls_add_stas_tmp = []
                sta_ev = read_station_event(address_events[i])

                for j in range(len(sta_ev[0])):
                    if input['plot_type'] == 'raw':
                        BH_file = 'BH_RAW'
                        network = sta_ev[0][j][0]
                    elif input['plot_type'] == 'corrected':
                        if input['corr_unit'] == 'DIS':
                            BH_file = 'BH'
                            network = 'dis.%s' % sta_ev[0][j][0]
                        elif input['corr_unit'] == 'VEL':
                            BH_file = 'BH_%s' % input['corr_unit']
                            network = 'vel.%s' % sta_ev[0][j][0]
                        elif input['corr_unit'] == 'ACC':
                            BH_file = 'BH_%s' % input['corr_unit']
                            network = 'acc.%s' % sta_ev[0][j][0]

                    station_id = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
                                 % (network, sta_ev[0][j][1], sta_ev[0][j][2],
                                    sta_ev[0][j][3], sta_ev[0][j][4],
                                    sta_ev[0][j][5], sta_ev[0][j][6],
                                    sta_ev[0][j][7], sta_ev[0][j][8],
                                    sta_ev[0][j][9], sta_ev[0][j][10],
                                    sta_ev[0][j][11], sta_ev[0][j][12],
                                    sta_ev[0][j][13])

                    if input['plot_all'] != 'Y':
                        if clients == sta_ev[0][j][13]:
                            ls_saved_stas_tmp.append(station_id)
                            ls_add_stas_tmp.append(
                                os.path.join(address_events[i], BH_file,
                                             '%s.%s.%s.%s'
                                             % (network, sta_ev[0][j][1],
                                                sta_ev[0][j][2],
                                                sta_ev[0][j][3])))
                    elif input['plot_all'] == 'Y':
                        ls_saved_stas_tmp.append(station_id)
                        ls_add_stas_tmp.append(
                            os.path.join(address_events[i], BH_file,
                                         '%s.%s.%s.%s'
                                         % (network, sta_ev[0][j][1],
                                            sta_ev[0][j][2], sta_ev[0][j][3])))

                ls_saved_stas.append(ls_saved_stas_tmp)
                ls_add_stas.append(ls_add_stas_tmp)

            for i in range(len(ls_saved_stas)):
                for j in range(len(ls_saved_stas[i])):
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
    one of the following configurations (based on the inputs) will be Plotted:
    station
    event
    both station and event
    ray path
    """
    plt.clf()

    m = Basemap(projection='aeqd', lon_0=-100, lat_0=40)
    #m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90., 120., 30.))
    m.drawmeridians(np.arange(0., 420., 60.))
    m.drawmapboundary()

    pattern_sta = '%s.%s.%s' % (input['sta'], input['loc'], input['cha'])
    for i in range(len(ls_saved_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%"
                         % ('='*int(100.*(i+1)/len(ls_saved_stas)),
                            100.*(i+1)/len(ls_saved_stas)))
        sys.stdout.flush()

        ls_stas = ls_saved_stas[i]
        if not input['evlatmin']:
            input['evlatmin'] = -90
            input['evlatmax'] = +90
            input['evlonmin'] = -180
            input['evlonmax'] = +180
        if input['plot_se'] != 'N' or input['plot_ev'] != 'N' or \
                        input['plot_ray'] != 'N':
            if not input['evlatmin'] <= float(ls_stas[0][9]) <= \
                    input['evlatmax'] or \
               not input['evlonmin'] <= float(ls_stas[0][10]) <= \
                       input['evlonmax'] or \
               not input['max_depth'] <= float(ls_stas[0][11]) <= \
                       input['min_depth'] or \
               not input['min_mag'] <= float(ls_stas[0][12]) \
                       <= input['max_mag']:
                continue

        if input['plot_se'] != 'N' or input['plot_ev'] != 'N' or \
                        input['plot_ray'] != 'N':
            x_ev, y_ev = m(float(ls_stas[0][10]), float(ls_stas[0][9]))
            m.scatter(x_ev, y_ev, math.log(float(ls_stas[0][12])) ** 6,
                      color="red", marker="o", edgecolor="black", zorder=10)

        for j in range(len(ls_stas)):
            try:
                station_name = '%s.%s.%s' % (ls_stas[j][1],
                                             ls_stas[j][2],
                                             ls_stas[j][3])
                station_ID = ls_stas[j][0] + '.' + station_name

                if not fnmatch.fnmatch(station_name, pattern_sta):
                    continue
                if not input['mlat_rbb']:
                    input['mlat_rbb'] = -90.0
                    input['Mlat_rbb'] = +90.0
                    input['mlon_rbb'] = -180.0
                    input['Mlon_rbb'] = +180.0
                if not input['mlat_rbb'] <= float(ls_stas[j][4]) \
                        <= input['Mlat_rbb'] or \
                   not input['mlon_rbb'] <= float(ls_stas[j][5]) \
                           <= input['Mlon_rbb']:
                    continue
                st_lat = float(ls_stas[j][4])
                st_lon = float(ls_stas[j][5])
                ev_lat = float(ls_stas[j][9])
                ev_lon = float(ls_stas[j][10])
                ev_mag = float(ls_stas[j][12])

                if input['plot_ray'] != 'N':
                    m.drawgreatcircle(ev_lon, ev_lat,
                                      st_lon, st_lat, alpha=0.1)
                if input['plot_se'] != 'N' or input['plot_sta'] != 'N' or \
                                input['plot_ray'] != 'N':
                    x_sta, y_sta = m(st_lon, st_lat)
                    m.scatter(x_sta, y_sta, 40, color='blue', marker="v",
                              edgecolor="black", zorder=10)

            except Exception as e:
                print 'WARNING: %s' % e
                pass

    print '\nSaving the plot in the following address:'
    print os.path.join(input['plot_save'], 'plot.%s' % input['plot_format'])
    plt.savefig(os.path.join(input['plot_save'],
                             'plot.%s' % input['plot_format']))

###################### plot_ray_gmt ####################################


def plot_ray_gmt(input, ls_saved_stas):
    """
    Plot: stations, events and ray paths for the specified directory using GMT
    """
    evsta_info_open = open(os.path.join(input['plot_save'],
                                        'evsta_info.txt'), 'w')
    evsta_plot_open = open(os.path.join(input['plot_save'],
                                        'evsta_plot.txt'), 'w')
    ev_plot_open = open(os.path.join(input['plot_save'],
                                     'ev_plot.txt'), 'w')
    sta_plot_open = open(os.path.join(input['plot_save'],
                                      'sta_plot.txt'), 'w')

    ls_sta = []
    for i in range(len(ls_saved_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%"
                         % ('='*int(100.*(i+1)/len(ls_saved_stas)),
                            100.*(i+1)/len(ls_saved_stas)))
        sys.stdout.flush()

        ls_stas = ls_saved_stas[i]
        if not input['evlatmin']:
            input['evlatmin'] = -90
            input['evlatmax'] = +90
            input['evlonmin'] = -180
            input['evlonmax'] = +180
        if not input['evlatmin'] <= float(ls_stas[0][9]) \
                <= input['evlatmax'] or \
           not input['evlonmin'] <= float(ls_stas[0][10]) \
                   <= input['evlonmax'] or \
           not input['max_depth'] <= float(ls_stas[0][11]) \
                   <= input['min_depth'] or \
           not input['min_mag'] <= float(ls_stas[0][12]) \
                   <= input['max_mag']:
            continue
        ev_plot_open.writelines('%s %s \n'
                                % (round(float(ls_stas[0][10]), 5),
                                   round(float(ls_stas[0][9]), 5)))
        pattern_sta = '%s.%s.%s' % (input['sta'], input['loc'], input['cha'])

        for j in range(len(ls_stas)):
            station_name = '%s.%s.%s' % (ls_stas[j][1],
                                         ls_stas[j][2],
                                         ls_stas[j][3])
            station_ID = '%s.%s' % (ls_stas[j][0], station_name)

            if not fnmatch.fnmatch(station_name, pattern_sta):
                continue
            if not input['mlat_rbb']:
                    input['mlat_rbb'] = -90.0
                    input['Mlat_rbb'] = +90.0
                    input['mlon_rbb'] = -180.0
                    input['Mlon_rbb'] = +180.0
            if not input['mlat_rbb'] <= float(ls_stas[j][4]) \
                    <= input['Mlat_rbb'] or \
               not input['mlon_rbb'] <= float(ls_stas[j][5]) \
                       <= input['Mlon_rbb']:
                continue

            evsta_info_open.writelines('%s , %s , \n' % (ls_stas[j][8],
                                                         station_ID))

            evsta_plot_open.writelines(
                '> -G%s/%s/%s\n%s %s %s\n%s %s %s \n'
                % (int(random.random()*256), int(random.random()*256),
                   int(random.random()*256), round(float(ls_stas[j][10]), 5),
                   round(float(ls_stas[j][9]), 5), random.random(),
                   round(float(ls_stas[j][5]), 5),
                   round(float(ls_stas[j][4]), 5), random.random()))
            ls_sta.append([station_ID, [str(round(float(ls_stas[j][4]), 5)),
                                        str(round(float(ls_stas[j][5]), 5))]])

    for k in range(len(ls_sta)):
        sta_plot_open.writelines('%s %s \n'
                                 % (ls_sta[k][1][1], ls_sta[k][1][0]))

    evsta_info_open.close()
    evsta_plot_open.close()
    ev_plot_open.close()
    sta_plot_open.close()

    pwd_str = os.getcwd()

    os.chdir(input['plot_save'])
    os.system('psbasemap -Rd -JK180/9i -B45g30 -K > output.ps')
    os.system('pscoast -Rd -JK180/9i -B45g30:."World-wide Ray Path Coverage": '
              '-Dc -A1000 -Glightgray -Wthinnest -t0 -O -K >> output.ps')
    os.system('psxy ./evsta_plot.txt -JK180/9i -Rd -O -K -W0.2 -t85 >> '
              'output.ps')
    os.system('psxy ./sta_plot.txt -JK180/9i -Rd -Si0.2c -Gblue -O -K >>'
              ' output.ps')
    os.system('psxy ./ev_plot.txt -JK180/9i -Rd -Sa0.28c -Gred -O >>'
              ' output.ps')
    os.system('ps2raster output.ps -A -P -Tf')

    os.system('mv output.ps plot.ps')
    os.system('mv output.pdf plot.pdf')

    os.system('xdg-open plot.pdf')

    os.chdir(pwd_str)

###################### plot_epi ########################################


def plot_epi(input, ls_add_stas, ls_saved_stas):
    """
    Plot arranged waveforms by epicentral distance versus time
    """

    plt.clf()

    for target in range(len(ls_add_stas)):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%"
                         % ('='*int(100.*(target+1)/len(ls_add_stas)),
                            100.*(target+1)/len(ls_add_stas)))
        sys.stdout.flush()

        for i in range(len(ls_add_stas[target])):
            try:
                tr = read(ls_add_stas[target][i])[0]
                tr.normalize()
                dist = locations2degrees(float(ls_saved_stas[target][i][9]),
                                         float(ls_saved_stas[target][i][10]),
                                         float(ls_saved_stas[target][i][4]),
                                         float(ls_saved_stas[target][i][5]))
                if input['min_epi'] <= dist <= input['max_epi']:
                    plt.plot(
                        np.linspace(0,
                                    (tr.stats.npts-1)/tr.stats.sampling_rate,
                                    tr.stats.npts), tr.data + dist,
                        color='black')
            except Exception as e:
                print 'WARNING: %s' % e
                pass
            plt.xlabel('Time (sec)')
            plt.ylabel('Epicentral distance (deg)')

    print '\nSaving the plot in the following address:'
    print os.path.join(input['plot_save'], 'plot.%s' % input['plot_format'])
    plt.savefig(os.path.join(input['plot_save'],
                             'plot.%s' % input['plot_format']))

###################### plot_dt #########################################


def plot_dt(input, address_events):
    """
    Plot stored Data(MB) as a function of Time(Sec)
    """

    for i in range(len(address_events)):
        for client_time in ['time_fdsn', 'time_arc']:
            print 'Event address: %s' % address_events[i]
            if os.path.isfile(os.path.join(address_events[i], 'info',
                                           client_time)):
                plt.clf()
                dt_open = open(os.path.join(address_events[i], 'info',
                                            client_time))
                dt_read = dt_open.readlines()
                for j in range(len(dt_read)):
                    dt_read[j] = dt_read[j].split(',')

                time_single = 0
                succ = 0
                fail = 0
                MB_all = []
                time_all = []

                for k in range(len(dt_read)):
                    time_single += eval(dt_read[k][4]) + \
                                   eval(dt_read[k][5])/(1024.**2)
                    time_all.append(time_single)

                    MB_single = eval(dt_read[k][6])
                    MB_all.append(MB_single)

                    if dt_read[k][7] == '+':
                        single_succ = plt.scatter(time_single,
                                                  MB_single,
                                                  s=1, c='b',
                                                  edgecolors='b', marker='o',
                                                  label='Serial (successful)')
                        succ += 1
                    elif dt_read[k][7] == '-':
                        single_fail = plt.scatter(time_single,
                                                  MB_single,
                                                  s=1, c='r',
                                                  edgecolors='r', marker='o',
                                                  label='Serial (failed)')
                        fail += 1

                if input['req_parallel'] == 'Y':
                    rep_par_open = open(os.path.join(address_events[i],
                                                     'info',
                                                     'report_parallel'))
                    rep_par_read = rep_par_open.readlines()
                    time_parallel = \
                        eval(rep_par_read[4].split(',')[0]) + \
                        eval(rep_par_read[4].split(',')[1])/(1024.**2)
                    MB_parallel = eval(rep_par_read[4].split(',')[2])
                    trans_rate_parallel = MB_parallel/time_parallel*60
                    parallel_succ = plt.scatter(time_parallel,
                                                MB_parallel,
                                                s=30, c='r',
                                                edgecolors='r', marker='o',
                                                label='Parallel')

                time_array = np.array(time_all)
                MB_array = np.array(MB_all)

                poly = np.poly1d(np.polyfit(time_array, MB_array, 1))
                #time_poly = np.linspace(0, time_all[-1], len(time_all))
                plt.plot(time_array, poly(time_array), 'k--')

                trans_rate = (poly(time_array[-1])-
                              poly(time_array[0]))/\
                             (time_array[-1]-time_array[0])*60

                plt.xlabel('Time (sec)', size='large', weight='bold')
                plt.ylabel('Stored Data (MB)', size='large', weight='bold')
                plt.xticks(size='large', weight='bold')
                plt.yticks(size='large', weight='bold')
                plt_title = \
                    '%s\nAll: %s--Succ: %s (%s%%)-Fail: %s (%s%%)--%sMb/min' \
                    % (client_time.split('_')[1].upper(), (succ + fail), succ,
                       round(float(succ)/(succ + fail)*100., 1), fail,
                       round(float(fail)/(succ + fail)*100., 1),
                       round(trans_rate, 2))
                plt.title(plt_title, size='x-large')

                if input['req_parallel'] == 'Y':
                    plt.legend([single_succ, parallel_succ],
                               ['Serial', 'Parallel'], loc=4)

                plt.savefig(os.path.join(address_events[i], 'info',
                                         'Data-Time_%s.%s'
                                         % (client_time.split('_')[1],
                                            input['plot_format'])))

###################### create_folders_files ############################


def create_folders_files(events, eventpath):
    """
    Create required folders and files in the event folder(s)
    """

    for i in range(len(events)):
        try:
            os.makedirs(os.path.join(eventpath, events[i]['event_id'],
                                     'BH_RAW'))
            os.makedirs(os.path.join(eventpath, events[i]['event_id'],
                                     'Resp'))
            os.makedirs(os.path.join(eventpath, events[i]['event_id'],
                                     'info'))
        except Exception as e:
            print 'ERROR: %s' % e
            pass

    for i in range(len(events)):
        report = open(os.path.join(eventpath, events[i]['event_id'],
                                   'info', 'report_st'), 'a+')
        report.close()

    for i in range(len(events)):
        exception_file = open(os.path.join(eventpath, events[i]['event_id'],
                                           'info', 'exception'), 'a+')
        exception_file.writelines('\n' + events[i]['event_id'] + '\n')
        exception_file.close()

        syn_file = open(os.path.join(eventpath, events[i]['event_id'],
                                     'info', 'station_event'), 'a+')
        syn_file.close()

    for i in range(len(events)):
        quake_file = open(os.path.join(eventpath, events[i]['event_id'],
                                       'info', 'quake'), 'a+')

        quake_file.writelines(repr(events[i]['datetime'].year).rjust(15) +
                              repr(events[i]['datetime'].julday).rjust(15)
                              + '\n')
        quake_file.writelines(repr(events[i]['datetime'].hour).rjust(15) +
                              repr(events[i]['datetime'].minute).rjust(15) +
                              repr(events[i]['datetime'].second).rjust(15) +
                              repr(events[i]['datetime'].microsecond).rjust(15)
                              + '\n')

        quake_file.writelines(' '*(15 - len('%.5f' % events[i]['latitude'])) +
                              '%.5f' % events[i]['latitude'] +
                              ' '*(15 - len('%.5f' % events[i]['longitude'])) +
                              '%.5f\n' % events[i]['longitude'])
        quake_file.writelines(' '*(15 - len('%.5f' % abs(events[i]['depth'])))
                              + '%.5f\n' % abs(events[i]['depth']))
        quake_file.writelines(' '*(15 -
                                   len('%.5f' % abs(events[i]['magnitude'])))
                              + '%.5f\n'
                              % abs(events[i]['magnitude']))
        quake_file.writelines(' '*(15 - len(events[i]['event_id'])) +
                              events[i]['event_id'] + '-' + '\n')

        quake_file.writelines(repr(events[i]['t1'].year).rjust(15) +
                              repr(events[i]['t1'].julday).rjust(15) +
                              repr(events[i]['t1'].month).rjust(15) +
                              repr(events[i]['t1'].day).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['t1'].hour).rjust(15) +
                              repr(events[i]['t1'].minute).rjust(15) +
                              repr(events[i]['t1'].second).rjust(15) +
                              repr(events[i]['t1'].microsecond).rjust(15) +
                              '\n')

        quake_file.writelines(repr(events[i]['t2'].year).rjust(15) +
                              repr(events[i]['t2'].julday).rjust(15) +
                              repr(events[i]['t2'].month).rjust(15) +
                              repr(events[i]['t2'].day).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['t2'].hour).rjust(15) +
                              repr(events[i]['t2'].minute).rjust(15) +
                              repr(events[i]['t2'].second).rjust(15) +
                              repr(events[i]['t2'].microsecond).rjust(15) +
                              '\n')

###################### writesac_all ####################################


def writesac_all(i, address_events):
    """
    Change the format of a trace to SAC and fill in the header information
    """
    sta_ev = read_station_event(address_events[i])
    ls_saved_stas = []

    for j in range(len(sta_ev[0])):
        station_id = '%s.%s.%s.%s' % (sta_ev[0][j][0],
                                      sta_ev[0][j][1],
                                      sta_ev[0][j][2],
                                      sta_ev[0][j][3])
        ls_saved_stas.append(os.path.join(address_events[i],
                                          'BH_RAW', station_id))
    for j in range(len(sta_ev[0])):
        try:
            st = read(ls_saved_stas[j])
            st[0].write(ls_saved_stas[j], format='SAC')
            tr = read(ls_saved_stas[j])[0]
            if sta_ev[0][j][4]:
                tr.stats.sac.stla = float(sta_ev[0][j][4])
            if sta_ev[0][j][5]:
                tr.stats.sac.stlo = float(sta_ev[0][j][5])
            if sta_ev[0][j][6]:
                tr.stats.sac.stel = float(sta_ev[0][j][6])
            if sta_ev[0][j][7]:
                tr.stats.sac.stdp = float(sta_ev[0][j][7])

            if sta_ev[0][j][9]:
                tr.stats.sac.evla = float(sta_ev[0][j][9])
            if sta_ev[0][j][10]:
                tr.stats.sac.evlo = float(sta_ev[0][j][10])
            if sta_ev[0][j][11]:
                tr.stats.sac.evdp = float(sta_ev[0][j][11])
            if sta_ev[0][j][12]:
                tr.stats.sac.mag = float(sta_ev[0][j][12])

            tr.write(ls_saved_stas[j], format='SAC')

        except Exception as e:
            print '\nWARNING: %s' % e
            print ls_saved_stas[j]
            print '------------------'

###################### writesac ########################################


def writesac(address_st, sta_info, ev_info):
    """
    Change the format of a trace to SAC and fill in the header information
    """

    st = read(address_st)
    st[0].write(address_st, format='SAC')
    st = read(address_st)

    if sta_info['latitude']:
        st[0].stats.sac.stla = sta_info['latitude']
    if sta_info['longitude']:
        st[0].stats.sac.stlo = sta_info['longitude']
    if sta_info['elevation']:
        st[0].stats.sac.stel = sta_info['elevation']
    if sta_info['depth']:
        st[0].stats.sac.stdp = sta_info['depth']

    if ev_info['latitude']:
        st[0].stats.sac.evla = ev_info['latitude']
    if ev_info['longitude']:
        st[0].stats.sac.evlo = ev_info['longitude']
    if ev_info['depth']:
        st[0].stats.sac.evdp = ev_info['depth']
    if ev_info['magnitude']:
        st[0].stats.sac.mag = ev_info['magnitude']

    st[0].write(address_st, format='SAC')

###################### rm_duplicate ####################################


def rm_duplicate(all_sta_avail, address):
    """
    remove duplicates and give back the required list for updating
    """

    id_avai_stas = []
    for sta in all_sta_avail:
        if sta[2] == '--' or sta[2] == '  ':
            sta[2] = ''
        if len(sta) == 7:
            id_avai_stas.append('%s_%s_%s_%s_%s_%s_%s'
                                % (sta[0], sta[1], sta[2],
                                   sta[3], sta[4], sta[5], sta[6]))
        elif len(sta) == 8:
            id_avai_stas.append('%s_%s_%s_%s_%s_%s_%s_%s'
                                % (sta[0], sta[1], sta[2],
                                   sta[3], sta[4], sta[5], sta[6], sta[7]))

    sta_ev_saved = read_station_event(address)

    id_all_saved_stas = []
    for saved_sta in sta_ev_saved[0]:
        id_all_saved_stas.append('%s_%s_%s_%s' % (saved_sta[0], saved_sta[1],
                                                  saved_sta[2], saved_sta[3]))

    stas_update = copy.deepcopy(id_avai_stas)
    del_num = []
    for saved_sta in id_all_saved_stas:
        for j in range(len(stas_update)):
            if saved_sta in stas_update[j]:
                del_num.append(j)

    del_num.sort(reverse=True)
    for dn in del_num:
        del stas_update[dn]

    for i in range(len(stas_update)):
        stas_update[i] = stas_update[i].split('_')

    stas_update.sort()
    print '------------------------------------------'
    print 'Info:'
    print 'Number of all saved stations:     %s' % len(id_all_saved_stas)
    print 'Number of all available stations: %s' % len(id_avai_stas)
    print 'Number of stations to update for: %s' % len(stas_update)
    print '------------------------------------------'

    return stas_update

###################### read_station_event ##############################


def read_station_event(address):
    """
    Reads the station_event file ("info" folder)
    """

    if not os.path.isabs(address):
        address = os.path.abspath(address)

    if os.path.basename(address) == 'info':
        target_add = [address]
    elif locate(address, 'info'):
        target_add = locate(address, 'info')
    else:
        print 'Error: There is no "info" directory in %s' % address

    sta_ev = []
    for t_add in target_add:
        if os.path.isfile(os.path.join(t_add, 'station_event')):
            sta_file_open = open(os.path.join(t_add, 'station_event'), 'r')
        else:
            print '====================================='
            print 'station_event could not be found'
            print 'Start Creating the station_event file'
            print '====================================='
            create_station_event(address=t_add)
            sta_file_open = open(os.path.join(t_add, 'station_event'), 'r')
        sta_file = sta_file_open.readlines()
        sta_ev_tmp = []
        for s_file in sta_file:
            sta_ev_tmp.append(s_file.split(','))
        sta_ev.append(sta_ev_tmp)

    return sta_ev

###################### create_station_event ############################


def create_station_event(address):
    """
    Creates the station_event file ("info" folder)
    """

    event_address = os.path.dirname(address)
    if os.path.isdir(os.path.join(event_address, 'BH_RAW')):
        sta_address = os.path.join(event_address, 'BH_RAW')
    elif os.path.isdir(os.path.join(event_address, 'BH')):
        sta_address = os.path.join(event_address, 'BH')
    else:
        print 'ERROR: There is no reference (BH_RAW or BH) ' \
              'to create station_event file!'
        sys.exit()

    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))
    ls_stas.sort()

    print '%s stations found in %s' % (len(ls_stas), sta_address)

    for i in range(len(ls_stas)):
        print i,

        sta_file_open = open(os.path.join(address, 'station_event'), 'a')

        try:
            sta = read(ls_stas[i])[0]
        except Exception as e:
            print 'WARNING: NOT readable: %s\n%s' % (ls_stas[i], e)

        sta_stats = sta.stats
        try:
            sta_info = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,iris,\n' \
                       % (sta_stats.network,
                          sta_stats.station,
                          sta_stats.location,
                          sta_stats.channel,
                          sta_stats.sac.stla,
                          sta_stats.sac.stlo,
                          sta_stats.sac.stel,
                          sta_stats.sac.stdp,
                          os.path.basename(event_address),
                          sta_stats.sac.evla,
                          sta_stats.sac.evlo,
                          sta_stats.sac.evdp,
                          sta_stats.sac.mag)
        except Exception as e:
            print '\nWARNING: Can not read all the required information ' \
                  'from the headers, some of them are presumed!'
            print e
            sta_info = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,iris,\n' \
                       % (sta_stats.network,
                          sta_stats.station,
                          sta_stats.location,
                          sta_stats.channel,
                          -12345.0, -12345.0, -12345.0, -12345.0,
                          os.path.basename(event_address),
                          -12345.0, -12345.0, -12345.0, -12345.0)

        sta_file_open.writelines(sta_info)
        sta_file_open.close()
    print 'station_event file is created in %s' % os.path.join(address,
                                                               'station_event')

###################### quake_info ######################################


def quake_info(address, target):
    """
    Reads the info in quake file ("info" folder)
    """

    events = []
    target_add = locate(address, target)
    for t_add in target_add:
        if not os.path.isfile(os.path.join(t_add, 'quake')):
            print '='*64
            print 'quake file could not be found'
            print 'Start Creating the quake file'
            print 'WARNING: it uses just one seismogram to ' \
                  're-create the quake file'
            print '='*64
            quake_create(address_info=t_add)
        quake_file_open = open(os.path.join(t_add, 'quake'), 'r')
        quake_file = quake_file_open.readlines()

        quake_read_tmp = []
        for q_file_l in quake_file:
            for q_l_item in q_file_l.split():
                try:
                    quake_read_tmp.append(float(q_l_item))
                except ValueError:
                    pass

        if len(quake_read_tmp) < 20:
            print '====================='
            print 'Modify the quake file'
            print '====================='
            quake_modify(quake_item=quake_read_tmp, address_info=t_add)

            quake_file_open = open(os.path.join(t_add, 'quake'), 'r')
            quake_file = quake_file_open.readlines()

            quake_read_tmp = []
            for q_file_l in quake_file:
                for q_l_item in q_file_l.split():
                    try:
                        quake_read_tmp.append(float(q_l_item))
                    except ValueError:
                        pass

        quake_d = {'year0': int(quake_read_tmp[0]),
                   'julday0': int(quake_read_tmp[1]),
                   'hour0': int(quake_read_tmp[2]),
                   'minute0': int(quake_read_tmp[3]),
                   'second0': int(quake_read_tmp[4]),
                   'lat': float(quake_read_tmp[6]),
                   'lon': float(quake_read_tmp[7]),
                   'dp': float(quake_read_tmp[8]),
                   'mag': float(quake_read_tmp[9]),
                   'year1': int(quake_read_tmp[10]),
                   'julday1': int(quake_read_tmp[11]),
                   'hour1': int(quake_read_tmp[14]),
                   'minute1': int(quake_read_tmp[15]),
                   'second1': int(quake_read_tmp[16]),
                   'year2': int(quake_read_tmp[18]),
                   'julday2': int(quake_read_tmp[19]),
                   'hour2': int(quake_read_tmp[22]),
                   'minute2': int(quake_read_tmp[23]),
                   'second2': int(quake_read_tmp[24])}

        quake_t0 = UTCDateTime(year=quake_d['year0'],
                               julday=quake_d['julday0'],
                               hour=quake_d['hour0'],
                               minute=quake_d['minute0'],
                               second=quake_d['second0'])
        quake_t1 = UTCDateTime(year=quake_d['year1'],
                               julday=quake_d['julday1'],
                               hour=quake_d['hour1'],
                               minute=quake_d['minute1'],
                               second=quake_d['second1'])
        quake_t2 = UTCDateTime(year=quake_d['year2'],
                               julday=quake_d['julday2'],
                               hour=quake_d['hour2'],
                               minute=quake_d['minute2'],
                               second=quake_d['second2'])

        events.append({'author': 'NONE',
                       'datetime': quake_t0,
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
    for t_add in target_add:
        address_event.append(os.path.dirname(t_add))

    return events, address_event

###################### quake_create ####################################


def quake_create(address_info):
    """
    if there is no quake file in the info folder
    it will be created based on the data available
    in the BH_RAW or BH file
    """

    quake_file = open(os.path.join(address_info, 'quake'), 'w')
    address = os.path.normpath(os.path.join(address_info, '..'))

    if os.path.isdir(os.path.join(address, 'BH_RAW')):
        sta_address = os.path.join(address, 'BH_RAW')
    elif os.path.isdir(os.path.join(address, 'BH')):
        sta_address = os.path.join(address, 'BH')
    else:
        print '\nERROR: There is no reference (BH_RAW or BH) ' \
              'to create a quake file...'

    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))

    sta = read(ls_stas[0])[0]
    sta_stats = sta.stats
    print '\nCreate the quake file based on: \n%s' % ls_stas[0]

    try:
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % sta_stats.sac.evla)) +
                              '%.5f' % sta_stats.sac.evla +
                              ' '*(15 - len('%.5f' % sta_stats.sac.evlo)) +
                              '%.5f' % sta_stats.sac.evlo + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(sta_stats.sac.evdp)))
                              + '%.5f' % abs(sta_stats.sac.evdp) + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(sta_stats.sac.mag))) +
                              '%.5f' % abs(sta_stats.sac.mag) + '\n')
        quake_file.writelines(' '*(15 - len(address.split('/')[-1])) +
                              address.split('/')[-1] + '-' + '\n')

        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              repr(sta_stats.starttime.month).rjust(15) +
                              repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')

        sta_stats_endtime = sta_stats.starttime + \
                            (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file.writelines(repr(sta_stats_endtime.year).rjust(15) +
                              repr(sta_stats_endtime.julday).rjust(15) +
                              repr(sta_stats_endtime.month).rjust(15) +
                              repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                              repr(sta_stats_endtime.minute).rjust(15) +
                              repr(sta_stats_endtime.second).rjust(15) +
                              repr(sta_stats_endtime.microsecond).rjust(15) +
                              '\n')

    except Exception as e:
        print '\n================='
        print 'WARNING: Can not read all the required information ' \
              'from the header'
        print 'Following parameters are presumed:'
        print 'evla=0, evlo=0, dp=-12345.0, mag=-12345.0'
        print 'Exception: %s' % e
        print '=================\n'
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % 0.0)) + '%.5f' % 0.0 +
                              ' '*(15 - len('%.5f' % 0.0)) + '%.5f' % 0.0
                              + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(-12345.0))) +
                              '%.5f' % abs(-12345.0) + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(-12345.0))) +
                              '%.5f' % abs(-12345.0) + '\n')
        quake_file.writelines(' '*(15 - len(address.split('/')[-1])) +
                              address.split('/')[-1] + '-' + '\n')

        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              repr(sta_stats.starttime.month).rjust(15) +
                              repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')

        sta_stats_endtime = sta_stats.starttime + \
                            (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file.writelines(repr(sta_stats_endtime.year).rjust(15) +
                              repr(sta_stats_endtime.julday).rjust(15) +
                              repr(sta_stats_endtime.month).rjust(15) +
                              repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                              repr(sta_stats_endtime.minute).rjust(15) +
                              repr(sta_stats_endtime.second).rjust(15) +
                              repr(sta_stats_endtime.microsecond).rjust(15) +
                              '\n')
    quake_file.close()

###################### quake_modify ####################################


def quake_modify(quake_item, address_info):
    """
    if the quake file does not contain all the required parameters
    it will be modified based on the available data in BH_RAW or BH directories
    """

    quake_file_new = open(os.path.join(address_info, 'quake'), 'w')
    address = os.path.normpath(os.path.join(address_info, '..'))

    if os.path.isdir(os.path.join(address, 'BH_RAW')):
        sta_address = os.path.join(address, 'BH_RAW')
    elif os.path.isdir(os.path.join(address, 'BH')):
        sta_address = os.path.join(address, 'BH')
    else:
        print '\nERROR: There is no reference (BH_RAW or BH) ' \
              'to modify the quake file...'

    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))

    sta = read(ls_stas[0])[0]
    sta_stats = sta.stats
    print '\nCreate the quake file based on: \n%s' % ls_stas[0]

    try:
        quake_file_new.writelines(repr(int(quake_item[0])).rjust(15) +
                                  repr(int(quake_item[1])).rjust(15) + '\n')
        quake_file_new.writelines(repr(int(quake_item[2])).rjust(15) +
                                  repr(int(quake_item[3])).rjust(15) +
                                  repr(int(quake_item[4])).rjust(15) +
                                  repr(int(quake_item[5])).rjust(15) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % quake_item[6])) +
                                  '%.5f' % quake_item[6] +
                                  ' '*(15 - len('%.5f' % quake_item[7])) +
                                  '%.5f' % quake_item[7] + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % abs(quake_item[8]))) +
                                  '%.5f' % abs(quake_item[8]) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f'
                                                % abs(sta_stats.sac.mag))) +
                                  '%.5f' % abs(sta_stats.sac.mag) + '\n')
        quake_file_new.writelines(' '*(15 - len(address.split('/')[-1])) +
                                  address.split('/')[-1] + '-' + '\n')

        quake_file_new.writelines(repr(sta_stats.starttime.year).rjust(15) +
                                  repr(sta_stats.starttime.julday).rjust(15) +
                                  repr(sta_stats.starttime.month).rjust(15) +
                                  repr(sta_stats.starttime.day).rjust(15) +
                                  '\n')
        quake_file_new.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                                  repr(sta_stats.starttime.minute).rjust(15) +
                                  repr(sta_stats.starttime.second).rjust(15) +
                                  repr(sta_stats.starttime.microsecond).
                                  rjust(15) + '\n')

        sta_stats_endtime = sta_stats.starttime + \
                            (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file_new.writelines(repr(sta_stats_endtime.year).rjust(15) +
                                  repr(sta_stats_endtime.julday).rjust(15) +
                                  repr(sta_stats_endtime.month).rjust(15) +
                                  repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                                  repr(sta_stats_endtime.minute).rjust(15) +
                                  repr(sta_stats_endtime.second).rjust(15) +
                                  repr(sta_stats_endtime.microsecond).rjust(15)
                                  + '\n')
    except Exception as e:
        print '\n================='
        print 'WARNING: Can not read all the required information ' \
              'from the header'
        print 'Following parameters are presumed:'
        print 'evla=0, evlo=0, dp=-12345.0, mag=-12345.0'
        print 'Exception: %s' % e
        print '=================\n'
        quake_file_new.writelines(repr(int(quake_item[0])).rjust(15) +
                                  repr(int(quake_item[1])).rjust(15) + '\n')
        quake_file_new.writelines(repr(int(quake_item[2])).rjust(15) +
                                  repr(int(quake_item[3])).rjust(15) +
                                  repr(int(quake_item[4])).rjust(15) +
                                  repr(int(quake_item[5])).rjust(15) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % quake_item[6])) +
                                  '%.5f' % quake_item[6] +
                                  ' '*(15 - len('%.5f' % quake_item[7])) +
                                  '%.5f' % quake_item[7] + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % abs(quake_item[8])))
                                  + '%.5f' % abs(quake_item[8]) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % abs(-12345.0)))
                                  + '%.5f' % abs(-12345.0) + '\n')
        quake_file_new.writelines(' '*(15 - len(address.split('/')[-1])) +
                                  address.split('/')[-1] + '-' + '\n')

        quake_file_new.writelines(repr(sta_stats.starttime.year).rjust(15) +
                                  repr(sta_stats.starttime.julday).rjust(15) +
                                  repr(sta_stats.starttime.month).rjust(15) +
                                  repr(sta_stats.starttime.day).rjust(15) +
                                  '\n')
        quake_file_new.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                                  repr(sta_stats.starttime.minute).rjust(15) +
                                  repr(sta_stats.starttime.second).rjust(15) +
                                  repr(sta_stats.starttime.microsecond).
                                  rjust(15) + '\n')

        sta_stats_endtime = sta_stats.starttime + \
                            (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file_new.writelines(repr(sta_stats_endtime.year).rjust(15) +
                                  repr(sta_stats_endtime.julday).rjust(15) +
                                  repr(sta_stats_endtime.month).rjust(15) +
                                  repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                                  repr(sta_stats_endtime.minute).rjust(15) +
                                  repr(sta_stats_endtime.second).rjust(15) +
                                  repr(sta_stats_endtime.microsecond).rjust(15)
                                  + '\n')
    quake_file_new.close()

###################### create_tar_file ########################################


def create_tar_file(input, address):
    """
    create a tar file out of a given directory
    """
    events, address_events = quake_info(address, 'info')
    for i in range(len(events)):
        # ---------Creating Tar files (Waveform files)
        if input['zip_w'] == 'Y':
            print 'Compressing Raw files...'
            path = os.path.join(address_events[i], 'BH_RAW')
            tar_file = os.path.join(path, 'BH_RAW.tar')
            files = '*.*.*.*'
            compress_gzip(path=path, tar_file=tar_file, files=files)

        # ---------Creating Tar files (Response files)
        if input['zip_r'] == 'Y':
            print 'Compressing Resp files...'
            path = os.path.join(address_events[i], 'Resp')
            tar_file = os.path.join(path, 'Resp.tar')
            files = '*.*.*.*'
            compress_gzip(path=path, tar_file=tar_file, files=files)

###################### compress_gzip ###################################


def compress_gzip(path, tar_file, files):
    """
    Compressing files and creating a tar file
    """
    tar = tarfile.open(tar_file, "w:gz")
    os.chdir(path)

    for infile in glob.glob(os.path.join(path, files)):
        print '.',
        tar.add(os.path.basename(infile))
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

    fromaddr = 'obspyDMT'
    toaddrs = input['email']

    msg = "request at:\n%s\n\nfinished at:\n%s\n\nTotal time:\n%s" \
          % (t1_str, t2_str, t2_pro-t1_pro)

    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddr, toaddrs, msg)

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
        st_argus += '%s: %s\n' %(item, inputs[item])
    logger_open = open(address, 'w')
    logger_open.write(st_argus)
    logger_open.close()

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


def locate(root='.', target='info'):
    """
    Locates a subdirectory within a directory.
    """

    matches = []
    for root, dirnames, filenames in os.walk(root):
        for dirname in fnmatch.filter(dirnames, target):
            matches.append(os.path.join(root, dirname))

    return matches

########################################################################
########################################################################
########################################################################


def main():

    global t1_pro, t1_str
    t1_pro = time.time()
    t1_str = datetime.now()

    # Run the main program
    obspyDMT()

    print "\n\n=================================================="
    print "obspyDMT main program is finished normally!\n"

    try:
        global input, events
        size = getFolderSize(input['datapath'])
        size /= (1024.**2)
        print "Info:"
        print "* The following directory contains %f MB of data." % size
        print input['datapath']
        print "* Total time %f sec" % (time.time() - t1_pro)
        print "==================================================\n\n"
    except Exception as e:
        print 'ERROR: %s' % e
        pass
    # pass the return of main to the command line.
    sys.exit()

if __name__ == "__main__":
    main()
