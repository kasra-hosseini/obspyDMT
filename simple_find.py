import glob
import os
from obspy.core import read
from datetime import datetime

t1 = datetime.now()

min_lat = -40
max_lat = -10
min_lon = 110
max_lon = 155

address_events = '/import/neptun-radler/hosseini-downloads/KASRA/tmp/management_application/2012-04-15_2012-09-09_5.5_9.9'

list_events = ['20120415_0000015']
#sta_file = open('simple_station_lat_lon.tex', 'a')
#sta_file.close()

for ev in list_events:
    sta_file = open('simple_station_lat_lon' + ev + '.tex', 'a')
    
    ls_stas = glob.glob(os.path.join(address_events, ev, 'BH_RAW', '*.*.*.*'))        
    for st in ls_stas:
        try:
            tr = read(st)[0]
            if min_lat <= tr.stats.sac.stla <= max_lat and min_lon <= tr.stats.sac.stlo <= max_lon:
                sta_file.write(tr.stats.network + '.' + tr.stats.station + '.' + tr.stats.location + '.' + tr.stats.channel + \
                                ' -- ' + str(tr.stats.sac.stlo) + ' -- ' + str(tr.stats.sac.stla) + ' \n')
        except Exception, e:
            print e
            pass
    """
    sta_read = sta_file.readlines()
    
    for i in range(0, len(sta_read)):
        sta_read[i] = sta_read[i].split(' -- ')
    
        if min_lat <= float(sta_read[i][2]) <= max_lat and min_lon <= float(sta_read[i][1]) <= max_lon:
            print sta_read[1]
    sta_file.close()
    """
t2 = datetime.now()
print t2-t1   
