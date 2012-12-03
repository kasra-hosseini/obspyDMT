#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  managing_node.py
#   Purpose:   managing_node main program 
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
import subprocess
import random
import glob
import time
import fnmatch
from optparse import OptionParser

from netCDF4 import Dataset

from obspy.core import read, UTCDateTime
from obspy.core.util import locations2degrees
#from obspy.taup.taup import getTravelTimes
from obspy.iris import Client as Client_iris

########################################################################
############################# Main Program #############################
########################################################################

def managing_node(**kwargs):
    
    """
    managing_node: is the function dedicated to the main part of the code.
    """
    
    print '\n-----------------------------------------------------'
    bold = "\033[1m"
    reset = "\033[0;0m"
    print '\t\t' + bold + 'Managing Node' + reset
    print '\t' + '  Automatic tool for Managing'
    print '     Large Seismic Datasets using netCDF4'
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
    
    # ------------------ncCreate----------------------------------------
    if input['ncCreate'] != 'N':
        ncCreate()
    
    # ------------------ncSelect----------------------------------------
    if input['ncSelect'] != 'N':
        ncSelect()
    
    # ------------------plot_nc-----------------------------------------
    if input['plot_nc'] != 'N':
        plot_nc()
        
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
    
    helpmsg = "show how to run managing_node.py and exit"
    parser.add_option("--how", action="store_true",
                      dest="how", help=helpmsg)
    
    helpmsg = "Create a netCDF4 file out of the event folder(s) " + \
                "specified here [Default: 'N']"
    parser.add_option("--ncCreate", action="store",
                        dest="ncCreate", help=helpmsg)
    
    helpmsg = "Managing address where the managing_node.nc will be located " + \
                "[Default: '.' (current folder)]"
    parser.add_option("--managing_address", action="store",
                        dest="managing_address", help=helpmsg)
    
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
    
    helpmsg = "Select required stations and events from a netCDF4 file " + \
                "specified here [Default: 'N']"
    parser.add_option("--ncSelect", action="store",
                        dest="ncSelect", help=helpmsg)
    
    helpmsg = "search for all the events within the defined rectangle, " + \
                "GMT syntax: <lonmin>/<lonmax>/<latmin>/<latmax> " + \
                "[Default: -180.0/+180.0/-90.0/+90.0]"
    parser.add_option("--event_rect", action="store", dest="event_rect",
                        help=helpmsg)
    
    helpmsg = "minimum magnitude. [Default: 0.0]"
    parser.add_option("--evmagmin", action="store",
                      dest="evmagmin", help=helpmsg)
    
    helpmsg = "maximum magnitude. [Default: 9.9]"
    parser.add_option("--evmagmax", action="store",
                      dest="evmagmax", help=helpmsg)

    helpmsg = "minimum depth (event). [Default: +10.0 (above the surface!)]"
    parser.add_option("--evdpmin", action="store",
                      dest="evdpmin", help=helpmsg)
    
    helpmsg = "maximum depth (event). [Default: -6000.0]"
    parser.add_option("--evdpmax", action="store",
                      dest="evdpmax", help=helpmsg)
    
    helpmsg = "search for all the stations within the defined " + \
                "rectangle, GMT syntax: " + \
                "<lonmin>/<lonmax>/<latmin>/<latmax>." + \
                "[Default: -180.0/+180.0/-90.0/+90.0]"
    parser.add_option("--station_rect", action="store", 
                      dest="station_rect", help=helpmsg)
    
    helpmsg = "minimum station elevation. [Default: -10.0]"
    parser.add_option("--stelmin", action="store",
                      dest="stelmin", help=helpmsg)
    
    helpmsg = "maximum station elevation. [Default: +100000.0]"
    parser.add_option("--stelmax", action="store",
                      dest="stelmax", help=helpmsg)

    helpmsg = "minimum depth (station). [Default: +10.0 (above the surface!)]"
    parser.add_option("--stdpmin", action="store",
                      dest="stdpmin", help=helpmsg)
    
    helpmsg = "maximum depth (station). [Default: -6000.0]"
    parser.add_option("--stdpmax", action="store",
                      dest="stdpmax", help=helpmsg)
    
    helpmsg = "plot the events, stations and ray path in the given folder " + \
                "[Default: 'N']"
    parser.add_option("--plot", action="store",
                        dest="plot_nc", help=helpmsg)
    
    helpmsg = "plot just the events"
    parser.add_option("--plot_ev", action="store_true",
                        dest="plot_ev", help=helpmsg)
    
    helpmsg = "plot just the stations"
    parser.add_option("--plot_sta", action="store_true",
                        dest="plot_sta", help=helpmsg)
    
    helpmsg = "plot just the ray paths"
    parser.add_option("--plot_ray", action="store_true",
                        dest="plot_ray", help=helpmsg)
    
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
    
                'managing_address': '.',
                
                'net': '*', 'sta': '*', 'loc': '*', 'cha': '*',
                
                'data_type': 'DIS',
                
                'ncSelect': 'N',
                
                'evlatmin': -90.0, 'evlatmax': +90.0, 
                'evlonmin': -180.0, 'evlonmax': +180.0,
                
                'evdpmin': +10.0, 'evdpmax': -6000,
                'evmagmin': +0.0, 'evmagmax': +10.0,
                
                'stlatmin': -90.0, 'stlatmax': +90.0, 
                'stlonmin': -180.0, 'stlonmax': +180.0,
                
                'stdpmin': +10.0, 'stdpmax': -6000,
                'stelmin': -10.0, 'stelmax': +100000.0,
                
                'plot_nc': 'N',
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
        print 'To run managing_node:'
        
        print '\n1. To Create a netCDF4 file out of the event folder(s) specified here:'
        print '\t./managing_node.py --ncCreate address'
        print 'To change the address where managing_node.nc will be located:'
        print '\t./managing_node.py --ncCreate address --managing_address managing_address\n'
        print '----------'
        print '\n2. To Select the data from the managing_node.nc file:'
        print '\t./managing_node.py --ncSelect address_of_managing_node.nc --options'
        print '--options here means station and event location, event magnitude, event depth, '
        print 'station elevation, station burrial. To know more about each please refer to:'
        print '\t./managing_node.py --help\n'
        print '----------'
        print '\n3. managing_node.py could also plot your selected event-station pairs:'
        print '\t./managing_node.py --plot address'
        print 'Here address is the location where *.txt files were created (previous section).'
        print '====================================================================================\n'
        sys.exit(2)
    
    if options.ncCreate != 'N':
        if not os.path.isabs(options.ncCreate):
            options.ncCreate = os.path.join(os.getcwd(), options.ncCreate)
    
    if options.managing_address != 'N':
        if not os.path.isabs(options.managing_address):
            options.managing_address = os.path.join(os.getcwd(), options.managing_address)
    
    if options.ncSelect != 'N':
        if not os.path.isabs(options.ncSelect):
            options.ncSelect = os.path.join(os.getcwd(), options.ncSelect)
    
    if options.plot_nc != 'N':
        if not os.path.isabs(options.plot_nc):
            options.plot_nc = os.path.join(os.getcwd(), options.plot_nc)
    
    input['ncCreate'] = options.ncCreate
    input['managing_address'] = options.managing_address
    input['ncSelect'] = options.ncSelect
    input['plot_nc'] = options.plot_nc
    
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
                
    # extract min. and max. longitude and latitude if the user has given the
    # coordinates with -r (GMT syntax)
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
        except:
            print "Erroneous rectangle given."
            sys.exit(2)
    
    # extract min. and max. longitude and latitude if the user has given the
    # coordinates with -g (GMT syntax)
    if options.station_rect:
        try:
            options.station_rect = options.station_rect.split('/')
            if len(options.station_rect) != 4:
                print "Erroneous rectangle given."
                sys.exit(2)
            options.stlonmin = float(options.station_rect[0])
            options.stlonmax = float(options.station_rect[1])
            options.stlatmin = float(options.station_rect[2])
            options.stlatmax = float(options.station_rect[3])
        except:
            print "Erroneous rectangle given."
            sys.exit(2)
    
    # Extract network, station, location, channel if the user has given an
    # identity code (-i xx.xx.xx.xx)
    if options.identity:
        try:
            options.net, options.sta, options.loc, options.cha = \
                                    options.identity.split('.')
        except:
            print "Erroneous identity code given."
            sys.exit(2)
    
    input['evlonmin'] = options.evlonmin
    input['evlonmax'] = options.evlonmax
    input['evlatmin'] = options.evlatmin
    input['evlatmax'] = options.evlatmax
    
    
    input['evmagmin'] = float(options.evmagmin)
    input['evmagmax'] = float(options.evmagmax)
    input['evdpmin'] = float(options.evdpmin)
    input['evdpmax'] = float(options.evdpmax)
    
    input['stlonmin'] = options.stlonmin
    input['stlonmax'] = options.stlonmax
    input['stlatmin'] = options.stlatmin
    input['stlatmax'] = options.stlatmax
    
    input['stdpmin'] = float(options.stdpmin)
    input['stdpmax'] = float(options.stdpmax)
    input['stelmin'] = float(options.stelmin)
    input['stelmax'] = float(options.stelmax)
    
    if options.plot_ev:
        input['plot_ev'] = 'Y'
        input['plot_sta'] = 'N'
        input['plot_ray'] = 'N'
        input['plot_all'] = 'N'
    elif options.plot_sta:
        input['plot_ev'] = 'N'
        input['plot_sta'] = 'Y'
        input['plot_ray'] = 'N'
        input['plot_all'] = 'N'
    elif options.plot_ray:
        input['plot_ev'] = 'N'
        input['plot_sta'] = 'N'
        input['plot_ray'] = 'Y'
        input['plot_all'] = 'N'
    else:
        input['plot_ev'] = 'N'
        input['plot_sta'] = 'N'
        input['plot_ray'] = 'N'
        input['plot_all'] = 'Y'
        
