#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MAGNITUDE for event check!
# Station selection based on SAC...change it to the station_event file! (generate it for all station_events in psdata)

#-------------------------------------------------------------------
#   Filename:  NDLB_find.py
#   Purpose:   NDLB_find main program 
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
import fnmatch
import time
import glob
from optparse import OptionParser

import numpy as np

from obspy.core import read, UTCDateTime
from obspy.taup.taup import getTravelTimes, locations2degrees

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

########################################################################
############################# Main Program #############################
########################################################################

def NDLB_find(**kwargs):
    
    global input
    
    # ------------------Parsing command-line options--------------------
    (options, args, parser) = command_parse()
    
    # ------------------Read INPUT file (Parameters)--------------------
    read_input_command(parser, **kwargs)
    
    # ------------------find_event--------------------------------------
    find_event()
    
    # ------------------select_sta--------------------------------------
    select_sta()
    

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
    
    avail_ph = \
        "P ,  P'P'ab ,  P'P'bc ,  P'P'df ,  PKKPab ,  PKKPbc ,  PKKPdf , PKKSab ," + '\n' + \
        "PKKSbc ,  PKKSdf ,  PKPab ,  PKPbc ,  PKPdf ,  PKPdiff ,  PKSab ,  PKSbc ," + '\n' + \
        "PKSdf ,  PKiKP ,  PP ,  PS ,  PcP ,  PcS ,  Pdiff ,  Pn ,  PnPn ,  PnS ," + '\n' + \
        "S ,  S'S'ac ,  S'S'df ,  SKKPab ,  SKKPbc ,  SKKPdf ,  SKKSac ,  SKKSdf ," + '\n' + \
        "SKPab ,  SKPbc ,  SKPdf ,  SKSac ,  SKSdf ,  SKiKP ,  SP ,  SPg ,  SPn ," + '\n' + \
        "SS ,  ScP ,  ScS ,  Sdiff ,  Sn ,  SnSn ,  pP ,  pPKPab ,  pPKPbc ," + '\n' + \
        "pPKPdf ,  pPKPdiff ,  pPKiKP ,  pPdiff ,  pPn ,  pS ,  pSKSac ,  pSKSdf ," + '\n' + \
        "pSdiff ,  sP ,  sPKPab ,  sPKPbc ,  sPKPdf ,  sPKPdiff ,  sPKiKP ,  sPb ," + '\n' + \
        "sPdiff ,  sPg ,  sPn ,  sS ,  sSKSac ,  sSKSdf ,  sSdiff ,  sSn" + '\n'
    
    helpmsg = "The address of the event folder."
    parser.add_option("--address", action="store",
                      dest="address", help=helpmsg)
    
    helpmsg = "Start time. Default: 10 days ago."
    parser.add_option("--min_date", action="store",
                      dest="min_date", help=helpmsg)

    parser.add_option("--max_date", action="store",
                      dest="max_date", help="End time. Default: now.")
    
    helpmsg = "Minimum magnitude. Default: 3.0"
    parser.add_option("--min_mag", action="store",
                      dest="min_mag", help=helpmsg)
    
    helpmsg = "Maximum magnitude. Default: 9.9"
    parser.add_option("--max_mag", action="store",
                      dest="max_mag", help=helpmsg)

    helpmsg = "message"
    parser.add_option("--min_depth", action="store",
                      dest="min_depth", help=helpmsg)
    
    helpmsg = "message"
    parser.add_option("--max_depth", action="store",
                      dest="max_depth", help=helpmsg)
    
    helpmsg = "Geographical restriction: minlat/minlon/maxlat/maxlon"
    parser.add_option("--event_rect", action="store",
                      dest="event_rect", help=helpmsg)
    
    helpmsg = "Save the info of all the stations in the folder."
    parser.add_option("--all_sta", action="store_true",
                      dest="all_sta", help=helpmsg)
    
    helpmsg = "Identity code restriction, syntax: dis/vel/acc.sta.loc.cha"
    parser.add_option("--identity", action="store", dest="identity",
                        help=helpmsg)
    
    helpmsg = "The file name in which the info of selected stations " + \
                "will be stored."
    parser.add_option("-n", "--file_name", action="store", dest="file",
                        help=helpmsg)
    
    helpmsg = "The background model to compute arrival times. " + \
                         "(iasp91 or ak135)"
    parser.add_option("--back_model", action="store", dest="model",
                        help=helpmsg)
    
    helpmsg = 'The phase(s) that you are looking for.' \
                        + ' format: Phase1-Phase2-...' + '\n' + \
                        'Available phases are as follow:' + '\n' + avail_ph
    parser.add_option("--phase", action="store", dest="phase",
                        help=helpmsg)
    
    helpmsg = 'The frequency to which all seismograms will be ' + \
                         'downsampled:'
    parser.add_option("--freq", action="store", dest="freq",
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
                'min_date': UTCDateTime.utcnow() - 60 * 60 * 24 * 10 * 1,
                'max_date': UTCDateTime.utcnow(),
                'min_mag': 3.0, 'max_mag': 9.9,
                'min_depth': +10.0, 'max_depth': -6000.0,
                'evlatmin': -90.0, 'evlatmax': +90.0, 
                'evlonmin': -180.0, 'evlonmax': +180.0,
                'identity': '*.*.*.*',
                'file': 'Pdiff',
                'model': 'iasp91',
                'phase': 'Pdiff',
                'freq': None,
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
    
    # extract min. and max. longitude and latitude if the user has given the
    # coordinates with -r (GMT syntax)
    if options.event_rect:
        try:
            options.event_rect = options.event_rect.split('/')
            if len(options.event_rect) != 4:
                print "Erroneous rectangle given."
                sys.exit(2)
            options.evlatmin = float(options.event_rect[0])
            options.evlonmin = float(options.event_rect[1])
            options.evlatmax = float(options.event_rect[2])
            options.evlonmax = float(options.event_rect[3])           
        except:
            print "Erroneous rectangle given."
            sys.exit(2)
    
    
    input['address'] = options.address
    input['min_date'] = UTCDateTime(options.min_date)
    input['max_date'] = UTCDateTime(options.max_date)
    input['min_mag'] = float(options.min_mag)
    input['max_mag'] = float(options.max_mag)
    input['min_depth'] = float(options.min_depth)
    input['max_depth'] = float(options.max_depth)
    
    if options.event_rect:
        input['evlonmin'] = options.evlonmin
        input['evlonmax'] = options.evlonmax
        input['evlatmin'] = options.evlatmin
        input['evlatmax'] = options.evlatmax
    
    input['all_sta'] = options.all_sta
    input['identity'] = options.identity
    input['file'] = options.file
    input['model'] = options.model
    input['phase'] = options.phase.split('-')
    input['freq'] = options.freq
    if input['freq'] != None: input['freq'] = float(options.freq)

###################### find_event ######################################

def find_event():
    
    """
    Search in the event folder and find the events that meet the 
    requested parameters
    """
    
    global input
    
    quake_files = []
    quake_req = []
    quake_files_tmp = glob.glob(os.path.join(input['address']))
    
    for i in range(0, len(quake_files_tmp)):
        quake_tmp = quake_files_tmp[i].split('/')[-1]
        try:
            if float(quake_tmp.split('.')[0]) and \
                float(quake_tmp.split('.')[1]) and \
                float(quake_tmp.split('.')[2]):
                quake_files.append(quake_files_tmp[i])
        except ValueError:
            print quake_tmp
            pass
                
    for i in range(0, len(quake_files)):
        print str(i) + '/' + str(len(quake_files))
        
        (quake_d, quake_t) = read_quake(quake_files[i])
        
        if input['min_date'] <= quake_t <= input['max_date']:
            if input['evlatmin'] <= quake_d['lat'] <= input['evlatmax'] and \
                    input['evlonmin'] <= quake_d['lon'] <= input['evlonmax']:
                if input['max_depth'] <= -abs(quake_d['dp']) <= input['min_depth']:
                    quake_req.append(quake_files[i])
        
    if len(quake_req) != 0:
        quake_file_req = open(os.path.join(os.getcwd(), 'quake_req.txt'), 'w')
        for l in quake_req:
            quake_file_req.writelines(l + '\n')
        print '----------------------------------------'
        print '"quake_req.txt" is created for ' + \
                    str(len(quake_req)) + ' events in:'
        print '---------------'
        print str(os.path.join(os.getcwd(), 'quake_req.txt'))
        print '----------------------------------------'

###################### select_sta ######################################

def select_sta():
    
    """
    Select required stations
    """
    
    global input
    
    map_proj = Basemap(projection='cyl', llcrnrlat=-90,urcrnrlat=90,\
                llcrnrlon=-180,urcrnrlon=180, resolution='c')
    ev_file = open(os.path.join(os.getcwd(), 'quake_req.txt'), 'r')
    ev_add = ev_file.read().split('\n')[:-1]
    select = open(os.path.join(os.getcwd(), input['file'] + '.dat'), 'w')
    select.close()
    
    for k in range(0, len(ev_add)):
        
        '''
        select = open(os.path.join(os.getcwd(), \
                input['file'] + '-' + ev_add[k].split('/')[-1] + \
                '.dat'), 'w')
        '''
        
        (quake_d, quake_t) = read_quake(ev_add[k])
        
        list_sta = glob.glob(os.path.join(ev_add[k], 'BH', \
                                input['identity']))
        
        for i in range(0, len(list_sta)):
            
            try:
                
                st = read(list_sta[i])
                print '***************************************'
                print str(i) + '/' + str(len(list_sta)) + ' -- ' + \
                        str(k) + '/' + str(len(ev_add))
                print list_sta[i].split('/')[-1]
                
                info_sac = st[0].stats['sac']
                
                if input['all_sta'] == None:
                    
                    dist = locations2degrees(lat1 = quake_d['lat'], \
                            long1 = quake_d['lon'], lat2 = info_sac['stla'], \
                            long2 = info_sac['stlo'])
                    tt = getTravelTimes(delta=dist, depth=quake_d['dp'], \
                                            model=input['model'])
                    
                    for m in range(0, len(tt)):
                        
                        if tt[m]['phase_name'] in input['phase']:

                            try:
                                print '--------------------'
                                print list_sta[i].split('/')[-1] + ' has ' + \
                                        tt[m]['phase_name'] + ' phase'
                                
                                if input['freq'] != None:
                                    st[0].decimate(int(round(\
                                        st[0].stats['sampling_rate'])/input['freq']), \
                                        no_filter=False)
                                    
                                    if st[0].stats['sampling_rate'] != input['freq']:
                                        print list_sta[i].split('/')[-1]
                                        print st[0].stats['sampling_rate']
                                        print '------------------------------------------'
                                '''
                                np_evt = round((events[0]['datetime'] - st[0].stats['starttime'])*st[0].stats['sampling_rate'])
                                np_pha = np_evt + round(tt[m]['time']*st[0].stats['sampling_rate'])
                                
                                select = open(Address_events + '/' + events[l]['event_id'] + '/IRIS/info/' + name_select, 'a')
                                '''
                                if tt[m]['phase_name'] != 'Pdiff':
                                    lat_1 = str(quake_d['lat'])
                                    lon_1 = str(quake_d['lon'])
                                    lat_2 = str(info_sac['stla'])
                                    lon_2 = str(info_sac['stlo'])
                                elif tt[m]['phase_name'] == 'Pdiff':
                                    dist_limit = 97.0
                                    num_gcp = 1000
                                    gcp = map_proj.gcpoints(quake_d['lon'], \
                                            quake_d['lat'], info_sac['stlo'], \
                                            info_sac['stla'], num_gcp)

                                    if dist >= dist_limit:
                                        diff_dist = dist - dist_limit
                                                        
                                        req_gcp = diff_dist*(float(num_gcp)/dist)
                                        req_gcp = round(req_gcp)/2

                                        mid_p = len(gcp[0])/2
                                        #before = int(mid_p - req_gcp)
                                        #after = int(mid_p + req_gcp)
                                        before = mid_p - int(2.0 * len(gcp[0])/dist)
                                        after = mid_p + int(2.0 * len(gcp[0])/dist)
                                        
                                        x_p, y_p = gcp
                                        lat_1 = y_p[before]
                                        lat_2 = y_p[after]
                                        lon_1 = x_p[before]
                                        lon_2 = x_p[after]
                                        
                                ph_info = tt[m]['phase_name'] + ',' + \
                                    str(dist) + ',' + \
                                    str(tt[m]['time']) + ',' + \
                                    str(st[0].stats['sampling_rate']) + ',' + \
                                    st[0].stats['network'] + ',' + \
                                    st[0].stats['station'] + \
                                    ',' + st[0].stats['location'] + ',' + \
                                    st[0].stats['channel'] + ',' + \
                                    str(info_sac['stla']) + ',' + \
                                    str(info_sac['stlo']) + ',' + \
                                    str(info_sac['stdp']) + ',' + \
                                    str(info_sac['stel']) + ',' + \
                                    str(quake_d['lat']) + ',' + \
                                    str(quake_d['lon']) + ',' + \
                                    str(quake_d['dp']) + ',' + \
                                    '-----' + ',' + \
                                    str(lat_1) + ',' + \
                                    str(lon_1) + ',' + \
                                    str(lat_2) + ',' + \
                                    str(lon_2) + ',' + \
                                    '-----' + ',' + \
                                    ev_add[k].split('/')[-1] + ',' + \
                                    list_sta[i] + '\n'
                                    
                                #select = open(os.path.join(os.getcwd(), \
                                #    input['file'] + '-' + \
                                #    ev_add[k].split('/')[-1] + '.dat'), 'a')
                                select = open(os.path.join(os.getcwd(), \
                                    input['file'] + '.dat'), 'a')
                                select.writelines(ph_info)
                                select.close()
                            
                            except Exception, e:
                                print e
                
                elif input['all_sta'] != None:
                    
                    ph_info = 'NA' + ',' + 'NA' + ',' + \
                    'NA' + ',' + \
                    str(st[0].stats['sampling_rate']) + ',' + \
                    st[0].stats['network'] + ',' + st[0].stats['station'] + \
                    ',' + st[0].stats['location'] + ',' + \
                    st[0].stats['channel'] + ',' + \
                    str(info_sac['stla']) + ',' + \
                    str(info_sac['stlo']) + ',' + \
                    str(info_sac['stdp']) + ',' + \
                    str(info_sac['stel']) + ',' + \
                    str(quake_d['lat']) + ',' + str(quake_d['lon']) + ',' + \
                    str(quake_d['dp']) + ',' + \
                    ev_add[k].split('/')[-1] + ',' + \
                    list_sta[i] + '\n'
                    
                    '''
                    select = open(os.path.join(os.getcwd(), \
                        input['file'] + '-' + \
                        ev_add[k].split('/')[-1] + '.dat'), 'a')
                    '''
                    select = open(os.path.join(os.getcwd(), \
                        input['file'] + '.dat'), 'a')
                    select.writelines(ph_info)
                    select.close()
            
            except Exception, e:
                print e
                pass

###################### read_quake ######################################

def read_quake(quake_fi):

    quake_file = open(os.path.join(quake_fi, 'info', \
                            'quake'), 'r')
    quake_info = quake_file.readlines()
    
    info_tmp = []
    for j in range(0, len(quake_info)):
        for k in quake_info[j].split():
            try:
                info_tmp.append(float(k))
            except ValueError:
                print k
                pass
    
    quake_d = {'year': int(info_tmp[0]), 'julday': int(info_tmp[1]), \
                'hour': int(info_tmp[2]), 'minute': int(info_tmp[3]), \
                'second': int(info_tmp[4]), 'lat': float(info_tmp[6]), \
                'lon': float(info_tmp[7]), 'dp': float(info_tmp[8])}
    quake_t = UTCDateTime(year=quake_d['year'], julday=quake_d['julday'], \
                hour=quake_d['hour'], minute=quake_d['minute'], \
                second=quake_d['second'])
    
    return quake_d, quake_t
    
########################################################################
########################################################################
########################################################################

if __name__ == "__main__":
    
    t1_pro = time.time()
    status = NDLB_find()
    
    t_pro = time.time() - t1_pro
    print "Total time: %f seconds" % (t_pro)
    print '----------------------------------------'
    
    # pass the return of main to the command line.
    sys.exit(status)
