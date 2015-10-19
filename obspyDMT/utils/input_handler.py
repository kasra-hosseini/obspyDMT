#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  input_handler.py
#   Purpose:   reading option flags and generate input_dics
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from obspy.core import UTCDateTime
from optparse import OptionParser, OptionGroup
import os
import shutil
import sys
import time

#  ##################### command_parse ###################################


def command_parse():
    """
    Parsing command-line options.
    :return:
    """
    # create command line option parser
    parser = OptionParser("%prog [options]")
    # configure command line options
    # action=".." tells OptionsParser what to save:
    # store_true saves bool TRUE,
    # store_false saves bool FALSE, store saves string; into the variable
    # given with dest="var"
    # * you need to provide every possible option here.

    helpmsg = "show the description of all option groups."
    parser.add_option("--options", action="store_true", default=False,
                      dest="options", help=helpmsg)

    helpmsg = "show the options inside specified option group. " \
              "syntax: --list_option 1, " \
              "the numbers can be seen from --options flag."
    parser.add_option("--list_option", action="store", default=False,
                      dest="list_option", help=helpmsg)

    # --------------- check the installation and obspyDMT version -------------
    group_check = OptionGroup(parser, "01. check the installation and "
                                      "obspyDMT version")
    helpmsg = "run a quick tour!"
    group_check.add_option("--tour", action="store_true",
                           dest="tour", help=helpmsg)

    helpmsg = "check all the basic dependencies and " \
              "their installed versions on " \
              "the local machine and exit!"
    group_check.add_option("--check", action="store_true",
                           dest="check", help=helpmsg)

    helpmsg = "show the obspyDMT version and exit!"
    group_check.add_option("--version", action="store_true",
                           dest="version", help=helpmsg)
    parser.add_option_group(group_check)

    # --------------- path specification --------------------------------------
    group_path = OptionGroup(parser, "02. path specification")
    helpmsg = "the path where obspyDMT will store/process/plot data " \
              "[default: './obspydmt-data']"
    group_path.add_option("--datapath", action="store",
                          dest="datapath", help=helpmsg)

    helpmsg = "if the datapath is found deleting it before running obspyDMT."
    group_path.add_option("--reset", action="store_true",
                          dest="reset", help=helpmsg)
    parser.add_option_group(group_path)

    # --------------- obspyDMT modes ------------------------------------------
    group_mode = OptionGroup(parser, "03. obspyDMT modes")
    helpmsg = "event-based request mode. [default]"
    group_mode.add_option("--event_based", action="store_true",
                          dest="event_based", help=helpmsg)

    helpmsg = "continuous request mode."
    group_mode.add_option("--continuous", action="store_true",
                          dest="continuous", help=helpmsg)

    helpmsg = "meta_data request mode."
    group_mode.add_option("--meta_data", action="store_true",
                          dest="meta_data", help=helpmsg)

    helpmsg = "local mode for processing/plotting."
    group_mode.add_option("--local", action="store_true",
                          dest="local", help=helpmsg)
    parser.add_option_group(group_mode)

    # --------------- General options (all modes) -----------------------------
    group_general = OptionGroup(parser, "04. general options (all modes)")
    helpmsg = "print available data sources. " \
              "These are the data-centers that can be given as " \
              "arguments for --data_source."
    group_general.add_option("--print_data_sources", action="store_true",
                             dest="print_data_sources", help=helpmsg)

    helpmsg = "print available event catalogs. " \
              "These are the event-catalogs that can be given as " \
              "arguments for --event_catalog."
    group_general.add_option("--print_event_catalogs", action="store_true",
                             dest="print_event_catalogs", help=helpmsg)

    helpmsg = "data source(s) to be used for retrieving " \
              "waveform/response/metadata. To know about all the available " \
              "data sources: --print_data_sources. " \
              "syntax: --data_source 'IRIS' or --data_source 'IRIS,LMU' for " \
              "which all the stations of IRIS and LMU will be downloaded. " \
              "It is also possible to '--data_source all' which will " \
              "download waveforms from all available data sources. " \
              "[default: 'IRIS']"
    group_general.add_option("--data_source", action="store",
                             dest="data_source", help=helpmsg)

    helpmsg = "retrieve waveform(s). [default]"
    group_general.add_option("--waveform", action="store_true",
                             dest="waveform", help=helpmsg)

    helpmsg = "retrieve the response file(s). [default]"
    group_general.add_option("--response", action="store_true",
                             dest="response", help=helpmsg)

    helpmsg = "set of selected directory names to work with. This option " \
              "acts as a filter on already created dataset. The default " \
              "behavior is all available directories in one dataset."
    group_general.add_option("--dir_select", action="store",
                             dest="dir_select", help=helpmsg)

    helpmsg = "use a station list instead of checking the availability. " \
              "[default: False]"
    group_general.add_option("--list_stas", action="store",
                             dest="list_stas", help=helpmsg)

    helpmsg = "retrieve/plot all the stations with " \
              "epicentral-distance >= min_epi."
    group_general.add_option("--min_epi", action="store",
                             dest="min_epi", help=helpmsg)

    helpmsg = "retrieve/plot all the stations with " \
              "epicentral-distance <= max_epi."
    group_general.add_option("--max_epi", action="store",
                             dest="max_epi", help=helpmsg)

    helpmsg = "retrieve/plot all the stations with " \
              "azimuth >= min_azi."
    group_general.add_option("--min_azi", action="store",
                             dest="min_azi", help=helpmsg)

    helpmsg = "retrieve/plot all the stations with " \
              "azimuth <= max_azi."
    group_general.add_option("--max_azi", action="store",
                             dest="max_azi", help=helpmsg)

    helpmsg = "generate a data-time file for the requests. " \
              "This file shows the required time for each request and " \
              "the size of stored data in the directory."
    group_general.add_option("--time_get_data", action="store_true",
                             dest="time_get_data", help=helpmsg)

    helpmsg = "test the program for the desired number of requests, " \
              "eg: '--test 10' will test the program for 10 " \
              "requests. [default: False]"
    group_general.add_option("--test", action="store",
                             dest="test", help=helpmsg)
    parser.add_option_group(group_general)

    # --------------- time window, waveform format and sampling rate ----------
    group_tw = OptionGroup(parser, "05. time window, waveform format and "
                                   "sampling rate (all modes)")
    helpmsg = "start time, syntax: Y-M-D-H-M-S " \
              "(eg: '2010-01-01-00-00-00') or just " \
              "Y-M-D. [default: 10 days ago]"
    group_tw.add_option("--min_date", action="store",
                        dest="min_date", help=helpmsg)

    helpmsg = "end time, syntax: Y-M-D-H-M-S " \
              "(eg: '2011-01-01-00-00-00') or just " \
              "Y-M-D. [default: 5 days ago]"
    group_tw.add_option("--max_date", action="store",
                        dest="max_date", help=helpmsg)

    helpmsg = "time parameter in seconds which determines " \
              "how close the time series data (waveform) will be cropped " \
              "before the origin time of the event (event-based mode) or " \
              "time before EACH interval (refer to '--interval' option) in " \
              "continuous mode. [default: 0.0s]"
    group_tw.add_option("--preset", action="store",
                        dest="preset", help=helpmsg)

    helpmsg = "time parameter in seconds which determines " \
              "how close the time series data (waveform) will be cropped " \
              "after the origin time of the event (event-based mode) or " \
              "time after EACH interval (refer to '--interval' option) in " \
              "continuous mode. [default: 0.0 seconds]"
    group_tw.add_option("--offset", action="store",
                        dest="offset", help=helpmsg)

    helpmsg = "consider the first phase arrival (P, Pdiff, PKIKP) to use " \
              "as the reference time, i.e. --preset and --offset will " \
              "be calculated from the first phase arrival."
    group_tw.add_option("--cut_time_phase", action="store_true",
                        dest="cut_time_phase", help=helpmsg)

    helpmsg = "format of the waveforms. the retrieved waveforms are in " \
              "mseed format and it is possible to '--waveform_format sac'. " \
              "This will fill in some basic header information as well."
    group_tw.add_option("--waveform_format", action="store",
                        dest="waveform_format", help=helpmsg)

    helpmsg = "resampling method: decimate, lanczos. " \
              "Both methods use sharp low pass filter before resampling " \
              "to avoid any aliasing effects. If the desired sampling rate " \
              "is 5 times lower than the original one, it will be " \
              "automatically done in several stages. [default: decimate]"
    group_tw.add_option("--resample_method", action="store",
                        dest="resample_method", help=helpmsg)

    helpmsg = "desired sampling rate (in Hz). Resampling is done using " \
              "either lanczos or decimation with sharp low pass filter. " \
              "If not specified, the sampling rate of the waveforms " \
              "will not be changed."
    group_tw.add_option("--des_sampling_rate", action="store",
                        dest="desired_sampling_rate", help=helpmsg)
    parser.add_option_group(group_tw)

    # --------------- stations ------------------------------------------------
    group_sta = OptionGroup(parser, "06. stations (all modes)")
    helpmsg = "identity code restriction, syntax: " \
              "net.sta.loc.cha (eg: TA.*.*.BHZ to search for " \
              "all BHZ channels in TA network). [default: *.*.*.*]"
    group_sta.add_option("--identity", action="store",
                         dest="identity", help=helpmsg)

    helpmsg = "network code. [default: *]"
    group_sta.add_option("--net", action="store",
                         dest="net", help=helpmsg)

    helpmsg = "station code. [default: *]"
    group_sta.add_option("--sta", action="store",
                         dest="sta", help=helpmsg)

    helpmsg = "location code. [default: *]"
    group_sta.add_option("--loc", action="store",
                         dest="loc", help=helpmsg)

    helpmsg = "channel code. [default: *]"
    group_sta.add_option("--cha", action="store",
                         dest="cha", help=helpmsg)

    helpmsg = "search for all the stations within the defined rectangle, " \
              "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax>. " \
              "May not be used together with circular bounding box station " \
              "restrictions (station_circle) " \
              "[default: -180.0/+180.0/-90.0/+90.0]"
    group_sta.add_option("--station_rect", action="store",
                         dest="station_rect", help=helpmsg)

    helpmsg = "search for all the stations within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "May not be used together with rectangular bounding box " \
              "station restrictions (station_rect)."
    group_sta.add_option("--station_circle", action="store",
                         dest="station_circle", help=helpmsg)
    parser.add_option_group(group_sta)

    # --------------- parallel request/process and bulk request ---------------
    group_parallel = OptionGroup(parser, "07. parallel request/process and "
                                         "bulk request (all modes)")
    helpmsg = "enable parallel waveform/response request."
    group_parallel.add_option("--req_parallel", action="store_true",
                              dest="req_parallel", help=helpmsg)

    helpmsg = "number of threads to be used in --req_parallel. [default: 4]"
    group_parallel.add_option("--req_np", action="store",
                              dest="req_np", help=helpmsg)

    helpmsg = "using the bulkdataselect web service. " \
              "Since this method returns multiple channels of " \
              "time series data for specified time ranges in one request, " \
              "it speeds up the waveform retrieving approximately by " \
              "a factor of two. [RECOMMENDED]"
    group_parallel.add_option("--bulk", action="store_true",
                              dest="bulk", help=helpmsg)

    helpmsg = "parallel processing."
    group_parallel.add_option("--parallel_process", action="store_true",
                              dest="parallel_process", help=helpmsg)

    helpmsg = "number of threads to be used in --parallel_process. " \
              "[default: 4]"
    group_parallel.add_option("--process_np", action="store",
                              dest="process_np", help=helpmsg)
    parser.add_option_group(group_parallel)

    # --------------- restricted data request ----------
    group_restrict = OptionGroup(parser, "08. restricted data request "
                                         "(all modes)")
    helpmsg = "username for restricted data requests (waveform/response). " \
              "[default: None]"
    group_restrict.add_option("--user", action="store",
                              dest="username", help=helpmsg)

    helpmsg = "password for restricted data requests (waveform/response). " \
              "[default: None]"
    group_restrict.add_option("--pass", action="store",
                              dest="password", help=helpmsg)
    parser.add_option_group(group_restrict)

    # --------------- event_based mode ----------------------------------------
    group_ev_based = OptionGroup(parser, "09. event-based mode")
    helpmsg = "event catalog (LOCAL, NEIC_USGS, GCMT_COMBO, IRIS, NCEDC, " \
              "USGS, INGV, ISC, NERIES). [default: LOCAL]"
    group_ev_based.add_option("--event_catalog", action="store",
                              dest="event_catalog", help=helpmsg)

    helpmsg = "only retrieve event information and exit!"
    group_ev_based.add_option("--event_info", action="store",
                              dest="event_info", help=helpmsg)

    helpmsg = "read in an existing event catalog and proceed. " \
              "Currently supported data formats: " \
              "'QUAKEML', 'MCHEDR' e.g.: --read_catalog 'path/to/file'"
    group_ev_based.add_option("--read_catalog", action="store",
                              dest="read_catalog", help=helpmsg)

    helpmsg = "minimum depth. [default: -10.0 (above the surface!)]"
    group_ev_based.add_option("--min_depth", action="store",
                              dest="min_depth", help=helpmsg)

    helpmsg = "maximum depth. [default: +6000.0]"
    group_ev_based.add_option("--max_depth", action="store",
                              dest="max_depth", help=helpmsg)

    helpmsg = "minimum magnitude. [default: 5.5]"
    group_ev_based.add_option("--min_mag", action="store",
                              dest="min_mag", help=helpmsg)

    helpmsg = "maximum magnitude. [default: 9.9]"
    group_ev_based.add_option("--max_mag", action="store",
                              dest="max_mag", help=helpmsg)

    helpmsg = "magnitude type. " \
              "Some common types (there are many) include " \
              "'Ml' (local/Richter magnitude), " \
              "'Ms' (surface magnitude), " \
              "'mb' (body wave magnitude), " \
              "'Mw' (moment magnitude). " \
              "[default: None, i.e. all magnitude types]"
    group_ev_based.add_option("--mag_type", action="store",
                              dest="mag_type", help=helpmsg)

    helpmsg = "search for all the events within the defined rectangle, " \
              "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax> " \
              "[default: -180.0/+180.0/-90.0/+90.0]"
    group_ev_based.add_option("--event_rect", action="store",
                              dest="event_rect", help=helpmsg)

    helpmsg = "search for all the events within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "May not be used together with rectangular bounding box " \
              "event restrictions (--event_rect)."
    group_ev_based.add_option("--event_circle", action="store",
                              dest="event_circle", help=helpmsg)

    helpmsg = "maximum number of events to be requested. [default: 2500]"
    group_ev_based.add_option("--max_result", action="store",
                              dest="max_result", help=helpmsg)

    helpmsg = "retrieve synthetic waveforms calculated by normal mode " \
              "summation code. (ShakeMovie project)"
    group_ev_based.add_option("--normal_mode_syn", action="store_true",
                              dest="normal_mode_syn", help=helpmsg)

    helpmsg = "retrieve synthetic waveforms calculated by SPECFEM3D. " \
              "(ShakeMovie project)"
    group_ev_based.add_option("--specfem3D", action="store_true",
                              dest="specfem3D", help=helpmsg)
    parser.add_option_group(group_ev_based)

    # --------------- continuous request --------------------------------------
    group_cont = OptionGroup(parser, "10. continuous request")
    helpmsg = "time interval for dividing the continuous request. " \
              "[default: 86400 sec (1 day)]"
    group_cont.add_option("--interval", action="store",
                          dest="interval", help=helpmsg)
    parser.add_option_group(group_cont)

    # --------------- processing ----------------------------------------------
    group_process = OptionGroup(parser, "11. processing")
    helpmsg = "process the local/retrieved data. XXX"
    group_process.add_option("--pre_process", action="store",
                             dest="pre_process", help=helpmsg)

    helpmsg = "apply instrument correction in the process unit."
    group_process.add_option("--instrument_correction", action="store",
                             dest="instrument_correction", help=helpmsg)

    helpmsg = "correct the raw waveforms for DIS (m), VEL (m/s) or " \
              "ACC (m/s^2). [default: DIS]"
    group_process.add_option("--corr_unit", action="store",
                             dest="corr_unit", help=helpmsg)

    helpmsg = "apply a bandpass filter to the data trace before " \
              "deconvolution ('None' if you do not need pre_filter), " \
              "syntax: '(f1,f2,f3,f4)' which " \
              "are the four corner frequencies " \
              "of a cosine taper, one between f2 and f3 and tapers to zero " \
              "for f1 < f < f2 and f3 < f < f4. " \
              "[default: '(0.008, 0.012, 3.0, 4.0)']"
    group_process.add_option("--pre_filt", action="store",
                             dest="pre_filt", help=helpmsg)

    helpmsg = "water level for spectrum [default: 600.0]"
    group_process.add_option("--water_level", action="store",
                             dest="water_level", help=helpmsg)
    parser.add_option_group(group_process)

    # --------------- plotting ------------------------------------------------
    group_plt = OptionGroup(parser, "12. plotting")
    helpmsg = "activating the plotting functionality."
    group_plt.add_option("--plot", action="store_true",
                         dest="plot", help=helpmsg)

    helpmsg = "plot all the stations found " \
              "in the specified directory (--datapath)."
    group_plt.add_option("--plot_sta", action="store_true",
                         dest="plot_sta", help=helpmsg)

    helpmsg = "plot all the events found " \
              "in the specified directory (--datapath)."
    group_plt.add_option("--plot_ev", action="store_true",
                         dest="plot_ev", help=helpmsg)

    helpmsg = "plot Beachballs instead of dots for the event location."
    group_plt.add_option("--plot_focal", action="store_true",
                         dest="plot_focal", help=helpmsg)

    helpmsg = "plot the ray coverage for all the station-event pairs " \
              "found in the specified directory (--datapath)."
    group_plt.add_option("--plot_ray", action="store_true",
                         dest="plot_ray", help=helpmsg)

    helpmsg = "plot \"Data(MB)-Time(Sec)\" for the " \
              "specified directory (--datapath) " \
              "-- ATTENTION: \"time_get_data\" file should " \
              "exist in the \"info\" folder " \
              "[refer to \"--time_get_data\" option]"
    group_plt.add_option("--plot_dt", action="store_true",
                         dest="plot_dt", help=helpmsg)

    helpmsg = "create a seismicity map and some basic statistics on the " \
              "results."
    group_plt.add_option("--plot_seismicity", action="store_true",
                         dest="plot_seismicity", help=helpmsg)

    helpmsg = "depth bins for plotting the seismicity histrogram. " \
              "[default: 10]"
    group_plt.add_option("--depth_bins_seismicity", action="store",
                         dest="depth_bins_seismicity", help=helpmsg)

    helpmsg = "plot waveforms arranged by the epicentral distance."
    group_plt.add_option("--plot_waveform", action="store_true",
                         dest="plot_waveform", help=helpmsg)

    helpmsg = "directory name that contains the waveforms, e.g. raw. " \
              "[default: raw]"
    group_plt.add_option("--plot_dir_name", action="store",
                         dest="plot_dir_name", help=helpmsg)

    helpmsg = "the path where obspyDMT will store the plots " \
              "[default: '.', i.e. current directory]"
    group_plt.add_option("--plot_save", action="store",
                         dest="plot_save", help=helpmsg)

    helpmsg = "format of the plots saved on the local machine [default: 'png']"
    group_plt.add_option("--plot_format", action="store",
                         dest="plot_format", help=helpmsg)

    helpmsg = "central meridian (x-axis origin) for projection " \
              "[default: 180]"
    group_plt.add_option("--plot_lon0", action="store",
                         dest="plot_lon0", help=helpmsg)
    parser.add_option_group(group_plt)

    # --------------- explore stationXML --------------------------------------
    group_pltxml = OptionGroup(parser, "13. explore stationXML")
    helpmsg = "plot the contents of stationXML file(s)."
    group_pltxml.add_option("--plot_stationxml", action="store_true",
                            dest="plot_stationxml", help=helpmsg)

    helpmsg = "datetime to be used for plotting the transfer function, " \
              "syntax: Y-M-D-H-M-S (eg: '2011-01-01-00-00-00') or just " \
              "Y-M-D. If this is not set, the starting date of the last " \
              "channel in stationXML will be used instead!"
    group_pltxml.add_option("--plotxml_date", action="store",
                            dest="plotxml_date", help=helpmsg)

    helpmsg = "plot all the stages available in the response file."
    group_pltxml.add_option("--plotxml_allstages", action="store_true",
                            dest="plotxml_allstages", help=helpmsg)

    helpmsg = "plot Poles And Zeros (PAZ) of the response file."
    group_pltxml.add_option("--plotxml_paz", action="store_true",
                            dest="plotxml_paz", help=helpmsg)

    helpmsg = "plot only stage 1 and 2 of full response file."
    group_pltxml.add_option("--plotxml_plotstage12", action="store_true",
                            dest="plotxml_plotstage12", help=helpmsg)

    helpmsg = "start stage in response file to be considered for plotting " \
              "the transfer function. [default: 1]"
    group_pltxml.add_option("--plotxml_start_stage", action="store",
                            dest="plotxml_start_stage", help=helpmsg)

    helpmsg = "final stage in response file to be considered for plotting " \
              "the transfer function. " \
              "[default: 100, in normal cases this is order of magnitude " \
              "more than the available stages; " \
              "however, obspyDMT will adjust itself with the number of " \
              "available stages at each stationXML file " \
              "if there are less than 100 stages!]"
    group_pltxml.add_option("--plotxml_end_stage", action="store",
                            dest="plotxml_end_stage", help=helpmsg)

    helpmsg = "minimum frequency to be used for plotting the transfer " \
              "function. [default: 0.01]"
    group_pltxml.add_option("--plotxml_min_freq", action="store",
                            dest="plotxml_min_freq", help=helpmsg)

    helpmsg = "plot all the stations that their instrument responses have " \
              "been compared (PAZ against full response)."
    group_pltxml.add_option("--plotxml_map_compare", action="store_true",
                            dest="plotxml_map_compare", help=helpmsg)

    helpmsg = "percentage of the phase transfer function length to be used " \
              "for checking the difference between different methods, " \
              "e.g. 100 will be the whole transfer function, " \
              "80 means compare the transfer function from " \
              "min_freq (determined by --plotxml_min_freq) up to " \
              "20 percent before the Nyquist frequency. [default: 80]"
    group_pltxml.add_option("--plotxml_percentage", action="store",
                            dest="plotxml_percentage", help=helpmsg)

    helpmsg = "maximum allowable length (in percentage) to differ between " \
              "two different methods of instrument correction. " \
              "This only applies to phase difference. [default: 10]"
    group_pltxml.add_option("--plotxml_phase_threshold", action="store",
                            dest="plotxml_phase_threshold", help=helpmsg)

    helpmsg = "output of the transfer function: DIS/VEL/ACC. [default: VEL]"
    group_pltxml.add_option("--plotxml_output", action="store",
                            dest="plotxml_output", help=helpmsg)

    helpmsg = "do not plot the full response file."
    group_pltxml.add_option("--plotxml_no_response", action="store_true",
                            dest="plotxml_no_response", help=helpmsg)
    parser.add_option_group(group_pltxml)

    # --------------- others --------------------------------------------------
    group_others = OptionGroup(parser, "14. others (email, time-out)")
    helpmsg = "send an email to the specified email-address after " \
              "completing the job, syntax: --email email_address. " \
              "[default: False]"
    group_others.add_option("--email", action="store",
                            dest="email", help=helpmsg)

    helpmsg = "timeout (in sec) for sending request (availability) to " \
              "ArcLink. [default: 40]"
    group_others.add_option("--arc_avai_timeout", action="store",
                            dest="arc_avai_timeout", help=helpmsg)

    helpmsg = "timeout for sending request (waveform/response) to ArcLink. " \
              "[default: 2]"
    group_others.add_option("--arc_wave_timeout", action="store",
                            dest="arc_wave_timeout", help=helpmsg)

    parser.add_option_group(group_others)

    # parse command line options
    (options, args) = parser.parse_args()

    return options, args, parser

