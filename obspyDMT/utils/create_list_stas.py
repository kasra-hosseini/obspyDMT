#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  create_list_stas.py
#   Purpose:   simple code to create list_stas to be used by DMT
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GNU Lesser General Public License, Version 3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from obspy import UTCDateTime
from obspy.fdsn import Client
from plotting_tools import get_coordinates


# ########################## INPUT
req_client = "RESIF"
starttime = None
endtime = None
network = "YV"
station = "*"
location = '*'
channel = '*H*'

file_name = 'list_stas_created.txt'
# ########################## END INPUT

client = Client(req_client)
if starttime:
    starttime = UTCDateTime(starttime)
if endtime:
    endtime = UTCDateTime(endtime)
inv = client.get_stations(network=network, station=station,
                          location=location, channel=channel,
                          starttime=starttime, endtime=endtime,
                          level='channel')
content = inv.get_contents()
chans = list(set(content['channels']))
chans.sort()

net_inv = inv.networks[0]

fio = open(file_name, 'w')
for _i in range(len(chans)):
    net, sta, loc, cha = chans[_i].split('.')
    try:
        coord_chan = get_coordinates(net_inv, chans[_i], None)
        fio.writelines('%s  %s  %s  %s  %s  %s  %s  %s\n'
                       % (sta, net, loc, cha, coord_chan['latitude'],
                          coord_chan['longitude'], coord_chan['elevation'],
                          coord_chan['local_depth']))
    except Exception, e:
        fio.writelines('%s  %s  %s  %s  %s  %s  %s  %s\n'
                       % (sta, net, loc, cha, 'XXX', 'XXX', 'XXX', 'XXX'))


fio.close()
