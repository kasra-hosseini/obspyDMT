#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  utility_codes.py
#   Purpose:   collection of helping scripts and utility codes
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from datetime import datetime, timedelta
import fnmatch
import glob
import numpy as np
from obspy.core import read
try:
    from obspy.clients.fdsn import URL_MAPPINGS
except:
    from obspy.fdsn.header import URL_MAPPINGS
try:
    from obspy.geodetics import locations2degrees
except:
    from obspy.core.util import locations2degrees
try:
    from obspy.signal.util import next_pow_2 as nextpow2
except:
    from obspy.signal.util import nextpow2

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
    clear the screen and print the welcome message.
    :return:
    """
    os.system('clear')
    print(80*'-')
    print('\t\t   obspyDMT (obspy Data Management Tool)\n')
    print('\tPython Toolbox for Retrieving, Processing and Management of')
    print('\t\t\tLarge Seismological Datasets\n')
    print(':copyright:')
    print('The ObsPy Development Team (devs@obspy.org)\n')
    print('Developed by Kasra Hosseini')
    print('email: kasra.hosseinizad@earth.ox.ac.uk\n')
    print(':license:')
    print('GNU General Public License, Version 3')
    print('(http://www.gnu.org/licenses/gpl-3.0-standalone.html)')
    print(80*'-' + '\n')

# ##################### goodbye_printer ##################################


def goodbye_printer(input_dics, t1_pro):
    """
    print the goodbye message which contains information about duration of
    the run and size of the directory.
    :param input_dics:
    :param t1_pro:
    :return:
    """
    print("\n\n==================================================")
    print("obspyDMT main program has finished!\n")
    try:
        #size = getFolderSize(input_dics['datapath'])
        #size /= (1024.**2)
        #print("Info:")
        #print("* The directory contains %s MB of data." \
        #      % "{:.3f}".format(float(size)))
        print(input_dics['datapath'])
        print("* Total time of execution: %s (h:m:s)" \
              % str(timedelta(seconds=round(float(time.time() - t1_pro)))))
        print("==================================================\n\n")
    except Exception as error:
        print('ERROR: %s' % error)
        pass

# ##################### print_data_sources ##################################


def print_data_sources():
    """
    Function to print available data providers
    :return:
    """
    print("\n--------------------------")
    print("list of all shortcut names")
    print("--------------------------\n")
    for key in sorted(URL_MAPPINGS.keys()):
        print("{0:<7} {1}".format(key,  URL_MAPPINGS[key]))
    print("ARCLINK")
    print("\n============================================================")
    print("This is the list of all shortcut names which can be used for")
    print("--data_source option.")
    print("However, FDSN base URLs can be entered directly as well.")
    print("============================================================")
    sys.exit()

# ##################### print_event_catalogs ##################################


def print_event_catalogs():
    """
    Function to print available event catalogs
    :return:
    """
    print("\n------------------------")
    print("supported event catalogs")
    print("------------------------\n")
    for ev_cat in ['LOCAL', 'NEIC_USGS', 'GCMT_COMBO', 'IRIS', 'NCEDC',
                   'USGS', 'INGV', 'ISC']:
        print(ev_cat)

    print("\n============================================================")
    print("This is the list of all available event catalogs that can be")
    print("used for --event_catalog option.")
    print("============================================================")
    sys.exit()

# ##################### print_syngine_models ##################################


def print_syngine_models():
    """
    Function to print available syngine models
    :return:
    """
    print("\n------------------------")
    print("Available syngine models")
    print("------------------------\n")

    from obspy.clients.syngine import Client as Client_syngine
    client_syngine = Client_syngine()
    avail_syngine_models = client_syngine.get_available_models()

    for count_mod, avail_mod in enumerate(avail_syngine_models.keys()):
        print('%s. %s' % (count_mod+1, avail_mod))
    print('\n')
    for count_mod, avail_mod in enumerate(avail_syngine_models.keys()):
        print("------------------------")
        print('%s. %s' % (count_mod+1, avail_mod))
        for inf in avail_syngine_models[avail_mod].keys():
            print("%s: %s" % (inf, avail_syngine_models[avail_mod][inf]))

    print("\n============================================================")
    print("This is the list of all available syngine models that can be")
    print("used for --syngine_bg_model option.")
    print("============================================================")
    sys.exit()

# ##################### create_folders_files ############################


def create_folders_files(event, eventpath, input_dics):
    """
    create required directories and files for one event
    :param event:
    :param eventpath:
    :param input_dics:
    :return:
    """
    try:
        for t_dir in ['raw', 'resp', 'info']:
            tar_dir = os.path.join(eventpath, event['event_id'], t_dir)
            if not os.path.isdir(tar_dir):
                os.makedirs(tar_dir)

        inp_file = open(os.path.join(eventpath, event['event_id'],
                                     'info', 'input_dics.pkl'), 'wb')
        pickle.dump(input_dics, inp_file, protocol=2)
        inp_file.close()

        event_file = open(os.path.join(eventpath, event['event_id'],
		          'info', 'event.pkl'), 'wb')
        pickle.dump(event, event_file, protocol=2)
        event_file.close()

        report = open(os.path.join(eventpath, event['event_id'],
                                   'info', 'report_st'), 'at+')
        report.close()

        exception_file = open(os.path.join(eventpath, event['event_id'],
                                           'info', 'exception'), 'at+')
        exception_file.writelines('\n' + event['event_id'] + '\n')
        exception_file.close()

        syn_file = open(os.path.join(eventpath, event['event_id'],
                                     'info', 'station_event'), 'at+')
        syn_file.close()

    except Exception as error:
        print('ERROR: %s' % error)
        pass

# ##################### read_list_stas ##################################


def read_list_stas(add_list, normal_mode_syn, specfem3D):
    """
    read a list of stations instead of checking the availability
    :param add_list:
    :param normal_mode_syn:
    :param specfem3D:
    :return:
    """
    print('\n---------------------------------------------')
    print('INFO:')
    print('Format of the station list:')
    print('net,sta,loc,cha,lat,lon,ele,depth,data_source')
    print('---------------------------------------------\n\n')

    list_stas_fio = open(add_list, 'rt')
    list_stas = list_stas_fio.readlines()
    for sta in range(len(list_stas)):
        if not list_stas[sta].startswith('\n'):
            list_stas[sta] = [x.strip() for x in list_stas[sta].split(',')]

    final_list = []
    if specfem3D:
        for sta in range(len(list_stas)):
            for chan in ['MXE', 'MXN', 'MXZ']:
                st_id = 'SY_%s_S3_%s' % (list_stas[sta][1], chan)
                final_list.append(['SY', list_stas[sta][1],
                                   'S3', chan,
                                   list_stas[sta][4],
                                   list_stas[sta][5],
                                   list_stas[sta][6],
                                   list_stas[sta][7],
                                   'IRIS', st_id])
    elif normal_mode_syn:
        for sta in range(len(list_stas)):
            for chan in ['LXE', 'LXN', 'LXZ']:
                st_id = 'SY_%s_S1_%s' % (list_stas[sta][1], chan)
                final_list.append(['SY', list_stas[sta][1],
                                   'S1', chan,
                                   list_stas[sta][4],
                                   list_stas[sta][5],
                                   list_stas[sta][6],
                                   list_stas[sta][7],
                                   'IRIS', st_id])
    else:
        for sta in range(len(list_stas)):
            st_id = '%s_%s_%s_%s' % (list_stas[sta][0],
                                     list_stas[sta][1],
                                     list_stas[sta][2],
                                     list_stas[sta][3])
            final_list.append([list_stas[sta][0], list_stas[sta][1],
                               list_stas[sta][2], list_stas[sta][3],
                               list_stas[sta][4], list_stas[sta][5],
                               list_stas[sta][6], list_stas[sta][7],
                               list_stas[sta][8], st_id])
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
        print('Error: There is no "info" directory in %s' % address)
        target_add = None

    if len(target_add) > 1:
        print("[ERROR] there are more than one directory to " \
              "read the event info:")
        for tar_add in target_add:
            print(tar_add)
        sys.exit('\nonly one directory should be specified to proceed!')

    event_dic = False
    for t_add in target_add:
        if os.path.isfile(os.path.join(t_add, 'event.pkl')):
            ev_file_fio = open(os.path.join(t_add, 'event.pkl'), 'rb')
            event_dic = pickle.load(ev_file_fio)
        else:
            sys.exit('[ERROR] event.pkl can not be found in: %s' % t_add)
    return event_dic

# ##################### read_station_event ##############################


def read_station_event(address):
    """
    reads the station_event file ("info" folder)
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
        print('[ERROR] There is no "info" directory in:\n%s' % address)
        target_add = None

    sta_ev = []
    for t_add in target_add:
        if os.path.isfile(os.path.join(t_add, 'station_event')):
            sta_file_open = open(os.path.join(t_add, 'station_event'), 'rt')
        else:
            print('=====================================')
            print('station_event could not be found')
            print('start creating the station_event file')
            print('=====================================')
            create_station_event(address=t_add)
            sta_file_open = open(os.path.join(t_add, 'station_event'), 'rt')
        sta_file = sta_file_open.readlines()
        sta_ev_tmp = []
        for s_file in sta_file:
            sta_ev_tmp.append(s_file.split(','))
        sta_ev.append(sta_ev_tmp)
    return sta_ev