###################### ncCreate ########################################

def ncCreate():
    
    """
    This function is the main function for creating netCDF file.
    """
    
    global input, rootgrp, client_iris
    
    client_iris = Client_iris()
    
    address = input['ncCreate']
    events, address_events = quake_info(address, 'info')
    
    rootgrp = Dataset(os.path.join(input['managing_address'], 'managing_node.nc'), \
                                                        'w', format = 'NETCDF4')
    
    rootgrp.number_events = len(events)
    
    for i in range(0, len(events)):
        
        eventname = address_events[i].split('/')[-1]
        eventgrp = rootgrp.createGroup(eventname)
        
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
                         
            ls_saved_stas_tmp.append(os.path.join(address_events[i], BH_file,\
                                    station_id))
        
        pattern_sta = input['net'] + '.' + input['sta'] + '.' + \
                        input['loc'] + '.' + input['cha']
        
        for k in range(0, len(ls_saved_stas_tmp)):
            if fnmatch.fnmatch(ls_saved_stas_tmp[k].split('/')[-1], pattern_sta):
                ls_saved_stas.append(ls_saved_stas_tmp[k])
        
        if len(ls_saved_stas) != 0:        
            print '\n**********'
            print 'event: ' + str(i+1) + '/' + str(len(events))
            print '**********'
            ncCreate_core(input, ls_saved_stas, address_events[i], eventgrp)
            
        else:
            print "There is no station in the folder to convert!"
    
    rootgrp.close()

