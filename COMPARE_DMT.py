#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  COMPARE_DMT.py
#   Purpose:   ObsPyDMT Instrument Correction Analyser
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
#-------------------------------------------------------------------

#for debugging: import ipdb; ipdb.set_trace()

#-----------------------------------------------------------------------
#----------------Import required Modules (Python and Obspy)-------------
#-----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from __future__ import with_statement
import sys
import os
import glob
import time
from optparse import OptionParser

import numpy as np
import matplotlib.pyplot as plt

from obspy.core import read, UTCDateTime, util
from obspy.iris import Client
from obspy.signal import cross_correlation, pazToFreqResp, invsim
from obspy.taup import taup


########################################################################
############################# Main Program #############################
########################################################################

def COMPARE_DMT(**kwargs):
    
    """
    COMPARE_DMT: is the function dedicated to the main part of the code.
    For more information about each part, please refer to the relevant function
    """
    
    print '\n--------------------------------------------------------'
    bold = "\033[1m"
    reset = "\033[0;0m"
    print '\t\t' + bold + 'COMPARE_DMT' + reset
    print '\t' + 'Automatic tool for comparing '
    print '\t' + '   Large Seismic Datasets'
    print '\n'
    print ':copyright:'
    print 'The ObsPy Development Team (devs@obspy.org)' + '\n'
    print 'Developed by Kasra Hosseini'
    print 'email: hosseini@geophysik.uni-muenchen.de' + '\n'
    print ':license:'
    print 'GNU General Public License, Version 3'
    print '(http://www.gnu.org/licenses/gpl-3.0-standalone.html)'
    print '--------------------------------------------------------'
    
    # global variables
    global input
    
    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()
    
    # ------------------Read INPUT file (Parameters)--------------------
    read_input_command(parser, **kwargs)

    # ------------------Single Comparison-------------------------------
    if input['single_comparison'] == 'Y':
        single_comparison()
    
    # ------------------Cross Correlation-------------------------------
    if input['cc'] == 'Y' or input['cc_parallel'] == 'Y':
        cross_corr()
        read_cc(max_coeff = input['max_cc'])
    
    # ------------------Read Cross Correlation File---------------------
    if input['read_cc'] == 'Y':
        read_cc(max_coeff = input['max_cc'])
    
    
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
    
    helpmsg = "show how to run COMPARE_DMT.py and exit"
    parser.add_option("--how", action="store_true",
                      dest="how", help=helpmsg)
    
    helpmsg = "the path where COMPARE_DMT will read the FIRST dataset"
    parser.add_option("--first_path", action="store",
                      dest="first_path", help=helpmsg)
    
    helpmsg = "the path where COMPARE_DMT will read the SECOND dataset"
    parser.add_option("--second_path", action="store",
                      dest="second_path", help=helpmsg)
    
    helpmsg = "unit (DIS, VEL and ACC) of the corrected seismograms. [Default: DIS]"
    parser.add_option("--corr_unit", action="store", dest="corr_unit",
                        help=helpmsg)
    
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
    
    helpmsg = "one by one comparison of the waveforms in the first path " + \
                "with the second path."
    parser.add_option("--single_comparison", action="store_true",
                      dest="single_comparison", help=helpmsg)
    
    helpmsg = "add response file and PAZ for plotting"
    parser.add_option("--resp_paz", action="store_true",
                      dest="resp_paz", help=helpmsg)
    
    helpmsg = "create a 'cc.txt' file for the waveforms in the first path and " + \
                "the second path by measuring the cross correlation coefficient and" + \
                "the time shift."
    parser.add_option("--cc", action="store_true",
                      dest="cc", help=helpmsg)
    
    helpmsg = "Maximum Cross Correlation Coefficient for plotting"
    parser.add_option("--max_cc", action="store",
                      dest="max_cc", help=helpmsg)
    
    helpmsg = "Parallel Cross Correlation"
    parser.add_option("--cc_parallel", action="store_true",
                      dest="cc_parallel", help=helpmsg)
    
    helpmsg = "Number of processors to be used in --cc_parallel. [Default: 4]"
    parser.add_option("--cc_np", action="store",
                        dest="cc_np", help=helpmsg)
    
    helpmsg = "Read cc.txt file [refer to --cc] and create some plots"
    parser.add_option("--read_cc", action="store_true",
                      dest="read_cc", help=helpmsg)
    
    helpmsg = "Required phases to search for. format: 'Pdiff'"
    parser.add_option("--phase", action="store",
                      dest="phase", help=helpmsg)
    
    helpmsg = "Cut a time window around the requested phase"
    parser.add_option("--tw", action="store_true",
                      dest="tw", help=helpmsg)
    
    helpmsg = "Time parameter in seconds which determines how close " + \
                "the time series data (waveform) will be cropped " + \
                "before the estimated time of the phase. Default: 5.0 seconds."
    parser.add_option("--preset", action="store",
                      dest="preset", help=helpmsg)
    
    helpmsg = "Time parameter in seconds which determines how close " + \
                "the time series data (waveform) will be cropped " + \
                "after the estimated time of the phase. Default: 5.0 seconds."
    parser.add_option("--offset", action="store",
                      dest="offset", help=helpmsg)
    
    helpmsg = "Filter all the traces with two types (lowpass and highpass)"
    parser.add_option("--filter", action="store_true",
                      dest="hlfilter", help=helpmsg)
    
    helpmsg = "Lower Frequency (for highpass filter)"
    parser.add_option("--lfreq", action="store",
                      dest="lfreq", help=helpmsg)
    
    helpmsg = "Higher Frequency (for lowpass filter)"
    parser.add_option("--hfreq", action="store",
                      dest="hfreq", help=helpmsg)
    
    helpmsg = "Resample all the traces with sampling rate specified here"
    parser.add_option("--resample", action="store",
                      dest="resample", help=helpmsg)
    
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
    # By defining the required command-line flag
        
    input = {   'first_path': None,
                'second_path': None,
                
                'corr_unit': 'dis',
                'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
                
                'max_cc': 0.99,
                'cc_np': 4,
                
                'phase': 'N',
                
                'preset': 10,
                'offset': 40,
                
                'lfreq': 0.008,
                'hfreq': 4.0,
                
                'resample': 'N'
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
    
    if options.how:
        print '\n===================================================================================='
        print 'To run COMPARE_DMT:'
        
        print '\n1. For single comparison:'
        print '\t./COMPARE_DMT.py --first_path first_path --second_path second_path --single_comparison'
        print '\nTo compare specific stations, we could define the identity as:'
        print '\t./COMPARE_DMT.py --first_path first_path --second_path second_path --single_comparison' + \
                        ' --identity "*.736A.*.BHZ"\n'
        print '----------'
        print '\n2. For creating a cross correlation file (cc.txt):'
        print '\t./COMPARE_DMT.py --first_path first_path --second_path second_path --cc'
        print '\nThis could be done in parallel:'
        print '\t./COMPARE_DMT.py --first_path first_path --second_path second_path --cc_parallel'
        print '\nThe number of cores could be defined as:'
        print '\t./COMPARE_DMT.py --first_path first_path --second_path second_path --cc_parallel --cc_np 12\n'
        print '----------'
        print '\n3. For reading the cc.txt file and plot:'
        print '\t./COMPARE_DMT.py --first_path first_path --second_path second_path --read_cc'
        print '====================================================================================\n'
        sys.exit(2)
    
    # parse datapath (check if given absolute or relative)
    if options.first_path:
        if not os.path.isabs(options.first_path):
            options.first_path = os.path.join(os.getcwd(), options.first_path)
    
    if options.second_path:
        if not os.path.isabs(options.second_path):
            options.second_path = os.path.join(os.getcwd(), options.second_path)
            
    
    input['corr_unit'] = options.corr_unit.lower()
    
    # Extract network, station, location, channel if the user has given an
    # identity code (-i xx.xx.xx.xx)
    if options.identity:
        try:
            options.net, options.sta, options.loc, options.cha = \
                                    options.identity.split('.')
        except:
            print "Erroneous identity code given."
            sys.exit(2)
    
    input['net'] = options.net
    input['sta'] = options.sta
    if options.loc == "''":
        input['loc'] = ''
    elif options.loc == '""':
        input['loc'] = ''
    else:
        input['loc'] = options.loc
    
    input['cha'] = options.cha
    
    
    input['first_path'] = options.first_path
    input['second_path'] = options.second_path
    
    if options.single_comparison: options.single_comparison = 'Y'
    input['single_comparison'] = options.single_comparison
    
    if options.resp_paz: options.resp_paz = 'Y'
    input['resp_paz'] = options.resp_paz
    
    if options.cc: options.cc = 'Y'
    input['cc'] = options.cc
    
    input['max_cc'] = float(options.max_cc)
    
    if options.cc_parallel: options.cc_parallel = 'Y'
    input['cc_parallel'] = options.cc_parallel
    
    input['cc_np'] = int(options.cc_np)
    
    if options.read_cc: options.read_cc = 'Y'
    input['read_cc'] = options.read_cc
    
    input['phase'] = options.phase
    
    if options.tw: options.tw = 'Y'
    input['tw'] = options.tw
    input['preset'] = float(options.preset)
    input['offset'] = float(options.offset)
    
    if options.hlfilter: options.hlfilter = 'Y'
    input['hlfilter'] = options.hlfilter
    input['lfreq'] = float(options.lfreq)
    input['hfreq'] = float(options.hfreq)
    
    if options.resample != 'N': options.resample = float(options.resample)
    input['resample'] = options.resample
    
###################### single_comparison ###############################

def single_comparison():
    
    """
    one by one comparison of the waveforms in the first path with the second path.
    """
    
    client = Client()
    
    global input
    
    # identity of the waveforms (first and second paths) to be compared with each other
    identity_all = input['net'] + '.' + input['sta'] + '.' + \
                    input['loc'] + '.' + input['cha']
    ls_first = glob.glob(os.path.join(input['first_path'], identity_all))
    ls_second = glob.glob(os.path.join(input['second_path'], identity_all))
    
    for i in range(0, len(ls_first)):
        try:
            tr1 = read(ls_first[i])[0]
    
            if input['phase'] != 'N':
                evsta_dist = util.locations2degrees(lat1 = tr1.stats.sac.evla, \
                                        long1 = tr1.stats.sac.evlo, lat2 = tr1.stats.sac.stla, \
                                        long2 = tr1.stats.sac.stlo)
                
                taup_tt = taup.getTravelTimes(delta = evsta_dist, depth = tr1.stats.sac.evdp)
                
                phase_exist = 'N'
                
                for tt_item in taup_tt:
                    if tt_item['phase_name'] == input['phase']:
                        print 'Requested phase:'
                        print input['phase']
                        print '------'
                        print tt_item['phase_name']
                        print 'exists in the waveform!'
                        print '-----------------------'
                        t_phase = tt_item['time']
                        
                        phase_exist = 'Y'
                        break
                        
                if phase_exist != 'Y':
                    continue
            
            # identity of the current waveform
            identity = tr1.stats.network + '.' + tr1.stats.station + '.' + \
                        tr1.stats.location + '.' + tr1.stats.channel
            
            # tr1: first path, tr2: second path, tr3: Raw data
            #tr3 = read(os.path.join(input['first_path'], '..', 'BH_RAW', identity))[0]
            
            if input['resp_paz'] == 'Y':
                response_file = os.path.join(input['first_path'], '..', 'Resp/RESP.' + identity)
                
                # Extract the PAZ info from response file
                paz = readRESP(response_file, unit = input['corr_unit'])
                
                poles = paz['poles']
                zeros = paz['zeros']
                scale_fac = paz['gain']
                sensitivity = paz['sensitivity']
            
                print paz
                
                # Convert Poles and Zeros (PAZ) to frequency response.
                h, f = pazToFreqResp(poles, zeros, scale_fac, \
                                1./tr1.stats.sampling_rate, tr1.stats.npts*2, freq=True)
                # Use the evalresp library to extract 
                # instrument response information from a SEED RESP-file.
                resp = invsim.evalresp(t_samp = 1./tr1.stats.sampling_rate, \
                        nfft = tr1.stats.npts*2, filename = response_file, \
                        date = tr1.stats.starttime, units = input['corr_unit'].upper())
            
            # Keep the current identity in a new variable
            id_name = identity
            
            try:
                tr2 = read(os.path.join(input['second_path'], identity))[0]
            except Exception, error:
                # if it is not possible to read the identity in the second path
                # then change the network part of the identity based on
                # correction unit
                identity = input['corr_unit'] + '.' + tr1.stats.station + '.' + \
                        tr1.stats.location + '.' + tr1.stats.channel
                tr2 = read(os.path.join(input['second_path'], identity))[0]
            
            if input['resample'] != 'N':
                tr1.resample(input['resample'])
                tr2.resample(input['resample'])
            
            if input['tw'] == 'Y':
                t_cut_1 = tr1.stats.starttime + t_phase - input['preset']
                t_cut_2 = tr1.stats.starttime + t_phase + input['offset']
                tr1.trim(starttime = t_cut_1, endtime = t_cut_2)
                
                t_cut_1 = tr2.stats.starttime + t_phase - input['preset']
                t_cut_2 = tr2.stats.starttime + t_phase + input['offset']
                tr2.trim(starttime = t_cut_1, endtime = t_cut_2)
            
            
            if input['hlfilter'] == 'Y':
                tr1.filter('lowpass', freq=input['hfreq'], corners=2)
                tr2.filter('lowpass', freq=input['hfreq'], corners=2)
                tr1.filter('highpass', freq=input['lfreq'], corners=2)
                tr2.filter('highpass', freq=input['lfreq'], corners=2)
            
            # normalization of all three waveforms to the 
            # max(max(tr1), max(tr2), max(tr3)) to keep the scales
            #maxi = max(abs(tr1.data).max(), abs(tr2.data).max(), abs(tr3.data).max())
            
            #maxi = max(abs(tr1.data).max(), abs(tr2.data).max())
            #tr1_data = tr1.data/abs(maxi)
            #tr2_data = tr2.data/abs(maxi)
            #tr3_data = tr3.data/abs(maxi)
            
            tr1_data = tr1.data/abs(max(tr1.data))
            tr2_data = tr2.data/abs(max(tr2.data))
            
            #tr1_data = tr1.data
            #tr2_data = tr2.data*1e9
            
            print max(tr1.data)
            print max(tr2.data)
            
            # create time arrays for tr1, tr2 and tr3
            time_tr1 = np.arange(0, tr1.stats.npts/tr1.stats.sampling_rate, \
                                                1./tr1.stats.sampling_rate)
            time_tr2 = np.arange(0, tr2.stats.npts/tr2.stats.sampling_rate, \
                                                1./tr2.stats.sampling_rate)
            #time_tr3 = np.arange(0, tr3.stats.npts/tr3.stats.sampling_rate, \
            #                                    1./tr3.stats.sampling_rate)
            
            # label for plotting
            label_tr1 = ls_first[i].split('/')[-2]
            label_tr2 = ls_second[i].split('/')[-2]
            label_tr3 = 'RAW'
        
            if input['resp_paz'] == 'Y':
                # start plotting
                plt.figure()
                plt.subplot2grid((3,4), (0,0), colspan=4, rowspan=2)
                #plt.subplot(211)
            
            plt.plot(time_tr1, tr1_data, color = 'blue', label = label_tr1)
            plt.plot(time_tr2, tr2_data, color = 'red', label = label_tr2)
            #plt.plot(time_tr3, tr3_data, color = 'black', ls = '--', label = label_tr3)

            plt.xlabel('Time (sec)', fontsize = 'large', weight = 'bold')
            
            if input['corr_unit'] == 'dis':
                ylabel_str = 'Relative Dis'
            elif input['corr_unit'] == 'vel':
                ylabel_str = 'Relative Vel'
            elif input['corr_unit'] == 'acc':
                ylabel_str = 'Relative Acc'
            
            plt.ylabel(ylabel_str, fontsize = 'large', weight = 'bold')
            
            plt.xticks(fontsize = 'large')
            plt.yticks(fontsize = 'large')
            
            plt.legend()
            
            #-------------------Cross Correlation
            # 5 seconds as total length of samples to shift for cross correlation.
            
            cc_np = tr1.stats.sampling_rate * 3
            
            np_shift, coeff = cross_correlation.xcorr(tr1, tr2, int(cc_np))
            
            t_shift = float(np_shift)/tr1.stats.sampling_rate
            
            print "Cross Correlation:"
            print "Shift:       " + str(t_shift)
            print "Coefficient: " + str(coeff)
            
            plt.title('Single Comparison' + '\n' + str(t_shift) + \
                        ' sec , coeff: ' + str(round(coeff, 5)) + \
                        '\n' + id_name, \
                        fontsize = 'large', weight = 'bold')
            
            if input['resp_paz'] == 'Y':
                # -----------------------
                #plt.subplot(223)
                plt.subplot2grid((3,4), (2,0), colspan=2)
                
                plt.plot(np.log10(f), np.log10(abs(resp)/(sensitivity*sensitivity)), \
                                            color = 'blue', label = 'RESP')
                plt.plot(np.log10(f), np.log10(abs(h)/sensitivity), \
                                            color = 'red', label = 'PAZ')
                
                #for j in [0.008, 0.012, 0.025, 0.5, 1, 2, 3, 4]:
                for j in [0.5]:
                    plt.axvline(np.log10(j), linestyle = '--')

                plt.xlabel('Frequency [Hz] -- power of 10')
                plt.ylabel('Amplitude -- power of 10')

                plt.legend(loc=2)
                
                # -----------------------
                #plt.subplot(224)
                plt.subplot2grid((3,4), (2,2), colspan=2)

                #take negative of imaginary part
                phase_paz = np.unwrap(np.arctan2(h.imag, h.real))
                phase_resp = np.unwrap(np.arctan2(resp.imag, resp.real))
                plt.plot(np.log10(f), phase_resp, color = 'blue', label = 'RESP')
                plt.plot(np.log10(f), phase_paz, color = 'red', label = 'PAZ')
                
                #for j in [0.008, 0.012, 0.025, 0.5, 1, 2, 3, 4]:
                for j in [0.5]:
                    plt.axvline(np.log10(j), linestyle = '--')

                plt.xlabel('Frequency [Hz] -- power of 10')
                plt.ylabel('Phase [radian]')

                plt.legend()

                # title, centered above both subplots
                # make more room in between subplots for the ylabel of right plot
                plt.subplots_adjust(wspace=0.3)
                """
                # -----------------------
                plt.subplot(325)
                
                plt.plot(np.log10(f), np.log10(abs(resp)/(sensitivity*sensitivity)) - \
                                        np.log10(abs(h)/sensitivity), \
                                        color = 'black', label = 'RESP - PAZ')

                for j in [0.008, 0.012, 0.025, 0.5, 1, 2, 3, 4]:
                    plt.axvline(np.log10(j), linestyle = '--')

                plt.xlabel('Frequency [Hz] -- power of 10')
                plt.ylabel('Amplitude -- power of 10')

                plt.legend()
                
                # -----------------------
                plt.subplot(326)
                #take negative of imaginary part
                phase_paz = np.unwrap(np.arctan2(h.imag, h.real))
                phase_resp = np.unwrap(np.arctan2(resp.imag, resp.real))
                plt.plot(np.log10(f), np.log10(phase_resp) - np.log10(phase_paz), \
                                        color = 'black', label = 'RESP - PAZ')

                for j in [0.008, 0.012, 0.025, 0.5, 1, 2, 3, 4]:
                    plt.axvline(np.log10(j), linestyle = '--')

                plt.xlabel('Frequency [Hz] -- power of 10')
                plt.ylabel('Phase [radian] -- power of 10')

                plt.legend()

                # title, centered above both subplots
                # make more room in between subplots for the ylabel of right plot
                plt.subplots_adjust(wspace=0.3)
                """
            plt.show()
                
            
            print str(i+1) + '/' + str(len(ls_first))
            print ls_first[i]
            print '------------------'
            wait = raw_input(id_name)
            print '***************************'
            
        except Exception, error:
            print '##################'
            print error
            print '##################'


###################### cross_correlation ###############################

def cross_corr(max_ts = 5.):
    
    """
    create a 'cc.txt' file for the waveforms in the first path and 
    the second path by measuring the cross correlation coefficient and
    the time shift.
    'cc.txt' is located in the same folder as COMPARE_DMT.py
    """
    
    global input
    
    identity_all = input['net'] + '.' + input['sta'] + '.' + \
                    input['loc'] + '.' + input['cha']
    ls_first = glob.glob(os.path.join(input['first_path'], identity_all))
    ls_second = glob.glob(os.path.join(input['second_path'], identity_all))
    
    if os.path.isfile('./cc.txt'):
        print '----------------------------------------------------'
        
        usr_input = raw_input(\
                    '"cc.txt" exists in the directory, do you want to:\n\n' + \
                    'A. append to the existing "cc.txt"\n' + \
                    'N. generate a new one\n\n' + \
                    'please enter A or N based on your ' + \
                    'decision:\n').upper()
        
        if  usr_input == 'A':
            print '###################################'
            print 'Continue with appending to "cc.txt"'
            print '###################################'
            
        elif usr_input == 'N':
            os.remove('./cc.txt')
            print '"cc.txt" is removed'
        print '----------------------------------------------------'
    
    # open the cc.txt file that exists in the directory OR create a new one
    cc_open = open('./cc.txt', 'a')
    cc_open.writelines(str(len(ls_first)) + ',\n')
    cc_open.close()
    
    if input['cc_parallel'] == 'Y':
        # Parallel Cross Correlation
        import pprocess
        
        print "###################"
        print "Parallel Request"
        print "Number of Nodes: " + str(input['cc_np'])
        print "###################"
        
        # using pprocess.Map to define the parallel job
        parallel_results = pprocess.Map(limit=input['cc_np'], reuse=1)
        parallel_job = parallel_results.manage(pprocess.MakeReusable(cc_core))
        
        for i in range(0, len(ls_first)):
            parallel_job(ls_first = ls_first[i], ls_second = ls_second, \
                            identity_all = identity_all, max_ts = max_ts,
                            print_sta = str(i+1) + '/' + str(len(ls_first)))        
        
        parallel_results.finish()
    
    else:
        for i in range(0, len(ls_first)):
        #for i in range(0, 20):
            cc_core(ls_first = ls_first[i], ls_second = ls_second, \
                            identity_all = identity_all, max_ts = max_ts,
                            print_sta = str(i+1) + '/' + str(len(ls_first)))

###################### cc_core #########################################

def cc_core(ls_first, ls_second, identity_all, max_ts, print_sta):
    
    """
    Perform the main part of the cross correlation and creating 
    the cc.txt file
    """
    
    global input
    
    try:
        
        cc_open = open('./cc.txt', 'a')
        
        tr1 = read(ls_first)[0]
            
        if input['phase'] != 'N':
            evsta_dist = util.locations2degrees(lat1 = tr1.stats.sac.evla, \
                                    long1 = tr1.stats.sac.evlo, lat2 = tr1.stats.sac.stla, \
                                    long2 = tr1.stats.sac.stlo)
            
            taup_tt = taup.getTravelTimes(delta = evsta_dist, depth = tr1.stats.sac.evdp)
            
            phase_exist = 'N'
            
            for tt_item in taup_tt:
                if tt_item['phase_name'] == input['phase']:
                    print 'Requested phase:'
                    print input['phase']
                    print '------'
                    print tt_item['phase_name']
                    print 'exists in the waveform!'
                    print '-----------------------'
                    t_phase = tt_item['time']
                    
                    phase_exist = 'Y'
                    break
                    
        if input['phase'] == 'N' or (input['phase'] != 'N' and phase_exist == 'Y'):
            
            # identity of the current waveform
            identity = tr1.stats.network + '.' + tr1.stats.station + '.' + \
                        tr1.stats.location + '.' + tr1.stats.channel
            
            # Keep the current identity in a new variable
            id_name = identity
            
            try:
                tr2 = read(os.path.join(input['second_path'], identity))[0]
            except Exception, error:
                # if it is not possible to read the identity in the second path
                # then change the network part of the identity based on
                # correction unit
                identity = input['corr_unit'] + '.' + tr1.stats.station + '.' + \
                        tr1.stats.location + '.' + tr1.stats.channel
                tr2 = read(os.path.join(input['second_path'], identity))[0]
            
            if input['resample'] != 'N':
                tr1.resample(input['resample'])
                tr2.resample(input['resample'])
            
            if input['tw'] == 'Y':
                t_cut_1 = tr1.stats.starttime + t_phase - input['preset']
                t_cut_2 = tr1.stats.starttime + t_phase + input['offset']
                tr1.trim(starttime = t_cut_1, endtime = t_cut_2)
                
                t_cut_1 = tr2.stats.starttime + t_phase - input['preset']
                t_cut_2 = tr2.stats.starttime + t_phase + input['offset']
                tr2.trim(starttime = t_cut_1, endtime = t_cut_2)
            
            if input['hlfilter'] == 'Y':
                tr1.filter('lowpass', freq=input['hfreq'], corners=2)
                tr2.filter('lowpass', freq=input['hfreq'], corners=2)
                tr1.filter('highpass', freq=input['lfreq'], corners=2)
                tr2.filter('highpass', freq=input['lfreq'], corners=2)
            
            # normalization of all three waveforms to the 
            # max(max(tr1), max(tr2), max(tr3)) to keep the scales
            #maxi = max(abs(tr1.data).max(), abs(tr2.data).max(), abs(tr3.data).max())
            '''
            maxi = max(abs(tr1.data).max(), abs(tr2.data).max())
            tr1_data = tr1.data/abs(maxi)
            tr2_data = tr2.data/abs(maxi)
            tr3_data = tr3.data/abs(maxi)
            '''
            tr1.data = tr1.data/abs(max(tr1.data))
            tr2.data = tr2.data/abs(max(tr2.data))
        
            cc_np = tr1.stats.sampling_rate * max_ts
            np_shift, coeff = cross_correlation.xcorr(tr1, tr2, int(cc_np))
            t_shift = float(np_shift)/tr1.stats.sampling_rate
            
            # scale_str shows whether the scale of the waveforms are the same or not
            # if scale_str = 'Y' then the scale is correct.
            scale_str = 'Y'
            
            if abs(tr1.data).max() > 2.0 * abs(tr2.data).max():
                label_tr1 = ls_first.split('/')[-2]
                label_tr2 = ls_second[0].split('/')[-2]
                print '#####################################################'
                print "Scale is not correct! " + label_tr1 + '>' + label_tr2
                print '#####################################################'
                scale_str = 'N'
            elif abs(tr2.data).max() >= 2.0 * abs(tr1.data).max():
                label_tr1 = ls_first.split('/')[-2]
                label_tr2 = ls_second[0].split('/')[-2]
                print '#####################################################'
                print "Scale is not correct! " + label_tr2 + '>' + label_tr1
                print '#####################################################'
                scale_str = 'N'
            
            if not str(coeff) == 'nan':
                cc_open.writelines(id_name + ',' + str(round(coeff, 4)) + ',' + str(t_shift) + \
                                                ',' + scale_str + ',' + '\n')
                                
            print "Cross Correlation:"
            print id_name
            print "Shift:       " + str(t_shift)
            print "Coefficient: " + str(coeff)
            print print_sta
            print '------------------'
       
            cc_open.close()
            cc_open.close()
    
    except Exception, error:
        print '##################'
        print error
        print '##################'

###################### read_cc #########################################

def read_cc(max_coeff = 0.99, width = 0.01, max_ts = 5.):
    
    """
    This function reads the cc.txt file and create some plots
    """
    
    t_shift_array = np.array([])
    num_stas = 0
    num_cc_tt = 0
    zero_count = 0
    
    cc_open = open('./cc.txt', 'r')
    cc_read = cc_open.readlines()
    
    # create a new file (cc_error.txt) for the problematic comparisons
    cc_error_open = open('./cc_error.txt', 'w')
    
    len_ls_first = str(int(cc_read[0].split(',')[0]))
    
    for i in range(1, len(cc_read)):
        cc_read[i] = cc_read[i].split(',')
        coeff = eval(cc_read[i][1])
        t_shift = eval(cc_read[i][2])
        
        if abs(coeff) > max_coeff and cc_read[i][3] == 'Y':
            t_shift_array = np.append(t_shift_array, t_shift)
            num_stas += 1
        
        if abs(coeff) > max_coeff and abs(t_shift) <= width:
            num_cc_tt += 1
        
        if abs(t_shift) >= width or abs(coeff) <= max_coeff or cc_read[i][3] == 'N':
            cc_error_open.writelines(cc_read[i][0] + ',' + \
                        str(round(float(cc_read[i][1]), 4)) + ',' + \
                        cc_read[i][2] + ',' + cc_read[i][3] + ',' + '\n')
        else:
            zero_count += 1
    
    bins = np.arange(-int(max_ts), int(max_ts), width)
    digit = np.digitize(t_shift_array, bins)
    digit_list = digit.tolist()
    
    digit_count = {}
    for i in range(0, len(bins)):
        digit_count[str(i)] = digit_list.count(i)
    
    plt.clf()
    
    for i in range(0, len(bins)):
        plt.bar(left = bins[i]-(width), width = width, \
                height = digit_count[str(i)], color = 'blue', edgecolor = 'blue')
    
    plt.xlabel('Time Shift (sec)', fontsize = 'large', weight = 'bold')
    plt.ylabel('Number of Waveforms', fontsize = 'large', weight = 'bold')
    plt.xticks(fontsize = 'large')
    plt.yticks(fontsize = 'large')
    
    plt.title(str(num_stas) + '/' + len_ls_first +  \
                '  with |cc_coeff| > ' + \
                str(max_coeff) + '\n' + '|time shift| < ' + \
                str(width) + ':   ' + str(zero_count), \
                fontsize = 'large', weight = 'bold')
    
    print 'Number of stations with good phase shift'
    print num_cc_tt
    
    plt.show()

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
        print '\n*****************************************************'
        print 'The response file is not in the right dimension (M/S)'
        print 'This could cause problems in the instrument correction.'
        print 'Please check the response file:'
        print resp_file
        print '*****************************************************'
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

########################################################################
########################################################################
########################################################################

if __name__ == "__main__":
    
    t1_pro = time.time()
    
    status = COMPARE_DMT()
    
    t_pro = time.time() - t1_pro
    print "\n------------"
    print "Total time:"
    print "%f sec" % (t_pro)
    print "------------"

    sys.exit(status)
