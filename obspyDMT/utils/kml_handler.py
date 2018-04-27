#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  kml_handler.py
#   Purpose:   handling KML format in obspyDMT
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import matplotlib.pyplot as plt
import numpy as np
try:
    from obspy.imaging.beachball import beachball as Beachball
except:
    from obspy.imaging.beachball import Beachball
try:
    from obspy.geodetics import locations2degrees
except:
    from obspy.core.util import locations2degrees
try:
    from obspy.geodetics.base import gps2dist_azimuth as gps2DistAzimuth
except:
    try:
        from obspy.geodetics import gps2DistAzimuth
    except:
        from obspy.core.util import gps2DistAzimuth
import os
import sys

from .data_handler import update_sta_ev_file
from .utility_codes import locate, plot_filter_station

# ##################### create_ev_sta_kml ###############################


def create_ev_sta_kml(input_dics, events):
    """
    create event/station/ray in KML format readable by Google-Earth
    :param input_dics:
    :param events:
    :return:
    """
    try:
        from pykml.factory import KML_ElementMaker as KML
        from lxml import etree
    except:
        sys.exit('[ERROR] pykml should be installed first!')

    if not os.path.isdir('kml_dir'):
        os.mkdir('kml_dir')
    else:
        print('[INFO] kml_dir already exists!')

    # create a document element with multiple label style
    kmlobj = KML.kml(KML.Document())
    counter = 0
    for ei in range(len(events)):
        print(events[ei]['event_id'])
        counter += 1

        ev_date = '%04i/%02i/%02i-%02i:%02i:%02i' \
                  % (events[ei]['datetime'].year,
                     events[ei]['datetime'].month,
                     events[ei]['datetime'].day,
                     events[ei]['datetime'].hour,
                     events[ei]['datetime'].minute,
                     events[ei]['datetime'].second
                     )

        if input_dics['plot_focal']:
            try:
                focmecs = [float(events[ei]['focal_mechanism'][0]),
                           float(events[ei]['focal_mechanism'][1]),
                           float(events[ei]['focal_mechanism'][2]),
                           float(events[ei]['focal_mechanism'][3]),
                           float(events[ei]['focal_mechanism'][4]),
                           float(events[ei]['focal_mechanism'][5])]
            except:
                print("WARNING: 'focal_mechanism' does not exist!")
                focmecs = [1, 1, 1, 0, 0, 0]
        else:
            focmecs = [1, 1, 1, 0, 0, 0]

        if 0 <= events[ei]['depth'] < 70:
            event_color = 'red'
        elif 70 <= events[ei]['depth'] < 300:
            event_color = 'green'
        else:
            event_color = 'blue'

        try:
            Beachball(focmecs,
                      outfile=os.path.join(
                          'kml_dir', events[ei]['event_id'] + '.png'),
                      facecolor=event_color,
                      edgecolor=event_color)
        except Exception as error:
            print(error)
            print(focmecs)
            continue
        plt.close()
        plt.clf()

        if input_dics['plot_ev'] or input_dics['plot_ray']:
            kmlobj.Document.append(
                KML.Style(
                    KML.IconStyle(
                        KML.Icon(KML.href(os.path.join(
                            events[ei]['event_id'] + '.png')),
                        ),
                        KML.scale(events[ei]['magnitude']/2.),
                        KML.heading(0.0),
                    ),
                    id='beach_ball_%i' % counter
                ),
            )

            kmlobj.Document.append(
                KML.Placemark(
                    KML.name(events[ei]['event_id']),
                    KML.ExtendedData(
                        KML.Data(
                            KML.value('%s' % events[ei]['event_id']),
                            name='event_id'
                        ),
                        KML.Data(
                            KML.value('%s' % events[ei]['magnitude']),
                            name='magnitude'
                        ),
                        KML.Data(
                            KML.value('%s' % ev_date),
                            name='datetime'
                        ),
                        KML.Data(
                            KML.value('%s' % events[ei]['depth']),
                            name='depth'
                        ),
                        KML.Data(
                            KML.value('%s' % events[ei]['latitude']),
                            name='latitude'
                        ),
                        KML.Data(
                            KML.value('%s' % events[ei]['longitude']),
                            name='longitude'
                        ),
                    ),
                    KML.styleUrl('#beach_ball_%i' % counter),
                    # KML.Point(KML.coordinates(events[ei]['longitude'], ',',
                    #                           events[ei]['latitude'], ',',
                    #                           700000 -
                    #                           abs(events[ei]['depth']*1000)),
                    #           KML.altitudeMode('absolute')
                    #           ),
                    KML.Point(KML.coordinates(events[ei]['longitude'], ',',
                                              events[ei]['latitude'], ',',
                                              0.),
                              KML.altitudeMode('absolute')
                              ),
                ),
            )

        if input_dics['plot_sta'] or input_dics['plot_ray']:
            target_path = locate(input_dics['datapath'],
                                 events[ei]['event_id'], num_matches=1)
            if len(target_path) < 1:
                continue
            if len(target_path) > 1:
                print("[LOCAL] more than one path was found for the event:")
                print(target_path)
                print("[INFO] use the first one:")
                target_path = target_path[0]
                print(target_path)
            else:
                print("[LOCAL] Path:")
                target_path = target_path[0]
                print(target_path)

            update_sta_ev_file(target_path, events[ei])
            sta_ev_arr = np.loadtxt(os.path.join(target_path,
                                                 'info', 'station_event'),
                                    delimiter=',', dtype=bytes, ndmin=2).astype(np.str)
            sta_ev_arr = sta_ev_arr.astype(np.object)
            del_index = []
            for sti in range(len(sta_ev_arr)):

                if not plot_filter_station(input_dics, sta_ev_arr[sti]):
                    del_index.append(sti)

                dist, azi, bazi = gps2DistAzimuth(events[ei]['latitude'],
                                                  events[ei]['longitude'],
                                                  float(sta_ev_arr[sti, 4]),
                                                  float(sta_ev_arr[sti, 5]))

                epi_dist = dist/111.194/1000.
                if input_dics['min_azi'] or input_dics['max_azi'] or \
                        input_dics['min_epi'] or input_dics['max_epi']:
                    if input_dics['min_epi']:
                        if epi_dist < input_dics['min_epi']:
                            del_index.append(sti)
                    if input_dics['max_epi']:
                        if epi_dist > input_dics['max_epi']:
                            del_index.append(sti)
                    if input_dics['min_azi']:
                        if azi < input_dics['min_azi']:
                            del_index.append(sti)
                    if input_dics['max_azi']:
                        if azi > input_dics['max_azi']:
                            del_index.append(sti)

            del_index = list(set(del_index))
            del_index.sort(reverse=True)
            for di in del_index:
                sta_ev_arr = np.delete(sta_ev_arr, (di), axis=0)

            kmlobj.Document.append(
                KML.Style(
                    KML.IconStyle(
                        KML.scale(2.5),
                        KML.heading(0.0),
                    ),
                    id='station'
                ),
            )
            kmlobj.Document.append(
                KML.Style(
                    KML.LineStyle(
                        KML.width(1.0),
                        # KML.color('ff33ccff'),
                        KML.color('2333ccff'),
                    ),
                    id='great_circle_distance'
                ),
            )
            for sti in sta_ev_arr:
                dist, azi, bazi = gps2DistAzimuth(events[ei]['latitude'],
                                                  events[ei]['longitude'],
                                                  float(sti[4]),
                                                  float(sti[5]))
                epi_dist = dist/111.194/1000.
                sta_id = '%s.%s.%s.%s' % (sti[0], sti[1], sti[2], sti[3])
                kmlobj.Document.append(
                    KML.Placemark(
                        KML.name(sta_id),
                        KML.ExtendedData(
                            KML.Data(
                                KML.value('%s' % sta_id),
                                name='StationID'
                            ),
                            KML.Data(
                                KML.value('%s' % epi_dist),
                                name='Distance'
                            ),
                            KML.Data(
                                KML.value('%s' % sti[6]),
                                name='Elevation'
                            ),
                            KML.Data(
                                KML.value('%s' % sti[7]),
                                name='Depth'
                            ),
                            KML.Data(
                                KML.value('%s' % bazi),
                                name='Back-Azimuth'
                            ),
                            KML.Data(
                                KML.value('%s' % azi),
                                name='Azimuth'
                            ),
                            KML.Data(
                                KML.value('%s' % events[ei]['event_id']),
                                name='EventID'
                            ),
                            KML.Data(
                                KML.value('%s' % sti[8]),
                                name='Source'
                            ),
                        ),
                        KML.styleUrl('station'),
                        KML.Point(KML.coordinates(
                            float(sti[5]), ',', float(sti[4]))
                        ),
                    ),
                )
                if input_dics['plot_ray']:
                    kmlobj.Document.append(
                        KML.Placemark(
                            KML.name(sta_id),
                            KML.ExtendedData(
                                KML.Data(
                                    KML.value('%s' % sta_id),
                                    name='StationID'
                                ),
                            ),
                            KML.styleUrl('great_circle_distance'),
                            KML.LineString(KML.coordinates(
                                '%s,%s,0\n'
                                '%s,%s,0' % (float(sti[5]),
                                             float(sti[4]),
                                             events[ei]['longitude'],
                                             events[ei]['latitude'])),
                                KML.tessellate(1)),
                        ),
                    )
    kml_outfile = file(os.path.join(
        'kml_dir',
        'kml_output.kml'), 'w')
    kml_outfile.write(etree.tostring(kmlobj, pretty_print=True))
    sys.exit('[INFO] KML file is stored in ./kml_dir!')