###################### ncCreate_core ###################################

def ncCreate_core(input, ls_saved_stas, address, eventgrp):
    
    """
    """
    
    global rootgrp, client_iris
    
    eventname = address.split('/')[-1]
    
    print "========================"
    print "Create netCDF file from:"
    print address
    print "========================"
    
    print "All available stations:"
    print len(ls_saved_stas)

    tr_tmp = read(ls_saved_stas[0])[0]
    
    eventgrp.evla = tr_tmp.stats.sac.evla
    eventgrp.evlo = tr_tmp.stats.sac.evlo
    eventgrp.evdp = tr_tmp.stats.sac.evdp
    eventgrp.mag = tr_tmp.stats.sac.mag
    
    stgrp = eventgrp.createGroup('stations')
    
    stationIDS = str(len(ls_saved_stas)) + ' --- , '
    
    eventgrp.createDimension('latitude', len(ls_saved_stas))
    eventgrp.createDimension('longitude', len(ls_saved_stas))
    eventgrp.createDimension('depth', len(ls_saved_stas))
    eventgrp.createDimension('elevation', len(ls_saved_stas))
    eventgrp.createDimension('epicentral', len(ls_saved_stas))
    
    stasla = eventgrp.createVariable('latitude', 'f4', ('latitude',) , zlib = True)
    staslo = eventgrp.createVariable('longitude', 'f4', ('longitude',) , zlib = True)
    stasdp = eventgrp.createVariable('depth', 'f4', ('depth',) , zlib = True)
    stasel = eventgrp.createVariable('elevation', 'f4', ('elevation',) , zlib = True)
    stasepi = eventgrp.createVariable('epicentral', 'f4', ('epicentral',) , zlib = True)
    
    
    for i in range(0, len(ls_saved_stas)):
        
        print str(i+1),
        
        try:
            tr = read(ls_saved_stas[i])[0]
        except Exception, e:
            print "\nProblem with reading the: " + ls_saved_stas[i]
            print e
            print "------------------------------------------------"
            continue
        
        stationID = tr.stats.network + '.' + tr.stats.station + '.' + \
                        tr.stats.location + '.' + tr.stats.channel
        
        stationIDS += stationID + ' , '
        
        stasla[i] = tr.stats.sac.stla
        staslo[i] = tr.stats.sac.stlo
        stasdp[i] = tr.stats.sac.stdp
        stasel[i] = tr.stats.sac.stel
        stasepi[i] = locations2degrees(lat1 = eventgrp.evla, \
                        long1 = eventgrp.evlo, lat2 = stasla[i], \
                        long2 = staslo[i])
        
        """
        req_phases = ['P', 'PP', 'S', 'SS', 'PcP', 'ScS', 'Pdiff', 'Sdiff', \
                        'PKP', 'SKS', 'PKiKP', 'SKiKS', 'PKIKP', 'SKIKS']
        #tt = getTravelTimes(delta=stasepi[i], depth=eventgrp.evdp, \
        #                                    model='iasp91')
        tt = client_iris.traveltime(model='prem', phases=req_phases, \
                        evdepth=eventgrp.evdp, distdeg=(stasepi[i],), \
                        distkm=None, evloc=None, staloc=None, \
                        noheader=True, traveltimeonly=True, \
                        rayparamonly=False, mintimeonly=False, filename=None)
        tt = tt.split('\n')
        
        for j in range(0, len(tt)-1):
            if tt[i].split('=')[1].strip() == 'Pdiff':
                print 'this one has Pdiff'
        
        for m in range(0, len(tt)):
            if tt[m]['phase_name'] in input['phase']:
        """
        
    print '\n----------------'
    eventgrp.stations = stationIDS

