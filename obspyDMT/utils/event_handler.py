#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  event_handler.py
#   Purpose:   handling events in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from __future__ import print_function
from collections import OrderedDict
import copy
from datetime import datetime, timedelta
import glob
import numpy as np
from obspy.core.event import Catalog
try:
    from obspy.core.event import readEvents
except Exception as e:
    from obspy import read_events as readEvents
from obspy.core import UTCDateTime
try:
    from obspy.geodetics import locations2degrees
except Exception as e:
    from obspy.core.util import locations2degrees
try:
    from obspy.clients.fdsn import Client as Client_fdsn
except Exception as e:
    from obspy.fdsn import Client as Client_fdsn
import os
import pickle
import sys
import time
try:
    from urllib2 import urlopen 
except ImportError:
    from urllib.request import urlopen
try:
    from urllib import urlencode as urlencodeparse
except ImportError:
    from urllib.parse import urlencode as urlencodeparse
from .input_handler import input_logger
from .utility_codes import locate

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### get_time_window ######################################


def get_time_window(input_dics, request):
    """
    generating a list of requests for both event_based and continuous requests.
    :param input_dics:
    :param request:
    :return:
    """
    t_event_1 = time.time()

    # request can be 'event_based' or 'continuous'
    # events list contains all the information for requested time-window
    # Although we do not have any events in continuous requests,
    # it is still called as events.
    events = []
    events_qml = Catalog(events=[])
    try:
        if not input_dics['read_catalog']:
            events_local = read_info(input_dics)
            if input_dics['event_catalog'].lower() == 'local':
                if events_local == 'no_local':
                    print("[WARNING] no local event was found!")
                    if request == 'event_based':
                        print("[WARNING] use IRIS catalog instead!")
                        input_dics['event_catalog'] = 'IRIS'
                else:
                    events = copy.deepcopy(events_local)
        else:
            events_QML, ev_already_list = \
                read_local_events(input_dics['read_catalog'])
            if not ev_already_list:
                # no matter if list was passed or requested, sort catalogue,
                # plot events and proceed
                events_QML = sort_catalogue(events_QML)
                events = qml_to_event_list(events_QML)
            else:
                events = copy.deepcopy(events_QML)
                events_QML = False
            for i in range(len(events)):
                events[i]['t1'] = events[i]['datetime'] - input_dics['preset']
                events[i]['t2'] = events[i]['datetime'] + input_dics['offset']

        if events == 'no_local' or events == []:
            if request.lower() == 'event_based':
                events, events_qml = event_info(input_dics)
            elif request.lower() == 'continuous':
                events, events_qml = continuous_info(input_dics)

        if not input_dics['continuous']:
            remove_indx = []
            if input_dics['event_catalog'].lower() != 'local':
                if events_local != 'no_local':
                    for nei in range(len(events)):
                        for oei in range(len(events_local)):
                            if (events[nei]['event_id'] ==
                                    events_local[oei]['event_id']):
                                remove_indx.append(nei)
                                break
                    if len(remove_indx) > 0:
                        remove_indx.sort(reverse=True)
                        for ri in remove_indx:
                            del events[ri]

                    for oei in range(len(events_local)):
                        events.append(events_local[oei])

    except Exception as error:
        print('WARNING: %s' % error)
        return []

    if len(events) == 0:
        return []

    events2, row_format, header = output_shell_event(events, request)

    print('Number of events/intervals: %s' % len(events))
    print('Time for retrieving and saving the event info: %s' \
          % str(timedelta(seconds=round(float(time.time() - t_event_1)))))

    if input_dics['primary_mode'] in ['event_based', 'continuous',
                                      'meta_data']:
        # formatting output / check if directory exists
        eventpath = os.path.join(input_dics['datapath'])
        write_cat_logger(input_dics, eventpath, events, events_qml,
                         events2, row_format, header)
    return events

# ##################### read_info #####################################


def read_info(input_dics):
    """
    read already created events (for both event_based and continuous requests)
    :param input_dics:
    :return:
    """
    evs_info = locate(input_dics['datapath'], 'EVENTS-INFO', num_matches=1)
    if len(evs_info) == 0:
        return "no_local"
    if len(evs_info) > 1:
        print("[WARNING] Found two directories that have EVENTS-INFO. Continue with:")
        print(evs_info[0])
        print('\n')

    ev_info = evs_info[0]

    if not os.path.isfile(os.path.join(ev_info, 'event_list_pickle')):
        print("[WARNING] no 'event_list_pickle' was found at %s, "
              "try to re-generate it..." % ev_info)
        info_dirs = locate(input_dics['datapath'], 'info')
        event_list_regen = []
        for info_d in info_dirs:
            if os.path.isfile(os.path.join(info_d, 'event.pkl')):
                try:
                    ev_pkl_tmp = pickle.load(open(os.path.join(info_d, 'event.pkl'), 'r'))
                    # to check whether t1 and t2 variables are there:
                    test_t1 = ev_pkl_tmp['t1']
                    test_t2 = ev_pkl_tmp['t2']
                    event_list_regen.append(ev_pkl_tmp)
                except Exception as e:
                    print("ERROR: %s" % e)
        if len(event_list_regen) > 0:
            print("[WARNING] a new 'event_list_pickle' was generated with %s events." % len(event_list_regen))
            fio = open(os.path.join(ev_info, 'event_list_pickle'), 'w')
            pickle.dump(event_list_regen, fio, protocol=2)
        else:
            print("[WARNING] a new 'event_list_pickle' could NOT be generated.")
            return "no_local"

    fio = open(os.path.join(ev_info, 'event_list_pickle'), 'rb')
    events = pickle.load(fio)
    if input_dics['event_catalog'].lower() == 'local':
        print("\n=========================================================")
        print("use the local files:")
        print(os.path.join(ev_info, 'event_list_pickle'))
        print("=========================================================\n")
    return events

# ##################### event_info #####################################


