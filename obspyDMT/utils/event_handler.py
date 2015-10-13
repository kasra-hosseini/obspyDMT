#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  event_handler.py
#   Purpose:   handling events in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from collections import OrderedDict
import copy
from datetime import datetime, timedelta
import glob
import numpy as np
from obspy.core.event import Catalog
try:
    from obspy.core.event import readEvents
except Exception, e:
    from obspy import read_events as readEvents
from obspy.core import UTCDateTime
try:
    from obspy.geodetics import locations2degrees
except Exception, e:
    from obspy.core.util import locations2degrees
try:
    from obspy.clients.fdsn import Client as Client_fdsn
except Exception, e:
    from obspy.fdsn import Client as Client_fdsn
import os
import pickle
import sys
import time
import urllib2

from input_handler import input_logger
from utility_codes import locate

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### get_time_window ######################################


def get_time_window(input_dics, request):
    """
    Generating a list of requests for both event_based and continuous requests.
    :param input_dics:
    :param request:
    :return:
    """
    t_event_1 = time.time()

    # request can be 'event_based' or 'continuous'
    # events contains all the information for requested time-window
    # Although we do not have any events in continuous requests,
    # it is still called as events.
    events = []
    events_qml = []
    try:
        events_local, events_qml_local = read_info(input_dics)
        if input_dics['event_catalog'].lower() == 'local':
            if events_local == 'no_local':
                input_dics['event_catalog'] = 'IRIS'
            else:
                events = copy.deepcopy(events_local)
                events_qml = copy.deepcopy(events_qml_local)
        if events == 'no_local' or events == []:
            if request.lower() == 'event_based':
                events, events_qml = event_info(input_dics)
            elif request.lower() == 'continuous':
                events, events_qml = continuous_info(input_dics)
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
                        del events_qml[ri]
                for oei in range(len(events_local)):
                    events.append(events_local[oei])
                    events_qml.append(events_qml_local[oei])

    except Exception, error:
        print 'WARNING: %s' % error
        return 0

    if len(events) < 1:
        return 0

    events2, row_format, header = output_shell_event(events, request)

    print 'Number of events/intervals: %s' % len(events)
    print 'Time for retrieving and saving the event info: %s' \
          % str(timedelta(seconds=round(float(time.time() - t_event_1))))

    # formatting output / check if directory exists
    period = '{0:s}_{1:s}'.format(
        input_dics['min_date'].split('T')[0],
        input_dics['max_date'].split('T')[0])
    eventpath = os.path.join(input_dics['datapath'], period)

    write_cat_logger(input_dics, eventpath, period, events, events_qml,
                     events2, row_format, header)
    return events

# ##################### read_info #####################################


def read_info(input_dics):
    """
    read already created events (for both event_based and continuous requests)
    :param input_dics:
    :return:
    """
    evs_info = locate(input_dics['datapath'], 'EVENTS-INFO')
    if len(evs_info) < 1:
        return "no_local", "no_local"
    if len(evs_info) > 1:
        print "WARNING: Found two directories that have EVENTS-INFO. " \
              "Continue with:"
        print evs_info[0]
        print '\n'

    ev_info = evs_info[0]

    if not os.path.isfile(os.path.join(ev_info, 'event_list_pickle')):
        return "no_local", "no_local"
    if not os.path.isfile(os.path.join(ev_info, 'catalog.ml')):
        return "no_local", "no_local"

    fio = open(os.path.join(ev_info, 'event_list_pickle'), 'r')
    events = pickle.load(fio)
    events_QML = readEvents(os.path.join(ev_info, 'catalog.ml'),
                            format='QuakeML')
    if input_dics['event_catalog'].lower() == 'local':
        print "Use local files:"
        print "(all relevant options will be omitted!)"
        print os.path.join(ev_info, 'event_list_pickle')
        print os.path.join(ev_info, 'catalog.ml')
    return events, events_QML

# ##################### event_info #####################################


