#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  early_warning.py
#   Purpose:   Automatic data processing for earthquake parameter estimation
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------
from obspy import readEvents, UTCDateTime
from obspy.clients.fdsn import Client as Client_fdsn
import os
import time

from util_early_warning import create_dmt_commands, plot_src_rcv_pairs
from util_early_warning import plot_all_src

# =========== INPUTS ============
min_mag = 2.0
# waveform length in second
waveform_length = 1000.
min_req_stations = 5.
sleep_time_original = 60.
remote_add = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.quakeml"
web_address = "hosseini@venus:/home/hosseini/public_html/early_warning"
# ===============================

print "\n################ EARLY WARNING ########################\n\n"
print "[INFO] initializing FDSN client...",
client_fdsn = Client_fdsn(base_url='IRIS')
print "DONE"

# iterate_flag should be kept to True (just for debugging purposes)
iterate_flag = True
resources_id = []
resources_done = []
all_events = []
while iterate_flag:
    # Address for FEED in USGS
    all_events_recent = readEvents(remote_add, format='QUAKEML')
    passed_events = all_events_recent.filter('magnitude >= %s' % min_mag)
    if len(passed_events) > 0:
        dmt_commands, resources_id, resources_done, all_events = \
            create_dmt_commands(passed_events, resources_id, resources_done,
                                all_events, waveform_length,
                                min_req_stations, client_fdsn)
        if len(dmt_commands) > 0:
            for dmt_command in dmt_commands:
                os.system(dmt_command[0])
                resources_done = plot_src_rcv_pairs(all_events, dmt_command,
                                                    resources_done,
                                                    min_req_stations)
            plot_all_src(all_events)
            print "[INFO] synchronizing with the server!"
            os.system("rsync -a ./events %s" % web_address)
    else:
        print "[INFO] no new event was found: %s" % UTCDateTime.now()
    del passed_events
    print "[INFO] recheck in %s sec" % sleep_time_original
    time.sleep(sleep_time_original)
