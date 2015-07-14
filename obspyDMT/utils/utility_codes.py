#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  utility_codes.py
#   Purpose:   Collection of helping scripts, utility codes
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from datetime import datetime, timedelta
import fnmatch
import glob
import numpy as np
try:
    from obspy.geodetics import locations2degrees
except Exception, e:
    from obspy.core.util import locations2degrees
from obspy.core import read
from obspy.signal.util import nextpow2
try:
    from obspy.taup import getTravelTimes
except Exception, e:
    from obspy.taup.taup import getTravelTimes
import os
import pickle
import smtplib
import sys
import time

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### header_printer ##################################


def header_printer():
    """
    Printing the welcome message
    :return:
    """
    os.system('clear')
    print 80*'-'
    print '\t\tobspyDMT (ObsPy Data Management Tool)\n'
    print '\tAutomatic tool for Downloading, Processing and Management'
    print '\t\t\tof Large Seismological Datasets\n'
    print ':copyright:'
    print 'The ObsPy Development Team (devs@obspy.org)\n'
    print 'Developed by Kasra Hosseini'
    print 'email: hosseini@geophysik.uni-muenchen.de\n'
    print ':license:'
    print 'GNU General Public License, Version 3'
    print '(http://www.gnu.org/licenses/gpl-3.0-standalone.html)'
    print 80*'-' + '\n'

# ##################### goodbye_printer ##################################


def goodbye_printer(input_dics, t1_pro):
    print "\n\n=================================================="
    print "obspyDMT main program has finished !\n"
    try:
        size = getFolderSize(input_dics['datapath'])
        size /= (1024.**2)
        print "Info:"
        print "* The storing directory contains %s MB of data." \
            % "{:.3f}".format(float(size))
        print input_dics['datapath']
        print "* Total time of execution: %s (h:m:s)" \
              % str(timedelta(seconds=round(float(time.time() - t1_pro))))
        print "==================================================\n\n"
    except Exception as e:
        print 'ERROR: %s' % e
        pass
# ##################### read_list_stas ##################################


def read_list_stas(add_list, normal_mode_syn, specfem3D):
    """
    read a list of stations instead of checking the availability.
    :param add_list:
    :param normal_mode_syn:
    :param specfem3D:
    :return:
    """

    print '\n----------------------------------------'
    print 'INFO:'
    print 'Format of the station list:'
    print 'sta  net  loc  cha  lat  lon  ele  depth'
    print '----------------------------------------\n\n'

    list_stas_fio = open(add_list)
    list_stas = list_stas_fio.readlines()
    for sta in range(len(list_stas)):
        if not list_stas[sta].startswith('\n'):
            list_stas[sta] = list_stas[sta].split()

    final_list = []
    if specfem3D == 'Y':
        for sta in range(len(list_stas)):
            for chan in ['MXE', 'MXN', 'MXZ']:
                final_list.append(['SY', list_stas[sta][0],
                                   'S3', chan,
                                   list_stas[sta][4],
                                   list_stas[sta][5],
                                   list_stas[sta][6]])
    elif normal_mode_syn == 'Y':
        for sta in range(len(list_stas)):
            for chan in ['LXE', 'LXN', 'LXZ']:
                final_list.append(['SY', list_stas[sta][0],
                                   'S1', chan,
                                   list_stas[sta][4],
                                   list_stas[sta][5],
                                   list_stas[sta][6]])
    else:
        for sta in range(len(list_stas)):
            # for chan in ['BH1', 'BH2', 'BHE', 'BHN', 'BHZ']:
            final_list.append([list_stas[sta][1], list_stas[sta][0],
                               list_stas[sta][2], list_stas[sta][3],
                               list_stas[sta][4], list_stas[sta][5],
                               list_stas[sta][6], list_stas[sta][7]])
    return final_list

# ##################### read_event_dic ##############################


def read_event_dic(address):
    """
    Reads event dictionary ("info" folder)
    :param address:
    :return:
    """
    if not os.path.isabs(address):
        address = os.path.abspath(address)

    if os.path.basename(address) == 'info':
        target_add = [address]
    elif locate(address, 'info'):
        target_add = locate(address, 'info')
    else:
        print 'Error: There is no "info" directory in %s' % address
        target_add = None

    if len(target_add) > 1:
        sys.exit('length of directories to read the event info: %s'
                 % len(target_add))

    event_dic = False
    for t_add in target_add:
        if os.path.isfile(os.path.join(t_add, 'event.pkl')):
            ev_file_fio = open(os.path.join(t_add, 'event.pkl'), 'r')
            event_dic = pickle.load(ev_file_fio)
        else:
            sys.exit('event.pkl can not be found in: %s' % t_add)
    return event_dic

# ##################### read_station_event ##############################


def read_station_event(address):
    """
    Reads the station_event file ("info" folder)
    :param address:
    :return:
    """
    if not os.path.isabs(address):
        address = os.path.abspath(address)

    if os.path.basename(address) == 'info':
        target_add = [address]
    elif locate(address, 'info'):
        target_add = locate(address, 'info')
    else:
        print 'Error: There is no "info" directory in %s' % address
        target_add = None

    sta_ev = []
    for t_add in target_add:
        if os.path.isfile(os.path.join(t_add, 'station_event')):
            sta_file_open = open(os.path.join(t_add, 'station_event'), 'r')
        else:
            print '====================================='
            print 'station_event could not be found'
            print 'Start Creating the station_event file'
            print '====================================='
            create_station_event(address=t_add)
            sta_file_open = open(os.path.join(t_add, 'station_event'), 'r')
        sta_file = sta_file_open.readlines()
        sta_ev_tmp = []
        for s_file in sta_file:
            sta_ev_tmp.append(s_file.split(','))
        sta_ev.append(sta_ev_tmp)
    return sta_ev