def event_info(input_dics):
    """
    Get event(s) info for event_based request.
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
        event_fdsn_cat = None

        if event_url.lower() == 'gcmt_combo':
            event_switch = 'gcmt_combo'
        if event_url.lower() == 'neic_usgs':
            event_switch = 'neic_usgs'
        if event_url.lower() == 'isc':
            event_url = 'IRIS'
            event_fdsn_cat = 'ISC'

        print 'Event(s) are based on:\t',
        print input_dics['event_catalog']

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
                neic_catalog(input_dics['min_date'],
                             input_dics['max_date'],
                             evlatmin, evlatmax, evlonmin, evlonmax,
                             evlat, evlon, evradmin, evradmax,
                             input_dics['min_depth'],
                             input_dics['max_depth'],
                             input_dics['min_mag'],
                             input_dics['max_mag'])

        else:
            sys.exit('%s is not supported'
                     % input_dics['event_catalog'])

        # no matter if list was passed or requested, sort catalogue,
        # plot events and proceed
        events_QML = sort_catalogue(events_QML)
        events = qml_to_event_list(events_QML)

    except Exception as error:
        print 60*'-'
        print 'ERROR: %s' % error
        print 60*'-'
        events = []
        events_QML = []

    for i in range(len(events)):
        events[i]['t1'] = events[i]['datetime'] - input_dics['preset']
        events[i]['t2'] = events[i]['datetime'] + input_dics['offset']

    return events, events_QML

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
        except Exception, error:
            print error
            continue

        try:
            if not events_QML.events[i].focal_mechanisms == []:
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
                focal_mechanism = False
        except AttributeError:
            print "WARNING: focal_mechanism does not exist for " \
                  "event: %s -- set to False" % (i+1)
            focal_mechanism = False
        except TypeError:
            focal_mechanism = False
        except Exception, error:
            print error
            focal_mechanism = False

        try:
            if not events_QML.events[i].focal_mechanisms == []:
                half_duration = [
                    events_QML.events[i].preferred_focal_mechanism()
                    ['moment_tensor']['source_time_function']['type'],
                    events_QML.events[i].preferred_focal_mechanism()
                    ['moment_tensor']['source_time_function']
                    ['duration']]
                if not half_duration[1]:
                    half_duration = mag_halfduration(
                        mag=events_QML.events[i].preferred_magnitude().mag)
            else:
                half_duration = mag_halfduration(
                    mag=events_QML.events[i].preferred_magnitude().mag)
        except AttributeError:
            print "WARNING: half_duration does not exist for " \
                  "event: %s -- set to False" % (i+1)
            half_duration = False
        except TypeError:
            half_duration = False
        except Exception, error:
            print error
            half_duration = False

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
                  events_QML.events[i].preferred_magnitude().mag or
                  events_QML.events[i].magnitudes[0].mag),
                 ('magnitude_type',
                  events_QML.events[i].preferred_magnitude().magnitude_type or
                  events_QML.events[i].magnitudes[0].magnitude_type),
                 ('author',
                  events_QML.events[i].preferred_magnitude().
                  creation_info.author or
                  events_QML.events[i].magnitudes[0].creation_info.author),
                 ('event_id', str(event_time.year) +
                  event_time_month + event_time_day + '_' +
                  event_time_hour + event_time_minute +
                  event_time_second + '.a'),
                 ('origin_id', events_QML.events[i].preferred_origin_id or
                  events_QML.events[i].origins[0].resource_id.resource_id),
                 ('focal_mechanism', focal_mechanism),
                 ('half_duration', half_duration),
                 ('flynn_region', 'NAN'),
                 ]))
        except Exception, error:
            print error
            continue
    return events

# ##################### continuous_info #####################################


def continuous_info(input_dics):
    """
    Get 'event(s)' info for continuous request.
    :param input_dics:
    :return:
    """
    print 'Start identifying the intervals ..'
    m_date = UTCDateTime(input_dics['min_date'])
    M_date = UTCDateTime(input_dics['max_date'])
    t_cont = M_date - m_date

    if t_cont < 0:
        sys.exit("\nERROR: max_date is lower than min_date!")

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
                 ('half_duration', False),
                 ('flynn_region', 'NAN'),
                 ('t1', m_date + (i-1)*input_dics['interval'] +
                  input_dics['preset_cont']),
                 ('t2', m_date + i*input_dics['interval'] +
                  input_dics['offset_cont']),
                 ]))

        final_time = m_date + num_div*input_dics['interval'] + \
                     input_dics['offset_cont']
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
                 ('half_duration', False),
                 ('flynn_region', 'NAN'),
                 ('t1', m_date + num_div*input_dics['interval'] +
                  input_dics['preset_cont']),
                 ('t2', M_date),
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
             ('half_duration', False),
             ('flynn_region', 'NAN'),
             ('t1', m_date),
             ('t2', M_date),
             ]))
    print 'DONE'
    events_QML = Catalog(events=[])
    return events, events_QML

# ##################### neic_catalog ############################


def neic_catalog(t_start, t_end, min_latitude, max_latitude, min_longitude,
                 max_longitude, latitude, longitude, radius_min, radius_max,
                 d_min, d_max, mag_min, mag_max,
                 link_neic="http://earthquake.usgs.gov/earthquakes/search/"):
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
    try:
        import mechanize
    except Exception, error:
        sys.exit('ERROR:\nFor NEIC_USGS, "mechanize" should be installed: %s\n'
                 '\npip install mechanize\n' % error)

    tic = time.clock()

    dir_name = '%s_temp_xml_files' % int(UTCDateTime.now().timestamp)
    os.mkdir(dir_name)

    # Defines which website we want to look at
    br = mechanize.Browser()
    br.open(link_neic)

    # NEIC has two forms, but the relevant one for us is the first form!
    br.form1 = list(br.forms())[0]

    br.form1['minmagnitude'] = str(mag_min)
    br.form1['maxmagnitude'] = str(mag_max)
    br.form1['mindepth'] = str(d_min)
    br.form1['maxdepth'] = str(d_max)

    if None in [latitude, longitude, radius_min, radius_max]:
        if None in [min_latitude, max_latitude, min_longitude, max_longitude]:
            br.form1['minlongitude'] = '-180'
            br.form1['maxlongitude'] = '180'
            br.form1['minlatitude'] = '-90'
            br.form1['maxlatitude'] = '90'
        else:
            br.form1['maxlatitude'] = str(max_latitude)
            br.form1['minlongitude'] = str(min_longitude)
            br.form1['maxlongitude'] = str(max_longitude)
            br.form1['minlatitude'] = str(min_latitude)
    else:
        br.form1['latitude'] = str(latitude)
        br.form1['longitude'] = str(longitude)
        br.form1['minradiuskm'] = str(float(radius_min)*111.32)
        br.form1['maxradiuskm'] = str(float(radius_max)*111.32)

    # This function at this moment only provides these settings
    br.form1['format'] = ['quakeml']
    br.form1['includeallorigins'] = ['true']
    br.form1['includeallmagnitudes'] = ['true']
    br.form1['producttype'] = 'moment-tensor'

    m_date = UTCDateTime(t_start)
    M_date = UTCDateTime(t_end)
    dur_event = M_date - m_date
    interval = 30.*24.*60.*60.

    num_div = int(dur_event/interval)
    print 'Number of divisions: %s' % num_div
    # residual time is: (has not been used here)
    # t_res = t_cont - num_div*input_dics['interval']
    for i in range(1, num_div+1):
        print i,
        sys.stdout.flush()
        t_start_split = m_date + (i-1)*interval
        t_end_split = m_date + i*interval
        br.form1['starttime'] = str(t_start_split)
        br.form1['endtime'] = str(t_end_split)

        # Final output will be now porcessed
        request = br.form1.click()
        br.open(request)
        url = br.geturl()

        remotefile = ('%s' % url)
        page = urllib2.urlopen(remotefile)
        page_content = page.read()

        if 'quakeml' in page_content:
            with open(os.path.join(dir_name,
                                   'temp_neic_xml_%05i.xml' % i),
                      'w') as fid:
                fid.write(page_content)
            fid.close()
        else:
            continue

    final_time = m_date + num_div*interval
    if not M_date == final_time:
        t_start_split = m_date + num_div*interval
        t_end_split = M_date
        print '\nEnd time: %s\n' % t_end_split
        br.form1['starttime'] = str(t_start_split)
        br.form1['endtime'] = str(t_end_split)

        # Final output will be now porcessed
        request = br.form1.click()
        br.open(request)
        url = br.geturl()

        remotefile = ('%s' % url)
        page = urllib2.urlopen(remotefile)
        page_content = page.read()

        if 'quakeml' in page_content:
            with open(os.path.join(dir_name,
                                   'temp_neic_xml_%05i.xml' % (num_div+1)),
                      'w') as fid:
                fid.write(page_content)
            fid.close()

    xml_add = glob.glob(os.path.join(dir_name, 'temp_neic_xml_*.xml'))
    xml_add.sort()
    cat = Catalog()
    print 'Start assembling the xml files: %s...\n' % len(xml_add)
    counter = 1
    for x_add in xml_add:
        print counter,
        sys.stdout.flush()
        counter += 1
        try:
            cat.extend(readEvents(x_add, format='QuakeML'))
            os.remove(x_add)
        except Exception, error:
            print 'WARNING: %s' % error
            os.remove(x_add)

    os.rmdir(dir_name)
    toc = time.clock()
    print '\nIt took %s sec to retrieve the earthquakes form NEIC.' % (toc-tic)
    return cat

# ##################### gcmt_catalog ############################


def gcmt_catalog(t_start, t_end, min_latitude, max_latitude, min_longitude,
                 max_longitude, latitude, longitude, radius_min, radius_max,
                 d_min, d_max, mag_min, mag_max,
                 link_gcmt='http://www.ldeo.columbia.edu/~gcmt/projects/CMT/'
                           'catalog'):
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
    :return:
    """
    # for the time record
    tic = datetime.now()

    if not os.path.exists('gcmt_catalog'):
        os.mkdir('gcmt_catalog')
        os.mkdir(os.path.join('gcmt_catalog', 'NEW_MONTHLY'))
        os.mkdir(os.path.join('gcmt_catalog', 'COMBO'))

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
    try:
        for i in range(len(yymmls)):
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
                file_to_open = os.path.join('gcmt_catalog', new_monthly,
                                            '%s%s.ndk'
                                            % (month_year[int(mm)-1], yy[-2:]))
                remotefile_add = '%s/%s/%s/%s%s.ndk' \
                                 % (link_gcmt, new_monthly, yy,
                                    month_year[int(mm)-1], yy[-2:])
            else:
                new_monthly = 'COMBO'
                if yy in yy_ret:
                    continue
                file_to_open = os.path.join('gcmt_catalog', new_monthly,
                                            '%s.qml' % yy)
            if not os.path.exists(file_to_open) and not new_monthly == 'COMBO':
                print 'Reading the data from GCMT webpage: %s' % yymmls[i]
                remotefile = urllib2.urlopen(remotefile_add)
                remotefile_read = remotefile.readlines()
                search_fio = open(file_to_open, 'w')
                search_fio.writelines(remotefile_read)
                search_fio.close()
            print 'Reading the data from local gcmt_catalog: %s' % yymmls[i]
            cat.extend(readEvents(file_to_open))
            yy_ret.append(yy)
            mm_ret.append(mm)
        print 'Done reading the data from GCMT webpage.'
    except Exception, error:
        print "ERROR: %s" % error

    toc = datetime.now()
    print 'It took %s to retrieve the earthquakes form GCMT.' % (toc-tic)

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
        print '\n' + row_format.format(*header)
        print 80 * '-'
        for i in range(len(events2)):
            print (row_format.format(*events2[i].values())).rstrip()
        print 80 * '-' + '\n'

    else:
        print '\n' + row_format.format(*header)
        print 80 * '-'
        print (row_format.format(*events2[0].values())).rstrip()
        print (row_format.format(*events2[1].values())).rstrip()
        print (row_format.format(*events2[2].values())).rstrip()
        print '..'
        print (row_format.format(*events2[-3].values())).rstrip()
        print (row_format.format(*events2[-2].values())).rstrip()
        print (row_format.format(*events2[-1].values())).rstrip()
        print 80 * '-' + '\n'
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
                        'focal_mechanism', 'half_duration']:
            try:
                del events2[i][item_ev]
            except Exception, error:
                print 'WARNING: %s' % error
                pass

        try:
            events2[i]['datetime'] = str(events2[i]['datetime'])[:-8]
        except Exception, error:
            print 'WARNING: %s' % error
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
        except Exception, error:
            print 'WARNING: %s' % error
            pass

    try:
        k, spaces = [], []
        for i in range(len(events2)):
            k.append(events2[i].values())

        for j in range(len(k[0])):
            spaces.append(max([len(str(k[i][j])) for i in range(len(k))]))

        return spaces, events2, header
    except Exception, error:
        print 'WARNING: %s' % error
        pass

