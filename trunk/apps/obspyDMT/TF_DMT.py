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
    
    
    for i in range(572, len(ls_first)):
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
            
            t_shift = np_shift/tr1.stats.sampling_rate
            
            print "Cross Correlation:"
            print "Shift:       " + str(t_shift)
            print "Coefficient: " + str(coeff)
            
            plt.title('Single Comparison' + '\n' + str(t_shift) + \
                        ' sec , coeff: ' + str(round(coeff, 5)) + '\n' + id_name, \
                        fontsize = 'large', weight = 'bold')
            plt.show()
            
            print str(i+1) + '/' + str(len(ls_first))
            wait = raw_input(identity)
            
            print ls_first[i]
            print '------------------'
        
        except Exception, error:
            print '##################'
            print error
            print '##################'
            
            
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
