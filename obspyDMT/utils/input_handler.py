#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  input_handler.py
#   Purpose:   reading and generating input_dics
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from obspy.core import UTCDateTime
from optparse import OptionParser, OptionGroup
import os
import shutil
import sys
import time

#  ##################### descrip_generator ###################################


def descrip_generator():
    print "*********************************"
    print "Check all the BASIC dependencies:"
    try:
        from obspy import __version__ as obs_ver
    except Exception as error:
        print '---------------------------------------------------'
        print 'Have you properly installed ObsPy on your computer?'
        print 'Error: %s' % error
        print '---------------------------------------------------'
        sys.exit(2)

    descrip = ['obspy ver: ' + obs_ver]

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
    return descrip

#  ##################### command_parse ###################################


def command_parse():
    """
    Parsing command-line options.
    :return:
    options, args, parser
    These three variables contain the information of the command line; i.e.
    the values that have been passed by the user.
    """
    # create command line option parser
    parser = OptionParser("%prog [options]")
    # configure command line options
    # action=".." tells OptionsParser what to save:
    # store_true saves bool TRUE,
    # store_false saves bool FALSE, store saves string; into the variable
    # given with dest="var"
    # * you need to provide every possible option here.

    helpmsg = "Show the description of all option groups"
    parser.add_option("--options", action="store_true", default=False,
                      dest="options", help=helpmsg)

    helpmsg = "Show the options inside specified option group. " \
              "Syntax: --option 1, " \
              "the numbers can be seen from --options flag."
    parser.add_option("--list_option", action="store", default=False,
                      dest="list_option", help=helpmsg)

    # --------------- Check installation and obspyDMT version
    group_check = OptionGroup(parser,
                              "1. Check installation and obspyDMT version")
    helpmsg = "run a quick tour!"
    group_check.add_option("--tour", action="store_true",
                           dest="tour", help=helpmsg)

    helpmsg = "check all the dependencies and their installed versions on " \
              "the local machine and exit!"
    group_check.add_option("--check", action="store_true",
                           dest="check", help=helpmsg)

    helpmsg = "show the obspyDMT version and exit!"
    group_check.add_option("--version", action="store_true",
                           dest="version", help=helpmsg)
    parser.add_option_group(group_check)

    # --------------- Path specification
    group_path = OptionGroup(parser, "2. Path specification")
    helpmsg = "the path where obspyDMT will store the data " \
              "[Default: './obspyDMT-data']"
    group_path.add_option("--datapath", action="store",
                          dest="datapath", help=helpmsg)

    helpmsg = "if the datapath is found deleting it before running obspyDMT."
    group_path.add_option("--reset", action="store_true",
                          dest="reset", help=helpmsg)

    parser.add_option_group(group_path)

    # --------------- General options for requests
    group_req = OptionGroup(parser, "3. General options for requests")
    helpmsg = "continuous request (please refer to the tutorial)."
    group_req.add_option("--continuous", action="store_true",
                         dest="get_continuous", help=helpmsg)

    helpmsg = "event-based request " \
              "(please refer to the tutorial). [Default: 'Y']"
    group_req.add_option("--get_events", action="store",
                         dest="get_events", help=helpmsg)

    helpmsg = "retrieve waveform(s). [Default: 'Y']"
    group_req.add_option("--waveform", action="store",
                         dest="waveform", help=helpmsg)

    helpmsg = "send request (waveform/response) to FDSN. [Default: 'Y']"
    group_req.add_option("--FDSN", action="store",
                         dest="FDSN", help=helpmsg)

    helpmsg = "send request (waveform/response) to ArcLink. [Default: 'N']"
    group_req.add_option("--arc", action="store",
                         dest="ArcLink", help=helpmsg)

    helpmsg = "retrieve the response file. [Default: 'Y']"
    group_req.add_option("--response", action="store",
                         dest="response", help=helpmsg)

    helpmsg = "retrieve the PAZ."
    group_req.add_option("--paz", action="store_true",
                         dest="paz", help=helpmsg)

    helpmsg = "parallel waveform/response/paz request"
    group_req.add_option("--req_parallel", action="store_true",
                         dest="req_parallel", help=helpmsg)

    helpmsg = "number of processors to be used in --req_parallel. [Default: 4]"
    group_req.add_option("--req_np", action="store",
                         dest="req_np", help=helpmsg)

    helpmsg = "use a station list instead of checking the availability. " \
              "[Default: False]"
    group_req.add_option("--list_stas", action="store",
                         dest="list_stas", help=helpmsg)

    helpmsg = "retrieve synthetic waveforms calculated by normal mode " \
              "summation code. (ShakeMovie project)"
    group_req.add_option("--normal_mode_syn", action="store_true",
                         dest="normal_mode_syn", help=helpmsg)

    helpmsg = "retrieve synthetic waveforms of SPECFEM3D."
    group_req.add_option("--specfem3D", action="store_true",
                         dest="specfem3D", help=helpmsg)

    helpmsg = "test the program for the desired number of requests, " \
              "eg: '--test 10' will test the program for 10 " \
              "requests. [Default: 'N']"
    group_req.add_option("--test", action="store",
                         dest="test", help=helpmsg)
    parser.add_option_group(group_req)

    # --------------- Continuous request
    group_cont = OptionGroup(parser, "4. Continuous request")
    helpmsg = "time interval for dividing the continuous request. " \
              "[Default: 86400 sec (1 day)]"
    group_cont.add_option("--interval", action="store",
                          dest="interval", help=helpmsg)
    helpmsg = "preset defined for EACH continuous request, i.e. time before " \
              "EACH interval (refer to '--interval' option) " \
              "in continuous request. [Default: 0]"
    group_cont.add_option("--preset_cont", action="store",
                          dest="preset_cont", help=helpmsg)

    helpmsg = "offset defined for EACH continuous request, i.e. time after " \
              "EACH interval (refer to '--interval' option) " \
              "in continuous request. [Default: 0]"
    group_cont.add_option("--offset_cont", action="store",
                          dest="offset_cont", help=helpmsg)
    parser.add_option_group(group_cont)

    # --------------- Events
    group_ev = OptionGroup(parser, "5. Events")
    helpmsg = "just retrieve the event information and " \
              "create an event archive."
    group_ev.add_option("--event_info", action="store_true",
                        dest="event_info", help=helpmsg)

    helpmsg = "read in an existing event catalog and proceed. " \
              "Currently supported data formats: " \
              "'QUAKEML', 'MCHEDR' e.g.: --read_catalog 'path/to/file'"
    group_ev.add_option("--read_catalog", action="store",
                        dest="read_catalog", help=helpmsg)

    helpmsg = "user can interactively select events of retrieved event " \
              "catalog"
    group_ev.add_option("--user_select_event", action="store_true",
                        dest="user_select_event", help=helpmsg)

    helpmsg = "start time, syntax: Y-M-D-H-M-S " \
              "(eg: '2010-01-01-00-00-00') or just " \
              "Y-M-D [Default: 10 days ago]"
    group_ev.add_option("--min_date", action="store",
                        dest="min_date", help=helpmsg)

    helpmsg = "end time, syntax: Y-M-D-H-M-S " \
              "(eg: '2011-01-01-00-00-00') or just " \
              "Y-M-D [Default: 5 days ago]"
    group_ev.add_option("--max_date", action="store",
                        dest="max_date", help=helpmsg)

    helpmsg = "minimum depth. [Default: -10.0 (above the surface!)]"
    group_ev.add_option("--min_depth", action="store",
                        dest="min_depth", help=helpmsg)

    helpmsg = "maximum depth. [Default: +6000.0]"
    group_ev.add_option("--max_depth", action="store",
                        dest="max_depth", help=helpmsg)

    helpmsg = "minimum magnitude. [Default: 5.5]"
    group_ev.add_option("--min_mag", action="store",
                        dest="min_mag", help=helpmsg)

    helpmsg = "maximum magnitude. [Default: 9.9]"
    group_ev.add_option("--max_mag", action="store",
                        dest="max_mag", help=helpmsg)

    helpmsg = "magnitude type. " \
              "Some common types (there are many) include " \
              "'Ml' (local/Richter magnitude), " \
              "'Ms' (surface magnitude), " \
              "'mb' (body wave magnitude), " \
              "'Mw' (moment magnitude). " \
              "[Default: None]"
    group_ev.add_option("--mag_type", action="store",
                        dest="mag_type", help=helpmsg)

    helpmsg = "search for all the events within the defined rectangle, " \
              "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax> " \
              "[Default: -180.0/+180.0/-90.0/+90.0]"
    group_ev.add_option("--event_rect", action="store",
                        dest="event_rect", help=helpmsg)

    helpmsg = "search for all the events within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "May not be used together with rectangular bounding box " \
              "event restrictions (event_rect)."
    group_ev.add_option("--event_circle", action="store",
                        dest="event_circle", help=helpmsg)

    helpmsg = "event webservice (IRIS or NERIES). [Default: 'IRIS']"
    group_ev.add_option("--event_url", action="store",
                        dest="event_url", help=helpmsg)

    helpmsg = "event catalog (GCMT_COMBO, IRIS, ISC, EMSC, GCMT, NEIC PDE). " \
              "[Default: IRIS]"
    group_ev.add_option("--event_catalog", action="store",
                        dest="event_catalog", help=helpmsg)

    helpmsg = "maximum number of events to be requested. [Default: 2500]"
    group_ev.add_option("--max_result", action="store",
                        dest="max_result", help=helpmsg)
    parser.add_option_group(group_ev)

    # --------------- Stations
    group_sta = OptionGroup(parser, "6. Stations")
    helpmsg = "identity code restriction, syntax: " \
              "net.sta.loc.cha (eg: TA.*.*.BHZ to search for " \
              "all BHZ channels in TA network). [Default: *.*.*.*]"
    group_sta.add_option("--identity", action="store",
                         dest="identity", help=helpmsg)

    helpmsg = "network code. [Default: *]"
    group_sta.add_option("--net", action="store",
                         dest="net", help=helpmsg)

    helpmsg = "station code. [Default: *]"
    group_sta.add_option("--sta", action="store",
                         dest="sta", help=helpmsg)

    helpmsg = "location code. [Default: *]"
    group_sta.add_option("--loc", action="store",
                         dest="loc", help=helpmsg)

    helpmsg = "channel code. [Default: *]"
    group_sta.add_option("--cha", action="store",
                         dest="cha", help=helpmsg)

    helpmsg = "search for all the stations within the defined rectangle, " \
              "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax>. " \
              "May not be used together with circular bounding box station " \
              "restrictions (station_circle) " \
              "[Default: -180.0/+180.0/-90.0/+90.0]"
    group_sta.add_option("--station_rect", action="store",
                         dest="station_rect", help=helpmsg)

    helpmsg = "search for all the stations within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "May not be used together with rectangular bounding box " \
              "station restrictions (station_rect). Currently, " \
              "ArcLink does not support this option!"
    group_sta.add_option("--station_circle", action="store",
                         dest="station_circle", help=helpmsg)
    parser.add_option_group(group_sta)

    # --------------- Time window, waveform format and sampling rate
    group_tw = OptionGroup(parser, "7. Time window, waveform format and "
                                   "sampling rate")
    helpmsg = "time parameter in seconds which determines " \
              "how close the time series data (waveform) will be cropped " \
              "before the origin time of the event. Default: 0.0 seconds."
    group_tw.add_option("--preset", action="store",
                        dest="preset", help=helpmsg)

    helpmsg = "time parameter in seconds which determines " \
              "how close the time series data (waveform) will be cropped " \
              "after the origin time of the event. Default: 1800.0 seconds."
    group_tw.add_option("--offset", action="store",
                        dest="offset", help=helpmsg)

    helpmsg = "consider the first phase arrival (P, Pdiff, PKIKP) to use " \
              "as the reference time, i.e. --min_date and --max_date will " \
              "be calculated from the first phase arrival."
    group_tw.add_option("--cut_time_phase", action="store_true",
                        dest="cut_time_phase", help=helpmsg)

    helpmsg = "SAC format for saving the waveforms. " \
              "Station location (stla and stlo), " \
              "station elevation (stel), " \
              "station depth (stdp), " \
              "event location (evla and evlo), " \
              "event depth (evdp) and " \
              "event magnitude (mag) " \
              "will be stored in the SAC headers. [Default: 'Y'] "
    group_tw.add_option("--SAC", action="store",
                        dest="SAC", help=helpmsg)

    helpmsg = "MSEED format for saving the waveforms."
    group_tw.add_option("--mseed", action="store_true",
                        dest="mseed", help=helpmsg)

    helpmsg = "Resampling method: decimate, lanczos (not working). " \
              "'decimate' uses ObsPy tools with sharp low pass filter " \
              "to do the decimation. " \
              "'lanczos' uses 'lanczos resampling' method. [Default: decimate]"
    group_tw.add_option("--resample_method", action="store",
                        dest="resample_method", help=helpmsg)

    helpmsg = "Desired sampling rate (in Hz) for RAW seismograms. " \
              "Resampling is done using decimation with sharp low pass filter. " \
              "If not specified, the sampling rate of the waveforms " \
              "will not be changed."
    group_tw.add_option("--resample_raw", action="store",
                        dest="resample_raw", help=helpmsg)

    helpmsg = "Desired sampling rate (in Hz) for CORRECTED seismograms. " \
              "Resampling is done using decimation with sharp low pass filter. " \
              "If not specified, the sampling rate of the waveforms " \
              "will not be changed."
    group_tw.add_option("--resample_corr", action="store",
                        dest="resample_corr", help=helpmsg)
    parser.add_option_group(group_tw)

    # --------------- FDSN
    group_fdsn = OptionGroup(parser, "8. FDSN")
    helpmsg = "base_url for FDSN requests (waveform/response). " \
              "[Default: 'IRIS']"
    group_fdsn.add_option("--fdsn_base_url", action="store",
                          dest="fdsn_base_url", help=helpmsg)

    helpmsg = "using the FDSN bulkdataselect Web service. " \
              "Since this method returns multiple channels of " \
              "time series data for specified time ranges in one request, " \
              "it speeds up the waveform retrieving approximately by " \
              "a factor of two. [RECOMMENDED]"
    group_fdsn.add_option("--fdsn_bulk", action="store_true",
                          dest="fdsn_bulk", help=helpmsg)

    helpmsg = "username for FDSN requests (waveform/response). [Default: None]"
    group_fdsn.add_option("--fdsn_user", action="store",
                          dest="fdsn_user", help=helpmsg)

    helpmsg = "password for FDSN requests (waveform/response). [Default: None]"
    group_fdsn.add_option("--fdsn_pass", action="store",
                          dest="fdsn_pass", help=helpmsg)

    helpmsg = "generate a data-time file for a FDSN request. " \
              "This file shows the required time for each request and " \
              "the stored data in the folder."
    group_fdsn.add_option("--time_fdsn", action="store_true",
                          dest="time_fdsn", help=helpmsg)
    parser.add_option_group(group_fdsn)

    # --------------- ArcLink
    group_arc = OptionGroup(parser, "9. ArcLink")
    helpmsg = "timeout for sending request (availability) to ArcLink. " \
              "[Default: 40]"
    group_arc.add_option("--arc_avai_timeout", action="store",
                         dest="arc_avai_timeout", help=helpmsg)

    helpmsg = "timeout for sending request (waveform/response) to ArcLink. " \
              "[Default: 2]"
    group_arc.add_option("--arc_wave_timeout", action="store",
                         dest="arc_wave_timeout", help=helpmsg)

    helpmsg = "generate a data-time file for an ArcLink request. " \
              "This file shows the required time for each request " \
              "and the stored data in the folder."
    group_arc.add_option("--time_arc", action="store_true",
                         dest="time_arc", help=helpmsg)
    parser.add_option_group(group_arc)

    # --------------- Instrument correction
    group_ic = OptionGroup(parser, "10. Instrument correction")
    helpmsg = "correct the raw waveforms for DIS (m), VEL (m/s) or " \
              "ACC (m/s^2). [Default: DIS]"
    group_ic.add_option("--corr_unit", action="store",
                        dest="corr_unit", help=helpmsg)

    helpmsg = "apply a bandpass filter to the data trace before " \
              "deconvolution ('None' if you do not need pre_filter), " \
              "syntax: '(f1,f2,f3,f4)' which " \
              "are the four corner frequencies " \
              "of a cosine taper, one between f2 and f3 and tapers to zero " \
              "for f1 < f < f2 and f3 < f < f4. " \
              "[Default: '(0.008, 0.012, 3.0, 4.0)']"
    group_ic.add_option("--pre_filt", action="store",
                        dest="pre_filt", help=helpmsg)

    helpmsg = "water level for spectrum [Default: 600.0]"
    group_ic.add_option("--water_level", action="store",
                        dest="water_level", help=helpmsg)

    helpmsg = "parallel Instrument Correction. "
    group_ic.add_option("--ic_parallel", action="store_true",
                        dest="ic_parallel", help=helpmsg)

    helpmsg = "number of processors to be used in --ic_parallel. [Default: 20]"
    group_ic.add_option("--ic_np", action="store",
                        dest="ic_np", help=helpmsg)

    helpmsg = "apply instrument correction to the specified folder for " \
              "all the waveforms (FDSN and ArcLink), " \
              "syntax: --ic_all address_of_the_target_folder. [Default: 'N']"
    group_ic.add_option("--ic_all", action="store",
                        dest="ic_all", help=helpmsg)

    helpmsg = "apply instrument correction to the specified folder for " \
              "downloaded waveforms from FDSN, " \
              "syntax: --fdsn_ic address_of_the_target_folder. [Default: 'N']"
    group_ic.add_option("--fdsn_ic", action="store",
                        dest="fdsn_ic", help=helpmsg)

    helpmsg = "apply instrument correction to the specified folder for " \
              "downloaded waveforms from ArcLink, " \
              "syntax: --arc_ic address_of_the_target_folder. [Default: 'N']"
    group_ic.add_option("--arc_ic", action="store",
                        dest="arc_ic", help=helpmsg)

    helpmsg = "apply instrument correction automatically " \
              "after downloading the waveforms from FDSN. [Default: 'Y']"
    group_ic.add_option("--fdsn_ic_auto", action="store",
                        dest="fdsn_ic_auto", help=helpmsg)

    helpmsg = "apply instrument correction automatically " \
              "after downloading the waveforms from ArcLink. [Default: 'Y']"
    group_ic.add_option("--arc_ic_auto", action="store",
                        dest="arc_ic_auto", help=helpmsg)

    helpmsg = "do not apply instrument correction automatically. " \
              "This is equivalent to: \"--fdsn_ic_auto N --arc_ic_auto N\""
    group_ic.add_option("--ic_no", action="store_true",
                        dest="ic_no", help=helpmsg)

    helpmsg = "instrument Correction (full response), using obspy modules. " \
              "[Default: 'Y']"
    group_ic.add_option("--ic_obspy_full", action="store",
                        dest="ic_obspy_full", help=helpmsg)

    helpmsg = "instrument Correction (full response), using SAC"
    group_ic.add_option("--ic_sac_full", action="store_true",
                        dest="ic_sac_full", help=helpmsg)

    helpmsg = "instrument Correction (Poles And Zeros), " \
              "using SAC (for FDSN) and obspy (for ArcLink)"
    group_ic.add_option("--ic_paz", action="store_true",
                        dest="ic_paz", help=helpmsg)
    parser.add_option_group(group_ic)

    # --------------- Updating
    group_up = OptionGroup(parser, "11. Updating")
    helpmsg = "update the specified folder for FDSN and ArcLink, " \
              "syntax: --update_all address_of_the_target_folder. " \
              "[Default: 'N']"
    group_up.add_option("--update_all", action="store",
                        dest="update_all", help=helpmsg)

    helpmsg = "update the specified folder for FDSN, " \
              "syntax: --fdsn_update address_of_the_target_folder. " \
              "[Default: 'N']"
    group_up.add_option("--fdsn_update", action="store",
                        dest="fdsn_update", help=helpmsg)

    helpmsg = "update the specified folder for ArcLink, " \
              "syntax: --arc_update address_of_the_target_folder. " \
              "[Default: 'N']"
    group_up.add_option("--arc_update", action="store",
                        dest="arc_update", help=helpmsg)
    parser.add_option_group(group_up)

    # --------------- Merging
    group_merg = OptionGroup(parser, "12. Merging")
    helpmsg = "merge 'raw' or 'corrected' waveforms. [Default: 'raw']"
    group_merg.add_option("--merge_type", action="store",
                          dest="merge_type", help=helpmsg)

    helpmsg = "merge all waveforms (FDSN and ArcLink) in " \
              "the specified folder, " \
              "syntax: --merge_all address_of_the_target_folder. " \
              "[Default: 'N']"
    group_merg.add_option("--merge_all", action="store",
                          dest="merge_all", help=helpmsg)

    helpmsg = "merge the FDSN waveforms in the specified folder, " \
              "syntax: --fdsn_merge address_of_the_target_folder. " \
              "[Default: 'N']"
    group_merg.add_option("--fdsn_merge", action="store",
                          dest="fdsn_merge", help=helpmsg)

    helpmsg = "merge the ArcLink waveforms in the specified folder, " \
              "syntax: --arc_merge address_of_the_target_folder." \
              "[Default: 'N']"
    group_merg.add_option("--arc_merge", action="store",
                          dest="arc_merge", help=helpmsg)

    helpmsg = "merge automatically after downloading the waveforms " \
              "from FDSN. [Default: 'Y']"
    group_merg.add_option("--fdsn_merge_auto", action="store",
                          dest="fdsn_merge_auto", help=helpmsg)

    helpmsg = "merge automatically after downloading the waveforms " \
              "from ArcLink. [Default: 'Y']"
    group_merg.add_option("--arc_merge_auto", action="store",
                          dest="arc_merge_auto", help=helpmsg)

    helpmsg = "do not merge automatically. This is equivalent to: " \
              "\"--fdsn_merge_auto N --arc_merge_auto N\""
    group_merg.add_option("--merge_no", action="store_true",
                          dest="merge_no", help=helpmsg)
    parser.add_option_group(group_merg)

    # --------------- Plotting
    group_plt = OptionGroup(parser, "13. Plotting")
    helpmsg = "create a seismicity map according to " \
              "the event and location specifications."
    group_plt.add_option("--seismicity", action="store_true",
                         dest="seismicity", help=helpmsg)

    helpmsg = "depth bins for plotting the seismicity histrogram. " \
              "[Default: 10]"
    group_plt.add_option("--depth_bins_seismicity", action="store",
                         dest="depth_bins_seismicity", help=helpmsg)

    helpmsg = "specify directory for plotting purposes [Default: 'N']"
    group_plt.add_option("--plot_dir", action="store",
                         dest="plot_dir", help=helpmsg)

    helpmsg = "plot 'raw' or 'corrected' waveforms. [Default: 'raw']"
    group_plt.add_option("--plot_type", action="store",
                         dest="plot_type", help=helpmsg)

    helpmsg = "plot all waveforms (FDSN and ArcLink). [Default: 'Y']"
    group_plt.add_option("--plot_all", action="store",
                         dest="plot_all", help=helpmsg)

    helpmsg = "plot waveforms downloaded from FDSN."
    group_plt.add_option("--plot_fdsn", action="store_true",
                         dest="plot_fdsn", help=helpmsg)

    helpmsg = "plot waveforms downloaded from ArcLink."
    group_plt.add_option("--plot_arc", action="store_true",
                         dest="plot_arc", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" for " \
              "all the waveforms found in the specified folder (--plot_dir)."
    group_plt.add_option("--plot_epi", action="store_true",
                         dest="plot_epi", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" (refer to --plot_epi') " \
              "for all the waveforms with " \
              "epicentral-distance >= min_epi. [Default: 0.0]"
    group_plt.add_option("--min_epi", action="store",
                         dest="min_epi", help=helpmsg)

    helpmsg = "plot \"epicentral distance-time\" " \
              "(refer to '--plot_epi') for all the waveforms with " \
              "epicentral-distance <= max_epi. [Default: 180.0]"
    group_plt.add_option("--max_epi", action="store",
                         dest="max_epi", help=helpmsg)

    helpmsg = "plot all the events, stations and ray path between them " \
              "found in the specified directory (--plot_dir)."
    group_plt.add_option("--plot_ray_gmt", action="store_true",
                         dest="plot_ray_gmt", help=helpmsg)

    helpmsg = "plot the ray coverage for all the station-event pairs " \
              "found in the specified folder (--plot_dir)."
    group_plt.add_option("--plot_ray", action="store_true",
                         dest="plot_ray", help=helpmsg)

    helpmsg = "plot all the events found " \
              "in the specified directory (--plot_dir)."
    group_plt.add_option("--plot_ev", action="store_true",
                         dest="plot_ev", help=helpmsg)

    helpmsg = "plot Beachballs instead of dots for the event location."
    group_plt.add_option("--plot_focal", action="store_true",
                         dest="plot_focal", help=helpmsg)

    helpmsg = "plot all the stations found " \
              "in the specified directory (--plot_dir)."
    group_plt.add_option("--plot_sta", action="store_true",
                         dest="plot_sta", help=helpmsg)

    helpmsg = "plot \"Data(MB)-Time(Sec)\" for the " \
              "specified directory (--plot_dir) " \
              "-- ATTENTION: \"time_fdsn\" and/or \"time_arc\" should " \
              "exist in the \"info\" folder [refer to \"time_fdsn\" and " \
              "\"time_arc\" options]"
    group_plt.add_option("--plot_dt", action="store_true",
                         dest="plot_dt", help=helpmsg)

    helpmsg = "the path where obspyDMT will store the plots " \
              "[Default: '.' (the same directory as obspyDMT.py)]"
    group_plt.add_option("--plot_save", action="store",
                         dest="plot_save", help=helpmsg)

    helpmsg = "format of the plots saved on the local machine [Default: 'png']"
    group_plt.add_option("--plot_format", action="store",
                         dest="plot_format", help=helpmsg)

    helpmsg = "central meridian (x-axis origin) for projection " \
              "[Default: 180]"
    group_plt.add_option("--plot_lon0", action="store",
                         dest="plot_lon0", help=helpmsg)
    parser.add_option_group(group_plt)

    # --------------- Plotting SationXML
    group_pltxml = OptionGroup(parser, "14. Plotting StationXML")
    helpmsg = "address of a file/directory that contains StationXML files. " \
              "[Default: False]"
    group_pltxml.add_option("--plotxml_dir", action="store",
                            dest="plotxml_dir", help=helpmsg)

    helpmsg = "plot all the stages available in the response file."
    group_pltxml.add_option("--plotxml_allstages", action="store_true",
                            dest="plotxml_allstages", help=helpmsg)

    helpmsg = "plot PAZ of the response file."
    group_pltxml.add_option("--plotxml_paz", action="store_true",
                            dest="plotxml_paz", help=helpmsg)

    helpmsg = "plot only stage 1 and 2 of full response file."
    group_pltxml.add_option("--plotxml_plotstage12", action="store_true",
                            dest="plotxml_plotstage12", help=helpmsg)

    helpmsg = "start stage in response file to be considered for plotting " \
              "the transfer function. [Default: 1]"
    group_pltxml.add_option("--plotxml_start_stage", action="store",
                            dest="plotxml_start_stage", help=helpmsg)

    helpmsg = "final stage in response file to be considered for plotting " \
              "the transfer function. [Default: 100]"
    group_pltxml.add_option("--plotxml_end_stage", action="store",
                            dest="plotxml_end_stage", help=helpmsg)

    helpmsg = "datetime to be used for plotting the transfer function," \
              "syntax: Y-M-D-H-M-S (eg: '2011-01-01-00-00-00') or just " \
              "Y-M-D. If this is not set, the starting date of the " \
              "stationXML will be used instead!"
    group_pltxml.add_option("--plotxml_date", action="store",
                            dest="plotxml_date", help=helpmsg)

    helpmsg = "minimum frequency to be used for plotting the transfer " \
              "function. [Default: 0.01]"
    group_pltxml.add_option("--plotxml_min_freq", action="store",
                            dest="plotxml_min_freq", help=helpmsg)

    helpmsg = "plot all the stations that have been compared in terms of " \
              "instrument response."
    group_pltxml.add_option("--plotxml_map_compare", action="store_true",
                            dest="plotxml_map_compare", help=helpmsg)

    helpmsg = "percentage of the phase transfer function length to be used " \
              "for checking the difference between different methods, " \
              "e.g. 100 will be the whole transfer function, " \
              "80 means consider the transfer function from min_freq until " \
              "20 percent before the Nyquist frequency. [Default: 80]"
    group_pltxml.add_option("--plotxml_percentage", action="store",
                            dest="plotxml_percentage", help=helpmsg)

    helpmsg = "maximum allowable length (in percentage) to differ between " \
              "two different methods of instrument correction. " \
              "This only applies to phase difference. [Default: 10]"
    group_pltxml.add_option("--plotxml_phase_threshold", action="store",
                            dest="plotxml_phase_threshold", help=helpmsg)

    helpmsg = "output of the transfer function: DIS/VEL/ACC. [Default: VEL]"
    group_pltxml.add_option("--plotxml_output", action="store",
                            dest="plotxml_output", help=helpmsg)

    helpmsg = "do not plot the full response file."
    group_pltxml.add_option("--plotxml_no_response", action="store_true",
                            dest="plotxml_no_response", help=helpmsg)
    parser.add_option_group(group_pltxml)

    # --------------- Email and compressing
    group_ec = OptionGroup(parser, "15. Email and compressing")
    helpmsg = "send an email to the specified email-address after " \
              "completing the job, syntax: --email email_address. " \
              "[Default: 'N']"
    group_ec.add_option("--email", action="store",
                        dest="email", help=helpmsg)

    helpmsg = "compress the raw-waveform files after " \
              "applying instrument correction."
    group_ec.add_option("--zip_w", action="store_true",
                        dest="zip_w", help=helpmsg)

    helpmsg = "compress the response files after " \
              "applying instrument correction."
    group_ec.add_option("--zip_r", action="store_true",
                        dest="zip_r", help=helpmsg)
    parser.add_option_group(group_ec)
    # --------------- END

    # parse command line options
    (options, args) = parser.parse_args()

    return options, args, parser

# ##################### read_input_command ##############################


def read_input_command(parser, **kwargs):
    """
    Create input_dics object (dictionary) based on command-line options.
    The default values are as "input_dics" object (below)
    :param parser: this object should be passed from another function (e.g
    command_parser) which contains the values that have been passed by the
    command line.
    :param kwargs:
    :return:
    """
    # Defining the default values.
    input_dics = {'datapath': 'obspyDMT-data',
                  'min_date': str(UTCDateTime() - 60 * 60 * 24 * 10 * 1),
                  'max_date': str(UTCDateTime() - 60 * 60 * 24 * 5 * 1),
                  'event_url': 'IRIS',
                  'event_catalog': 'IRIS',
                  'mag_type': None,
                  'min_mag': 5.5, 'max_mag': 9.9,
                  'min_depth': -10.0, 'max_depth': +6000.0,
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
                  'SAC': 'Y',
                  'resample_method': None,
                  'resample_raw': None,
                  'resample_corr': None,
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
                  'water_level': 600.0,
                  'corr_unit': 'DIS',
                  'merge_all': 'N',
                  'fdsn_merge': 'N', 'fdsn_merge_auto': 'Y',
                  'merge_type': 'raw',
                  'arc_merge': 'N', 'arc_merge_auto': 'Y',
                  'plot_dir': 'N',
                  'plot_all': 'Y',
                  'plot_type': 'raw',
                  'plot_save': '.', 'plot_format': 'png',
                  'plot_lon0': 180,
                  'min_epi': 0.0, 'max_epi': 180.0,
                  'plotxml_dir': False,
                  'plotxml_date': False,
                  'plotxml_min_freq': 0.01,
                  'plotxml_output': 'VEL',
                  'plotxml_start_stage': 1,
                  'plotxml_end_stage': 100,
                  'plotxml_percentage': 80,
                  'plotxml_phase_threshold': 10.,
                  }

    # feed input_dics dictionary of defaults into parser object
    parser.set_defaults(**input_dics)

    # parse command line options
    (options, args) = parser.parse_args()
    # command line options can now be accessed via options.varname.

    # Check if keyword arguments have been passed to the main function from
    # another script and parse here:
    if kwargs:
        # assigning kwargs to entries of OptionParser object
        for arg in kwargs:
            exec "options.%s = kwargs[arg]" % arg

    # printing the description of all option groups
    if options.options:
        print "=============="
        print "option groups:"
        print "=============="
        for grp in parser.option_groups:
            print grp.title
        print "\n\n==============================================="
        print "To check the available options in each group:"
        print "python obspyDMT.py --list_option <group_number>"
        print "==============================================="
        sys.exit()

    # printing the available options in each option group
    if options.list_option:
        if int(options.list_option) > len(parser.option_groups):
            sys.exit('Specified option group: %s does not exist'
                     % options.list_option)
        print parser.option_groups[int(options.list_option)-1].title
        for opt_grp in \
                parser.option_groups[int(options.list_option)-1].option_list:
            print "{0:20s}\t{1:20s}\t{2:20s}\t\t{3:20s}".\
                format(opt_grp.get_opt_string(), opt_grp.dest,
                       opt_grp.type, opt_grp.help)
        sys.exit()

    if options.version:
        print '\n\t\t' + '*********************************'
        print '\t\t' + '*        obspyDMT version:      *'
        print '\t\t' + '*' + '\t\t' + '1.0.0rc1' + '\t\t' + '*'
        print '\t\t' + '*********************************'
        print '\n'
        sys.exit(2)

    # Check whether it is possible to import all required modules
    if options.check:
        descrip = descrip_generator()
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
        options.event_catalog = 'IRIS'
        options.req_parallel = True
        options.ArcLink = 'N'

    # ############Parse paths and make sure that they are all absolute path
    for paths in ['datapath', 'fdsn_update', 'arc_update', 'update_all',
                  'fdsn_ic', 'arc_ic', 'ic_all', 'fdsn_merge', 'arc_merge',
                  'merge_all', 'plot_dir', 'plot_save', 'plotxml_dir']:
        optatr_path = getattr(options, paths)
        if optatr_path:
            if optatr_path != 'N' and not os.path.isabs(optatr_path):
                setattr(options, paths, os.path.join(os.getcwd(),
                                                     getattr(options, paths)))
    # ############END Parse paths

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

    input_dics['plotxml_dir'] = options.plotxml_dir
    if options.plotxml_date:
        input_dics['plotxml_date'] = UTCDateTime(options.plotxml_date)
    else:
        input_dics['plotxml_date'] = options.plotxml_date
    input_dics['plotxml_min_freq'] = float(options.plotxml_min_freq)
    input_dics['plotxml_output'] = options.plotxml_output
    input_dics['plotxml_start_stage'] = int(options.plotxml_start_stage)
    input_dics['plotxml_end_stage'] = int(options.plotxml_end_stage)
    input_dics['plotxml_percentage'] = float(options.plotxml_percentage)
    input_dics['plotxml_phase_threshold'] = \
        float(options.plotxml_phase_threshold)
    if options.plotxml_no_response:
        input_dics['plotxml_response'] = False
    else:
        input_dics['plotxml_response'] = True
    if options.plotxml_plotstage12:
        input_dics['plotxml_plotstage12'] = True
    else:
        input_dics['plotxml_plotstage12'] = False
    if options.plotxml_paz:
        input_dics['plotxml_paz'] = True
    else:
        input_dics['plotxml_paz'] = False
    if options.plotxml_allstages:
        input_dics['plotxml_allstages'] = True
    else:
        input_dics['plotxml_allstages'] = False
    if options.plotxml_map_compare:
        input_dics['plotxml_map_compare'] = True
    else:
        input_dics['plotxml_map_compare'] = False
    input_dics['datapath'] = options.datapath
    if options.cut_time_phase:
        input_dics['cut_time_phase'] = True
    else:
        input_dics['cut_time_phase'] = False
    input_dics['min_date'] = str(UTCDateTime(options.min_date))
    input_dics['max_date'] = str(UTCDateTime(options.max_date))
    input_dics['event_url'] = options.event_url.upper()

    if options.event_catalog:
        input_dics['event_catalog'] = options.event_catalog.upper()
    if input_dics['event_catalog'].upper() == 'IRIS':
        input_dics['event_catalog'] = None

    if options.read_catalog:
        input_dics['read_catalog'] = options.read_catalog
    else:
        input_dics['read_catalog'] = 'N'
    input_dics['mag_type'] = options.mag_type
    input_dics['min_mag'] = float(options.min_mag)
    input_dics['max_mag'] = float(options.max_mag)
    input_dics['min_depth'] = float(options.min_depth)
    input_dics['max_depth'] = float(options.max_depth)
    input_dics['evlonmin'] = options.evlonmin
    input_dics['evlonmax'] = options.evlonmax
    input_dics['evlatmin'] = options.evlatmin
    input_dics['evlatmax'] = options.evlatmax
    input_dics['evlat'] = options.evlat
    input_dics['evlon'] = options.evlon
    input_dics['evradmax'] = options.evradmax
    input_dics['evradmin'] = options.evradmin
    input_dics['preset'] = float(options.preset)
    input_dics['offset'] = float(options.offset)
    input_dics['max_result'] = int(options.max_result)
    input_dics['depth_bins_seismicity'] = int(options.depth_bins_seismicity)
    if options.user_select_event:
        input_dics['user_select_event'] = 'Y'
    else:
        input_dics['user_select_event'] = 'N'
    if options.seismicity:
        input_dics['seismicity'] = 'Y'
    else:
        input_dics['seismicity'] = 'N'
    input_dics['get_events'] = options.get_events
    if options.get_continuous:
        input_dics['plot_all_events'] = None
        input_dics['get_events'] = 'N'
        input_dics['get_continuous'] = 'Y'
    else:
        input_dics['get_continuous'] = 'N'
    input_dics['interval'] = float(options.interval)
    input_dics['preset_cont'] = float(options.preset_cont)
    input_dics['offset_cont'] = float(options.offset_cont)
    if options.req_parallel:
        options.req_parallel = 'Y'
    input_dics['req_parallel'] = options.req_parallel
    input_dics['req_np'] = int(options.req_np)
    input_dics['list_stas'] = options.list_stas
    if options.fdsn_bulk:
        options.fdsn_bulk = 'Y'
    input_dics['fdsn_bulk'] = options.fdsn_bulk
    if options.specfem3D:
        options.specfem3D = 'Y'
    input_dics['specfem3D'] = options.specfem3D
    if options.normal_mode_syn:
        options.normal_mode_syn = 'Y'
    input_dics['normal_mode_syn'] = options.normal_mode_syn
    input_dics['waveform'] = options.waveform
    input_dics['response'] = options.response
    if options.paz:
        options.paz = 'Y'
    input_dics['paz'] = options.paz
    input_dics['SAC'] = options.SAC
    if options.mseed:
        input_dics['SAC'] = 'N'
        input_dics['mseed'] = 'Y'
    else:
        input_dics['mseed'] = 'N'

    if options.resample_method:
        input_dics['resample_method'] = options.resample_method
    else:
        input_dics['resample_method'] = 'decimate'
    if options.resample_raw:
        input_dics['resample_raw'] = float(options.resample_raw)
    else:
        input_dics['resample_raw'] = False
    if options.resample_corr:
        input_dics['resample_corr'] = float(options.resample_corr)
    else:
        input_dics['resample_corr'] = False
    input_dics['FDSN'] = options.FDSN
    input_dics['fdsn_base_url'] = options.fdsn_base_url
    input_dics['fdsn_user'] = options.fdsn_user
    input_dics['fdsn_pass'] = options.fdsn_pass
    input_dics['ArcLink'] = options.ArcLink

    input_dics['arc_avai_timeout'] = float(options.arc_avai_timeout)
    input_dics['arc_wave_timeout'] = float(options.arc_wave_timeout)

    if options.time_fdsn:
        options.time_fdsn = 'Y'
    input_dics['time_fdsn'] = options.time_fdsn
    if options.time_arc:
        options.time_arc = 'Y'
    input_dics['time_arc'] = options.time_arc
    input_dics['net'] = options.net
    input_dics['sta'] = options.sta
    if options.loc == "''":
        input_dics['loc'] = ''
    elif options.loc == '""':
        input_dics['loc'] = ''
    else:
        input_dics['loc'] = options.loc
    input_dics['cha'] = options.cha
    input_dics['lon_cba'] = options.lon_cba
    input_dics['lat_cba'] = options.lat_cba
    input_dics['mr_cba'] = options.mr_cba
    input_dics['Mr_cba'] = options.Mr_cba
    input_dics['mlon_rbb'] = options.mlon_rbb
    input_dics['Mlon_rbb'] = options.Mlon_rbb
    input_dics['mlat_rbb'] = options.mlat_rbb
    input_dics['Mlat_rbb'] = options.Mlat_rbb
    if options.test != 'N':
        input_dics['test'] = 'Y'
        input_dics['test_num'] = int(options.test)
    input_dics['fdsn_update'] = options.fdsn_update
    input_dics['arc_update'] = options.arc_update
    input_dics['update_all'] = options.update_all
    if input_dics['update_all'] != 'N':
        input_dics['fdsn_update'] = input_dics['update_all']
        input_dics['arc_update'] = input_dics['update_all']
    input_dics['fdsn_ic'] = options.fdsn_ic
    input_dics['fdsn_ic_auto'] = options.fdsn_ic_auto
    input_dics['arc_ic'] = options.arc_ic
    input_dics['arc_ic_auto'] = options.arc_ic_auto
    input_dics['ic_all'] = options.ic_all
    if input_dics['ic_all'] != 'N':
        input_dics['fdsn_ic'] = input_dics['ic_all']
        input_dics['arc_ic'] = input_dics['ic_all']
    if options.ic_parallel:
        options.ic_parallel = 'Y'
    input_dics['ic_parallel'] = options.ic_parallel
    input_dics['ic_np'] = int(options.ic_np)
    input_dics['ic_obspy_full'] = options.ic_obspy_full
    if options.ic_sac_full:
        options.ic_sac_full = 'Y'
    input_dics['ic_sac_full'] = options.ic_sac_full
    if options.ic_paz:
        options.ic_paz = 'Y'
    input_dics['ic_paz'] = options.ic_paz
    if input_dics['ic_sac_full'] == 'Y' or input_dics['ic_paz'] == 'Y':
        input_dics['SAC'] = 'Y'
        input_dics['ic_obspy_full'] = 'N'
    input_dics['corr_unit'] = options.corr_unit
    input_dics['pre_filt'] = options.pre_filt
    input_dics['water_level'] = float(options.water_level)
    if options.zip_w:
        options.zip_w = 'Y'
    input_dics['zip_w'] = options.zip_w
    if options.zip_r:
        options.zip_r = 'Y'
    input_dics['zip_r'] = options.zip_r
    input_dics['fdsn_merge'] = options.fdsn_merge
    input_dics['arc_merge'] = options.arc_merge
    input_dics['merge_all'] = options.merge_all
    if input_dics['merge_all'] != 'N':
        input_dics['fdsn_merge'] = input_dics['merge_all']
        input_dics['arc_merge'] = input_dics['merge_all']
    input_dics['plot_type'] = options.plot_type
    input_dics['plot_all'] = options.plot_all
    if options.plot_fdsn:
        options.plot_fdsn = 'Y'
    input_dics['plot_fdsn'] = options.plot_fdsn
    if options.plot_arc:
        options.plot_arc = 'Y'
    input_dics['plot_arc'] = options.plot_arc
    input_dics['plot_dir'] = options.plot_dir
    if options.plot_ev:
        input_dics['plot_ev'] = True
    else:
        input_dics['plot_ev'] = False
    if options.plot_focal:
        input_dics['plot_focal'] = True
    else:
        input_dics['plot_focal'] = False
    if options.plot_sta:
        input_dics['plot_sta'] = True
    else:
        input_dics['plot_sta'] = False
    if options.plot_ray:
        input_dics['plot_ray'] = True
    else:
        input_dics['plot_ray'] = False
    if options.plot_ray_gmt:
        input_dics['plot_ray_gmt'] = True
    else:
        input_dics['plot_ray_gmt'] = False
    if options.plot_epi:
        input_dics['plot_epi'] = True
    else:
        input_dics['plot_epi'] = False
    if options.plot_dt:
        input_dics['plot_dt'] = True
    else:
        input_dics['plot_dt'] = False
    input_dics['min_epi'] = float(options.min_epi)
    input_dics['max_epi'] = float(options.max_epi)
    input_dics['plot_save'] = options.plot_save
    input_dics['plot_format'] = options.plot_format
    input_dics['plot_lon0'] = float(options.plot_lon0)
    input_dics['email'] = options.email
    if input_dics['email'] != 'N':
        try:
            import smtplib
        except Exception as error:
            print "\n********************************************************"
            print "Unable to import smtplib. Sending email is not possible!"
            print "Error: %s" % error
            print "********************************************************\n"
            sys.exit()

    # --------------Changing relevant options for some specific options
    if input_dics['get_continuous'] == 'N':
        input_dics['fdsn_merge_auto'] = 'N'
        input_dics['arc_merge_auto'] = 'N'
        input_dics['merge_type'] = options.merge_type
    else:
        input_dics['fdsn_merge_auto'] = options.fdsn_merge_auto
        input_dics['arc_merge_auto'] = options.arc_merge_auto
        input_dics['merge_type'] = options.merge_type

    for opts in ['fdsn_ic', 'arc_ic', 'fdsn_merge', 'arc_merge', 'plot_dir']:
        if input_dics[opts] != 'N':
            input_dics['datapath'] = input_dics[opts]
            input_dics['get_events'] = 'N'
            input_dics['get_continuous'] = 'N'
            input_dics['FDSN'] = 'N'
            input_dics['ArcLink'] = 'N'
            input_dics['fdsn_ic_auto'] = 'N'
            input_dics['arc_ic_auto'] = 'N'
            input_dics['fdsn_merge_auto'] = 'N'
            input_dics['arc_merge_auto'] = 'N'

    for opts in ['fdsn_update', 'arc_update']:
        if input_dics[opts] != 'N':
            input_dics['datapath'] = input_dics[opts]
            input_dics['get_events'] = 'N'
            input_dics['get_continuous'] = 'N'
            input_dics['FDSN'] = 'N'
            input_dics['ArcLink'] = 'N'

    if options.event_info:
        input_dics['FDSN'] = 'N'
        input_dics['ArcLink'] = 'N'
        input_dics['fdsn_ic_auto'] = 'N'
        input_dics['arc_ic_auto'] = 'N'
        input_dics['fdsn_merge_auto'] = 'N'
        input_dics['arc_merge_auto'] = 'N'
        input_dics['plot_all_events'] = True
        if options.identity or options.get_continuous:
            input_dics['waveform'] = 'N'
    else:
        input_dics['plot_all_events'] = False

    if options.event_info and options.get_continuous:
        input_dics['plot_all_events'] = False

    if options.seismicity:
        input_dics['FDSN'] = 'N'
        input_dics['ArcLink'] = 'N'
        input_dics['fdsn_ic_auto'] = 'N'
        input_dics['arc_ic_auto'] = 'N'
        input_dics['fdsn_merge_auto'] = 'N'
        input_dics['arc_merge_auto'] = 'N'
        input_dics['max_result'] = 1000000

    if options.FDSN == 'N':
        input_dics['fdsn_ic_auto'] = 'N'
        input_dics['fdsn_merge_auto'] = 'N'

    if options.ArcLink == 'N':
        input_dics['arc_ic_auto'] = 'N'
        input_dics['arc_merge_auto'] = 'N'

    if options.ic_no:
        input_dics['fdsn_ic_auto'] = 'N'
        input_dics['arc_ic_auto'] = 'N'

    if options.merge_no:
        input_dics['fdsn_merge_auto'] = 'N'
        input_dics['arc_merge_auto'] = 'N'

    if input_dics['plot_fdsn'] == 'Y' or input_dics['plot_arc'] == 'Y':
        input_dics['plot_all'] = 'N'

    # Create a priority list (for all requested clients)
    # For the moment, we just support: FDSN and ArcLink, but it should be
    # easily extendable!
    input_dics['priority_clients'] = []
    for cli in ['FDSN', 'ArcLink']:
        if input_dics[cli] == 'Y':
            input_dics['priority_clients'].append(cli)

    return input_dics

# ##################### input_logger ###################################


def input_logger(argus, address, inputs):
    """
    log the entered command line!
    :param argus:
    :param address:
    :param inputs:
    :return:
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
        st_argus += '%s: %s\n' % (item, inputs[item])
    logger_open = open(address, 'w')
    logger_open.write(st_argus)
    logger_open.close()
