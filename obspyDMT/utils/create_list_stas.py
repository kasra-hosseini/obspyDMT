#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  create_list_stas.py
#   Purpose:   simple code to create list_stas to be used by DMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from obspy import UTCDateTime
from obspy.fdsn import Client


# ########################## INPUT
req_client = "RESIF"
starttime = "2012-01-01"
endtime = "2013-01-01"
network = "YV"
station = "*"
location = '*'
channel = '*H*'

file_name = 'list_stas_created.txt'
# ########################## END INPUT

client = Client(req_client)
starttime = UTCDateTime(starttime)
endtime = UTCDateTime(endtime)
inv = client.get_stations(network=network, station=station,
                          location=location, channel=channel,
                          starttime=starttime, endtime=endtime,
                          level='channel')
content = inv.get_contents()
chans = content['channels']

fio = open(file_name, 'w')
for _i in range(len(chans)):
    net, sta, loc, cha = chans[_i].split('.')
    target_channel = inv.select(net, sta, loc, cha)
    coord_chan = target_channel.get_coordinates('%s.%s.%s.%s'
                                                % (net, sta, loc, cha))

    fio.writelines('%s  %s  %s  %s  %s  %s  %s  %s\n'
                   % (sta, net, loc, cha, coord_chan['latitude'],
                      coord_chan['longitude'], coord_chan['elevation'],
                      coord_chan['local_depth']))

fio.close()

#fio = open('list_stas_created.txt', 'w')
#
#for i in range(len(inv)):
#    if not inv[0][i].code:
#        sta net location channel lat lon elevation depth
#        fio.writelines('%s  %s  ??  %s  %s  %s  %s  %s\n' \
#                % (inv[0][i].code, net, ))