###################### ncSelect ########################################

def ncSelect():

    """
    """
    
    global input, rootgrp
    
    print "============================"
    print "Extracting netCDF file from:"
    print os.path.join(input['ncSelect'])
    print "============================"
    
    rootgrp = Dataset(os.path.join(input['ncSelect']), \
                                            'r', format = 'NETCDF4')
    
    if input['data_type'] == 'raw':
        BH_file = 'BH_RAW'
    elif input['data_type'].upper() == 'DIS':
        BH_file = 'BH'
    elif input['data_type'].upper() == 'VEL':
        BH_file = 'BH_VEL'
    elif input['data_type'].upper() == 'ACC':
        BH_file = 'BH_ACC'
    
    evsta_info_open = open('./evsta_info.txt', 'w')
    evsta_plot_open = open('./evsta_plot.txt', 'w')
    ev_plot_open = open('./ev_plot.txt', 'w')
    sta_plot_open = open('./sta_plot.txt', 'w')
    
    ev_num = 1
    ls_sta = []
    pattern_sta = input['net'] + '.' + input['sta'] + '.' + \
                        input['loc'] + '.' + input['cha']
    
    for evgrp in rootgrp.groups:
        
        print '\n\n====================='
        print 'Event: \n' + str(ev_num) + '/' + str(len(rootgrp.groups))
        ev_num += 1
        print '====================='
        event_grp = rootgrp.groups[evgrp]
        
        # check the required events:
        if not input['evlatmin']<=float(event_grp.evla)<=input['evlatmax'] or \
           not input['evlonmin']<=float(event_grp.evlo)<=input['evlonmax'] or \
           not input['evdpmax']<=float(event_grp.evdp)<=input['evdpmin'] or \
           not input['evmagmin']<=float(event_grp.mag)<=input['evmagmax']:
            continue
            
        ev_plot_open.writelines(str(round(float(event_grp.evlo), 5)) + ' ' + \
                                str(round(float(event_grp.evla), 5)) + ' ' + \
                                '\n')
        
        print str(len(event_grp.stations.split(' , '))-2)
        
        for i in range(1, len(event_grp.stations.split(' , '))-2):
            
            station_name = event_grp.stations.split(' , ')[i]
            
            if not fnmatch.fnmatch(station_name, pattern_sta):
                continue
            
            if not input['stlatmin']<=float(event_grp.variables['latitude'][i])<=input['stlatmax'] or \
               not input['stlonmin']<=float(event_grp.variables['longitude'][i])<=input['stlonmax'] or \
               not input['stdpmax']<=float(event_grp.variables['depth'][i])<=input['stdpmin'] or \
               not input['stelmin']<=float(event_grp.variables['elevation'][i])<=input['stelmax']:
                continue
            print str(i),
            
            evsta_info_open.writelines(evgrp + ' , ' + station_name + ' , \n')
            
            evsta_plot_open.writelines(\
                '> -G' + str(int(random.random()*256)) + '/' + \
                str(int(random.random()*256)) + '/' + str(int(random.random()*256)) + '\n' + \
                str(round(float(event_grp.evlo), 5)) + ' ' + \
                str(round(float(event_grp.evla), 5)) + ' ' + \
                str(random.random()) + ' ' + \
                '\n' + \
                str(round(float(event_grp.variables['longitude'][i]), 5)) + ' ' + \
                str(round(float(event_grp.variables['latitude'][i]), 5)) + ' ' + \
                str(random.random()) + ' ' + \
                '\n')
            
            if ls_sta == [] or not station_name in ls_sta[:][0]:
                ls_sta.append([station_name, \
                    [str(round(float(event_grp.variables['latitude'][i]), 5)), \
                     str(round(float(event_grp.variables['longitude'][i]), 5))]])
            
    for k in range(0, len(ls_sta)):
        sta_plot_open.writelines(\
                str(round(float(ls_sta[k][1][1]), 5)) + ' ' + \
                str(round(float(ls_sta[k][1][0]), 5)) + ' ' + \
                '\n')

    evsta_info_open.close()
    evsta_plot_open.close()
    ev_plot_open.close()
    rootgrp.close()

    
