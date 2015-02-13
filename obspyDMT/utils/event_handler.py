#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  event_handler.py
#   Purpose:   handling events in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from collections import OrderedDict
import copy
from datetime import timedelta
import glob
import matplotlib.pyplot as plt
from obspy.core.event import Catalog, readEvents
from obspy.core import read, UTCDateTime
from obspy.fdsn import Client as Client_fdsn
import os
import pickle
import re
import shutil
import sys
import tarfile
import time

from input_handler import input_logger
from utility_codes import locate
from gcmt_cat_func import gcmt_catalog

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ##################### get_Events ######################################


def get_Events(input_dics, request):
    """
    Getting list of events
    :param input_dics:
    :param request:
    :return:
    """
    t_event_1 = time.time()

    # request can be 'event-based' or continuous
    try:
        events, catalog, successful_read = events_info(input_dics, request)
    except Exception, e:
        print 'WARNING: %s' % e
        return 0

    # output shell
    spaces, events2, header = event_spaces(events=events, request=request)
    header_template = ['{:<'+str(e+2)+'}' for e in spaces]
    row_format = '{}'.format(''.join(header_template))

    if input_dics['user_select_event'] == 'Y':

        print '\n' + row_format.format(*header)
        print 80 * '-'
        for i in range(len(events2)):
            print (row_format.format(*events2[i].values())).rstrip()
        print 80 * '-' + '\n'
        garbage = delete_events(events=events, catalog=catalog)

    else:
        garbage = '0'
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

    if len(events) == 0:
        return 0

    # if read in event catalog, define variables new which determine
    # the name of the folder where results will be stored. (Other-
    # wise folder is named after defaults (10 & 5 days ago)). For
    # renaming use max and min from quakes of read catalog
    if (input_dics['read_catalog'] != 'N' and successful_read == 1) \
            or len(garbage) != 0:
        input_dics['max_date'] = str(max([e['datetime'] for e in events]))
        input_dics['min_date'] = str(min([e['datetime'] for e in events]))
        input_dics['max_mag'] = str(max([e['magnitude'] for e in events]))
        input_dics['min_mag'] = str(min([e['magnitude'] for e in events]))

    print 'Number of event(s): %s' % len(events)
    print 'Time for retrieving and saving the event info: %s' \
          % str(timedelta(seconds=round(float(time.time() - t_event_1))))

    # formatting output / check if directory exists
    period = '{0:s}_{1:s}_{2:s}_{3:s}'.format(
        input_dics['min_date'].split('T')[0],
        input_dics['max_date'].split('T')[0],
        str(input_dics['min_mag']),
        str(input_dics['max_mag']))
    eventpath = os.path.join(input_dics['datapath'], period)

    if os.path.exists(eventpath):
        print '\n********************************************************'
        if raw_input('Directory for the requested period already exists:'
                     '\n%s\n\nOptions:\nN: Close the program and try '
                     'the updating mode.\nY: Remove the tree, continue the '
                     'program and re-download.\n' % eventpath).upper() == 'Y':
            print '********************************************************'
            shutil.rmtree(eventpath)
            os.makedirs(eventpath)
        else:
            sys.exit('Exit the program ..')
    else:
        os.makedirs(eventpath)

    os.makedirs(os.path.join(eventpath, 'EVENTS-INFO'))
    input_logger(argus=sys.argv, address=os.path.join(eventpath,
                                                      'EVENTS-INFO',
                                                      'logger_command.txt'),
                 inputs=input_dics)

    # output catalogue as ASCII
    Event_cat = \
        open(os.path.join(eventpath, 'EVENTS-INFO', 'catalog.txt'), 'a+')
    st_argus = 'Command line:\n-------------\n'
    for item in sys.argv:
        st_argus += item + ' '
    st_argus += '\n'
    Event_cat.writelines(str(period) + '\n')
    Event_cat.writelines(st_argus)
    Event_cat.writelines('-------------------------------------' + '\n')
    Event_cat.writelines('Information about the requested Events:' + '\n\n')
    Event_cat.writelines('Number of Events: %s\n' % len(events))
    Event_cat.writelines('min datetime: %s\n' % input_dics['min_date'])
    Event_cat.writelines('max datetime: %s\n' % input_dics['max_date'])
    Event_cat.writelines('min magnitude: %s\n' % input_dics['min_mag'])
    Event_cat.writelines('max magnitude: %s\n' % input_dics['max_mag'])
    Event_cat.writelines('min latitude: %s\n' % input_dics['evlatmin'])
    Event_cat.writelines('max latitude: %s\n' % input_dics['evlatmax'])
    Event_cat.writelines('min longitude: %s\n' % input_dics['evlonmin'])
    Event_cat.writelines('max longitude: %s\n' % input_dics['evlonmax'])
    Event_cat.writelines('min depth: %s\n' % input_dics['min_depth'])
    Event_cat.writelines('max depth: %s\n' % input_dics['max_depth'])
    Event_cat.writelines('\n\n-------------------------------------\n')
    Event_cat.close()

    for i in range(len(events)):
        Event_cat = open(os.path.join(eventpath, 'EVENTS-INFO',
                                      'catalog.txt'), 'a')
        Event_cat.writelines("Event No: %s\n" % (i+1))
        Event_cat.writelines("Catalog: %s\n" % events[i]['author'])
        Event_cat.writelines("Event-ID: %s\n" % events[i]['event_id'])
        Event_cat.writelines("Date Time: %s\n" % events[i]['datetime'])
        Event_cat.writelines("Magnitude: %s\n" % events[i]['magnitude'])
        Event_cat.writelines("Magnitude Type: %s\n"
                             % events[i]['magnitude_type'])
        Event_cat.writelines("Depth: %s\n" % events[i]['depth'])
        Event_cat.writelines("Latitude: %s\n" % events[i]['latitude'])
        Event_cat.writelines("Longitude: %s\n" % events[i]['longitude'])
        try:
            Event_cat.writelines("Flynn-Region: %s\n"
                                 % events[i]['flynn_region'])
        except KeyError:
            Event_cat.writelines("Flynn-Region: None\n")
        Event_cat.writelines('-------------------------------------' + '\n')
        Event_cat.close()
    Event_file = open(os.path.join(eventpath, 'EVENTS-INFO',
                                   'event_list_pickle'), 'a+')
    pickle.dump(events, Event_file)
    Event_file.close()

    # output catalogue as ASCII but in table form
    try:
        st_argus = 'Command line:\n-------------\n'
        for item in sys.argv:
            st_argus += item + ' '
        st_argus += '\n'
        Event_table = \
            open(os.path.join(eventpath,
                              'EVENTS-INFO', 'catalog_table.txt'), 'w')

        Event_table.writelines(st_argus)
        Event_table.writelines('\n' + row_format.format(*header))
        Event_table.writelines('-'*80 + '\n')
        for i in range(len(events2)):
            Event_table.writelines(
                (row_format.format(*events2[i].values())).rstrip() + '\n')
        Event_table.writelines('-'*80 + '\n')
    except Exception as err:
        print '\nCouldn\'t write catalog object to ASCII file as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err

    # output catalogue as QUAKEML / JSON files
    try:
        catalog.write(
            os.path.join(eventpath, 'EVENTS-INFO', 'catalog.ml'),
            format="QUAKEML")
        catalog.write(
            os.path.join(eventpath, 'EVENTS-INFO', 'catalog.json'),
            format="JSON")
    except Exception as err:
        print '\nCouldn\'t write catalog object to file as:\n>>:\t %s\n' \
              'Proceed without ..\n' % err

    return events