# ##################### read_input_command ##############################


def read_input_command(parser, **kwargs):
    """
    Create input_dics object (dictionary) based on command-line options.
    The default values are as "input_dics" object (below)
    :param parser:
    :param kwargs:
    :return:
    """
    # Defining the default values.
    input_dics = {'datapath': 'obspydmt-data',

                  'event_based': True,

                  'data_source': 'IRIS',
                  'waveform': True, 'response': True,
                  'dir_select': False,
                  'list_stas': False,
                  'min_epi': False, 'max_epi': False,
                  'min_azi': False, 'max_azi': False,
                  'test': False,

                  'min_date': str(UTCDateTime() - 60 * 60 * 24 * 10 * 1),
                  'max_date': str(UTCDateTime() - 60 * 60 * 24 * 5 * 1),
                  'preset': 0.0, 'offset': 1800.0,
                  'waveform_format': False,
                  'resample_method': 'lanczos',
                  'des_sampling_rate': None,

                  'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
                  'lat_cba': None, 'lon_cba': None,
                  'mr_cba': None, 'Mr_cba': None,
                  'mlat_rbb': None, 'Mlat_rbb': None,
                  'mlon_rbb': None, 'Mlon_rbb': None,

                  'req_np': 4,
                  'process_np': 4,

                  'username': None,
                  'password': None,

                  'event_catalog': 'LOCAL',
                  'min_depth': -10.0, 'max_depth': +6000.0,
                  'min_mag': 5.5, 'max_mag': 9.9,
                  'mag_type': None,
                  'evlatmin': None, 'evlatmax': None,
                  'evlonmin': None, 'evlonmax': None,
                  'evlat': None, 'evlon': None,
                  'evradmin': None, 'evradmax': None,
                  'max_result': 2500,

                  'interval': 3600*24,

                  'pre_process': 'True',
                  'instrument_correction': 'True',
                  'corr_unit': 'DIS',
                  'pre_filt': '(0.008, 0.012, 3.0, 4.0)',
                  'water_level': 600.0,

                  'depth_bins_seismicity': 10,
                  'plot_dir_name': 'raw',
                  'plot_save': '.', 'plot_format': 'png',
                  'plot_lon0': 180,

                  'plotxml_date': False,
                  'plotxml_start_stage': 1,
                  'plotxml_end_stage': 100,
                  'plotxml_min_freq': 0.01,
                  'plotxml_percentage': 80,
                  'plotxml_phase_threshold': 10.,
                  'plotxml_output': 'VEL',

                  'email': False,
                  'arc_avai_timeout': 40,
                  'arc_wave_timeout': 2,
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

    # ===================== printing the description of all option groups======
    if options.options:
        print "============="
        print "option groups"
        print "=============\n"
        for grp in parser.option_groups:
            print grp.title
        print "\n\n==============================================="
        print "To check the available options in each group:"
        print "obspyDMT --list_option <group_number>"
        print "==============================================="
        sys.exit()

    # ==================== printing the available options in each option group=
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

    # ==================== obspyDMT version====================================
    if options.version:
        print '\n\t\t' + '*********************************'
        print '\t\t' + '*        obspyDMT version:      *'
        print '\t\t' + '*\t' + 5*' ' + '1.0.1b1' + '\t\t*'
        print '\t\t' + '*********************************'
        print '\n'
        sys.exit(2)

    # =================== Check importing the required modules=================
    if options.check:
        descrip = descrip_generator()
        print "================================="
        for i in range(len(descrip)):
            print descrip[i]
        print "=================================\n"
        sys.exit(2)

    # =================== obspyDMT quick tour==================================
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
        options.event_catalog = 'IRIS'
        options.req_parallel = True

    # =================== Absolute path generator==============================
    for paths in ['datapath']:
        optatr_path = getattr(options, paths)
        if optatr_path:
            if optatr_path != 'N' and not os.path.isabs(optatr_path):
                setattr(options, paths,
                        os.path.join(os.getcwd(), getattr(options, paths)))

    # delete data path if -R or --reset args are given at cmdline
    if options.reset:
        # try-except so we don't get an exception if path doesnt exist
        try:
            shutil.rmtree(options.datapath)
            print '\n================================'
            print 'Remove the following directory:'
            print str(options.datapath)
            print 'obspyDMT is going to re-create it...'
            print '================================\n'
        except Exception, e:
            print "Warning: can not remove the following directory: %s" % e
            pass
    input_dics['datapath'] = options.datapath

    # =================== obspyDMT mode========================================
    # plot_stationxml option always change the mode to local
    input_dics['plot_stationxml'] = options.plot_stationxml
    if input_dics['plot_stationxml']:
        options.event_based = False
        options.continuous = False
        options.meta_data = False
        options.local = True

    input_dics['event_based'] = options.event_based
    input_dics['primary_mode'] = 'event_based'

    if options.continuous:
        input_dics['event_based'] = False
        input_dics['continuous'] = options.continuous
        input_dics['meta_data'] = False
        input_dics['local'] = False
        input_dics['primary_mode'] = 'continuous'
    else:
        input_dics['continuous'] = False
    if options.meta_data:
        input_dics['event_based'] = False
        input_dics['continuous'] = False
        input_dics['meta_data'] = options.meta_data
        input_dics['local'] = False
        input_dics['primary_mode'] = 'meta_data'
    else:
        input_dics['meta_data'] = False
    if options.local:
        input_dics['event_based'] = False
        input_dics['continuous'] = False
        input_dics['meta_data'] = False
        input_dics['local'] = options.local
        input_dics['primary_mode'] = 'local'
    else:
        input_dics['local'] = False

    print "\nobspyDMT primary mode: %s\n" % input_dics['primary_mode']

    if input_dics['primary_mode'] in ['event_based', 'continuous']:
        input_dics['meta_data'] = True

    # =================== Print Data sources and Event catalogs
    if options.print_data_sources:
        input_dics['print_data_sources'] = True
    else:
        input_dics['print_data_sources'] = False

    if options.print_event_catalogs:
        input_dics['print_event_catalogs'] = True
    else:
        input_dics['print_event_catalogs'] = False

    # =================== Data sources
    input_dics['data_source'] = options.data_source
    if input_dics['data_source'].lower() == 'all':
        input_dics['data_source'] = \
            "LMU,GFZ,ETH,INGV,NIEP,IPGP,RESIF,ORFEUS,ODC,BGR,KOERI," \
            "GEONET,USP,NCEDC,SCEDC,IRIS,ARCLINK"
        print "\n================================="
        print "Waveforms will be retrieved from:"
        print input_dics['data_source']
        print "=================================\n\n"
    input_dics['data_source'] = \
        [x.strip() for x in input_dics['data_source'].split(',')]
    for cli in range(len(input_dics['data_source'])):
        input_dics['data_source'][cli] = input_dics['data_source'][cli].upper()

    input_dics['waveform'] = options.waveform
    input_dics['response'] = options.response

    input_dics['dir_select'] = options.dir_select
    if input_dics['dir_select']:
        input_dics['dir_select'] = \
            [x.strip() for x in input_dics['dir_select'].split(',')]

    input_dics['list_stas'] = options.list_stas

    if options.min_epi:
        input_dics['min_epi'] = float(options.min_epi)
    else:
        input_dics['min_epi'] = False

    if options.max_epi:
        input_dics['max_epi'] = float(options.max_epi)
    else:
        input_dics['max_epi'] = False

    if options.min_azi:
        input_dics['min_azi'] = float(options.min_azi)
    else:
        input_dics['min_azi'] = False

    if options.max_azi:
        input_dics['max_azi'] = float(options.max_azi)
    else:
        input_dics['max_azi'] = False

    input_dics['time_get_data'] = options.time_get_data
    if options.test:
        input_dics['test'] = True
        input_dics['test_num'] = int(options.test)

    input_dics['min_date'] = str(UTCDateTime(options.min_date))
    input_dics['max_date'] = str(UTCDateTime(options.max_date))
    input_dics['preset'] = float(options.preset)
    input_dics['offset'] = float(options.offset)
    if options.cut_time_phase:
        input_dics['cut_time_phase'] = True
    else:
        input_dics['cut_time_phase'] = False
    input_dics['waveform_format'] = options.waveform_format
    input_dics['resample_method'] = options.resample_method
    if options.des_sampling_rate:
        input_dics['des_sampling_rate'] = float(options.des_sampling_rate)
    else:
        input_dics['des_sampling_rate'] = False

    # Extract network, station, location, channel if the user has given an
    # identity code (-i xx.xx.xx.xx)
    if options.identity:
        try:
            options.net, options.sta, options.loc, options.cha = \
                options.identity.split('.')
        except Exception, e:
            print "Erroneous identity code given: %s" % e
            sys.exit(2)
    input_dics['net'] = options.net
    input_dics['sta'] = options.sta
    if options.loc == "''":
        input_dics['loc'] = ''
    elif options.loc == '""':
        input_dics['loc'] = ''
    else:
        input_dics['loc'] = options.loc
    input_dics['cha'] = options.cha

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

    input_dics['lon_cba'] = options.lon_cba
    input_dics['lat_cba'] = options.lat_cba
    input_dics['mr_cba'] = options.mr_cba
    input_dics['Mr_cba'] = options.Mr_cba

    input_dics['mlon_rbb'] = options.mlon_rbb
    input_dics['Mlon_rbb'] = options.Mlon_rbb
    input_dics['mlat_rbb'] = options.mlat_rbb
    input_dics['Mlat_rbb'] = options.Mlat_rbb

    input_dics['req_parallel'] = options.req_parallel
    input_dics['req_np'] = int(options.req_np)
    input_dics['bulk'] = options.bulk
    input_dics['parallel_process'] = options.parallel_process
    input_dics['process_np'] = int(options.process_np)

    input_dics['username'] = options.username
    input_dics['password'] = options.password

    if options.event_catalog:
        input_dics['event_catalog'] = options.event_catalog.upper()
    input_dics['event_info'] = options.event_info
    if options.read_catalog:
        input_dics['read_catalog'] = options.read_catalog
    else:
        input_dics['read_catalog'] = 'N'

    input_dics['min_depth'] = float(options.min_depth)
    input_dics['max_depth'] = float(options.max_depth)
    input_dics['min_mag'] = float(options.min_mag)
    input_dics['max_mag'] = float(options.max_mag)
    input_dics['mag_type'] = options.mag_type
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

    input_dics['evlonmin'] = options.evlonmin
    input_dics['evlonmax'] = options.evlonmax
    input_dics['evlatmin'] = options.evlatmin
    input_dics['evlatmax'] = options.evlatmax

    input_dics['evlat'] = options.evlat
    input_dics['evlon'] = options.evlon
    input_dics['evradmax'] = options.evradmax
    input_dics['evradmin'] = options.evradmin

    input_dics['max_result'] = int(options.max_result)
    input_dics['specfem3D'] = options.specfem3D
    input_dics['normal_mode_syn'] = options.normal_mode_syn

    input_dics['interval'] = float(options.interval)

    input_dics['pre_process'] = eval(options.pre_process)
    input_dics['instrument_correction'] = eval(options.instrument_correction)
    input_dics['corr_unit'] = options.corr_unit
    input_dics['pre_filt'] = options.pre_filt
    input_dics['water_level'] = float(options.water_level)

    input_dics['plot'] = options.plot
    input_dics['plot_sta'] = options.plot_sta
    input_dics['plot_ev'] = options.plot_ev
    input_dics['plot_focal'] = options.plot_focal
    input_dics['plot_ray'] = options.plot_ray
    input_dics['plot_dt'] = options.plot_dt
    input_dics['plot_seismicity'] = options.plot_seismicity
    input_dics['depth_bins_seismicity'] = int(options.depth_bins_seismicity)
    input_dics['plot_waveform'] = options.plot_waveform
    if input_dics['plot_waveform']:
        input_dics['plot'] = True
    input_dics['plot_dir_name'] = options.plot_dir_name
    input_dics['plot_save'] = options.plot_save
    input_dics['plot_format'] = options.plot_format
    input_dics['plot_lon0'] = float(options.plot_lon0)

    if input_dics['plot']:
        input_dics['pre_process'] = False

    if options.plotxml_date:
        input_dics['plotxml_date'] = UTCDateTime(options.plotxml_date)
    else:
        input_dics['plotxml_date'] = options.plotxml_date
    input_dics['plotxml_allstages'] = options.plotxml_allstages
    input_dics['plotxml_paz'] = options.plotxml_paz
    input_dics['plotxml_plotstage12'] = options.plotxml_plotstage12
    input_dics['plotxml_start_stage'] = int(options.plotxml_start_stage)
    input_dics['plotxml_end_stage'] = int(options.plotxml_end_stage)
    input_dics['plotxml_min_freq'] = float(options.plotxml_min_freq)
    input_dics['plotxml_map_compare'] = options.plotxml_map_compare
    input_dics['plotxml_percentage'] = float(options.plotxml_percentage)
    input_dics['plotxml_phase_threshold'] = \
        float(options.plotxml_phase_threshold)
    input_dics['plotxml_output'] = options.plotxml_output
    if options.plotxml_no_response:
        input_dics['plotxml_response'] = False
    else:
        input_dics['plotxml_response'] = True

    input_dics['email'] = options.email
    if input_dics['email']:
        try:
            import smtplib
        except Exception as error:
            print "\n********************************************************"
            print "Unable to import smtplib. Sending email is not possible!"
            print "Error: %s" % error
            print "********************************************************\n"
            input_dics['email'] = False
    input_dics['arc_avai_timeout'] = float(options.arc_avai_timeout)
    input_dics['arc_wave_timeout'] = float(options.arc_wave_timeout)

    return input_dics

#  ##################### descrip_generator ###################################


def descrip_generator():
    """
    check the basic dependencies!
    :return:
    """
    print "********************************"
    print "Check all the BASIC dependencies"

    try:
        from obspy import __version__ as obs_ver
        descrip = ['obspy ver: ' + obs_ver]
    except Exception as error:
        descrip = ['obspy: not installed\nerror:\n%s\n' % error]

    try:
        import numpy as np
        descrip.append('numpy ver: ' + np.__version__)
    except Exception, error:
        descrip.append('numpy: not installed\nerror:\n%s\n' % error)

    try:
        import scipy
        descrip.append('scipy ver: ' + scipy.__version__)
    except Exception, error:
        descrip.append('scipy: not installed\nerror:\n%s\n' % error)

    try:
        from matplotlib import __version__ as mat_ver
        import matplotlib.pyplot as plt
        descrip.append('matplotlib ver: ' + mat_ver)
    except Exception as error:
        descrip.append('matplotlib: not installed\nerror:\n%s\n' % error)

    try:
        from mpl_toolkits.basemap import __version__ as base_ver
        from mpl_toolkits.basemap import Basemap
        descrip.append('Basemap ver: ' + base_ver)
    except Exception as error:
        descrip.append('Basemap: not installed\nerror:\n%s\n'
                       'You can not use all the plot options' % error)
    print "********************************\n"
    return descrip

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
