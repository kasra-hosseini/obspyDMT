#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  TF_DMT.py
#   Purpose:   ObsPyDMT Time Frequency Plot
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

from obspy.core import read
from obspy.signal import cross_correlation


########################################################################
############################# Main Program #############################
########################################################################

def TF_DMT(**kwargs):
    
    """
    TF_DMT: is the function dedicated to the main part of the code.
    """
    
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
    if input['cc'] == 'Y':
        cross_corr()
        read_cc()
    
    # ------------------Read Cross Correlation File---------------------
    if input['read_cc'] == 'Y':
        read_cc()
    
    
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

    helpmsg = "the path where TF_DMT will read the FIRST dataset"
    parser.add_option("--first_path", action="store",
                      dest="first_path", help=helpmsg)
    
    helpmsg = "the path where TF_DMT will read the SECOND dataset"
    parser.add_option("--second_path", action="store",
                      dest="second_path", help=helpmsg)
    
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
    
    helpmsg = \
    '''
    create a 'cc.txt' file for the waveforms in the first path and 
    the second path by measuring the cross correlation coefficient and
    the time shift.
    '''
    parser.add_option("--cc", action="store_true",
                      dest="cc", help=helpmsg)
    
    helpmsg = "Parallel Cross Correlation"
    parser.add_option("--cc_parallel", action="store_true",
                      dest="cc_parallel", help=helpmsg)
    
    helpmsg = "Number of processors to be used in --cc_parallel. [Default: 4]"
    parser.add_option("--cc_np", action="store",
                        dest="cc_np", help=helpmsg)
    
    helpmsg = "Read cc.txt file [refer to --cc] and create some plots"
    parser.add_option("--read_cc", action="store_true",
                      dest="read_cc", help=helpmsg)
    
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
                
                'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
                
                'cc_np': 4,
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
        
    # parse datapath (check if given absolute or relative)
    if options.first_path:
        if not os.path.isabs(options.first_path):
            options.first_path = os.path.join(os.getcwd(), options.first_path)
    
    if options.second_path:
        if not os.path.isabs(options.second_path):
            options.second_path = os.path.join(os.getcwd(), options.second_path)
            
            
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
    
    if options.cc: options.cc = 'Y'
    input['cc'] = options.cc
    
    if options.cc_parallel: options.cc_parallel = 'Y'
    input['cc_parallel'] = options.cc_parallel
    
    input['cc_np'] = int(options.cc_np)
    
    if options.read_cc: options.read_cc = 'Y'
    input['read_cc'] = options.read_cc
    
###################### single_comparison ###############################

def single_comparison():
    
    """
    one by one comparison of the waveforms in the first path with the second path.
    """
    
    global input
    
    identity_all = input['net'] + '.' + input['sta'] + '.' + \
                    input['loc'] + '.' + input['cha']
    ls_first = glob.glob(os.path.join(input['first_path'], identity_all))
    ls_second = glob.glob(os.path.join(input['second_path'], identity_all))
    
    
    for i in range(0, len(ls_first)):
        try:
            
            tr1 = read(ls_first[i])[0]
            identity = tr1.stats.network + '.' + tr1.stats.station + '.' + \
                        tr1.stats.location + '.' + tr1.stats.channel
            
            id_name = identity
            
            try:
                tr2 = read(os.path.join(input['second_path'], identity))[0]
            except Exception, error:
                #print error
                identity = 'dis' + '.' + tr1.stats.station + '.' + \
                        tr1.stats.location + '.' + tr1.stats.channel
                tr2 = read(os.path.join(input['second_path'], identity))[0]
            
            plt.clf()
            
            time_tr1 = np.arange(0, tr1.stats.npts/tr1.stats.sampling_rate, \
                                                1./tr1.stats.sampling_rate)
            time_tr2 = np.arange(0, tr2.stats.npts/tr2.stats.sampling_rate, \
                                                1./tr2.stats.sampling_rate)
            
            label_tr1 = ls_first[i].split('/')[-2]
            label_tr2 = ls_second[i].split('/')[-2]
            
            plt.plot(time_tr1, tr1.data, color = 'blue', label = label_tr1)
            plt.plot(time_tr2, tr2.data, color = 'red', label = label_tr2)

            plt.xlabel('Time (sec)', fontsize = 'large', weight = 'bold')
            plt.ylabel('Displacement (nm)', fontsize = 'large', weight = 'bold')
            
            
            plt.xticks(fontsize = 'large')
            plt.yticks(fontsize = 'large')
            
            plt.legend()
            
            cc_np = tr1.stats.sampling_rate * 5
            
            np_shift, coeff = cross_correlation.xcorr(tr1, tr2, int(cc_np))
            
            t_shift = float(np_shift)/tr1.stats.sampling_rate
            
            print "Cross Correlation:"
            print "Shift:       " + str(t_shift)
            print "Coefficient: " + str(coeff)
            
            plt.title('Single Comparison' + '\n' + str(t_shift) + \
                        ' sec , coeff: ' + str(round(coeff, 5)) + \
                        '\n' + id_name, \
                        fontsize = 'large', weight = 'bold')
            plt.show()
            
            print str(i+1) + '/' + str(len(ls_first))
            wait = raw_input(identity)
            
            plt.close()
            
            print ls_first[i]
            print '------------------'
        
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
    'cc.txt' is located in the same folder as TF_DMT.py
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
    
    cc_open = open('./cc.txt', 'a')
    cc_open.writelines(str(len(ls_first)) + ',\n')
    cc_open.close()
    
    if input['cc_parallel'] == 'Y':
        import pprocess
        
        print "###################"
        print "Parallel Request"
        print "Number of Nodes: " + str(input['cc_np'])
        print "###################"
        
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
    
    try:
        
        cc_open = open('./cc.txt', 'a')
        
        tr1 = read(ls_first)[0]
        identity = tr1.stats.network + '.' + tr1.stats.station + '.' + \
                    tr1.stats.location + '.' + tr1.stats.channel
        
        id_name = identity
        
        try:
            tr2 = read(os.path.join(input['second_path'], identity))[0]
        except Exception, error:
            #print error
            identity = 'dis' + '.' + tr1.stats.station + '.' + \
                    tr1.stats.location + '.' + tr1.stats.channel
            tr2 = read(os.path.join(input['second_path'], identity))[0]
        
        cc_np = tr1.stats.sampling_rate * max_ts
        np_shift, coeff = cross_correlation.xcorr(tr1, tr2, int(cc_np))
        t_shift = float(np_shift)/tr1.stats.sampling_rate
        cc_open.writelines(id_name + ',' + str(coeff) + \
                            ',' + str(t_shift) + ',' + '\n')
                            
        print "Cross Correlation:"
        print id_name
        print "Shift:       " + str(t_shift)
        print "Coefficient: " + str(coeff)
        print print_sta
        print '------------------'
   
        cc_open.close()
    
    except Exception, error:
        print '##################'
        print error
        print '##################'