# ##################### events_info #####################################


def events_info(input_dics, request):
    """
    Get the event(s) info for event-based or continuous requests
    :param input_dics:
    :param request:
    :return:
    """
    successful_read = 0

    if input_dics['waveform'] == 'N':
        print '\nYou' \
              ' specifed "--event_info"\nand also data request.'   \
              '\nProceed without downloading files !\n'

    events = []
    events_QML = []
    if request == 'event-based':
        try:
            # if: read event file ; else make url request for events
            if input_dics['read_catalog'] != 'N':

                if not input_dics['event_catalog']:
                    print '\n\033[91mContradictory options chosen:\033[0m\nYou '\
                          'specifed a catalog by "--event_catalog"\nand by "--read'\
                          '_catalog".\nProceed with reading file !'

                try:
                    events_QML = readEvents(input_dics['read_catalog'])
                    print '\nRead events from catalog:\n' \
                          '>>:\t%s' % input_dics['read_catalog']
                    successful_read = 1
                except TypeError as err:
                    print 'WARNING: %s' % err
                    print '\n\033[91mData format not supported,\033[0m' \
                          ' tried to read file:\n>>:\t', \
                        input_dics['read_catalog']
                    print '\nFor valid data formats, see:'
                    print 'obspyDMT -h | grep --read_catalog'
                    return
                except IOError as err:
                    print '\n\033[91mStated file does not exist:\033[0m\n' \
                          '>>:\t', err
                    return
                except Exception as err:
                    print '\n\033[91mSomething went terribly wrong:\033[0m\n' \
                          '>>:\t', err
                    return

            else:
                print 'Event(s) are based on:\t',

                print input_dics['event_url']
                print 'Specified catalog:\t', input_dics['event_catalog']

                evlatmin = input_dics['evlatmin']
                evlatmax = input_dics['evlatmax']
                evlonmin = input_dics['evlonmin']
                evlonmax = input_dics['evlonmax']

                evlat = input_dics['evlat']
                evlon = input_dics['evlon']
                evradmax = input_dics['evradmax']
                evradmin = input_dics['evradmin']

                client_fdsn = Client_fdsn(base_url=input_dics['event_url'])
                events_QML = client_fdsn.get_events(
                    minlatitude=evlatmin,
                    maxlatitude=evlatmax,
                    minlongitude=evlonmin,
                    maxlongitude=evlonmax,
                    latitude=evlat,
                    longitude=evlon,
                    maxradius=evradmax,
                    minradius=evradmin,
                    mindepth=input_dics['min_depth'],
                    maxdepth=input_dics['max_depth'],
                    starttime=input_dics['min_date'],
                    endtime=input_dics['max_date'],
                    minmagnitude=input_dics['min_mag'],
                    maxmagnitude=input_dics['max_mag'],
                    orderby='time',
                    catalog=input_dics['event_catalog'],
                    magnitudetype=input_dics['mag_type'])
                # events_QML_test = \
                #     gcmt_catalog(input_dics['min_date'],
                #                  input_dics['max_date'],
                #                  evlatmin, evlatmax, evlonmin, evlonmax,
                #                  evlat, evlon, evradmin, evradmax,
                #                  input_dics['min_depth'],
                #                  input_dics['max_depth'],
                #                  input_dics['min_mag'],
                #                  input_dics['max_mag'],
                #                  input_dics['mag_type'])
                import ipdb; ipdb.set_trace()

            # no matter if list was passed or requested, sort catalogue,
            # plot events and proceed
            events_QML = sort_catalogue(events_QML)

            if input_dics['plot_all_events']:
                plt.ion()
                events_QML.plot()

            events = []
            for i in range(len(events_QML)):
                event_time = \
                    events_QML.events[i].preferred_origin().time or \
                    events_QML.events[i].origins[0].time
                if event_time.month < 10:
                    event_time_month = '0' + str(event_time.month)
                else:
                    event_time_month = str(event_time.month)
                if event_time.day < 10:
                    event_time_day = '0' + str(event_time.day)
                else:
                    event_time_day = str(event_time.day)

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
                      events_QML.events[i].preferred_magnitude().
                      magnitude_type.lower() or
                      events_QML.events[i].magnitudes[0].
                      magnitude_type.lower()),
                     ('author',
                      events_QML.events[i].preferred_magnitude().
                      creation_info.author or
                      events_QML.events[i].magnitudes[0].creation_info.author),
                     ('event_id', str(event_time.year) +
                      event_time_month + event_time_day + '_' + str(i+1)),
                     ('origin_id', events_QML.events[i].preferred_origin_id or
                      events_QML.events[i].origins[0].resource_id.resource_id),
                     ('flynn_region', 'NAN'),
                     ]))

                # if --read_catalog, redefine variables which determine
                # the name of the folder where results will be stored. (Other-
                # wise folder is named after defaults (10 & 5 days ago)). For
                # renaming use max and min from quakes of read catalog
                if input_dics['read_catalog'] != 'N' and successful_read == 1:
                    input_dics['max_date'] = \
                        str(max([e['datetime'] for e in events]))
                    input_dics['min_date'] = \
                        str(min([e['datetime'] for e in events]))
                    input_dics['max_mag'] = \
                        str(max([e['magnitude'] for e in events]))
                    input_dics['min_mag'] = \
                        str(min([e['magnitude'] for e in events]))

        except Exception as e:
            print 60*'-'
            print 'No event found with the requested criteria!'
            print 'ERROR: %s' % e
            print 60*'-'
            events = []
            events_QML = Catalog(events=[])

        for i in range(len(events)):
            events[i]['t1'] = events[i]['datetime'] - input_dics['preset']
            events[i]['t2'] = events[i]['datetime'] + input_dics['offset']

    elif request == 'continuous':

        if input_dics['read_catalog'] != 'N':
            print '\n\033[91mContradictory options chosen:\033[0m\nYou ' \
                  'specifed "--continuous"\ndata request and "--read_catalog".'\
                  '\nProceed with continuous data request !\n'
            print '-------------------------------------------------'

        print 'Start identifying the intervals ..'
        m_date = UTCDateTime(input_dics['min_date'])
        M_date = UTCDateTime(input_dics['max_date'])
        t_cont = M_date - m_date

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
                     ('origin_id', -12345), ('flynn_region', 'NAN'),
                     ('t1', m_date + (i-1)*input_dics['interval'] +
                      input_dics['preset_cont']),
                     ('t2', m_date + i*input_dics['interval'] +
                      input_dics['offset_cont']),
                     ]))

            cont_dir_name = \
                (len(str(num_div)) - len(str(num_div)))*'0' + str(num_div+1)
            events.append(OrderedDict(
                [('number', num_div+1),
                 ('latitude', -12345),
                 ('longitude', -12345),
                 ('depth', -12345),
                 ('datetime', m_date + (num_div-1)*input_dics['interval']),
                 ('magnitude', -12345),
                 ('magnitude_type', 'NAN'),
                 ('author', 'NAN'),
                 ('event_id', 'continuous' + cont_dir_name),
                 ('origin_id', -12345),
                 ('flynn_region', 'NAN'),
                 ('t1', m_date + (num_div-1)*input_dics['interval'] +
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
                 ('flynn_region', 'NAN'),
                 ('t1', m_date),
                 ('t2', M_date),
                 ]))
        print 'DONE'
        events_QML = Catalog(events=[])
    return events, events_QML, successful_read

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
        try:
            del events2[i]['t1']
        except Exception, e:
            print 'WARNING: %s' % e
            pass
        try:
            del events2[i]['t2']
        except Exception, e:
            print 'WARNING: %s' % e
            pass
        try:
            del events2[i]['origin_id']
        except Exception, e:
            print 'WARNING: %s' % e
            pass
        try:
            del events2[i]['magnitude_type']
        except Exception, e:
            print 'WARNING: %s' % e
            pass
        try:
            events2[i]['datetime'] = str(events2[i]['datetime'])[:-8]
        except Exception, e:
            print 'WARNING: %s' % e
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
                    int(round(float(events2[i]['depth'])/1000))
        except Exception, e:
            print 'WARNING: %s' % e
            pass

    try:
        k, spaces = [], []
        for i in range(len(events2)):
            k.append(events2[i].values())

        for j in range(len(k[0])):
            spaces.append(max([len(str(k[i][j])) for i in range(len(k))]))

        return spaces, events2, header
    except Exception, e:
        print 'WARNING: %s' % e
        pass

# ##################### delete_events ############################


def delete_events(events, catalog):
    """
    delete-event procedure
    :param events:
    :param catalog:
    :return:
    """
    garbage = []
    ev_num = raw_input(
        'Type the number of event you wish not to proceed with, '
        'then hit >Enter<.\nTo delete all events but number x, y .. '
        'type:  >!x[, y, z ..]<.\nTo proceed without making a selection, '
        'hit >Enter< now:\t')
    while re.search(r"\A\s*\d+\s*\Z|\A\s*!\s*\d+(\s*,\s*\d+)*\s*\Z", ev_num):
        if ev_num.strip()[0] == '!':
            keep = [int(i) for i in ev_num.strip().strip('!').split(',')]
            garbage = [i for i in range(1, len(events)+1) if i not in keep]
            break
        else:
            if int(ev_num) < 1 or int(ev_num) > len(events):
                break
            garbage.append(int(ev_num))
            ev_num = raw_input('Go on:\t')

    print '\nThe following events are not considered for ' \
          'further steps:\n%s\n' % garbage

    if len(garbage) != 0:
        garbage = list(set(garbage))
        garbage.sort()

        garbage.reverse()
        for ev_out in garbage:
            del events[ev_out-1]
            catalog.__delitem__(ev_out-1)
        if len(events) == 0:
            sys.exit('\nExit, seems like the catalog is '
                     'empty now. Try Again.')
    else:
        print

    return garbage

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

# ##################### quake_info ######################################


def quake_info(address, target):
    """
    Reads the info in quake file ("info" folder)
    :param address:
    :param target:
    :return:
    """
    events = []
    target_add = locate(address, target)
    for t_add in target_add:
        if not os.path.isfile(os.path.join(t_add, 'quake')):
            print '='*64
            print 'quake file could not be found'
            print 'Start Creating the quake file'
            print 'WARNING: it uses just one seismogram to ' \
                  're-create the quake file'
            print '='*64
            quake_create(address_info=t_add)
        quake_file_open = open(os.path.join(t_add, 'quake'), 'r')
        quake_file = quake_file_open.readlines()

        quake_read_tmp = []
        for q_file_l in quake_file:
            for q_l_item in q_file_l.split():
                try:
                    quake_read_tmp.append(float(q_l_item))
                except ValueError:
                    pass

        if len(quake_read_tmp) < 20:
            print '====================='
            print 'Modify the quake file'
            print '====================='
            quake_modify(quake_item=quake_read_tmp, address_info=t_add)

            quake_file_open = open(os.path.join(t_add, 'quake'), 'r')
            quake_file = quake_file_open.readlines()

            quake_read_tmp = []
            for q_file_l in quake_file:
                for q_l_item in q_file_l.split():
                    try:
                        quake_read_tmp.append(float(q_l_item))
                    except ValueError:
                        pass

        quake_d = {'year0': int(quake_read_tmp[0]),
                   'julday0': int(quake_read_tmp[1]),
                   'hour0': int(quake_read_tmp[2]),
                   'minute0': int(quake_read_tmp[3]),
                   'second0': int(quake_read_tmp[4]),
                   'lat': float(quake_read_tmp[6]),
                   'lon': float(quake_read_tmp[7]),
                   'dp': float(quake_read_tmp[8]),
                   'mag': float(quake_read_tmp[9]),
                   'year1': int(quake_read_tmp[10]),
                   'julday1': int(quake_read_tmp[11]),
                   'hour1': int(quake_read_tmp[14]),
                   'minute1': int(quake_read_tmp[15]),
                   'second1': int(quake_read_tmp[16]),
                   'year2': int(quake_read_tmp[18]),
                   'julday2': int(quake_read_tmp[19]),
                   'hour2': int(quake_read_tmp[22]),
                   'minute2': int(quake_read_tmp[23]),
                   'second2': int(quake_read_tmp[24])}

        quake_t0 = UTCDateTime(year=quake_d['year0'],
                               julday=quake_d['julday0'],
                               hour=quake_d['hour0'],
                               minute=quake_d['minute0'],
                               second=quake_d['second0'])
        quake_t1 = UTCDateTime(year=quake_d['year1'],
                               julday=quake_d['julday1'],
                               hour=quake_d['hour1'],
                               minute=quake_d['minute1'],
                               second=quake_d['second1'])
        quake_t2 = UTCDateTime(year=quake_d['year2'],
                               julday=quake_d['julday2'],
                               hour=quake_d['hour2'],
                               minute=quake_d['minute2'],
                               second=quake_d['second2'])

        events.append({'author': 'NONE',
                       'datetime': quake_t0,
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
    for t_add in target_add:
        address_event.append(os.path.dirname(t_add))

    return events, address_event

# ##################### quake_create ####################################


def quake_create(address_info):
    """
    if there is no quake file in the info folder it will be created
    based on the data available in the BH_RAW or BH file
    :param address_info:
    :return:
    """

    quake_file = open(os.path.join(address_info, 'quake'), 'w')
    address = os.path.normpath(os.path.join(address_info, '..'))

    if os.path.isdir(os.path.join(address, 'BH_RAW')):
        sta_address = os.path.join(address, 'BH_RAW')
    elif os.path.isdir(os.path.join(address, 'BH')):
        sta_address = os.path.join(address, 'BH')
    else:
        print '\nERROR: There is no reference (BH_RAW or BH) ' \
              'to create a quake file...'
        sta_address = None
    sta_stas = None
    try:
        ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))
        sta = read(ls_stas[0])[0]
        sta_stats = sta.stats
        print '\nCreate the quake file based on: \n%s' % ls_stas[0]
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % sta_stats.sac.evla)) +
                              '%.5f' % sta_stats.sac.evla +
                              ' '*(15 - len('%.5f' % sta_stats.sac.evlo)) +
                              '%.5f' % sta_stats.sac.evlo + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(sta_stats.sac.evdp)))
                              + '%.5f' % abs(sta_stats.sac.evdp) + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(sta_stats.sac.mag))) +
                              '%.5f' % abs(sta_stats.sac.mag) + '\n')
        quake_file.writelines(' '*(15 - len(address.split('/')[-1])) +
                              address.split('/')[-1] + '-' + '\n')

        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              repr(sta_stats.starttime.month).rjust(15) +
                              repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')

        sta_stats_endtime = \
            sta_stats.starttime + (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file.writelines(
            '{0}{1}{2}{3}\n'.format(repr(sta_stats_endtime.year).rjust(15),
                                    repr(sta_stats_endtime.julday).rjust(15),
                                    repr(sta_stats_endtime.month).rjust(15),
                                    repr(sta_stats_endtime.day).rjust(15)))
        quake_file.writelines(
            '{0}{1}{2}{3}\n'.format(repr(sta_stats_endtime.hour).rjust(15),
                                    repr(sta_stats_endtime.minute).rjust(15),
                                    repr(sta_stats_endtime.second).rjust(15),
                                    repr(sta_stats_endtime.microsecond).
                                    rjust(15)))

    except Exception as e:
        print '\n================='
        print 'WARNING: Can not read all the required information ' \
              'from the header'
        print 'Following parameters are presumed:'
        print 'evla=0, evlo=0, dp=-12345.0, mag=-12345.0'
        print 'Exception: %s' % e
        print '=================\n'
        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % 0.0)) + '%.5f' % 0.0 +
                              ' '*(15 - len('%.5f' % 0.0)) + '%.5f' % 0.0
                              + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(-12345.0))) +
                              '%.5f' % abs(-12345.0) + '\n')
        quake_file.writelines(' '*(15 - len('%.5f' % abs(-12345.0))) +
                              '%.5f' % abs(-12345.0) + '\n')
        quake_file.writelines(' '*(15 - len(address.split('/')[-1])) +
                              address.split('/')[-1] + '-' + '\n')

        quake_file.writelines(repr(sta_stats.starttime.year).rjust(15) +
                              repr(sta_stats.starttime.julday).rjust(15) +
                              repr(sta_stats.starttime.month).rjust(15) +
                              repr(sta_stats.starttime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                              repr(sta_stats.starttime.minute).rjust(15) +
                              repr(sta_stats.starttime.second).rjust(15) +
                              repr(sta_stats.starttime.microsecond).rjust(15)
                              + '\n')

        sta_stats_endtime = \
            sta_stats.starttime + (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file.writelines(repr(sta_stats_endtime.year).rjust(15) +
                              repr(sta_stats_endtime.julday).rjust(15) +
                              repr(sta_stats_endtime.month).rjust(15) +
                              repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                              repr(sta_stats_endtime.minute).rjust(15) +
                              repr(sta_stats_endtime.second).rjust(15) +
                              repr(sta_stats_endtime.microsecond).rjust(15) +
                              '\n')
    quake_file.close()

# ##################### quake_modify ####################################


def quake_modify(quake_item, address_info):
    """
    if the quake file does not contain all the required parameters
    it will be modified based on the available data in BH_RAW or BH directories
    :param quake_item:
    :param address_info:
    :return:
    """

    quake_file_new = open(os.path.join(address_info, 'quake'), 'w')
    address = os.path.normpath(os.path.join(address_info, '..'))

    if os.path.isdir(os.path.join(address, 'BH_RAW')):
        sta_address = os.path.join(address, 'BH_RAW')
    elif os.path.isdir(os.path.join(address, 'BH')):
        sta_address = os.path.join(address, 'BH')
    else:
        print '\nERROR: There is no reference (BH_RAW or BH) ' \
              'to modify the quake file...'
        sta_address = None

    ls_stas = glob.glob(os.path.join(sta_address, '*.*.*.*'))

    sta = read(ls_stas[0])[0]
    sta_stats = sta.stats
    print '\nCreate the quake file based on: \n%s' % ls_stas[0]

    try:
        quake_file_new.writelines(repr(int(quake_item[0])).rjust(15) +
                                  repr(int(quake_item[1])).rjust(15) + '\n')
        quake_file_new.writelines(repr(int(quake_item[2])).rjust(15) +
                                  repr(int(quake_item[3])).rjust(15) +
                                  repr(int(quake_item[4])).rjust(15) +
                                  repr(int(quake_item[5])).rjust(15) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % quake_item[6])) +
                                  '%.5f' % quake_item[6] +
                                  ' '*(15 - len('%.5f' % quake_item[7])) +
                                  '%.5f' % quake_item[7] + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % abs(quake_item[8]))) +
                                  '%.5f' % abs(quake_item[8]) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f'
                                                % abs(sta_stats.sac.mag))) +
                                  '%.5f' % abs(sta_stats.sac.mag) + '\n')
        quake_file_new.writelines(' '*(15 - len(address.split('/')[-1])) +
                                  address.split('/')[-1] + '-' + '\n')

        quake_file_new.writelines(repr(sta_stats.starttime.year).rjust(15) +
                                  repr(sta_stats.starttime.julday).rjust(15) +
                                  repr(sta_stats.starttime.month).rjust(15) +
                                  repr(sta_stats.starttime.day).rjust(15) +
                                  '\n')
        quake_file_new.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                                  repr(sta_stats.starttime.minute).rjust(15) +
                                  repr(sta_stats.starttime.second).rjust(15) +
                                  repr(sta_stats.starttime.microsecond).
                                  rjust(15) + '\n')

        sta_stats_endtime = \
            sta_stats.starttime + (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file_new.writelines(repr(sta_stats_endtime.year).rjust(15) +
                                  repr(sta_stats_endtime.julday).rjust(15) +
                                  repr(sta_stats_endtime.month).rjust(15) +
                                  repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                                  repr(sta_stats_endtime.minute).rjust(15) +
                                  repr(sta_stats_endtime.second).rjust(15) +
                                  repr(sta_stats_endtime.microsecond).rjust(15)
                                  + '\n')
    except Exception as e:
        print '\n================='
        print 'WARNING: Can not read all the required information ' \
              'from the header'
        print 'Following parameters are presumed:'
        print 'evla=0, evlo=0, dp=-12345.0, mag=-12345.0'
        print 'Exception: %s' % e
        print '=================\n'
        quake_file_new.writelines(repr(int(quake_item[0])).rjust(15) +
                                  repr(int(quake_item[1])).rjust(15) + '\n')
        quake_file_new.writelines(repr(int(quake_item[2])).rjust(15) +
                                  repr(int(quake_item[3])).rjust(15) +
                                  repr(int(quake_item[4])).rjust(15) +
                                  repr(int(quake_item[5])).rjust(15) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % quake_item[6])) +
                                  '%.5f' % quake_item[6] +
                                  ' '*(15 - len('%.5f' % quake_item[7])) +
                                  '%.5f' % quake_item[7] + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % abs(quake_item[8])))
                                  + '%.5f' % abs(quake_item[8]) + '\n')
        quake_file_new.writelines(' '*(15 - len('%.5f' % abs(-12345.0)))
                                  + '%.5f' % abs(-12345.0) + '\n')
        quake_file_new.writelines(' '*(15 - len(address.split('/')[-1])) +
                                  address.split('/')[-1] + '-' + '\n')

        quake_file_new.writelines(repr(sta_stats.starttime.year).rjust(15) +
                                  repr(sta_stats.starttime.julday).rjust(15) +
                                  repr(sta_stats.starttime.month).rjust(15) +
                                  repr(sta_stats.starttime.day).rjust(15) +
                                  '\n')
        quake_file_new.writelines(repr(sta_stats.starttime.hour).rjust(15) +
                                  repr(sta_stats.starttime.minute).rjust(15) +
                                  repr(sta_stats.starttime.second).rjust(15) +
                                  repr(sta_stats.starttime.microsecond).
                                  rjust(15) + '\n')

        sta_stats_endtime = \
            sta_stats.starttime + (sta_stats.npts-1)/sta_stats.sampling_rate

        quake_file_new.writelines(repr(sta_stats_endtime.year).rjust(15) +
                                  repr(sta_stats_endtime.julday).rjust(15) +
                                  repr(sta_stats_endtime.month).rjust(15) +
                                  repr(sta_stats_endtime.day).rjust(15) + '\n')
        quake_file_new.writelines(repr(sta_stats_endtime.hour).rjust(15) +
                                  repr(sta_stats_endtime.minute).rjust(15) +
                                  repr(sta_stats_endtime.second).rjust(15) +
                                  repr(sta_stats_endtime.microsecond).rjust(15)
                                  + '\n')
    quake_file_new.close()