# ##################### create_station_event ############################


def create_station_event(address):
    """
    create the station_event file ("info" folder)
    :param address:
    :return:
    """
    event_address = os.path.dirname(address)
    if os.path.isdir(os.path.join(event_address, 'raw')):
        sta_address = os.path.join(event_address, 'raw')
    elif os.path.isdir(os.path.join(event_address, 'processed')):
        sta_address = os.path.join(event_address, 'processed')
    else:
        sys.exit('[ERROR] There is no reference (raw or processed) '
                 'to create station_event file!')

    ls_stas = glob.glob(os.path.join(sta_address, '*'))
    ls_stas.sort()

    print('%s stations found in %s' % (len(ls_stas), sta_address))

    for i in range(len(ls_stas)):
        print(i),
        sta_file_open = open(os.path.join(address, 'station_event'), 'at')
        try:
            sta = read(ls_stas[i])[0]
        except Exception as e:
            print('[WARNING] NOT readable: %s\n%s' % (ls_stas[i], e))
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
        except Exception as error:
            print('\n[WARNING] Can not read all the required information ' \
                  'from the headers, some of them are presumed!')
            print(error)
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
    print('station_event file is created in %s' \
          % os.path.join(address, 'station_event'))

# ##################### locate ##########################################


def locate(root='.', target='info', num_matches=-1):
    """
    locates a subdirectory within a directory
    :param root:
    :param target:
    :param num_matches:
    :return:
    """
    matches = []
    for root, dirnames, filenames in os.walk(root):
        for dirname in fnmatch.filter(dirnames, target):
            matches.append(os.path.join(root, dirname))
        if num_matches > 0:
            if len(matches) >= num_matches:
                break

    return matches