def event_info(input_dics):
    """
    get event(s) info for event_based request
    :param input_dics:
    :return:
    """
    try:
        evlatmin = input_dics['evlatmin']
        evlatmax = input_dics['evlatmax']
        evlonmin = input_dics['evlonmin']
        evlonmax = input_dics['evlonmax']

        evlat = input_dics['evlat']
        evlon = input_dics['evlon']
        evradmin = input_dics['evradmin']
        evradmax = input_dics['evradmax']

        event_switch = 'fdsn'
        event_url = input_dics['event_catalog']
        if input_dics['read_catalog']:
            event_switch = 'local'
        event_fdsn_cat = None

        if event_url.lower() == 'gcmt_combo':
            event_switch = 'gcmt_combo'
        if event_url.lower() == 'neic_usgs':
            event_switch = 'neic_usgs'
        if event_url.lower() == 'isc':
            event_switch = 'isc_cat'

        print('\nEvent(s) are based on:\t%s' % input_dics['event_catalog'])

        if event_switch == 'fdsn':
            client_fdsn = Client_fdsn(base_url=event_url)
            events_QML = client_fdsn.get_events(
                minlatitude=evlatmin,
                maxlatitude=evlatmax,
                minlongitude=evlonmin,
                maxlongitude=evlonmax,
                latitude=evlat,
                longitude=evlon,
                minradius=evradmin,
                maxradius=evradmax,
                mindepth=input_dics['min_depth'],
                maxdepth=input_dics['max_depth'],
                starttime=input_dics['min_date'],
                endtime=input_dics['max_date'],
                minmagnitude=input_dics['min_mag'],
                maxmagnitude=input_dics['max_mag'],
                orderby='time-asc',
                catalog=event_fdsn_cat,
                magnitudetype=input_dics['mag_type'],
                includeallorigins=None,
                includeallmagnitudes=None,
                includearrivals=None,
                eventid=None,
                limit=None,
                offset=None,
                contributor=None,
                updatedafter=None)

        elif event_switch == 'gcmt_combo':
            events_QML = \
                gcmt_catalog(input_dics['min_date'],
                             input_dics['max_date'],
                             evlatmin, evlatmax, evlonmin, evlonmax,
                             evlat, evlon, evradmin, evradmax,
                             input_dics['min_depth'],
                             input_dics['max_depth'],
                             input_dics['min_mag'],
                             input_dics['max_mag'])

        elif event_switch == 'neic_usgs':
            events_QML = \
                neic_catalog_urllib(input_dics['min_date'],
                                    input_dics['max_date'],
                                    evlatmin, evlatmax, evlonmin, evlonmax,
                                    evlat, evlon, evradmin, evradmax,
                                    input_dics['min_depth'],
                                    input_dics['max_depth'],
                                    input_dics['min_mag'],
                                    input_dics['max_mag'])

        elif event_switch == 'isc_cat':
            events_QML = \
                isc_catalog(bot_lat=evlatmin, top_lat=evlatmax,
                            left_lon=evlonmin, right_lon=evlonmax,
                            ctr_lat=evlat, ctr_lon=evlon,
                            radius=evradmax,
                            start_time=input_dics['min_date'],
                            end_time=input_dics['max_date'],
                            min_dep=input_dics['min_depth'],
                            max_dep=input_dics['max_depth'],
                            min_mag=input_dics['min_mag'],
                            max_mag=input_dics['max_mag'],
                            mag_type=input_dics['mag_type'],
                            req_mag_agcy='Any',
                            rev_comp=input_dics['isc_catalog'])

        elif event_switch == 'local':
            events_QML = readEvents(input_dics['read_catalog'])

        else:
            sys.exit('[ERROR] %s is not supported'
                     % input_dics['event_catalog'])

        for i in range(len(events_QML)):
            if not hasattr(events_QML.events[i], 'preferred_mag'):
                events_QML.events[i].preferred_mag = \
                    events_QML.events[i].magnitudes[0].mag
                events_QML.events[i].preferred_mag_type = \
                    events_QML.events[i].magnitudes[0].magnitude_type
                events_QML.events[i].preferred_author = 'None'
            else:
                if not hasattr(events_QML.events[i], 'preferred_author'):
                    if events_QML.events[i].preferred_magnitude().creation_info:
                        events_QML.events[i].preferred_author = \
                            events_QML.events[i].preferred_magnitude().creation_info.author
                    elif events_QML.events[i].magnitudes[0].creation_info:
                        events_QML.events[i].preferred_author = \
                            events_QML.events[i].magnitudes[0].creation_info.author
        # no matter if list was passed or requested, sort catalogue,
        # plot events and proceed
        events_QML = sort_catalogue(events_QML)
        events = qml_to_event_list(events_QML)

    except Exception as error:
        print(60*'-')
        print('[WARNING] %s' % error)
        print(60*'-')
        events = []
        events_QML = []

    for i in range(len(events)):
        events[i]['t1'] = events[i]['datetime'] - input_dics['preset']
        events[i]['t2'] = events[i]['datetime'] + input_dics['offset']

    return events, events_QML

# ##################### read_local_events #####################################


def read_local_events(catalog_add):
    """
    read local events
    :param catalog_add:
    :return:
    """
    try:
        events_QML = readEvents(catalog_add)
        return events_QML, False
    except Exception as error:
        try:
            ev_csv = np.loadtxt(catalog_add, delimiter=',',
                                comments='#', ndmin=2, dtype='object')
            events = []
            for i in range(np.shape(ev_csv)[0]):
                events.append(OrderedDict(
                    [('number', i+1),
                     ('latitude', eval(ev_csv[i][3])),
                     ('longitude', eval(ev_csv[i][4])),
                     ('depth', eval(ev_csv[i][5])),
                     ('datetime', UTCDateTime(ev_csv[i][2])),
                     ('magnitude', eval(ev_csv[i][6])),
                     ('magnitude_type', ev_csv[i][7]),
                     ('author', ev_csv[i][8]),
                     ('event_id', ev_csv[i][1]),
                     ('origin_id', -12345),
                     ('focal_mechanism', [eval(ev_csv[i][10]),
                                          eval(ev_csv[i][11]),
                                          eval(ev_csv[i][12]),
                                          eval(ev_csv[i][13]),
                                          eval(ev_csv[i][14]),
                                          eval(ev_csv[i][15])
                                          ]),
                     ('source_duration', [ev_csv[i][16], eval(ev_csv[i][17])]),
                     ('flynn_region', ev_csv[i][9])]))
            return events, True
        except Exception as error:
            print(60*'-')
            print('[WARNING] %s' % error)
            print(60*'-')
            return Catalog(events=[]), False

