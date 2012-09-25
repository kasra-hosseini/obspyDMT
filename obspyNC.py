#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  obspyNC.py
#   Purpose:   obspyNC main program 
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
#-------------------------------------------------------------------

#for debugging: import ipdb; ipdb.set_trace()

'''
Add new and useful attributes
continue with explanation and ....
'''

#-----------------------------------------------------------------------
#----------------Import required Modules (Python and Obspy)-------------
#-----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from __future__ import with_statement
import sys
import os
import glob
import shutil
import time
import fnmatch
from optparse import OptionParser

import numpy as np

from netCDF4 import Dataset

from obspy.core import read, UTCDateTime, Trace
from obspy.core.util.attribdict import AttribDict

########################################################################
############################# Main Program #############################
########################################################################

def obspyNC(**kwargs):
    
    """
    obspyNC: is the function dedicated to the main part of the code.
    """
    
    print '\n-----------------------------------------------------'
    bold = "\033[1m"
    reset = "\033[0;0m"
    print '\t\t' + bold + 'ObsPyNC ' + reset + '(' + bold + 'ObsPy N' + \
        reset + 'et'+ bold + 'C' + reset + 'DF)' + reset + '\n'
    print '\t' + 'Automatic tool for Reading and Writing'
    print '       netCDF4 files for Large Seismic Datasets'
    print '\n'
    print ':copyright:'
    print 'The ObsPy Development Team (devs@obspy.org)' + '\n'
    print 'Developed by Kasra Hosseini'
    print 'email: hosseini@geophysik.uni-muenchen.de' + '\n'
    print ':license:'
    print 'GNU General Public License, Version 3'
    print '(http://www.gnu.org/licenses/gpl-3.0-standalone.html)'
    print '-----------------------------------------------------'
    
    # global variables
    global input
    
    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()
    
    # ------------------Read INPUT file (Parameters)--------------------
    read_input_command(parser, **kwargs)
    
    # ------------------ncMain------------------------------------------
    ncMain()


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
    
    helpmsg = "show how to run obspyNC.py and exit"
    parser.add_option("--how", action="store_true",
                      dest="how", help=helpmsg)
    
    helpmsg = "Create a netCDF4 file out of the event folder(s) " + \
                "specified here [Default: 'N']"
    parser.add_option("--ncCreate", action="store",
                        dest="ncCreate", help=helpmsg)
    
    helpmsg = "Extract from a netCDF file existed in the " + \
                "event folder(s) specified here [Default: 'N']"
    parser.add_option("--ncExtract", action="store",
                        dest="ncExtract", help=helpmsg)
    
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
    
    helpmsg = "work with 'raw', 'dis', 'vel' or 'acc' waveforms. [Default: 'raw']"
    parser.add_option("--data_type", action="store",
                        dest="data_type", help=helpmsg)
    
    helpmsg = "To not generate AXISEM input file. (STATION file)"
    parser.add_option("--noaxisem", action="store_true",
                      dest="noaxisem", help=helpmsg)
    
    helpmsg = "Parallel ncCreate and ncExtract"
    parser.add_option("--nc_parallel", action="store_true",
                      dest="nc_parallel", help=helpmsg)
    
    helpmsg = "Number of processors to be used in --nc_parallel. [Default: 4]"
    parser.add_option("--nc_np", action="store",
                        dest="nc_np", help=helpmsg)
    
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
    input = {   'ncCreate': 'N',
                'ncExtract': 'N',
    
                'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
                
                'data_type': 'raw',
                
                'nc_np': 4,
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
        print 'To run obspyNC:'
        
        print '\n1. To Create a netCDF4 file out of a given folder:'
        print '\t./obspyNC.py --ncCreate address --data_type dis'
        print '"--data_type dis" ---> says that the type of the data that we want to convert is dis'
        print '\nif you just want to convert specific stations:'
        print '\t./obspyNC.py --ncCreate address --data_type dis --identity "*.*.*.BHZ"\n'
        print '----------'
        print '\n2. To Extract the data from a netCDF4 file:'
        print '\t./obspyNC.py --ncExtract address\n'
        print '----------'
        print '\n3. obspyNC creates "STATIONS" file as an AXISEM input by default, if not needed:'
        print '\t./obspyNC.py --ncCreate address --noaxisem'
        print '\t./obspyNC.py --ncExtract address --noaxisem'
        print '====================================================================================\n'
        sys.exit(2)
    
    if options.ncCreate != 'N':
        if not os.path.isabs(options.ncCreate):
            options.ncCreate = os.path.join(os.getcwd(), options.ncCreate)
    
    if options.ncExtract != 'N':
        if not os.path.isabs(options.ncExtract):
            options.ncExtract = os.path.join(os.getcwd(), options.ncExtract)
    
    input['ncCreate'] = options.ncCreate
    input['ncExtract'] = options.ncExtract
    
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
    
    input['data_type'] = options.data_type
    
    if options.noaxisem: options.noaxisem = 'Y'
    input['noaxisem'] = options.noaxisem
    
    if options.nc_parallel: options.nc_parallel = 'Y'
    input['nc_parallel'] = options.nc_parallel
    
    input['nc_np'] = int(options.nc_np)
    
###################### ncMain ##########################################

def ncMain():
    
    """
    This function is the main netCDF (read/write) function. The required
    address, list of stations and other info will be collected here and
    will be passed to ncChoose (choose between Create/Extract)
    """
    
    global input
    
    if input['ncCreate'] != 'N':
        address = input['ncCreate']
    if input['ncExtract'] != 'N':
        address = input['ncExtract']
    
    events, address_events = quake_info(address, 'info')
    
    if input['nc_parallel'] == 'Y':
        import pprocess
        
        print "\n#######################"
        print "Parallel Create/Extract"
        print "Number of Nodes: " + str(input['nc_np'])
        print "#######################\n"
        
        parallel_results = pprocess.Map(limit=input['nc_np'], reuse=1)
        parallel_job = parallel_results.manage(pprocess.MakeReusable(nc_parallel_core))
        
        for i in range(0, len(events)):
            parallel_job(events = events, address_events = address_events, i = i)
        parallel_results.finish()
    
    else:
        for i in range(0, len(events)):
            nc_parallel_core(events = events, address_events = address_events, i = i)
            
###################### nc_parallel_core ################################

def nc_parallel_core(events, address_events, i):
    
    """
    """
    
    sta_ev = read_station_event(address_events[i])
    ls_saved_stas_tmp = []
    ls_saved_stas = []
    
    for j in range(0, len(sta_ev[0])):
        
        if input['data_type'] == 'raw':
            BH_file = 'BH_RAW'
            network = sta_ev[0][j][0]
        elif input['data_type'].upper() == 'DIS':
            BH_file = 'BH'
            network = 'dis'
        elif input['data_type'].upper() == 'VEL':
            BH_file = 'BH_VEL'
            network = 'vel'
        elif input['data_type'].upper() == 'ACC':
            BH_file = 'BH_ACC'
            network = 'acc'
        
        station_id = network + '.' + sta_ev[0][j][1] + '.' + \
                     sta_ev[0][j][2] + '.' + sta_ev[0][j][3]
        resp_id = sta_ev[0][j][0] + '.' + sta_ev[0][j][1] + '.' + \
                     sta_ev[0][j][2] + '.' + sta_ev[0][j][3]
        ls_saved_stas_tmp.append([os.path.join(address_events[i], BH_file,\
                                station_id), resp_id])
    
    pattern_sta = input['net'] + '.' + input['sta'] + '.' + \
                    input['loc'] + '.' + input['cha']
    
    for k in range(0, len(ls_saved_stas_tmp)):
        if fnmatch.fnmatch(ls_saved_stas_tmp[k][0].split('/')[-1], pattern_sta):
            ls_saved_stas.append(ls_saved_stas_tmp[k])
    
    if len(ls_saved_stas) != 0:        
        print '\n\n**********'
        print 'event: ' + str(i+1) + '/' + str(len(events))
        print '**********'
        ncChoose(input, ls_saved_stas, address_events[i])
        
    else:
        print "There is no station in the folder to convert!"

###################### ncChoose ########################################

def ncChoose(input, ls_saved_stas, address):
    
    """
    Based on the user request (Create or Extract), this function will 
    provide the required inputs for:
    ncCreate and ncExtract
    """
    
    global rootgrp, ls_converted_stas, st_converted_stas
    
    eventname = address.split('/')[-1]
    
    if input['ncCreate'] != 'N':
        
        print "========================"
        print "Create netCDF file from:"
        print address
        print "========================"
        
        if os.path.isdir(os.path.join(address, 'ncfolder')):
            shutil.rmtree(os.path.join(address, 'ncfolder'))
        
        os.mkdir(os.path.join(address, 'ncfolder'))
        
        print '\n-------------------------'
        print "Number of all available"
        print "stations in the folder to "
        print "be converted into netCDF:"
        print len(ls_saved_stas)
        print '-------------------------'

        rootgrp = Dataset(os.path.join(address, 'ncfolder', eventname + '.nc'), \
                                                        'w', format = 'NETCDF4')
        ls_converted_stas = []
        st_converted_stas = 'AXISEM STATIONS\n'
        for i in range(0, len(ls_saved_stas)):
            print_str = str(i+1)
            ncCreate(address = address, ls_saved_stas = ls_saved_stas[i], \
                            eventname = eventname, print_str = print_str)
        
        if not input['noaxisem'] == 'Y':
            rootgrp.axisem = st_converted_stas
        rootgrp.close()
        
        
    elif input['ncExtract'] != 'N':
        
        print "============================"
        print "Extracting netCDF file from:"
        print address
        print "============================"
        
        rootgrp = Dataset(os.path.join(address, 'ncfolder', eventname + '.nc'), \
                                                        'r', format = 'NETCDF4')
        ncExtract(address = address)

###################### ncCreate ########################################

def ncCreate(address, ls_saved_stas, eventname, print_str):
    
    """
    Function defined for parallel job which contains all the required steps
    for ncCreate (Creating a netCDF file out of an event folder)
    """
    
    global rootgrp, ls_converted_stas, st_converted_stas
    
    print print_str,
    
    try:
        if os.path.isfile(os.path.join(address, 'Resp', 'RESP' + '.' + \
                                ls_saved_stas[1])):
            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
                                    ls_saved_stas[1])
            resp_open = open(resp_file)
            resp_read = resp_open.read()
        else:
            print '\n' + os.path.join(address, 'Resp', 'RESP' + '.' + \
                                ls_saved_stas[1]) + ' -- ' + \
                                'DOES NOT EXIST!'
            resp_read = 'NO RESPONSE FILE AVAILABLE'
        
        tr = read(ls_saved_stas[0])[0]
        
        rootgrp.eventID = eventname
        rootgrp.evla = tr.stats.sac.evla
        rootgrp.evlo = tr.stats.sac.evlo
        rootgrp.evdp = tr.stats.sac.evdp
        rootgrp.mag = tr.stats.sac.mag
        
        ncCreate_core(tr = tr, resp_read = resp_read)
    except Exception, e:
        print "\n------------------------------------------------"
        print "Problem with reading the: " + ls_saved_stas[1]
        print e
        print "------------------------------------------------"