# ##################### create_folders_files ############################


def create_folders_files(events, eventpath):
    """
    Create required folders and files in the event folder(s)
    :param events:
    :param eventpath:
    :return:
    """
    for i in range(len(events)):
        try:
            os.makedirs(os.path.join(eventpath, events[i]['event_id'],
                                     'BH_RAW'))
            os.makedirs(os.path.join(eventpath, events[i]['event_id'],
                                     'Resp'))
            os.makedirs(os.path.join(eventpath, events[i]['event_id'],
                                     'info'))
        except Exception as e:
            print 'ERROR: %s' % e
            pass

    for i in range(len(events)):
        report = open(os.path.join(eventpath, events[i]['event_id'],
                                   'info', 'report_st'), 'a+')
        report.close()

    for i in range(len(events)):
        exception_file = open(os.path.join(eventpath, events[i]['event_id'],
                                           'info', 'exception'), 'a+')
        exception_file.writelines('\n' + events[i]['event_id'] + '\n')
        exception_file.close()

        syn_file = open(os.path.join(eventpath, events[i]['event_id'],
                                     'info', 'station_event'), 'a+')
        syn_file.close()

    for i in range(len(events)):
        quake_file = open(os.path.join(eventpath, events[i]['event_id'],
                                       'info', 'quake'), 'a+')

        quake_file.writelines(repr(events[i]['datetime'].year).rjust(15) +
                              repr(events[i]['datetime'].julday).rjust(15)
                              + '\n')
        quake_file.writelines(repr(events[i]['datetime'].hour).rjust(15) +
                              repr(events[i]['datetime'].minute).rjust(15) +
                              repr(events[i]['datetime'].second).rjust(15) +
                              repr(events[i]['datetime'].microsecond).rjust(15)
                              + '\n')

        quake_file.writelines(' '*(15 - len('%.5f' % events[i]['latitude'])) +
                              '%.5f' % events[i]['latitude'] +
                              ' '*(15 - len('%.5f' % events[i]['longitude'])) +
                              '%.5f\n' % events[i]['longitude'])
        quake_file.writelines(' '*(15 - len('%.5f' % abs(events[i]['depth'])))
                              + '%.5f\n' % abs(events[i]['depth']))
        quake_file.writelines(' '*(15 -
                                   len('%.5f' % abs(events[i]['magnitude'])))
                              + '%.5f\n'
                              % abs(events[i]['magnitude']))
        quake_file.writelines(' '*(15 - len(events[i]['event_id'])) +
                              events[i]['event_id'] + '-' + '\n')

        quake_file.writelines(repr(events[i]['t1'].year).rjust(15) +
                              repr(events[i]['t1'].julday).rjust(15) +
                              repr(events[i]['t1'].month).rjust(15) +
                              repr(events[i]['t1'].day).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['t1'].hour).rjust(15) +
                              repr(events[i]['t1'].minute).rjust(15) +
                              repr(events[i]['t1'].second).rjust(15) +
                              repr(events[i]['t1'].microsecond).rjust(15) +
                              '\n')

        quake_file.writelines(repr(events[i]['t2'].year).rjust(15) +
                              repr(events[i]['t2'].julday).rjust(15) +
                              repr(events[i]['t2'].month).rjust(15) +
                              repr(events[i]['t2'].day).rjust(15) + '\n')
        quake_file.writelines(repr(events[i]['t2'].hour).rjust(15) +
                              repr(events[i]['t2'].minute).rjust(15) +
                              repr(events[i]['t2'].second).rjust(15) +
                              repr(events[i]['t2'].microsecond).rjust(15) +
                              '\n')