# ##################### qml_to_event_list #####################################


def qml_to_event_list(events_QML):
    """
    convert QML to event list
    :param events_QML:
    :return:
    """
    events = []
    for i in range(len(events_QML)):
        try:
            event_time = events_QML.events[i].preferred_origin().time or \
                         events_QML.events[i].origins[0].time
            event_time_month = '%02i' % int(event_time.month)
            event_time_day = '%02i' % int(event_time.day)
            event_time_hour = '%02i' % int(event_time.hour)
            event_time_minute = '%02i' % int(event_time.minute)
            event_time_second = '%02i' % int(event_time.second)

            if not hasattr(events_QML.events[i], 'preferred_mag'):
                events_QML.events[i].preferred_mag = \
                    events_QML.events[i].magnitudes[0].mag
                events_QML.events[i].preferred_mag_type = \
                    events_QML.events[i].magnitudes[0].magnitude_type
                events_QML.events[i].preferred_author = 'None'
            else:
                if not hasattr(events_QML.events[i], 'preferred_author'):
                    if events_QML.events[i].preferred_magnitude().creation_info:
                        events_QML.events[i].preferred_author = \
                            events_QML.events[i].preferred_magnitude().creation_info.author
                    elif events_QML.events[i].magnitudes[0].creation_info:
                        events_QML.events[i].preferred_author = \
                            events_QML.events[i].magnitudes[0].creation_info.author
        except Exception as error:
            print(error)
            continue
        try:
            if not events_QML.events[i].focal_mechanisms == []:
                if events_QML.events[i].preferred_focal_mechanism()['moment_tensor']['tensor']:
                    focal_mechanism = [
                        events_QML.events[i].preferred_focal_mechanism()
                        ['moment_tensor']['tensor']['m_rr'],
                        events_QML.events[i].preferred_focal_mechanism()
                        ['moment_tensor']['tensor']['m_tt'],
                        events_QML.events[i].preferred_focal_mechanism()
                        ['moment_tensor']['tensor']['m_pp'],
                        events_QML.events[i].preferred_focal_mechanism()
                        ['moment_tensor']['tensor']['m_rt'],
                        events_QML.events[i].preferred_focal_mechanism()
                        ['moment_tensor']['tensor']['m_rp'],
                        events_QML.events[i].preferred_focal_mechanism()
                        ['moment_tensor']['tensor']['m_tp']]
                else:
                    found_foc_mech = False
                    for foc_mech_qml in events_QML.events[i].focal_mechanisms:
                        if foc_mech_qml['moment_tensor']['tensor']:
                            focal_mechanism = [
                                foc_mech_qml['moment_tensor']['tensor']['m_rr'],
                                foc_mech_qml['moment_tensor']['tensor']['m_tt'],
                                foc_mech_qml['moment_tensor']['tensor']['m_pp'],
                                foc_mech_qml['moment_tensor']['tensor']['m_rt'],
                                foc_mech_qml['moment_tensor']['tensor']['m_rp'],
                                foc_mech_qml['moment_tensor']['tensor']['m_tp']
                            ]
                            found_foc_mech = True
                            break
                    if not found_foc_mech:
                        focal_mechanism = False
            else:
                focal_mechanism = False
        except AttributeError:
            print("[WARNING] focal_mechanism does not exist for " \
                  "event: %s -- set to False" % (i+1))
            focal_mechanism = False
        except TypeError:
            focal_mechanism = False
        except Exception as error:
            print(error)
            focal_mechanism = False

        try:
            if not events_QML.events[i].focal_mechanisms == []:
                source_duration = [
                    events_QML.events[i].preferred_focal_mechanism()
                    ['moment_tensor']['source_time_function']['type'],
                    events_QML.events[i].preferred_focal_mechanism()
                    ['moment_tensor']['source_time_function']
                    ['duration']]
                if not source_duration[1]:
                    source_duration = mag_duration(
                        mag=events_QML.events[i].preferred_mag)
            else:
                source_duration = mag_duration(
                    mag=events_QML.events[i].preferred_mag)
        except AttributeError:
            print("[WARNING] source duration does not exist for " \
                  "event: %s -- set to False" % (i+1))
            source_duration = False
        except TypeError:
            source_duration = False
        except Exception as error:
            print(error)
            source_duration = False

        try:
            events.append(OrderedDict(
                [('number', i+1),
                 ('latitude',
                  events_QML.events[i].preferred_origin().latitude or
                  events_QML.events[i].origins[0].latitude),
                 ('longitude',
                  events_QML.events[i].preferred_origin().longitude or
                  events_QML.events[i].origins[0].longitude),
                 ('depth',
                  events_QML.events[i].preferred_origin().depth/1000. or
                  events_QML.events[i].origins[0].depth/1000.),
                 ('datetime', event_time),
                 ('magnitude',
                  events_QML.events[i].preferred_mag),
                 ('magnitude_type',
                  events_QML.events[i].preferred_mag_type),
                 ('author',
                  events_QML.events[i].preferred_author),
                 ('event_id', str(event_time.year) +
                  event_time_month + event_time_day + '_' +
                  event_time_hour + event_time_minute +
                  event_time_second + '.a'),
                 ('origin_id', events_QML.events[i].preferred_origin_id or
                  events_QML.events[i].origins[0].resource_id.resource_id),
                 ('focal_mechanism', focal_mechanism),
                 ('source_duration', source_duration),
                 ('flynn_region', 'NAN'),
                 ]))
        except Exception as error:
            print(error)
            continue
    return events