"""
    
    rootgrp = Dataset(os.path.join(address, 'ncfolder', eventname + '.nc'), \
                                                'r', format = 'NETCDF4')
    
    global rootgrp
    
    if not os.path.isdir(os.path.join(address, 'Resp_NC')):
        os.mkdir(os.path.join(address, 'Resp_NC'))
    
    if not os.path.isdir(os.path.join(address, 'BH_NC')):
        os.mkdir(os.path.join(address, 'BH_NC'))
    
    root_grps = rootgrp.groups
    
    num_iter = 1
    print "Number of all available stations in the netCDF file"
    print len(root_grps)
    print '----------------'
    
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
"""

###################### plot_nc #########################################

def plot_nc():
    
    """
    """
    
    pwd_str = os.getcwd()
    
    os.chdir(input['plot_nc'])
    
    os.system('psbasemap -Rd -JK180/9i -B45g30 -K > output.ps')
    os.system('pscoast -Rd -JK180/9i -B45g30:."World-wide Ray Path Coverage": -Dc -A1000 -Glightgray -Wthinnest -t20 -O -K >> output.ps')
    
    if input['plot_ray'] == 'Y':
        print '\n================================================='
        print 'Plot the ray path between each event-station pair'
        print '================================================='
        
        os.system('psxy ./evsta_plot.txt -JK180/9i -Rd -O -t100 >> output.ps')
    if input['plot_sta'] == 'Y':
        print '\n================================================'
        print 'Plot all available stations based on the options'
        print '================================================'
        
        os.system('psxy ./sta_plot.txt -JK180/9i -Rd -Si0.14c -Gblue -O >> output.ps')
    if input['plot_ev'] == 'Y':
        print '\n=============================================='
        print 'Plot all available events based on the options'
        print '=============================================='
        
        os.system('psxy ./ev_plot.txt -JK180/9i -Rd -Sa0.28c -Gred -O >> output.ps')
    if input['plot_all'] == 'Y':
        print '\n================================================'
        print 'Plot:'
        print 'all available events based on the options'
        print 'all available stations based on the options'
        print 'the ray path between each event-station pair'
        print '================================================'
        
        os.system('psxy ./evsta_plot.txt -JK180/9i -Rd -O -K -t100 >> output.ps')
        os.system('psxy ./sta_plot.txt -JK180/9i -Rd -Si0.14c -Gblue -O -K >> output.ps')
        os.system('psxy ./ev_plot.txt -JK180/9i -Rd -Sa0.28c -Gred -O >> output.ps')
        
    os.system('ps2raster output.ps -A -P -Tf')
    
    os.system('mv output.ps plot.ps')
    os.system('mv output.pdf plot.pdf')
    
    os.system('xdg-open plot.pdf')
    
    os.chdir(pwd_str)
    
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
    
    t1_pro = time.time()
    status = managing_node()
    t_pro = time.time() - t1_pro
    
    print'\n\n------------'
    print "Total Time:"
    print t_pro
    print'------------\n'
    
    # pass the return of main to the command line.
    sys.exit(status)