# ##################### write_cat_logger ############################


def write_cat_logger(input_dics, eventpath, period, events, catalog,
                     events2, row_format, header):
    """
    Writing outputs out of get_Events function
    :param input_dics:
    :param eventpath:
    :param period:
    :param events:
    :param catalog:
    :param events2:
    :param row_format:
    :return:
    """
    if not os.path.isdir(os.path.join(eventpath, 'EVENTS-INFO')):
        os.makedirs(os.path.join(eventpath, 'EVENTS-INFO'))
    input_logger(argus=sys.argv,
                 address=os.path.join(eventpath,
                                      'EVENTS-INFO',
                                      'logger_command.txt'),
                 inputs=input_dics)

    # output catalogue as ASCII
    event_cat = \
        open(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.txt'), 'a+')
    st_argus = 'Command line:\n-------------\n'
    for item in sys.argv:
        st_argus += item + ' '
    st_argus += '\n'
    event_cat.writelines('\n\n' + str(period) + '\n')
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

    for i in range(len(events)):
        event_cat = open(os.path.join(eventpath, 'EVENTS-INFO',
                                      'catalog.txt'), 'a')
        event_cat.writelines("Event No: %s\n" % (i+1))
        event_cat.writelines("Author: %s\n" % events[i]['author'])
        event_cat.writelines("Event-ID: %s\n" % events[i]['event_id'])
        event_cat.writelines("Date Time: %s\n" % events[i]['datetime'])
        event_cat.writelines("Magnitude: %s\n" % events[i]['magnitude'])
        event_cat.writelines("Magnitude Type: %s\n"
                             % events[i]['magnitude_type'])
        event_cat.writelines("Depth: %s\n" % events[i]['depth'])
        event_cat.writelines("Latitude: %s\n" % events[i]['latitude'])
        event_cat.writelines("Longitude: %s\n" % events[i]['longitude'])
        try:
            event_cat.writelines("Flynn-Region: %s\n"
                                 % events[i]['flynn_region'])
        except KeyError:
            event_cat.writelines("Flynn-Region: None\n")
        event_cat.writelines('=====================================' + '\n')
        event_cat.close()
    event_file = open(os.path.join(eventpath, 'EVENTS-INFO',
                                   'event_list_pickle'), 'w')
    pickle.dump(events, event_file)
    event_file.close()

    # output catalogue as ASCII but in table form
    try:
        st_argus = 'Command line:\n-------------\n'
        for item in sys.argv:
            st_argus += item + ' '
        st_argus += '\n'
        event_table = open(os.path.join(eventpath, 'EVENTS-INFO',
                                        'catalog_table.txt'), 'a+')
        event_table.writelines('\n\n' + str(period) + '\n')
        event_table.writelines(st_argus)
        event_table.writelines('\n' + row_format.format(*header))
        event_table.writelines('\n' + '-'*80 + '\n')
        for i in range(len(events2)):
            event_table.writelines(
                (row_format.format(*events2[i].values())).rstrip() + '\n')
        event_table.writelines('-'*80 + '\n')
    except Exception as err:
        print '\nCouldn\'t write catalog object to ASCII file as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err

    # output catalogue as QUAKEML / JSON files
    try:
        catalog.write(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.ml'),
                      format="QUAKEML")
    except Exception as err:
        print '\nCouldn\'t write catalog object to QuakeML as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err
    try:
        catalog.write(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.json'),
                      format="JSON")
    except Exception as err:
        print '\nCouldn\'t write catalog object to JSON as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err

# ##################### sort_catalogue ############################


def sort_catalogue(cat):
    """
    Sort catalogue of retrieved events chronological.
    :param cat:
    :return:
    """
    k = [[event, event.origins[0].time] for event in cat]
    k.sort(key=lambda x: x[1], reverse=True)
    events = [event[0] for event in k]
    cat = Catalog(events=events)
    return cat

# ##################### mag_halfduration ###################################


def mag_halfduration(mag, type_curve=1):
    """
    Calculate the half_duration out of magnitude
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
        sys.exit('%s Type for magnitude to half_duration conversion is not '
                 'implemented' % type_curve)
    return ['triangle', round(half_duration, 3)]
