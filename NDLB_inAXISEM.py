#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  NDLB_inAXISEM.py
#   Purpose:   NDLB_inAXISEM.py main program 
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
#
#   Copyright (C) 2012 Kasra Hosseini
#-------------------------------------------------------------------

#for debugging: import ipdb; ipdb.set_trace()

#-----------------------------------------------------------------------
#----------------Import required Modules (Python and Obspy)-------------
#-----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from __future__ import with_statement
import os
import sys
import time
import fnmatch
from optparse import OptionParser

from obspy.core import UTCDateTime

########################################################################
############################# Main Program #############################
########################################################################

def NDLB_inAXISEM(**kwargs):
    
    global input
    
    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()
    
    # ------------------Read INPUT file (Parameters)--------------------
    read_input_command(parser, **kwargs)
    
    # ------------------STATIONS----------------------------------------
    STATIONS()

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
    
    helpmsg = "The address of the event folder."
    parser.add_option("--address", action="store",
                      dest="address", help=helpmsg)
    
    helpmsg = "Identity code restriction, syntax: dis/vel/acc.sta.loc.cha"
    parser.add_option("--identity", action="store", dest="identity",
                        help=helpmsg)
    
    helpmsg = "create STATIONS file for AXISEM"
    parser.add_option("--STATIONS", action="store_true", dest="STATIONS",
                        help=helpmsg)
    
    # parse command line options
    (options, args) = parser.parse_args()
    
    return options, args, parser

###################### read_input_command ##############################

def read_input_command(parser):
    
    """
    Create input object (dictionary) based on command-line options.
    The default values are as "input" object (below) 
    """
    
    global input
    
    input = {   'address': 'psdata',
                'identity': '*.*.*.*',
            }
    
    # feed input dictionary of defaults into parser object
    parser.set_defaults(**input)
    
    # parse command line options
    (options, args) = parser.parse_args()
    # command line options can now be accessed via options.varname.
    
    # parse address (check if given absolute or relative)
    if options.address:
        if not os.path.isabs(options.address):
            options.address = os.path.join(os.getcwd(), options.address)
    
    input['address'] = options.address
    input['identity'] = options.identity
    if options.STATIONS: 
        input['STATIONS'] = 'Y'

###################### find_event ######################################

def STATIONS():
    
    """
    Create STATIONS file as an input for AXISEM
    """
    
    global input
    
    events, address_events = quake_info(input['address'], 'info')
    
    for i in range(0, len(events)):
        sta_ev = read_station_event(address_events[i])
        
        for j in range(0, len(sta_ev[0])):
            sta_ev[0][j][8] = sta_ev[0][j][0] + '_' + sta_ev[0][j][1]
        sta_ev_req = list(unique_items(sta_ev[0]))
        
        for j in range(0, len(sta_ev_req)):
            STATIONS_file = open(os.path.join(address_events[i],\
                                'info', 'STATIONS'), 'a+') 
            STATIONS_file.writelines(sta_ev_req[j][1] + \
                            ' '*(5 - len('%s' % sta_ev_req[j][0])) + '%s' \
                            % sta_ev_req[j][0] + \
                            ' '*(9 - len('%.2f' % float(sta_ev_req[j][4]))) + '%.2f' \
                            % float(sta_ev_req[j][4]) + \
                            ' '*(9 - len('%.2f' % float(sta_ev_req[j][5]))) + '%.2f' \
                            % float(sta_ev_req[j][5]) + \
                            ' '*(15 - len('0.0000000E+00')) + \
                            '0.0000000E+00' + \
                            ' '*(15 - len('0.0000000E+00')) + \
                            '0.0000000E+00' + '\n')
            
###################### unique_items ####################################

def unique_items(L):
    found = set()
    for item in L:
        if item[8] not in found:
            yield item
            found.add(item[8])

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

if __name__ == "__main__":
    
    t1_pro = time.time()
    status = NDLB_inAXISEM()
    
    t_pro = time.time() - t1_pro
    print "Total time: %f seconds" % (t_pro)
    print '----------------------------------------'
    
    # pass the return of main to the command line.
    sys.exit(status)