###################### ncCreate_core ###################################

def ncCreate_core(tr, resp_read):
    
    """
    This function puts one station (data, response file, header) in an
    already created netCDF file
    
    : type rootgrp: netCDF4.Dataset
    : param rootgrp: a netCDF version 4 group that contains one event
    : type tr: class 'obspy.core.trace.Trace'
    : param tr: the trace that will be added to the nc file
    : type resp_read: str
    : param resp_read: the whole response file of the trace in 
                       one string format to be added as an attribute
                       to the info group of the station group
    """
    
    global rootgrp, ls_converted_stas, st_converted_stas
    
    stationID = tr.stats.network + '.' + tr.stats.station + '.' + \
                        tr.stats.location + '.' + tr.stats.channel
        
    stgrp = rootgrp.createGroup(stationID)
    
    stgrp.identity = stationID
    stgrp.stla = tr.stats.sac.stla
    stgrp.stlo = tr.stats.sac.stlo
    stgrp.stdp = tr.stats.sac.stdp
    stgrp.stel = tr.stats.sac.stel
    
    stgrp.respfile = resp_read
    
    for i in tr.stats.sac.keys():
        if np.isnan(tr.stats.sac[i]) == True:
            tr.stats.sac[i] = -12345.0
    
    stgrp.headerV = str(tr.stats.values())
    stgrp.headerK = str(tr.stats.keys())

    stgrp.createDimension('data', len(tr.data))
    stdata = stgrp.createVariable('data', 'f8', ('data',), zlib = True)

    stdata[:] = tr.data
    
    if tr.stats.location == '' or tr.stats.location == ' ':
        tr.stats.location = '__'
    if tr.stats.network + '.' + tr.stats.station + '.' + \
                tr.stats.location not in ls_converted_stas:
        ls_converted_stas.append(tr.stats.network + '.' + tr.stats.station + \
                                                    '.' + tr.stats.location)
        st_converted_stas += tr.stats.station + tr.stats.location + \
                            ' '*(5 - len('%s' % tr.stats.network)) + '%s' \
                            % tr.stats.network + \
                            ' '*(9 - len('%.2f' % float(tr.stats.sac.stla))) + '%.2f' \
                            % float(tr.stats.sac.stla) + \
                            ' '*(9 - len('%.2f' % float(tr.stats.sac.stlo))) + '%.2f' \
                            % float(tr.stats.sac.stlo) + \
                            ' '*(15 - len('0.0000000E+00')) + \
                            '0.0000000E+00' + \
                            ' '*(15 - len('0.0000000E+00')) + \
                            '0.0000000E+00' + '\n'
    