# ##################### convert_to_sac ########################################


def convert_to_sac(tr, save_path, sta_ev_arr):
    """
    convert tr format to SAC and try to fill in some header information
    :param tr:
    :param save_path:
    :param sta_ev_arr:
    :return:
    """
    tr.write(save_path, format='SAC')
    tr = read(save_path)[0]

    # start filling in some header information
    try:
        tr.stats.sac.stla = float(sta_ev_arr[4])
    except:
        pass
    try:
        tr.stats.sac.stlo = float(sta_ev_arr[5])
    except:
        pass
    try:
        tr.stats.sac.stel = float(sta_ev_arr[6])
    except:
        pass
    try:
        tr.stats.sac.stdp = float(sta_ev_arr[7])
    except:
        pass
    try:
        tr.stats.sac.evla = float(sta_ev_arr[10])
    except:
        pass
    try:
        tr.stats.sac.evlo = float(sta_ev_arr[11])
    except:
        pass
    try:
        tr.stats.sac.evdp = float(sta_ev_arr[12])
    except:
        pass
    try:
        tr.stats.sac.mag = float(sta_ev_arr[13])
    except:
        pass
    try:
        tr.stats.sac.cmpaz = float(sta_ev_arr[14])
    except:
        pass
    try:
        tr.stats.sac.cmpinc = float(sta_ev_arr[15])
    except:
        pass
    return tr

# ##################### calculate_time_phase ##################################