# ##################### create_station_event ############################


def create_station_event(address):
    """
    Creates the station_event file ("info" folder)
    :param address:
    :return:
    """

    event_address = os.path.dirname(address)
    if os.path.isdir(os.path.join(event_address, 'BH_RAW')):
        sta_address = os.path.join(event_address, 'BH_RAW')
    elif os.path.isdir(os.path.join(event_address, 'BH')):
        sta_address = os.path.join(event_address, 'BH')
    else:
        print 'ERROR: There is no reference (BH_RAW or BH) ' \
              'to create station_event file!'
        sys.exit()

    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))
    ls_stas.sort()

    print '%s stations found in %s' % (len(ls_stas), sta_address)

    for i in range(len(ls_stas)):
        print i,
        sta_file_open = open(os.path.join(address, 'station_event'), 'a')
        try:
            sta = read(ls_stas[i])[0]
        except Exception as e:
            print 'WARNING: NOT readable: %s\n%s' % (ls_stas[i], e)
            sta = None
        try:
            sta_stats = sta.stats
            sta_info = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,iris,\n' \
                       % (sta_stats.network,
                          sta_stats.station,
                          sta_stats.location,
                          sta_stats.channel,
                          sta_stats.sac.stla,
                          sta_stats.sac.stlo,
                          sta_stats.sac.stel,
                          sta_stats.sac.stdp,
                          os.path.basename(event_address),
                          sta_stats.sac.evla,
                          sta_stats.sac.evlo,
                          sta_stats.sac.evdp,
                          sta_stats.sac.mag)
        except Exception as e:
            print '\nWARNING: Can not read all the required information ' \
                  'from the headers, some of them are presumed!'
            print e
            sta_info = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,iris,\n' \
                       % (sta_stats.network,
                          sta_stats.station,
                          sta_stats.location,
                          sta_stats.channel,
                          -12345.0, -12345.0, -12345.0, -12345.0,
                          os.path.basename(event_address),
                          -12345.0, -12345.0, -12345.0, -12345.0)
        sta_file_open.writelines(sta_info)
        sta_file_open.close()
    print 'station_event file is created in %s' % os.path.join(address,
                                                               'station_event')

# ##################### locate ##########################################


def locate(root='.', target='info'):
    """
    Locates a subdirectory within a directory.
    :param root:
    :param target:
    :return:
    """

    matches = []
    for root, dirnames, filenames in os.walk(root):
        for dirname in fnmatch.filter(dirnames, target):
            matches.append(os.path.join(root, dirname))

    return matches

# ##################### calculate_time_phase ##################################


def calculate_time_phase(event, sta):
    """
    calculate arrival time of the requested phase to use in retrieving
    waveforms.
    :param event:
    :param sta:
    :return:
    """

    ev_lat = event['latitude']
    ev_lon = event['longitude']
    ev_dp = abs(float(event['depth']))
    sta_lat = float(sta[4])
    sta_lon = float(sta[5])
    delta = locations2degrees(ev_lat, ev_lon, sta_lat, sta_lon)
    tt = getTravelTimes(delta, ev_dp)
    phase_list = ['P', 'Pdiff', 'PKIKP']

    time_ph = 0
    flag = False
    for ph in phase_list:
        for i in range(len(tt)):
            if tt[i]['phase_name'] == ph:
                flag = True
                time_ph = tt[i]['time']
                break
            else:
                continue
        if flag:
            print 'Phase: %s' % ph
            break
    t_start = event['t1'] + time_ph
    t_end = event['t2'] + time_ph
    return t_start, t_end

# ##################### getFolderSize ###################################


def getFolderSize(folder):
    """
    Returns the size of a folder in bytes.
    :param folder:
    :return:
    """
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

# ##################### send_email ######################################


def send_email(input_dics):
    """
    Sending email to the specified "email" address
    :param input_dics:
    :return:
    """
    print '\n*********************************************'
    print 'Sending email to the following email-address:'
    print input_dics['email']
    print '*********************************************'
    t2_str = datetime.now()

    fromaddr = 'obspyDMT'
    toaddrs = input_dics['email']
    msg = "request finished at:\n%s" % t2_str

    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(fromaddr, toaddrs, msg)
    except Exception as err:
        print '\nNo e-mail sent, as:\n>>:\t', err
        # err_info = traceback.extract_tb(sys.exc_info()[2])

# ##################### check_par_jobs ######################################


def check_par_jobs(jobs, sleep_time=1):
    """
    check whether all the parallel jobs are finished or not
    :param jobs:
    :param sleep_time:
    :return:
    """
    pp_flag = True
    while pp_flag:
        for proc in jobs:
            if proc.is_alive():
                time.sleep(sleep_time)
                pp_flag = True
                break
            else:
                pp_flag = False
    if not pp_flag:
        print '\n\nAll %s processes are finished...\n' % len(jobs)

# ##################### spectrum_calc ##################################


def spectrum_calc(tr):
    """
    Simple code to calculate the spectrum of a trace
    :param tr: obspy Trace
    :return:
    freqs, spec_tr
    which are frequencies and spectrum of the trace

    To plot the spectrum:

    import matplotlib.pyplot as plt
    plt.loglog(freqs, spec_tr)
    """

    nfft = nextpow2(tr.stats.npts)
    freqs = np.fft.rfftfreq(nfft) / tr.stats.delta

    spec_tr = np.abs(np.fft.rfft(tr.data, n=nfft))

    return freqs, spec_tr