# ##################### continuous_info #####################################


def continuous_info(input_dics):
    """
    get 'event(s)' info for continuous request
    :param input_dics:
    :return:
    """
    print('start identifying the intervals...', end='')
    m_date = UTCDateTime(input_dics['min_date'])
    M_date = UTCDateTime(input_dics['max_date'])
    t_cont = M_date - m_date

    if t_cont < 0:
        sys.exit("\n\n[ERROR] max_date is lower than min_date!")

    events = []
    if t_cont > input_dics['interval']:
        num_div = int(t_cont/input_dics['interval'])
        # residual time is: (has not been used here)
        # t_res = t_cont - num_div*input_dics['interval']
        for i in range(1, num_div+1):
            cont_dir_name = (len(str(num_div)) - len(str(i)))*'0' + str(i)
            events.append(OrderedDict(
                [('number', i),
                 ('latitude', -12345),
                 ('longitude', -12345),
                 ('depth', -12345),
                 ('datetime', m_date + (i-1)*input_dics['interval']),
                 ('magnitude', -12345),
                 ('magnitude_type', 'NAN'),
                 ('author', 'NAN'),
                 ('event_id', 'continuous' + cont_dir_name),
                 ('origin_id', -12345),
                 ('focal_mechanism', False),
                 ('source_duration', False),
                 ('flynn_region', 'NAN'),
                 ('t1', m_date + (i-1)*input_dics['interval'] -
                  input_dics['preset']),
                 ('t2', m_date + i*input_dics['interval'] +
                  input_dics['offset']),
                 ]))

        final_time = m_date + num_div*input_dics['interval'] + \
            input_dics['offset']

        if not M_date == final_time:
            cont_dir_name = str(num_div+1)
            events.append(OrderedDict(
                [('number', num_div+1),
                 ('latitude', -12345),
                 ('longitude', -12345),
                 ('depth', -12345),
                 ('datetime', m_date + num_div*input_dics['interval']),
                 ('magnitude', -12345),
                 ('magnitude_type', 'NAN'),
                 ('author', 'NAN'),
                 ('event_id', 'continuous' + cont_dir_name),
                 ('origin_id', -12345),
                 ('focal_mechanism', False),
                 ('source_duration', False),
                 ('flynn_region', 'NAN'),
                 ('t1', m_date + num_div*input_dics['interval'] -
                  input_dics['preset']),
                 ('t2', M_date + input_dics['offset']),
                 ]))
    else:
        events.append(OrderedDict(
            [('number', 1),
             ('latitude', -12345),
             ('longitude', -12345),
             ('depth', -12345),
             ('datetime', m_date),
             ('magnitude', -12345),
             ('magnitude_type', 'NAN'),
             ('author', 'NAN'),
             ('event_id', 'continuous1'),
             ('origin_id', -12345),
             ('focal_mechanism', False),
             ('source_duration', False),
             ('flynn_region', 'NAN'),
             ('t1', m_date - input_dics['preset']),
             ('t2', M_date + input_dics['offset']),
             ]))
    print('DONE')
    events_QML = Catalog(events=[])
    return events, events_QML

# ##################### neic_catalog_urllib ############################


def neic_catalog_urllib(t_start, t_end, min_latitude,
                        max_latitude, min_longitude,
                        max_longitude, latitude, longitude,
                        radius_min, radius_max, d_min, d_max, mag_min, mag_max,
                        link_neic="http://earthquake.usgs.gov/fdsnws/event/1/query.quakeml?"):
    """
    Function for downloading data from NEIC
    :param t_start:
    :param t_end:
    :param min_latitude:
    :param max_latitude:
    :param min_longitude:
    :param max_longitude:
    :param latitude:
    :param longitude:
    :param radius_min:
    :param radius_max:
    :param d_min:
    :param d_max:
    :param mag_min:
    :param mag_max:
    :param link_neic:
    :return:
    """
    tic = time.clock()

    dir_name = '%s_temp_xml_files' % int(UTCDateTime.now().timestamp)
    os.mkdir(dir_name)

    getVars = {'minmagnitude': str(mag_min),
               'maxmagnitude': str(mag_max),
               'mindepth': str(d_min),
               'maxdepth': str(d_max),
               }

    if None in [latitude, longitude, radius_min, radius_max]:
        if not None in [min_latitude, max_latitude, min_longitude, max_longitude]:
            getVars['minlongitude'] = str(min_longitude)
            getVars['maxlongitude'] = str(max_longitude)
            getVars['minlatitude'] = str(min_latitude)
            getVars['maxlatitude'] = str(max_latitude)
    else:
        getVars['latitude'] = str(latitude)
        getVars['longitude'] = str(longitude)
        getVars['maxradiuskm'] = str(float(radius_max)*111.194)

    getVars['includeallorigins'] = 'true'
    getVars['includeallmagnitudes'] = 'true'
    getVars['producttype'] = 'moment-tensor'

    m_date = UTCDateTime(t_start)
    M_date = UTCDateTime(t_end)
    dur_event = M_date - m_date
    interval = 30.*24.*60.*60.

    num_div = int(dur_event/interval)
    print('#Divisions: %s' % num_div)
    remotefile = False
    if not num_div < 1:
        for i in range(1, num_div+1):
            try:
                print(i, end=',')
                sys.stdout.flush()
                t_start_split = m_date + (i-1)*interval
                t_end_split = m_date + i*interval
                getVars['starttime'] = str(t_start_split)
                getVars['endtime'] = str(t_end_split)

                url_values = urlencodeparse(getVars)
                remotefile = link_neic + url_values
                page = urlopen(remotefile)
                page_content = page.read()
                page_content = page_content.decode("utf-8")

                if 'quakeml' in page_content:
                    with open(os.path.join(dir_name,
                                           'temp_neic_xml_%05i.xml' % i), 'w') \
                            as fid:
                        fid.write(page_content)
                    fid.close()
                else:
                    continue
                page.close()
            except Exception as error:
                print("\nWARNING: %s -- %s\n" % (error, remotefile))
    elif num_div == 0:
        try:
            t_start_split = m_date
            t_end_split = M_date
            getVars['starttime'] = str(t_start_split)
            getVars['endtime'] = str(t_end_split)

            url_values = urlencodeparse(getVars)
            remotefile = link_neic + url_values
            page = urlopen(remotefile)
            page_content = page.read()
            page_content = page_content.decode("utf-8")

            if 'quakeml' in page_content:
                with open(os.path.join(dir_name,
                                       'temp_neic_xml_%05i.xml' % 0), 'w') \
                        as fid:
                    fid.write(page_content)
                fid.close()
            page.close()
        except Exception as error:
            print("\nWARNING: %s -- %s\n" % (error, remotefile))

    try:
        final_time = m_date + num_div*interval
        if (not M_date == final_time) and (not int(dur_event/interval) == 0):
            t_start_split = final_time
            t_end_split = M_date
            getVars['starttime'] = str(t_start_split)
            getVars['endtime'] = str(t_end_split)

            url_values = urlencodeparse(getVars)
            remotefile = link_neic + url_values
            page = urlopen(remotefile)
            page_content = page.read()
            page_content = page_content.decode("utf-8")

            if 'quakeml' in page_content:
                with open(os.path.join(dir_name,
                                       'temp_neic_xml_%05i.xml' % (num_div+1)),
                          'w') as fid:
                    fid.write(page_content)
                fid.close()
            page.close()
    except Exception as error:
        print("\nWARNING: %s\n" % error)

    xml_add = glob.glob(os.path.join(dir_name, 'temp_neic_xml_*.xml'))
    xml_add.sort()
    cat = Catalog()
    print('\nAssembling %s xml files...' % len(xml_add))
    counter = 1
    for x_add in xml_add:
        print(counter, end=',')
        sys.stdout.flush()
        counter += 1
        try:
            cat.extend(readEvents(x_add, format='QuakeML'))
            os.remove(x_add)
        except Exception as error:
            print('[WARNING] %s' % error)
            os.remove(x_add)

    print("\ncleaning up the temporary folder.")
    os.rmdir(dir_name)
    toc = time.clock()
    print('\n%s sec to retrieve the event info form NEIC.' % (toc-tic))
    return cat