###################### ncExtract #######################################

def ncExtract(address):

    """
    This function extract a station (data, response file, header) from a
    netCDF file

    : type rootgrp: netCDF4.Dataset
    : param rootgrp: a netCDF version 4 group that contains one event
    : type tr: class 'obspy.core.trace.Trace'
    : param tr: the trace that will be extracted from the nc file
    : type resp_read: str
    : param resp_read: the whole response file of the trace in 
                       one string format extracted from the info/respfile attribute
    """
    
    global rootgrp
    
    if not os.path.isdir(os.path.join(address, 'Resp_NC')):
        os.mkdir(os.path.join(address, 'Resp_NC'))
    
    if not os.path.isdir(os.path.join(address, 'BH_NC')):
        os.mkdir(os.path.join(address, 'BH_NC'))
    
    root_grps = rootgrp.groups
    
    num_iter = 1
    print "\n----------------------------"
    print "Number of all available"
    print "stations in the netCDF file:"
    print len(root_grps)
    print "----------------------------\n"
    
    if not input['noaxisem'] == 'Y':
        axi_open = open(os.path.join(address, 'STATIONS'), 'w')
        axi_open.writelines(rootgrp.axisem[17:])
        axi_open.close
        
    for grp in root_grps:
        
        print str(num_iter),
        
        stgrp = root_grps[grp]
        stdata = stgrp.variables['data'][:]
        
        resp_read = stgrp.respfile
        
        if not resp_read == 'NO RESPONSE FILE AVAILABLE':
            resp_open = open(os.path.join(address, 'Resp_NC', 'RESP.' + stgrp.identity), 'w')
            resp_open.writelines(resp_read)
            resp_open.close
        else:
            print '\nNO RESPONSE FILE AVAILABLE for ' + stgrp.identity
        
        ststats = {}
        
        for key in range(0, len(eval(stgrp.headerK))):
            ststats[eval(stgrp.headerK)[key]] = eval(stgrp.headerV)[key]
        
        tr = Trace(stdata, ststats)
        
        tr.write(os.path.join(address, 'BH_NC', stgrp.identity), format = 'SAC')
        
        num_iter += 1

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

########################################################################
########################################################################
########################################################################

if __name__ == "__main__":
    
    
    global rootgrp
    
    t1_pro = time.time()
    status = obspyNC()
    t_pro = time.time() - t1_pro
    
    print'\n\n==========='
    print "Total Time:"
    print t_pro
    print'===========\n'
    
    # pass the return of main to the command line.
    sys.exit(status)




###################### Trial and Error #################################
"""
if input['nc_parallel'] == 'Y':
    import pprocess
    
    print "###################"
    print "Parallel Request"
    print "Number of Nodes: " + str(input['nc_np'])
    print "###################"
    
    parallel_results = pprocess.Map(limit=input['nc_np'], reuse=1)
    parallel_job = parallel_results.manage(pprocess.MakeReusable(ncCreate_core))

    for i in range(660, len(ls_saved_stas)):
        print_str = 'station: ' + str(i+1) + '/' + str(len(ls_saved_stas))
        parallel_job(address = address, ls_saved_stas = ls_saved_stas[i],
                            eventname = eventname, print_str = print_str)
    
    parallel_results.finish()

    
else:
"""
