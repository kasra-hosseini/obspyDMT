#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  input_handler.py
#   Purpose:   reading option flags and generate input_dics
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
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

    # --------------- check installation -------------
    group_check = OptionGroup(parser, "01. check installation")
    helpmsg = "Run a quick tour."
    group_check.add_option("--tour", action="store_true",
                           dest="tour", help=helpmsg)

    helpmsg = "Check all basic dependencies and their installed versions " \
              "on the local machine and exit."
    group_check.add_option("--check", action="store_true",
                           dest="check", help=helpmsg)

    helpmsg = "Show the obspyDMT version and exit."
    group_check.add_option("--version", action="store_true",
                           dest="version", help=helpmsg)
    parser.add_option_group(group_check)

    # --------------- local path specification --------------------------------
    group_path = OptionGroup(parser, "02. local path specification")
    helpmsg = "Path where obspyDMT will store/process/plot data " \
              "(default: './obspydmt-data')."
    group_path.add_option("--datapath", action="store",
                          dest="datapath", help=helpmsg)

    helpmsg = "If the datapath is found, delete it before running obspyDMT."
    group_path.add_option("--reset", action="store_true",
                          dest="reset", help=helpmsg)
    parser.add_option_group(group_path)

    # --------------- data retrieval modes ------------------------------------
    group_mode = OptionGroup(parser, "03. data retrieval modes")
    helpmsg = "Event-based request mode (default)."
    group_mode.add_option("--event_based", action="store_true",
                          dest="event_based", help=helpmsg)

    helpmsg = "Continuous time series request mode."
    group_mode.add_option("--continuous", action="store_true",
                          dest="continuous", help=helpmsg)

    helpmsg = "Metadata request mode."
    group_mode.add_option("--meta_data", action="store_true",
                          dest="meta_data", help=helpmsg)

    helpmsg = "Local mode for processing/plotting (no data retrieval)."
    group_mode.add_option("--local", action="store_true",
                          dest="local", help=helpmsg)
    parser.add_option_group(group_mode)

    # --------------- general options (all modes) -------------------
    group_general = OptionGroup(parser, "04. general options (all modes)")
    helpmsg = "Data source(s) for retrieving waveform/response/metadata " \
              "(default: 'IRIS'). Examples: 'IRIS' or 'IRIS,ORFEUS' or 'all'"
    group_general.add_option("--data_source", action="store",
                             dest="data_source", help=helpmsg)

    helpmsg = "Print supported data centers that can be passed as " \
              "arguments to --data_source."
    group_general.add_option("--print_data_sources", action="store_true",
                             dest="print_data_sources", help=helpmsg)

    helpmsg = "Print supported earthquake catalogs that can be passed as " \
              "arguments to --event_catalog."
    group_general.add_option("--print_event_catalogs", action="store_true",
                             dest="print_event_catalogs", help=helpmsg)

    helpmsg = "Retrieve waveform(s) (default: True)."
    group_general.add_option("--waveform", action="store",
                             dest="waveform", help=helpmsg)

    helpmsg = "Retrieve waveform(s), force override of any pre-existing " \
              "waveforms in local datapath directory."
    group_general.add_option("--force_waveform", action="store_true",
                             dest="force_waveform", help=helpmsg)

    helpmsg = "Retrieve response file(s) (default: True)."
    group_general.add_option("--response", action="store",
                             dest="response", help=helpmsg)

    helpmsg = "Retrieve response file(s), force override of any pre-existing " \
              "response files in local datapath directory."
    group_general.add_option("--force_response", action="store_true",
                             dest="force_response", help=helpmsg)

    helpmsg = "Selects a subset of data directories for which to " \
              "update/process/plot the contents " \
              "(default False, i.e., all subdirectories will be considered). " \
              "Example: 'dir1,dir2'"
    group_general.add_option("--dir_select", action="store",
                             dest="dir_select", help=helpmsg)

    helpmsg = "Retrieve/plot all stations with epicentral distance >= min epi."
    group_general.add_option("--min_epi", action="store",
                             dest="min_epi", help=helpmsg)

    helpmsg = "Retrieve/plot all stations with epicentral distance <= max epi."
    group_general.add_option("--max_epi", action="store",
                             dest="max_epi", help=helpmsg)

    helpmsg = "Retrieve/plot all stations with azimuth >= min azi."
    group_general.add_option("--min_azi", action="store",
                             dest="min_azi", help=helpmsg)

    helpmsg = "Retrieve/plot all stations with azimuth <= max azi."
    group_general.add_option("--max_azi", action="store",
                             dest="max_azi", help=helpmsg)

    helpmsg = "User-provided station list instead of querying availability " \
              "with a data center (default: False). " \
              "Example: /path/list-stations"
    group_general.add_option("--list_stas", action="store",
                             dest="list_stas", help=helpmsg)

    # XXX NOT in Table-2
    helpmsg = "test the program for the desired number of requests, " \
              "e.g.: '--test 10' will test the program for 10 " \
              "requests. [default: False]"
    group_general.add_option("--test", action="store",
                             dest="test", help=helpmsg)
    parser.add_option_group(group_general)

    # ---------------  time window, waveform format, and sampling rate
    # ---------------  (all modes)
    group_tw = OptionGroup(parser, "05. time window, waveform format, and "
                                   "sampling rate (all modes)")
    helpmsg = "Start time, syntax: 'YYYY-MM-DD-HH-MM-SS' or 'YYYY-MM-DD' " \
              "(default: '1970-01-01')."
    group_tw.add_option("--min_date", action="store",
                        dest="min_date", help=helpmsg)

    helpmsg = "End time, syntax: 'YYYY-MM-DD-HH-MM-SS' or " \
              "'YYYY-MM-DD' (default: Today)."
    group_tw.add_option("--max_date", action="store",
                        dest="max_date", help=helpmsg)

    helpmsg = "Time interval in seconds to add to the retrieved time series " \
              "before its reference time. In event_based mode, " \
              "the reference time is the earthquake origin time " \
              "by default but can be modified by --cut_time_phase. " \
              "In continuous mode, the reference time(s) are specified by " \
              "--interval option, and --preset prepends " \
              "the specified lead to each interval (default: 0). " \
              "Example: 300"
    group_tw.add_option("--preset", action="store",
                        dest="preset", help=helpmsg)

    helpmsg = "Time interval in seconds to include to the retrieved " \
              "time series after the time(s) reference. " \
              "In event based mode, the reference time is " \
              "the earthquake origin time by default but can be modified " \
              "by --cut_time_phase. " \
              "In continuous mode, the reference time(s) are specified by " \
              "--interval option, and --offset appends " \
              "the specified offset to each interval "\
              "(default: 1800 for event-based mode and 0 for continuous mode). " \
              "Example: 3600"
    group_tw.add_option("--offset", action="store",
                        dest="offset", help=helpmsg)

    helpmsg = "In event based mode, use as reference time " \
              "the first-arriving phase " \
              "(i.e., P, Pdiff or PKIKP, determined automatically). " \
              "Overrides the use of origin time as default reference time."
    group_tw.add_option("--cut_time_phase", action="store_true",
                        dest="cut_time_phase", help=helpmsg)

    helpmsg = "Format of retrieved waveforms. " \
              "Default is miniseed ('mseed'), alternative option is 'sac'. " \
              "This fills in some basic header information as well."
    group_tw.add_option("--waveform_format", action="store",
                        dest="waveform_format", help=helpmsg)

    helpmsg = "desired sampling rate (in Hz). Resampling is done using " \
              "either lanczos or decimation with sharp low pass filter. " \
              "If not specified, the sampling rate of the waveforms " \
              "will not be changed."
    helpmsg = "Desired sampling rate (in Hz). If not specified, " \
              "the sampling rate of the waveforms will not be changed. " \
              "Example: 10"
    group_tw.add_option("--sampling_rate", action="store",
                        dest="sampling_rate", help=helpmsg)

    helpmsg = "Resampling method: 'decimate' or 'lanczos'. " \
              "Both methods use sharp low pass filters before resampling " \
              "in order to avoid aliasing. " \
              "If the desired sampling rate is 5 times lower " \
              "than the original one, resampling will be done " \
              "in several stages (default: 'lanczos'). " \
              "Example: 'decimate'"
    group_tw.add_option("--resample_method", action="store",
                        dest="resample_method", help=helpmsg)
    parser.add_option_group(group_tw)

    # --------------- stations (all modes) ------------------------------------
    group_sta = OptionGroup(parser, "06. stations (all modes)")
    helpmsg = "Network code (default: *). Example: 'TA' or 'TA,G' or 'T*'"
    group_sta.add_option("--net", action="store",
                         dest="net", help=helpmsg)

    helpmsg = "Station code (default: *). Example: 'R*' or " \
              "'RR01' or 'RR01,RR02'"
    group_sta.add_option("--sta", action="store",
                         dest="sta", help=helpmsg)

    helpmsg = "Location code (default: *). Example: '00' or '*'"
    group_sta.add_option("--loc", action="store",
                         dest="loc", help=helpmsg)

    helpmsg = "Channel code (default: *). Example: 'BHZ' or 'BHZ,BHE' or " \
              "'BH*'"
    group_sta.add_option("--cha", action="store",
                         dest="cha", help=helpmsg)

    helpmsg = "Identity code restriction, syntax: net.sta.loc.cha, " \
              "e.g.: IU.*.*.BHZ to search for all BHZ channels " \
              "in IU network (default: *.*.*.*)."
    group_sta.add_option("--identity", action="store",
                         dest="identity", help=helpmsg)

    helpmsg = "Include all stations within the defined rectangle, " \
              "syntax: <lonmin>/<lonmax>/<latmin>/<latmax>. " \
              "Cannot be combined with " \
              "circular bounding box (--station_circle) " \
              "(default: -180.0/+180.0/-90.0/+90.0). " \
              "Example: '20/30/-15/35'"
    group_sta.add_option("--station_rect", action="store",
                         dest="station_rect", help=helpmsg)

    helpmsg = "Include all stations within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "Cannnot be combined with rectangular bounding box " \
              "(--station_rect) (default: 0/0/0/180). " \
              "Example: '20/30/10/80'"
    group_sta.add_option("--station_circle", action="store",
                         dest="station_circle", help=helpmsg)
    parser.add_option_group(group_sta)

    # --------------- speed up options (all modes) ---------------
    group_parallel = OptionGroup(parser, "07. speed up options (all modes)")
    helpmsg = "Enable parallel waveform/response request. " \
              "Retrieve several waveforms/metadata in parallel."
    group_parallel.add_option("--req_parallel", action="store_true",
                              dest="req_parallel", help=helpmsg)

    helpmsg = "Number of thread to be used in --req_parallel (default: 4). " \
              "Example: 8"
    group_parallel.add_option("--req_np", action="store",
                              dest="req_np", help=helpmsg)

    helpmsg = "Send a bulk request to a FDSN data center. " \
              "Returns multiple seismogram channels in a single request. " \
              "Can be combined with --req_parallel."
    group_parallel.add_option("--bulk", action="store_true",
                              dest="bulk", help=helpmsg)

    helpmsg = "Enable parallel local processing of the waveforms, " \
              "useful on multicore hardware."
    group_parallel.add_option("--parallel_process", action="store_true",
                              dest="parallel_process", help=helpmsg)

    helpmsg = "Number of threads to be used in --parallel_process " \
              "(default: 4)."
    group_parallel.add_option("--process_np", action="store",
                              dest="process_np", help=helpmsg)
    parser.add_option_group(group_parallel)

    # --------------- restricted data ---------------------------------
    group_restrict = OptionGroup(parser, "08. restricted data")
    helpmsg = "Username for restricted data requests, " \
              "waveform/response modes (default: None)."
    group_restrict.add_option("--user", action="store",
                              dest="username", help=helpmsg)

    helpmsg = "Password for restricted data requests, " \
              "waveform/response modes (default: None)."
    group_restrict.add_option("--pass", action="store",
                              dest="password", help=helpmsg)
    parser.add_option_group(group_restrict)

    # --------------- event_based mode ----------------------------------------
    group_ev_based = OptionGroup(parser, "09. event-based mode")
    helpmsg = "Event catalog, currently supports LOCAL, NEIC_USGS, " \
              "GCMT_COMBO, IRIS, NCEDC, USGS, " \
              "INGV, ISC, NERIES (default: LOCAL). " \
              "'--event_catalog LOCAL' searches for an existing " \
              "event catalog on the user's local machine, " \
              "in the EVENTS-INFO subdirectory of --datapath <PATH>. " \
              "This is usually a previously retrieved catalog. " \
              "Example: IRIS"
    group_ev_based.add_option("--event_catalog", action="store",
                              dest="event_catalog", help=helpmsg)

    helpmsg = "Retrieve event information (meta-data) without " \
              "downloading actual waveforms."
    group_ev_based.add_option("--event_info", action="store_true",
                              dest="event_info", help=helpmsg)

    helpmsg = "Read in an existing local event catalog and proceed. " \
              "Currently supported catalog metadata formats: " \
              "'CSV', 'QUAKEML', 'NDK', 'ZMAP'. " \
              "Format of the plain text CSV (comma-separated values) is " \
              "explained in the obspyDMT tutorial. " \
              "Refer to obspy documentation for details on " \
              "QuakeML, NDK and ZMAP formats. " \
              "Example: /path/to/file.ml"
    group_ev_based.add_option("--read_catalog", action="store",
                              dest="read_catalog", help=helpmsg)

    helpmsg = "Minimum event depth (default: -10.0 (above the surface!))."
    group_ev_based.add_option("--min_depth", action="store",
                              dest="min_depth", help=helpmsg)

    helpmsg = "Maximum event depth (default: +6000.0)."
    group_ev_based.add_option("--max_depth", action="store",
                              dest="max_depth", help=helpmsg)

    helpmsg = "Minimum magnitude (default: 3.0)."
    group_ev_based.add_option("--min_mag", action="store",
                              dest="min_mag", help=helpmsg)

    helpmsg = "Maximum magnitude (default: 10.0)."
    group_ev_based.add_option("--max_mag", action="store",
                              dest="max_mag", help=helpmsg)

    helpmsg = "Magnitude type. Common types include " \
              "'Ml' (local/Richter magnitude), " \
              "'Ms' (surface wave magnitude), " \
              "'mb' (body wave magnitude), " \
              "'Mw' (moment magnitude), " \
              "(default: None, i.e., consider all magnitude types " \
              "in a given catalogue). " \
              "Example: 'Mw'"
    group_ev_based.add_option("--mag_type", action="store",
                              dest="mag_type", help=helpmsg)

    helpmsg = "Include all events within the defined rectangle, " \
              "syntax: <lonmin>/<lonmax>/<latmin>/<latmax>. " \
              "Cannot be combined with " \
              "circular bounding box (--event_circle) " \
              "(default: -180.0/+180.0/-90.0/+90.0). " \
              "Example: '80/135/-15/35'"
    group_ev_based.add_option("--event_rect", action="store",
                              dest="event_rect", help=helpmsg)

    helpmsg = "Search for all the events within the defined circle, " \
              "syntax: <lon>/<lat>/<rmin>/<rmax>. " \
              "Cannot be combined with " \
              "rectangular bounding box (--event_rect) " \
              "(default: 0/0/0/180). " \
              "Example: '20/30/10/80'"
    group_ev_based.add_option("--event_circle", action="store",
                              dest="event_circle", help=helpmsg)

    helpmsg = "Search either the COMPREHENSIVE or the REVIEWED bulletin " \
              "of the International Seismological Centre (ISC). " \
              "COMPREHENSIVE: all events collected by the ISC, " \
              "including most recent events that are awaiting review. " \
              "REVIEWED: includes only events that have been " \
              "relocated by ISC analysts. " \
              "(default: COMPREHENSIVE). Example: 'REVIEWED'"
    group_ev_based.add_option("--isc_catalog", action="store",
                              dest="isc_catalog", help=helpmsg)
    parser.add_option_group(group_ev_based)

    # --------------- continuous time series mode
    group_cont = OptionGroup(parser, "10. continuous time series mode")
    helpmsg = "Specify time interval for subdividing " \
              "long continuous time series (default: 86400 sec). " \
              "Example: '3600'"
    group_cont.add_option("--interval", action="store",
                          dest="interval", help=helpmsg)
    parser.add_option_group(group_cont)

    # --------------- local processing ----------------------------------------
    group_process = OptionGroup(parser, "11. local processing")
    helpmsg = "Process retrieved/local data based on processing " \
              "instructions in the selected processing unit " \
              "(default: 'process_unit'). " \
              "Example: process_unit_sac"
    group_process.add_option("--pre_process", action="store",
                             dest="pre_process", help=helpmsg)

    helpmsg = "Forces to run the processing unit on " \
              "the local/retrieved data, overwriting any previously " \
              "processed data in local datapath directory."
    group_process.add_option("--force_process", action="store_true",
                             dest="force_process", help=helpmsg)

    helpmsg = "Apply instrument correction in the process unit."
    group_process.add_option("--instrument_correction", action="store_true",
                             dest="instrument_correction", help=helpmsg)

    helpmsg = "Correct the raw waveforms for displacement in m (DIS), " \
              "velocity in m/s (VEL) or accelaration in m/s2 (ACC) " \
              "(default: DIS). " \
              "Example: 'VEL'"
    group_process.add_option("--corr_unit", action="store",
                             dest="corr_unit", help=helpmsg)

    helpmsg = "Apply a bandpass filter to the seismograms " \
              "before deconvolution, " \
              "syntax: 'None' or '(f1,f2,f3,f4)' " \
              "which are the four corner frequencies of a cosine taper, " \
              "default: '(0.008, 0.012, 3.0, 4.0)'."
    group_process.add_option("--pre_filt", action="store",
                             dest="pre_filt", help=helpmsg)

    helpmsg = "Water level in dB for instrument response deconvolution " \
              "(default: 600.0)."
    group_process.add_option("--water_level", action="store",
                             dest="water_level", help=helpmsg)

    # XXX NOT in Table-2
    helpmsg = "before processing, select one waveform every X degree(s). " \
              "syntax: --select_data 5, i.e. select one waveform every 5 " \
              "degrees. [default: False]"
    group_process.add_option("--select_data", action="store",
                             dest="select_data", help=helpmsg)
    parser.add_option_group(group_process)

    # --------------- Synthetic seismograms -----------------------------------
    group_synthetic = OptionGroup(parser, "12. synthetic seismograms")
    helpmsg = "Retrieve synthetic waveforms using IRIS/syngine webservice."
    group_synthetic.add_option("--syngine", action="store_true",
                               dest="syngine", help=helpmsg)

    helpmsg = "Syngine background model (default: 'iasp91_2s')."
    group_synthetic.add_option("--syngine_bg_model", action="store",
                               dest="syngine_bg_model", help=helpmsg)

    helpmsg = "Print supported syngine models that can be passed as " \
              "arguments to --syngine_bg_model."
    group_synthetic.add_option("--print_syngine_models", action="store_true",
                               dest="print_syngine_models", help=helpmsg)

    helpmsg = "Requesting synthetic seismograms based on geocentric " \
              "latitudes of events/stations (default: True)."
    group_synthetic.add_option("--syngine_geocentric_lat", action="store",
                               dest="syngine_geocentric_lat", help=helpmsg)

    # XXX NOT in Table-2
    helpmsg = "retrieve synthetic waveforms calculated by normal mode " \
              "summation code. (ShakeMovie project)"
    group_synthetic.add_option("--normal_mode_syn", action="store_true",
                               dest="normal_mode_syn", help=helpmsg)

    # XXX NOT in Table-2
    helpmsg = "retrieve synthetic waveforms calculated by SPECFEM3D. " \
              "(ShakeMovie project)"
    group_synthetic.add_option("--specfem3D", action="store_true",
                               dest="specfem3D", help=helpmsg)
    parser.add_option_group(group_synthetic)

    # --------------- plotting ------------------------------------------------
    group_plt = OptionGroup(parser, "13. plotting")
    helpmsg = "Activates plotting functionality."
    group_plt.add_option("--plot", action="store_true",
                         dest="plot", help=helpmsg)

    helpmsg = "Plot all stations found in the specified directory " \
              "(--datapath)."
    group_plt.add_option("--plot_sta", action="store_true",
                         dest="plot_sta", help=helpmsg)

    helpmsg = "Plot all availabilities (potential seismometers) found in " \
              "the specified directory (--datapath)."
    group_plt.add_option("--plot_availability", action="store_true",
                         dest="plot_availability", help=helpmsg)

    helpmsg = "Plot all events found in the specified directory (--datapath)."
    group_plt.add_option("--plot_ev", action="store_true",
                         dest="plot_ev", help=helpmsg)

    helpmsg = "Plot beachballs instead of dots for event locations."
    group_plt.add_option("--plot_focal", action="store_true",
                         dest="plot_focal", help=helpmsg)

    helpmsg = "Plot the ray coverage for all station-event pairs found in " \
              "the specified directory (--datapath)."
    group_plt.add_option("--plot_ray", action="store_true",
                         dest="plot_ray", help=helpmsg)

    helpmsg = "Create KML file(s) for event/station/ray. " \
              "KML format is readable by Google-Earth."
    group_plt.add_option("--create_kml", action="store_true",
                         dest="create_kml", help=helpmsg)

    helpmsg = "Create a VTK file for event(s). " \
              "VTK format is readable by Paraview."
    group_plt.add_option("--create_event_vtk", action="store_true",
                         dest="create_event_vtk", help=helpmsg)

    helpmsg = "Create a seismicity map and " \
              "some basic statistics on the results."
    group_plt.add_option("--plot_seismicity", action="store_true",
                         dest="plot_seismicity", help=helpmsg)

    helpmsg = "Depth bins for plotting the seismicity histogram " \
              "(default: 10 km)."
    group_plt.add_option("--depth_bins_seismicity", action="store",
                         dest="depth_bins_seismicity", help=helpmsg)

    helpmsg = "Plot waveforms arranged by epicentral distance."
    group_plt.add_option("--plot_waveform", action="store_true",
                         dest="plot_waveform", help=helpmsg)

    helpmsg = "Directory name that contains the waveforms for " \
              "--plot_waveform option flag, " \
              "e.g.: --plot_waveform 'processed' (default: raw)."
    group_plt.add_option("--plot_dir_name", action="store",
                         dest="plot_dir_name", help=helpmsg)

    helpmsg = "Path where plots will be store " \
              "(default: '.', i.e., the current directory)."
    group_plt.add_option("--plot_save", action="store",
                         dest="plot_save", help=helpmsg)

    helpmsg = "Image format of plots (default: 'png')."
    group_plt.add_option("--plot_format", action="store",
                         dest="plot_format", help=helpmsg)

    helpmsg = "Central meridian (x-axis origin) for projection (default: 180)."
    group_plt.add_option("--plot_lon0", action="store",
                         dest="plot_lon0", help=helpmsg)

    parser.add_option_group(group_plt)

    # --------------- explore instrument responses (stationXML files)
    group_pltxml = OptionGroup(parser, "14. explore instrument "
                                       "responses (stationXML files)")
    helpmsg = "Plot the contents of stationXML file(s), " \
              "i.e. transfer function of filter stages, " \
              "specified by --datapath."
    group_pltxml.add_option("--plot_stationxml", action="store_true",
                            dest="plot_stationxml", help=helpmsg)

    helpmsg = "Datetime to be used for plotting the transfer function, " \
              "syntax: 'YYYY-MM-DD-HH-MM-SS' or 'YYYY-MM-DD'. " \
              "If not specified, the starting date of the last channel in " \
              "the stationXML will be used. " \
              "Example: '2010-01-01'"
    group_pltxml.add_option("--plotxml_date", action="store",
                            dest="plotxml_date", help=helpmsg)

    helpmsg = "Type of transfer function to plot: DIS/VEL/ACC (default: VEL)."
    group_pltxml.add_option("--plotxml_output", action="store",
                            dest="plotxml_output", help=helpmsg)

    helpmsg = "Plot all filter stages specified in response file."
    group_pltxml.add_option("--plotxml_allstages", action="store_true",
                            dest="plotxml_allstages", help=helpmsg)

    helpmsg = "Plot only Poles And Zeros (PAZ) of the response file, " \
              "i.e. the analog stage."
    group_pltxml.add_option("--plotxml_paz", action="store_true",
                            dest="plotxml_paz", help=helpmsg)

    helpmsg = "Plot only stages 1 and 2 of full response file."
    group_pltxml.add_option("--plotxml_plotstage12", action="store_true",
                            dest="plotxml_plotstage12", help=helpmsg)

    helpmsg = "First stage in response file to be considered for " \
              "plotting the transfer function (default: 1)."
    group_pltxml.add_option("--plotxml_start_stage", action="store",
                            dest="plotxml_start_stage", help=helpmsg)

    helpmsg = "Final stage in response file to be considered for " \
              "plotting the transfer function, " \
              "(default: last stage given in response file or " \
              "the 100th stage, whichever number is smaller)."
    group_pltxml.add_option("--plotxml_end_stage", action="store",
                            dest="plotxml_end_stage", help=helpmsg)

    helpmsg = "Minimum frequency in Hz to be used in " \
              "transfer function plots (default: 0.01)."
    group_pltxml.add_option("--plotxml_min_freq", action="store",
                            dest="plotxml_min_freq", help=helpmsg)

    helpmsg = "Plot all stations for which instrument responses have been " \
              "compared (PAZ against full response)."
    group_pltxml.add_option("--plotxml_map_compare", action="store_true",
                            dest="plotxml_map_compare", help=helpmsg)

    helpmsg = "Percentage of the phase transfer function's frequency range " \
              "to be used for checking the difference between methods. " \
              "'100' will compare transfer functions across their " \
              "entire spectral range, i.e. from min freq " \
              "(set by --plotxml_min_freq) to Nyquist frequency; " \
              "'80' compares from min freq to 0.8 times Nyquist frequency " \
              "(default: 80)."
    group_pltxml.add_option("--plotxml_percentage", action="store",
                            dest="plotxml_percentage", help=helpmsg)

    # XXX NOT in Table-2
    helpmsg = "maximum allowable length (in percentage) to differ between " \
              "two different methods of instrument correction. " \
              "This only applies to phase difference. [default: 10]"
    group_pltxml.add_option("--plotxml_phase_threshold", action="store",
                            dest="plotxml_phase_threshold", help=helpmsg)

    # XXX NOT in Table-2
    helpmsg = "do not plot the full response file."
    group_pltxml.add_option("--plotxml_no_response", action="store_true",
                            dest="plotxml_no_response", help=helpmsg)
    parser.add_option_group(group_pltxml)

    # --------------- others --------------------------------------------------
    group_others = OptionGroup(parser, "15. others")
    helpmsg = "Send an email to the specified address after " \
              "completing the job (default: False)."
    group_others.add_option("--email", action="store",
                            dest="email", help=helpmsg)

    helpmsg = "Timeout (in sec) for sending a data availability " \
              "query via ArcLink (default: 40)."
    group_others.add_option("--arc_avai_timeout", action="store",
                            dest="arc_avai_timeout", help=helpmsg)

    helpmsg = "Timeout (in sec) for sending a waveform data or " \
              "metadata request via ArcLink (default: 2)."
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

                  # 'min_date': str(UTCDateTime() - 60 * 60 * 24 * 10 * 1),
                  'min_date': str(UTCDateTime(1970, 1, 1)),
                  'max_date': str(UTCDateTime()),
                  'preset': 0.0, 'offset': False,
                  'waveform_format': False,
                  'resample_method': 'lanczos',
                  'sampling_rate': False,

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
                  'min_mag': 3.0, 'max_mag': 10.,
                  'mag_type': None,
                  'evlatmin': None, 'evlatmax': None,
                  'evlonmin': None, 'evlonmax': None,
                  'evlat': None, 'evlon': None,
                  'evradmin': None, 'evradmax': None,
                  'isc_catalog': "COMPREHENSIVE",
                  'syngine_bg_model': 'iasp91_2s',
                  'syngine_geocentric_lat': True,

                  'interval': 3600*24,

                  'pre_process': 'process_unit',
                  'select_data': False,
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

    if len(sys.argv) == 1:
        print("\n")
        print(60*"#")
        print("WARNING: No option flag is set!")
        print("WARNING: --min_date is set to %s"
              % str(UTCDateTime(input_dics['min_date'])))
        print("WARNING: --min_mag is set to %s"
              % (input_dics['min_mag']))
        print(60*"#")
        print("\n")
        time.sleep(2)
    elif ('--tour' in sys.argv) or \
            ('--print_data_sources' in sys.argv) or \
            ('--print_data_source' in sys.argv) or \
            ('--version' in sys.argv) or \
            ('--print_event_catalogs' in sys.argv) or \
            ('--print_event_catalog' in sys.argv) or \
            ('--list_option' in sys.argv) or \
            ('--options' in sys.argv) or \
            ('--print_syngine_models' in sys.argv):
        pass
    else:
        warn_msg = []
        if '--min_date' not in sys.argv:
            warn_msg.append("WARNING: --min_date is set to %s"
                            % str(UTCDateTime(input_dics['min_date'])))
        if '--continuous' not in sys.argv:
            if '--min_mag' not in sys.argv:
                warn_msg.append("WARNING: --min_mag is set to %s"
                                % (input_dics['min_mag']))
        if warn_msg:
            warn_msg = str.join('\n', warn_msg)
            print("\n")
            print(60*"#")
            print(warn_msg)
            print(60*"#")
            print("\n")
            time.sleep(2)
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
            exec("options.%s = kwargs[arg]" % arg)

    # ===================== printing the description of all option groups======
    if options.options:
        print("=============")
        print("option groups")
        print("=============\n")
        for grp in parser.option_groups:
            print(grp.title)
        print("\n\n===============================================")
        print("To check the available options in each group:")
        print("obspyDMT --list_option <group_number>")
        print("===============================================")
        sys.exit()

    # ==================== printing the available options in each option group=
    if options.list_option:
        if int(options.list_option) > len(parser.option_groups):
            sys.exit('Specified option group: %s does not exist'
                     % options.list_option)
        print(parser.option_groups[int(options.list_option)-1].title)
        for opt_grp in \
                parser.option_groups[int(options.list_option)-1].option_list:
            print("{0:20s}\t{1:20s}\t{2!s:20}\t\t{3:20s}".\
                format(opt_grp.get_opt_string(), opt_grp.dest,
                       opt_grp.type, opt_grp.help))
        sys.exit()

    # ==================== obspyDMT version====================================
    if options.version:
        print('\n\t\t' + '*********************************')
        print('\t\t' + '*        obspyDMT version:      *')
        print('\t\t' + '*\t' + 5*' ' + '2.1.1' + '\t\t*')
        print('\t\t' + '*********************************')
        print('\n')
        sys.exit(2)

    # =================== Check importing the required modules=================
    if options.check:
        descrip = descrip_generator()
        print("=================================")
        for i in range(len(descrip)):
            print(descrip[i])
        print("=================================\n")
        sys.exit(2)

    # =================== obspyDMT quick tour==================================
    if options.tour:
        print('\n########################################')
        print('obspyDMT Quick Tour will start in 2 sec!')
        print('########################################\n')
        time.sleep(2)
        options.datapath = './dmt_tour_dir'
        options.min_date = '2011-03-10'
        options.max_date = '2011-03-12'
        options.min_mag = '8.9'
        options.identity = 'TA.1*.*.BHZ'
        options.event_catalog = 'IRIS'
        options.req_parallel = True
        options.instrument_correction = True

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
            print('\n================================')
            print('Remove the following directory:')
            print(str(options.datapath))
            print('obspyDMT is going to re-create it...')
            print('================================\n')
        except Exception as e:
            print("Warning: can not remove the following directory: %s" % e)
            pass
    input_dics['datapath'] = options.datapath

    if ('--print_data_sources' in sys.argv) or \
       ('--print_data_source' in sys.argv) or \
       ('--version' in sys.argv) or \
       ('--print_event_catalogs' in sys.argv) or \
       ('--print_event_catalog' in sys.argv) or \
       ('--print_syngine_models' in sys.argv):
        pass
    else:
        if not os.path.isdir(input_dics['datapath']):
            if not options.plot_stationxml:
                os.mkdir(input_dics['datapath'])

    # =================== obspyDMT mode========================================
    # plot_stationxml option always change the mode to local
    input_dics['plot_stationxml'] = options.plot_stationxml
    if input_dics['plot_stationxml']:
        options.event_based = False
        options.continuous = False
        options.meta_data = False
        options.local = True

    input_dics['pre_process'] = options.pre_process
    if input_dics['pre_process'].lower() in ['false']:
        input_dics['pre_process'] = False
    input_dics['force_process'] = options.force_process
    input_dics['select_data'] = options.select_data
    if input_dics['select_data']:
        input_dics['select_data'] = float(input_dics['select_data'])
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
        input_dics['event_based'] = options.event_based
        input_dics['continuous'] = options.continuous
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

    if input_dics['primary_mode'] in ['event_based', 'continuous']:
        input_dics['meta_data'] = True

    input_dics['event_info'] = options.event_info
    if input_dics['event_info']:
        input_dics['pre_process'] = False
    if input_dics['primary_mode'] == 'meta_data':
        input_dics['pre_process'] = False

    print("\nobspyDMT primary mode: %s\n" % input_dics['primary_mode'])

    # =================== Print Data sources and Event catalogs
    input_dics['print_data_sources'] = options.print_data_sources
    input_dics['print_event_catalogs'] = options.print_event_catalogs
    input_dics['print_syngine_models'] = options.print_syngine_models

    # =================== Data sources
    input_dics['data_source'] = options.data_source
    if input_dics['data_source'].lower() == 'all':
        input_dics['data_source'] = \
                "BGR,EMSC,ETH,GEONET,GFZ,INGV,IPGP,IRIS," \
                "ISC,KOERI,LMU,NCEDC,NIEP,NOA,ODC,ORFEUS," \
                "RESIF,SCEDC,USGS,USP,ARCLINK"
        print("\n=================================")
        print("Waveforms will be retrieved from:")
        print(input_dics['data_source'])
        print("=================================\n\n")
    input_dics['data_source'] = \
        [x.strip() for x in input_dics['data_source'].split(',')]
    for cli in range(len(input_dics['data_source'])):
        input_dics['data_source'][cli] = input_dics['data_source'][cli].upper()

    if str(options.waveform).lower() in ['false']:
        input_dics['waveform'] = False
    else:
        input_dics['waveform'] = True

    input_dics['force_waveform'] = options.force_waveform

    if str(options.response).lower() in ['false']:
        input_dics['response'] = False
    else:
        input_dics['response'] = True

    input_dics['force_response'] = options.force_response

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

    if (not options.test) or (options.test.lower() in ['false']):
        pass
    else:
        input_dics['test'] = True
        input_dics['test_num'] = int(options.test)

    input_dics['min_date'] = str(UTCDateTime(options.min_date))
    input_dics['max_date'] = str(UTCDateTime(options.max_date))
    input_dics['preset'] = float(options.preset)
    if options.offset:
        input_dics['offset'] = float(options.offset)
    elif options.continuous:
        input_dics['offset'] = 0.
    else:
        input_dics['offset'] = 1800.

    input_dics['cut_time_phase'] = options.cut_time_phase

    input_dics['waveform_format'] = options.waveform_format
    if input_dics['waveform_format']:
        input_dics['waveform_format'] = input_dics['waveform_format'].lower()
    input_dics['resample_method'] = options.resample_method
    if options.sampling_rate:
        input_dics['sampling_rate'] = float(options.sampling_rate)
    else:
        input_dics['sampling_rate'] = False

    # Extract network, station, location, channel if the user has given an
    # identity code (-i xx.xx.xx.xx)
    if options.identity:
        try:
            options.net, options.sta, options.loc, options.cha = \
                options.identity.split('.')
        except Exception as e:
            print("Erroneous identity code given: %s" % e)
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
                print("Erroneous rectangle given.")
                sys.exit(2)
            options.mlon_rbb = float(options.station_rect[0])
            options.Mlon_rbb = float(options.station_rect[1])
            options.mlat_rbb = float(options.station_rect[2])
            options.Mlat_rbb = float(options.station_rect[3])
        except Exception as e:
            print("Erroneous rectangle given: %s" % e)
            sys.exit(2)

    # circular station restriction option parsing
    if options.station_circle:
        try:
            options.station_circle = options.station_circle.split('/')
            if len(options.station_circle) != 4:
                print("Erroneous circle given.")
                sys.exit(2)
            options.lon_cba = float(options.station_circle[0])
            options.lat_cba = float(options.station_circle[1])
            options.mr_cba = float(options.station_circle[2])
            options.Mr_cba = float(options.station_circle[3])
        except Exception as e:
            print("Erroneous circle given: %s" % e)
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
    if options.read_catalog:
        input_dics['read_catalog'] = options.read_catalog
    else:
        input_dics['read_catalog'] = False

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
                print("Erroneous rectangle given.")
                sys.exit(2)
            options.evlonmin = float(options.event_rect[0])
            options.evlonmax = float(options.event_rect[1])
            options.evlatmin = float(options.event_rect[2])
            options.evlatmax = float(options.event_rect[3])
        except Exception as e:
            print("Erroneous rectangle given: %s" % e)
            sys.exit(2)

    # circular event restriction option parsing
    if options.event_circle:
        try:
            options.event_circle = options.event_circle.split('/')
            if len(options.event_circle) != 4:
                print("Erroneous circle given.")
                sys.exit(2)
            options.evlon = float(options.event_circle[0])
            options.evlat = float(options.event_circle[1])
            options.evradmin = float(options.event_circle[2])
            options.evradmax = float(options.event_circle[3])
        except Exception as e:
            print("Erroneous circle given: %s" % e)
            sys.exit(2)

    input_dics['evlonmin'] = options.evlonmin
    input_dics['evlonmax'] = options.evlonmax
    input_dics['evlatmin'] = options.evlatmin
    input_dics['evlatmax'] = options.evlatmax

    input_dics['evlat'] = options.evlat
    input_dics['evlon'] = options.evlon
    input_dics['evradmax'] = options.evradmax
    input_dics['evradmin'] = options.evradmin

    if 'rev' in options.isc_catalog.lower():
        input_dics['isc_catalog'] = 'REVIEWED'
    else:
        input_dics['isc_catalog'] = 'COMPREHENSIVE'
    input_dics['syngine'] = options.syngine
    input_dics['syngine_bg_model'] = options.syngine_bg_model
    if str(options.syngine_geocentric_lat).lower() in ['false']:
        input_dics['syngine_geocentric_lat'] = False
    else:
        input_dics['syngine_geocentric_lat'] = True

    input_dics['specfem3D'] = options.specfem3D
    input_dics['normal_mode_syn'] = options.normal_mode_syn

    input_dics['interval'] = float(options.interval)

    input_dics['instrument_correction'] = options.instrument_correction
    input_dics['corr_unit'] = options.corr_unit

    # XXX
    if input_dics['corr_unit'].lower() == 'dis':
        input_dics['syngine_units'] = 'displacement'
    elif input_dics['corr_unit'].lower() == 'vel':
        input_dics['syngine_units'] = 'velocity'
    elif input_dics['corr_unit'].lower() == 'acc':
        input_dics['syngine_units'] = 'acceleration'

    input_dics['pre_filt'] = options.pre_filt
    input_dics['water_level'] = float(options.water_level)

    input_dics['plot'] = options.plot
    input_dics['plot_sta'] = options.plot_sta
    input_dics['plot_availability'] = options.plot_availability
    input_dics['plot_ev'] = options.plot_ev
    input_dics['plot_focal'] = options.plot_focal
    input_dics['plot_ray'] = options.plot_ray
    input_dics['create_kml'] = options.create_kml
    input_dics['create_event_vtk'] = options.create_event_vtk
    input_dics['plot_seismicity'] = options.plot_seismicity
    input_dics['depth_bins_seismicity'] = int(options.depth_bins_seismicity)
    input_dics['plot_waveform'] = options.plot_waveform

    if input_dics['plot_sta'] or input_dics['plot_availability'] or \
            input_dics['plot_ev'] or input_dics['plot_focal'] or \
            input_dics['plot_ray'] or input_dics['create_kml'] or \
            input_dics['plot_seismicity'] or input_dics['plot_waveform'] or \
            input_dics['create_event_vtk']:
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
            print("\n********************************************************")
            print("Unable to import smtplib. Sending email is not possible!")
            print("Error: %s" % error)
            print("********************************************************\n")
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
    print("********************************")
    print("Check all the BASIC dependencies")

    try:
        from obspy import __version__ as obs_ver
        descrip = ['obspy ver: ' + obs_ver]
    except Exception as error:
        descrip = ['obspy: not installed\nerror:\n%s\n' % error]

    try:
        import numpy as np
        descrip.append('numpy ver: ' + np.__version__)
    except Exception as error:
        descrip.append('numpy: not installed\nerror:\n%s\n' % error)

    try:
        import scipy
        descrip.append('scipy ver: ' + scipy.__version__)
    except Exception as error:
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
    print("********************************\n")
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
    st_argus = '\n\n' + 20*'='
    st_argus += 'command line\n'
    for item in argus:
        st_argus += item + ' '
    st_argus += '\n\ninputs:\n-------\n'
    items = []
    for item in inputs:
        items.append(item)
    items.sort()
    for item in items:
        st_argus += '%s: %s, ' % (item, inputs[item])
    logger_open = open(address, 'at')
    logger_open.write(st_argus)
    logger_open.close()