def calculate_time_phase(event, sta, bg_model='iasp91'):
    """
    calculate arrival time of the requested phase
    :param event:
    :param sta:
    :param bg_model:
    :return:
    """
    phase_list = ['P', 'Pdiff', 'PKIKP']

    time_ph = 0
    ev_lat = event['latitude']
    ev_lon = event['longitude']
    evdp = abs(float(event['depth']))
    sta_lat = float(sta[4])
    sta_lon = float(sta[5])
    dist = locations2degrees(ev_lat, ev_lon, sta_lat, sta_lon)

    try:
        from obspy.taup import tau
        tau_bg = tau.TauPyModel(model=bg_model)
    except:
        tau_bg = False

    if not tau_bg:
        try:
            try:
                from obspy.taup import getTravelTimes
            except:
                from obspy.taup.taup import getTravelTimes
            tt = getTravelTimes(dist, evdp)
            flag = False
            for ph in phase_list:
                for i in range(len(tt)):
                    if tt[i]['phase_name'] == ph:
                        flag = True
                        time_ph = tt[i]['time']
                        break
                    else:
                        continue
            if not flag:
                time_ph = 0
        except:
            time_ph = 0
    else:
        try:
            for ph in phase_list:
                tt = tau_bg.get_travel_times(evdp, dist,
                                             phase_list=[ph])[0].time
                if not tt:
                    time_ph = 0
                    continue
                else:
                    time_ph = tt
                    break
        except:
            time_ph = 0

    t_start = event['t1'] + time_ph
    t_end = event['t2'] + time_ph
    return t_start, t_end

# ##################### plot_filter_station ###############################


def plot_filter_station(input_dics, sta_ev):
    """
    check whether the station can pass the criteria
    :param input_dics:
    :param sta_ev:
    :return:
    """
    if not fnmatch.fnmatch(sta_ev[0], input_dics['net']):
        return False
    if not fnmatch.fnmatch(sta_ev[1], input_dics['sta']):
        return False
    if not fnmatch.fnmatch(sta_ev[2], input_dics['loc']):
        return False
    if not fnmatch.fnmatch(sta_ev[3], input_dics['cha']):
        return False
    if isinstance(input_dics['mlat_rbb'], float):
        if not float(sta_ev[4]) <= input_dics['Mlat_rbb']:
            return False
        if not float(sta_ev[4]) >= input_dics['mlat_rbb']:
            return False
        if not float(sta_ev[5]) <= input_dics['Mlon_rbb']:
            return False
        if not float(sta_ev[5]) >= input_dics['mlon_rbb']:
            return False
    return True

# ##################### getFolderSize ###################################


def getFolderSize(folder):
    """
    returns the size of a folder in bytes
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
    send email to the specified "email" address
    :param input_dics:
    :return:
    """
    t2_str = datetime.now()

    fromaddr = 'obspyDMT'
    toaddrs = input_dics['email']
    msg = "request finished at:\n%s" % t2_str
    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(fromaddr, toaddrs, msg)
        print('\n*********************************************')
        print('Sending email to the following email-address:')
        print(input_dics['email'])
        print('*********************************************')
    except Exception as error:
        print('\n**************************')
        print('Email was not sent, ERROR:')
        print(error)
        print('**************************')
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
        print('\n\n================================')
        print('All %s processes are finished...' % len(jobs))
        print('================================')

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

# ------------------ geocen_calc ---------------------------


def geocen_calc(geog_lat):
    """
    Calculate geocentric latitudes
    :param geog_lat:
    :return:
    """
    fac = 0.993305621334896

    colat = 90.0 - geog_lat
    if abs(colat) < 1.0e-5:
        colat = np.sign(colat)*1.0e-5
    # arg = colat*rpd
    colat *= np.pi/180.
    colat_sin = np.sin(colat)
    if colat_sin < 1.0e-30:
        colat_sin = 1.0e-30
    # geocen=pi2-atan(fac*cos(arg)/(max(1.0e-30,sin(arg))))
    geocen_colat = np.pi/2. - np.arctan(fac*np.cos(colat)/colat_sin)
    geocen_colat = geocen_colat*180./np.pi
    geocen_lat = 90.0 - geocen_colat

    return geocen_lat

# ----------------------------------------------------------------------------
# process_unit:
# if len(st) > 1:
#     st.merge(method=1, fill_value=0, interpolation_samples=0)
#     gap_fio = open(os.path.join(target_path, 'info',
#                                 'waveform_gap.txt'), 'a+')
#     gap_msg = '%s.%s.%s.%s\t%s\n' % (st[0].stats.network,
#                                      st[0].stats.station,
#                                      st[0].stats.location,
#                                      st[0].stats.channel,
#                                      'instrument_correction')
#     gap_fio.writelines(gap_msg)
#     gap_fio.close()