# ##################### gcmt_catalog ############################


def gcmt_catalog(t_start, t_end, min_latitude, max_latitude, min_longitude,
                 max_longitude, latitude, longitude, radius_min, radius_max,
                 d_min, d_max, mag_min, mag_max,
                 link_gcmt='http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog'):
    """
    Function for downloading data from GCMT
    :param t_start:
    :param t_end:
    :param min_latitude:
    :param max_latitude:
    :param min_longitude:
    :param max_longitude:
    :param latitude:
    :param longitude:
    :param radius_min:
    :param radius_max:
    :param d_min:
    :param d_max:
    :param mag_min:
    :param mag_max:
    :param link_gcmt:
    :return:
    """
    # for the time record
    tic = datetime.now()

    try:
        import obspyDMT
        dmt_path = obspyDMT.__path__[0]
    except Exception as error:
        print("WARNING: %s" % error)
        dmt_path = '.'
    gcmt_cat_path = os.path.join(dmt_path, 'gcmt_catalog')
    if not os.path.exists(gcmt_cat_path):
        os.mkdir(gcmt_cat_path)
        os.mkdir(os.path.join(gcmt_cat_path, 'NEW_MONTHLY'))
        os.mkdir(os.path.join(gcmt_cat_path, 'COMBO'))

    # creating a time list
    t_list = []
    delta_t = int(UTCDateTime(t_end)-UTCDateTime(t_start)+1)/86400

    yymm = []
    for i in range(delta_t + 1):
        t_list.append((UTCDateTime(t_start)+i*60*60*24).strftime('%Y/%m/%d'))
        yy_tmp, mm_tmp, dd_tmp = t_list[i].split('/')
        yymm.append('%s%s' % (yy_tmp, mm_tmp))
    yymmset = set(yymm)
    yymmls = list(yymmset)
    yymmls.sort()

    # starting to search for all events in the time window given by the user:
    cat = Catalog()
    yy_ret = []
    mm_ret = []
    remotefile_add = False

    for i in range(len(yymmls)):
        try:
            yy = yymmls[i][0:4]
            mm = yymmls[i][4:6]
            if int(yy) < 2006:
                month_year = ['jan', 'feb', 'mar', 'apr', 'may', 'june',
                              'july', 'aug', 'sept', 'oct', 'nov', 'dec']
            else:
                month_year = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
            if int(yy) >= 2005:
                new_monthly = 'NEW_MONTHLY'
                file_to_open = os.path.join(gcmt_cat_path, new_monthly,
                                            '%s%s.ndk'
                                            % (month_year[int(mm)-1], yy[-2:]))
                remotefile_add = '%s/%s/%s/%s%s.ndk' \
                                 % (link_gcmt, new_monthly, yy,
                                    month_year[int(mm)-1], yy[-2:])
            else:
                new_monthly = 'COMBO'
                if yy in yy_ret:
                    continue
                file_to_open = os.path.join(gcmt_cat_path, new_monthly,
                                            '%s.qml' % yy)
            if not os.path.exists(file_to_open) and not new_monthly == 'COMBO':
                print('Reading the data from GCMT webpage: %s' % yymmls[i])
                remotefile = urlopen(remotefile_add)
                remotefile_read = remotefile.readlines()
                search_fio = open(file_to_open, 'w')
                search_fio.writelines(remotefile_read)
                search_fio.close()
            print('Reading the data from local gcmt_catalog: %s' % yymmls[i])
            cat.extend(readEvents(file_to_open))
            yy_ret.append(yy)
            mm_ret.append(mm)
        except Exception as error:
            print("ERROR: %s" % error)

    print('Done reading the data from GCMT webpage.')
    toc = datetime.now()
    print('%s sec to retrieve the event info form GCMT.' % (toc-tic))

    filt1 = 'time >= %s' % t_start
    filt2 = 'time <= %s' % t_end
    cat = cat.filter(filt1, filt2)

    filt1 = 'magnitude >= %s' % mag_min
    filt2 = 'magnitude <= %s' % mag_max
    cat = cat.filter(filt1, filt2)

    filt1 = 'depth >= %s' % (float(d_min)*1000.)
    filt2 = 'depth <= %s' % (float(d_max)*1000.)
    cat = cat.filter(filt1, filt2)

    if None not in [min_latitude, max_latitude, min_longitude, max_longitude]:
        filt1 = 'latitude >= %s' % min_latitude
        filt2 = 'latitude <= %s' % max_latitude
        cat = cat.filter(filt1, filt2)

        filt1 = 'longitude >= %s' % min_longitude
        filt2 = 'longitude <= %s' % max_longitude
        cat = cat.filter(filt1, filt2)

    # final filtering for the remaining requests
    if None not in [latitude, longitude, radius_min, radius_max]:
        index_rm = []
        for i in range(len(cat)):
            e_lat = cat.events[i].preferred_origin().latitude or \
                    cat.events[i].origins[0].latitude
            e_lon = cat.events[i].preferred_origin().longitude or \
                    cat.events[i].origins[0].longitude
            dist = locations2degrees(latitude, longitude, e_lat, e_lon)
            if not radius_min <= dist <= radius_max:
                index_rm.append(i)
        index_rm.sort()
        index_rm.reverse()
        for i in range(len(index_rm)):
            del cat[index_rm[i]]

    return cat

