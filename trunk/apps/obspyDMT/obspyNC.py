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
'''

#-----------------------------------------------------------------------
#----------------Import required Modules (Python and Obspy)-------------
#-----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from __future__ import with_statement
import sys
import os
import shutil
import time
import fnmatch
from optparse import OptionParser

from netCDF4 import Dataset

from obspy.core import read, UTCDateTime, Trace
from obspy.core.util.attribdict import AttribDict

########################################################################
############################# Main Program #############################
########################################################################

def obspyNC(**kwargs):
    
    """
    """
    
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
    
    helpmsg = "Create netCDF4 file out of the event folder(s) [Default: 'N']"
    parser.add_option("--ncCreate", action="store",
                        dest="ncCreate", help=helpmsg)
    
    helpmsg = "Extract from a netCDF file [Default: 'N']"
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

###################### ncMain ##########################################

def ncMain():
    
    """
    """
    
    global input
    
    if input['ncCreate'] != 'N':
        address = input['ncCreate']
    if input['ncExtract'] != 'N':
        address = input['ncExtract']
    
    events, address_events = quake_info(address, 'info')
    
    for i in range(0, len(events)):
        sta_ev = read_station_event(address_events[i])
        ls_saved_stas_tmp = []
        ls_saved_stas = []
        
        for j in range(0, len(sta_ev[0])):
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
            print 'event: ' + str(i+1) + '/' + str(len(events))
            print '------------------------------------'
            ncChoose(input, ls_saved_stas, address_events[i])
            
        else:
            print "There is no station in the folder to convert!"

###################### ncChoose ########################################

def ncChoose(input, ls_saved_stas, address):
    
    """
    """
    
    global rootgrp
    
    eventname = address.split('/')[-1]
    
    if input['ncCreate'] != 'N':
        
        if os.path.isdir(os.path.join(address, 'ncfolder')):
            shutil.rmtree(os.path.join(address, 'ncfolder'))
        
        os.mkdir(os.path.join(address, 'ncfolder'))
            
        rootgrp = Dataset(os.path.join(address, 'ncfolder', eventname + '.nc'), \
                                                        'w', format = 'NETCDF4')
        
        for i in range(0, len(ls_saved_stas)):
            
            #print str(i+1) + '/' + str(len(ls_saved_stas))
            
            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
                                        ls_saved_stas[i].split('/')[-1])
            resp_open = open(resp_file)
            resp_read = resp_open.read()
            
            try:
                tr = read(ls_saved_stas[i])[0]
            except Exception, e:
                print e
                continue

            """
            if os.path.isfile(eventname):
                os.remove(eventname)
            """
            
            ncCreate(eventname = eventname, tr = tr, resp_read = resp_read)
        rootgrp.close()
        
    elif input['ncExtract'] != 'N':
        
        rootgrp = Dataset(os.path.join(address, 'ncfolder', eventname + '.nc'), \
                                                        'r', format = 'NETCDF4')
        ncExtract(address = address)

###################### ncCreate ########################################

def ncCreate(eventname, tr, resp_read):
    
    """
    This function puts one station (data, response file, header) in an
    already created netCDF file
    
    : type rootgrp: netCDF4.Dataset
    : param rootgrp: a netCDF version 4 group that contains one event
    : type eventname: str
    : param eventname: name of the event folder that will be converted
                       to netCDF format
    : type tr: class 'obspy.core.trace.Trace'
    : param tr: the trace that will be added to the nc file
    : type resp_read: str
    : param resp_read: the whole response file of the trace in 
                       one string format to be added as an attribute
                       to the info group of the station group
    """
    
    global rootgrp
    
    stationID = tr.stats.network + '.' + tr.stats.station + '.' + \
                        tr.stats.location + '.' + tr.stats.channel
    try:
        
        stgrp = rootgrp.createGroup(stationID)
        
        stgrp.identity = stationID
        
        stinfo = stgrp.createGroup('info')
        stinfo.respfile = resp_read

        stinfo.headerV = str(tr.stats.values())
        stinfo.headerK = str(tr.stats.keys())

        stgrp.createDimension('data', len(tr.data))
        stdata = stgrp.createVariable('data', 'f8', ('data',), zlib = True)

        stdata[:] = tr.data
        
    except Exception, e:
        print e
        
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

    for grp in root_grps:
        
        stgrp = root_grps[grp]
        stdata = stgrp.variables['data'][:]
        stinfo = stgrp.groups['info']
        
        resp_read = stinfo.respfile
        resp_open = open(os.path.join(address, 'Resp_NC', 'RESP.' + stgrp.identity), 'w')
        resp_open.writelines(resp_read)
        resp_open.close
        
        ststats = {}
        
        for key in range(0, len(eval(stinfo.headerK))):
            ststats[eval(stinfo.headerK)[key]] = eval(stinfo.headerV)[key]
        
        tr = Trace(stdata, ststats)
        
        tr.write(os.path.join(address, 'BH_NC', stgrp.identity), format = 'SAC')

###################### quake_info ######################################

def quake_info(address, target):
    
    """
    Reads the info in quake file ("info" folder)
    """
    
    events = []
    target_add = locate(address, target)
    
    for k in range(0, len(target_add)):
        quake_file_open = open(os.path.join \
                                    (target_add[k], 'quake'), 'r')
        quake_file = quake_file_open.readlines()

        tmp = []
        
        for i in quake_file:
            for j in i.split():
                try:
                    tmp.append(float(j))
                except ValueError:
                    pass
        
        quake_d = {'year0': int(tmp[0]), 'julday0': int(tmp[1]), \
                'hour0': int(tmp[4]), 'minute0': int(tmp[5]), \
                'second0': int(tmp[6]), 'lat': float(tmp[8]), \
                'lon': float(tmp[9]), 'dp': float(tmp[10]), \
                'mag': float(tmp[11]), \
                'year1': int(tmp[12]), 'julday1': int(tmp[13]), \
                'hour1': int(tmp[16]), 'minute1': int(tmp[17]), \
                'second1': int(tmp[18]), \
                'year2': int(tmp[20]), 'julday2': int(tmp[21]), \
                'hour2': int(tmp[24]), 'minute2': int(tmp[25]), \
                'second2': int(tmp[26]),}
        
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

########################################################################
########################################################################
########################################################################

if __name__ == "__main__":
    
    t1_pro = time.time()
    status = obspyNC()
    t_pro = time.time() - t1_pro
    
    # pass the return of main to the command line.
    sys.exit(status)