# ##################### create_tar_file #######################################


def create_tar_file(input_dics, address):
    """
    create a tar file out of a given directory
    :param input_dics:
    :param address:
    :return:
    """
    print '\n**************************'
    print 'Start creating tar file(s)'
    print '**************************'
    events, address_events = quake_info(address, 'info')
    for i in range(len(events)):
        # ---------Creating Tar files (Waveform files)
        if input_dics['zip_w'] == 'Y':
            print 'Compressing Raw files...'
            path = os.path.join(address_events[i], 'BH_RAW')
            tar_file = os.path.join(path, 'BH_RAW.tar')
            files = '*.*.*.*'
            compress_gzip(path=path, tar_file=tar_file, files=files)

        # ---------Creating Tar files (Response files)
        if input_dics['zip_r'] == 'Y':
            print 'Compressing Resp files...'
            path = os.path.join(address_events[i], 'Resp')
            tar_file = os.path.join(path, 'Resp.tar')
            files = '*.*.*.*'
            compress_gzip(path=path, tar_file=tar_file, files=files)

# ##################### compress_gzip ###################################


def compress_gzip(path, tar_file, files):
    """
    Compressing files and creating a tar file
    :param path:
    :param tar_file:
    :param files:
    :return:
    """
    tar = tarfile.open(tar_file, "w:gz")
    os.chdir(path)

    for infile in glob.glob(os.path.join(path, files)):
        print '.',
        tar.add(os.path.basename(infile))
        os.remove(infile)
    tar.close()