# ##################### isc_catalog ####################################


def isc_catalog(bot_lat=-90, top_lat=90,
                left_lon=-180, right_lon=180,
                ctr_lat=0, ctr_lon=0, radius=180,
                start_time=UTCDateTime() - 30*24*3600,
                end_time=UTCDateTime(),
                min_dep=-10, max_dep=1000, min_mag=0, max_mag=10,
                mag_type='MW', req_mag_agcy='Any',
                rev_comp='REVIEWED'):

    search_domain = 'rectangular'
    if None in [ctr_lat, ctr_lon, radius]:
        if None in [bot_lat, top_lat, left_lon, right_lon]:
            left_lon = '-180'
            right_lon = '180'
            bot_lat = '-90'
            top_lat = '90'
            search_domain = 'rectangular'
    else:
        ctr_lat = str(ctr_lat)
        ctr_lon = str(ctr_lon)
        radius = str(radius)
        search_domain = 'circular'

    if not mag_type:
        mag_type = 'MW'
    else:
        mag_type = mag_type.upper()

    if req_mag_agcy.lower() == 'any':
        req_mag_agcy = ''

    start_time = UTCDateTime(start_time)
    end_time = UTCDateTime(end_time)

    base_url = isc_url_builder(search_domain=search_domain,
                               bot_lat=bot_lat, top_lat=top_lat,
                               left_lon=left_lon, right_lon=right_lon,
                               ctr_lat=ctr_lat, ctr_lon=ctr_lon,
                               radius=radius,
                               start_time=start_time,
                               end_time=end_time,
                               min_dep=min_dep, max_dep=max_dep,
                               min_mag=min_mag, max_mag=max_mag,
                               mag_type=mag_type,
                               req_mag_agcy=req_mag_agcy,
                               rev_comp=rev_comp)

    print("\nURL:\n%s\n" % base_url)

    try_url = 1
    isc_events = Catalog(events=[]) 
    while try_url < 6:
        print("---> Send event request (Try: %s)" % try_url)
        try:
            isc_req = urlopen(base_url)
            isc_contents = isc_req.read()
            isc_events = readEvents(isc_contents)
            try_url = 100
        except Exception as e:
            print("requested content from ISC:\n%s" % e)
        try_url += 1

    remove_index = []
    for i in range(len(isc_events)):
        found_mag_type = False
        for j in range(len(isc_events.events[i].magnitudes)):
            if mag_type in \
                    isc_events.events[i].magnitudes[j].magnitude_type.upper():
                isc_events.events[i].preferred_mag = \
                    isc_events.events[i].magnitudes[j].mag
                isc_events.events[i].preferred_mag_type = \
                    isc_events.events[i].magnitudes[j].magnitude_type
                isc_events.events[i].preferred_author = \
                    isc_events.events[i].magnitudes[j].creation_info.author
                if (min_mag <= isc_events.events[i].preferred_mag <= max_mag):
                    found_mag_type = True
                break
        if not found_mag_type:
            remove_index.append(i)

    if len(remove_index) > 0:
        remove_index.sort(reverse=True)
        for ri in remove_index:
            del isc_events.events[ri]

    return isc_events

# ##################### isc_url_builder ####################################