###################### cc_core #########################################

def read_cc(max_coeff = 0.99, width = 0.05, max_ts = 5.):
    
    """
    This function reads the cc.txt file and create some plots
    """
    
    t_shift_array = np.array([])
    num_stas = 0
    zero_count = 0
    
    cc_open = open('./cc.txt', 'r')
    cc_read = cc_open.readlines()
    
    cc_error_open = open('./cc_error.txt', 'w')
    
    len_ls_first = str(int(cc_read[0].split(',')[0]))
    
    for i in range(1, len(cc_read)):
        cc_read[i] = cc_read[i].split(',')
        coeff = eval(cc_read[i][1])
        t_shift = eval(cc_read[i][2])
        
        if abs(coeff) > max_coeff:
            t_shift_array = np.append(t_shift_array, t_shift)
            num_stas += 1
        
        if abs(t_shift) >= width or abs(coeff) <= max_coeff:
            cc_error_open.writelines(cc_read[i][0] + ',' + \
                        str(round(float(cc_read[i][1]), 4)) + ',' + \
                        cc_read[i][2] + ',' + '\n')
        else:
            zero_count += 1
    
    bins = np.arange(-int(max_ts), int(max_ts), width)
    digit = np.digitize(t_shift_array, bins)
    digit_list = digit.tolist()
    
    digit_count = {}
    for i in range(0, len(bins)):
        digit_count[str(i)] = digit_list.count(i)
    
    #zero_count = digit_count[str(int(len(bins)/2. + 1))] + \
    #                digit_count[str(int(len(bins)/2.))]
    
    plt.clf()
    
    for i in range(0, len(bins)):
        plt.bar(left = bins[i]-(width), width = width, \
                        height = digit_count[str(i)])
    
    plt.xlabel('Time Shift (sec)', fontsize = 'large', weight = 'bold')
    plt.ylabel('Number of Waveforms', fontsize = 'large', weight = 'bold')
    plt.xticks(fontsize = 'large')
    plt.yticks(fontsize = 'large')
    
    plt.title(str(num_stas) + '/' + len_ls_first +  \
                '  with |cc_coeff| > ' + \
                str(max_coeff) + '\n' + '|time shift| < ' + \
                str(width) + ':   ' + str(zero_count), \
                fontsize = 'large', weight = 'bold')
    
    plt.show()


########################################################################
########################################################################
########################################################################

if __name__ == "__main__":
    
    t1_pro = time.time()
    
    status = TF_DMT()
    
    t_pro = time.time() - t1_pro
    print "\n------------"
    print "Total time:"
    print "%f sec" % (t_pro)
    print "------------"

    sys.exit(status)