def isc_url_builder(search_domain='rectangular', bot_lat=-90, top_lat=90,
                    left_lon=-180, right_lon=180,
                    ctr_lat=0, ctr_lon=0, radius=180,
                    start_time=UTCDateTime() - 30*24*3600,
                    end_time=UTCDateTime(),
                    min_dep=-10, max_dep=1000, min_mag=0, max_mag=10,
                    mag_type='MW', req_mag_agcy='Any',
                    rev_comp='reviewed'):
    """
    URL builder for ISC event catalog
    :param search_domain:
    :param bot_lat:
    :param top_lat:
    :param left_lon:
    :param right_lon:
    :param ctr_lat:
    :param ctr_lon:
    :param radius:
    :param start_time:
    :param end_time:
    :param min_dep:
    :param max_dep:
    :param min_mag:
    :param max_mag:
    :param mag_type:
    :param req_mag_agcy:
    :return:
    """
    base_url = 'http://www.isc.ac.uk/cgi-bin/web-db-v4?'
    base_url += 'request=%s' % rev_comp
    base_url += '&out_format=QuakeML'
    if search_domain == 'rectangular':
        base_url += '&searchshape=RECT'
        base_url += '&bot_lat=%s' % bot_lat
        base_url += '&top_lat=%s' % top_lat
        base_url += '&left_lon=%s' % left_lon
        base_url += '&right_lon=%s' % right_lon
        base_url += '&ctr_lat=&ctr_lon=&radius=&max_dist_units=deg'
        base_url += '&srn=&grn='
    elif search_domain == 'circular':
        base_url += '&searchshape=CIRC'
        base_url += '&ctr_lat=%s' % ctr_lat
        base_url += '&ctr_lon=%s' % ctr_lon
        base_url += '&radius=%s' % radius
        base_url += '&max_dist_units=deg'
        base_url += '&bot_lat=&top_lat=&left_lon=&right_lon='
        base_url += '&srn=&grn='
    base_url += '&start_year=%s' % start_time.year
    base_url += '&start_month=%s' % start_time.month
    base_url += '&start_day=%s' % start_time.day
    base_url += '&start_time=%02i%%3A%02i%%3A%02i' % (start_time.hour,
                                              start_time.minute,
                                              start_time.second)
    base_url += '&end_year=%s' % end_time.year
    base_url += '&end_month=%s' % end_time.month
    base_url += '&end_day=%s' % end_time.day
    base_url += '&end_time=%02i%%3A%02i%%3A%02i' % (end_time.hour,
                                            end_time.minute,
                                            end_time.second)
    base_url += '&min_dep=%s' % min_dep
    base_url += '&max_dep=%s' % max_dep
    base_url += '&min_mag=%s' % min_mag
    base_url += '&max_mag=%s' % max_mag
    base_url += '&req_mag_type=%s' % mag_type
    base_url += '&req_mag_agcy=%s' % req_mag_agcy
    
    base_url += '&min_def='
    base_url += '&max_def='
    base_url += '&include_links=on'
    base_url += '&include_magnitudes=on'
    base_url += '&include_headers=on'
    base_url += '&include_comments=on'
    return base_url

# ##################### output_shell_event ####################################


def output_shell_event(events, request):
    """
    output event information to the shell
    :param events:
    :param request:
    :return:
    """
    # output shell
    spaces, events2, header = event_spaces(events=events, request=request)
    header_template = ['{:<'+str(he+2)+'}' for he in spaces]
    row_format = '{}'.format(''.join(header_template))

    if len(events) == 0:
        pass

    elif len(events) <= 50:
        print('\n' + row_format.format(*header))
        print(80 * '-')
        for i in range(len(events2)):
            print((row_format.format(*events2[i].values())).rstrip())
        print(80 * '-' + '\n')

    else:
        print('\n' + row_format.format(*header))
        print(80 * '-')
        print((row_format.format(*events2[0].values())).rstrip())
        print((row_format.format(*events2[1].values())).rstrip())
        print((row_format.format(*events2[2].values())).rstrip())
        print('..')
        print((row_format.format(*events2[-3].values())).rstrip())
        print((row_format.format(*events2[-2].values())).rstrip())
        print((row_format.format(*events2[-1].values())).rstrip())
        print(80 * '-' + '\n')
    return events2, row_format, header

# ##################### event_spaces ############################


def event_spaces(events, request):
    """
    calculate spaces used for table (shell ouput)
    :param events:
    :param request:
    :return:
    """
    header = ['None']
    events2 = copy.deepcopy(events)
    for i in range(len(events2)):
        for item_ev in ['t1', 't2', 'origin_id', 'magnitude_type',
                        'focal_mechanism', 'source_duration']:
            try:
                del events2[i][item_ev]
            except Exception as error:
                print('WARNING: %s' % error)
                pass

        try:
            events2[i]['datetime'] = str(events2[i]['datetime'])[:-8]
        except Exception as error:
            print('WARNING: %s' % error)
            pass

        try:
            if request == 'continuous':
                del events2[i]['flynn_region']
                header = ['#N', 'LAT', 'LON', 'DEP', 'DATETIME', 'MAG',
                          'AUTH', 'EV_ID']
                events2[i]['latitude'] = \
                    "{:>6}".format(int(events2[i]['latitude']))
                events2[i]['longitude'] = \
                    "{:>6}".format(int(events2[i]['longitude']))
                events2[i]['depth'] = \
                    "{:>6}".format(int(events2[i]['depth']))
            else:
                header = ['#N', 'LAT', 'LON', 'DEP', 'DATETIME', 'MAG',
                          'AUTH', 'EV_ID', 'FLY']
                events2[i]['latitude'] = \
                    "{:>8.3f}".format(float(events2[i]['latitude']))
                events2[i]['longitude'] = \
                    "{:>8.3f}".format(float(events2[i]['longitude']))
                events2[i]['depth'] = \
                    int(round(float(events2[i]['depth'])))
        except Exception as error:
            print('WARNING: %s' % error)
            pass

    try:
        k, spaces = [], []
        for i in range(len(events2)):
            # k.append(events2[i].values())
            k.append(list(events2[i].values()))

        for j in range(len(k[0])):
            spaces.append(max([len(str(k[i][j])) for i in range(len(k))]))

        return spaces, events2, header
    except Exception as error:
        print('WARNING: %s' % error)
        pass

# ##################### write_cat_logger ############################


def write_cat_logger(input_dics, eventpath, events, catalog,
                     events2, row_format, header):
    """
    writing outputs from get_time_window
    :param input_dics:
    :param eventpath:
    :param events:
    :param catalog:
    :param events2:
    :param row_format:
    :param header:
    :return:
    """
    if not os.path.isdir(os.path.join(eventpath, 'EVENTS-INFO')):
        os.makedirs(os.path.join(eventpath, 'EVENTS-INFO'))
    input_logger(argus=sys.argv,
                 address=os.path.join(eventpath,
                                      'EVENTS-INFO',
                                      'logger_command.txt'),
                 inputs=input_dics)

    # output catalogue creation info as ASCII
    event_cat = \
        open(os.path.join(eventpath, 'EVENTS-INFO', 'catalog_info.txt'), 'at+')
    st_argus = 'Command line:\n-------------\n'
    for item in sys.argv:
        st_argus += item + ' '
    st_argus += '\n'
    event_cat.writelines(st_argus)
    event_cat.writelines('\n')
    event_cat.writelines('Information about the requested Events:' + '\n\n')
    event_cat.writelines('Number of Events: %s\n' % len(events))
    event_cat.writelines('min datetime: %s\n' % input_dics['min_date'])
    event_cat.writelines('max datetime: %s\n' % input_dics['max_date'])
    event_cat.writelines('min magnitude: %s\n' % input_dics['min_mag'])
    event_cat.writelines('max magnitude: %s\n' % input_dics['max_mag'])
    event_cat.writelines('min latitude: %s\n' % input_dics['evlatmin'])
    event_cat.writelines('max latitude: %s\n' % input_dics['evlatmax'])
    event_cat.writelines('min longitude: %s\n' % input_dics['evlonmin'])
    event_cat.writelines('max longitude: %s\n' % input_dics['evlonmax'])
    event_cat.writelines('min depth: %s\n' % input_dics['min_depth'])
    event_cat.writelines('max depth: %s\n' % input_dics['max_depth'])
    event_cat.writelines('\n\n=====================================\n')
    event_cat.close()

    # output catalogue as ASCII
    event_cat = \
        open(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.txt'), 'at+')
    st_argus = 'Command line:\n-------------\n'
    for item in sys.argv:
        st_argus += item + ' '
    st_argus += '\n'
    event_cat.writelines(st_argus)
    event_cat.writelines('\n')
    event_cat.writelines('#number,event_id,datetime,latitude,longitude,'
                         'depth,magnitude,magnitude_type,author,'
                         'flynn_region,mrr,mtt,mpp,mrt,mrp,mtp,'
                         'stf_func,stf_duration,t1,t2\n')
    for ev in events:
        if ev['focal_mechanism']:
            mrr = ev['focal_mechanism'][0]
            mtt = ev['focal_mechanism'][1]
            mpp = ev['focal_mechanism'][2]
            mrt = ev['focal_mechanism'][3]
            mrp = ev['focal_mechanism'][4]
            mtp = ev['focal_mechanism'][5]
        else:
            mrr = None
            mtt = None
            mpp = None
            mrt = None
            mrp = None
            mtp = None
        if ev['source_duration']:
            stf_shape = ev['source_duration'][0]
            stf_dur = ev['source_duration'][1]
        else:
            stf_shape = None
            stf_dur = None
        event_cat.writelines('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'
                             '%s,%s,%s,%s,%s,%s,%s\n'
                             % (ev['number'], ev['event_id'], ev['datetime'],
                                ev['latitude'], ev['longitude'],
                                ev['depth'], ev['magnitude'],
                                ev['magnitude_type'], ev['author'],
                                ev['flynn_region'],
                                mrr, mtt, mpp, mrt, mrp, mtp,
                                stf_shape, stf_dur,
                                ev['t1'],
                                ev['t2']))
    event_cat.writelines('\n')
    event_cat.close()

    event_file = open(os.path.join(eventpath, 'EVENTS-INFO',
                                   'event_list_pickle'), 'wb')
    pickle.dump(events, event_file, protocol=2)
    event_file.close()

    # output catalogue as ASCII but in table form
    try:
        st_argus = 'Command line:\n-------------\n'
        for item in sys.argv:
            st_argus += item + ' '
        st_argus += '\n'
        event_table = open(os.path.join(eventpath, 'EVENTS-INFO',
                                        'catalog_table.txt'), 'at+')
        event_table.writelines(st_argus)
        event_table.writelines('\n' + row_format.format(*header))
        event_table.writelines('\n' + '-'*80 + '\n')
        for i in range(len(events2)):
            event_table.writelines(
                (row_format.format(*events2[i].values())).rstrip() + '\n')
        event_table.writelines('-'*80 + '\n')
    except Exception as err:
        print('\nCouldn\'t write catalog object to ASCII file as:\n %s\n' \
              'Proceed without ..\n' % err)

    # output catalogue as QUAKEML / JSON files
    try:
        catalog.write(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.ml'),
                      format="QUAKEML")
    except Exception as err:
        print('\nCouldn\'t write catalog object to QuakeML as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err)
    try:
        catalog.write(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.zmap'),
                      format="ZMAP")
    except Exception as err:
        print('\nCouldn\'t write catalog object to JSON as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err)

# ##################### sort_catalogue ############################


def sort_catalogue(cat):
    """
    sort catalogue of retrieved events chronological.
    :param cat:
    :return:
    """
    k = [[event, event.origins[0].time] for event in cat]
    k.sort(key=lambda x: x[1], reverse=True)
    events = [event[0] for event in k]
    cat = Catalog(events=events)
    return cat

# ##################### mag_duration ###################################


def mag_duration(mag, type_curve=1):
    """
    calculate the source duration out of magnitude
    type_curve can be 1, 2, 3:
    1: 2005-2014
    2: 1976-1990
    3: 1976-2014
    :param mag:
    :param type_curve:
    :return:
    """
    if type_curve == 1:
        half_duration = 0.00272*np.exp(1.134*mag)
    elif type_curve == 2:
        half_duration = 0.00804*np.exp(1.025*mag)
    elif type_curve == 3:
        half_duration = 0.00392*np.exp(1.101*mag)
    else:
        sys.exit('%s Type for magnitude to source duration conversion is not '
                 'implemented' % type_curve)
    source_duration = round(half_duration, 3)*2
    return ['triangle', source_duration]
