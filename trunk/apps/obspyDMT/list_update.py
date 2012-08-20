#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#   Filename:  list_update.py
#   Purpose:   list_update main program 
#   Author:    Kasra Hosseini
#   Email:     hosseini@geophysik.uni-muenchen.de
#   License:   GPLv3
#-------------------------------------------------------------------

#for debugging: import ipdb; ipdb.set_trace()

"""
To create the 'list_events.dat', one could use:
$ find `pwd` -name *.2009.*.*
"""

#-----------------------------------------------------------------------
#----------------Import required Modules (Python and Obspy)-------------
#-----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.

# Added this line for python 2.5 compatibility
from __future__ import with_statement
import os
import sys
import shutil
import time
import subprocess
import tarfile

########################################################################
############################# Main Program #############################
########################################################################

def list_update(**kwargs):
    
    """
    list_update: is the function dedicated to the main part of the code.
    """
    
    if not os.path.isfile(os.path.join('.', 'list_events.dat')):
        print '"list_events.dat" could not be found in:'
        print os.path.join('.', 'list_events.dat')
        print sys.exit()
    
    ls_ev_open = open(os.path.join('.', 'list_events.dat'), 'r')
    ls_ev_read = ls_ev_open.readlines()
    ls_ev = []
    for ev_num in ls_ev_read:
        ls_ev.append(ev_num.split('\n')[0])
    
    for i in range(0, len(ls_ev)):
        #subprocess.check_call(['./obspyDMT.py', '--update_all', ls_ev[i], \
        #'--identity', '*.*.*.BH*'])
        #subprocess.check_call(['./obspyDMT.py', '--ic_all', ls_ev[i], '--ic_sac'])
        '''
        print '\n==============='
        print 'Start updating:'
        print ls_ev[i]
        print '==============='
        subprocess.check_call(['./obspyDMT.py', '--update_all', ls_ev[i], \
                                '--identity', '*.*.*.BH*', '--req_parallel'])
        print '\n================'
        print 'Start correcting:'
        print ls_ev[i]
        print '================'
        subprocess.check_call(['./obspyDMT.py', '--ic_all', ls_ev[i], \
                                '--ic_sac', '--ic_parallel'])
        '''
        
        if os.path.isdir(os.path.join(ls_ev[i], 'BH_RAW')):
            print '\n======================'
            print 'Removing the raw data:'
            print os.path.join(ls_ev[i], 'BH_RAW')
            print '======================'
            subprocess.check_call(['rm', '-rf', os.path.join(ls_ev[i], 'BH_RAW')])
        
        if os.path.isfile(os.path.join(ls_ev[i], 'Resp', 'Resp.tar')):
            print '\n====================='
            print 'Opening the tar file:'
            print os.path.join(ls_ev[i], 'Resp', 'Resp.tar')
            print '====================='
            resp_tar = tarfile.open(os.path.join(ls_ev[i], 'Resp', 'Resp.tar'))
            resp_tar.extractall(os.path.join(ls_ev[i], 'Resp'))
            resp_tar.close()
            
            shutil.move(os.path.join(ls_ev[i], 'Resp', 'Resp', '*'), \
                                os.path.join(ls_ev[i], 'Resp'))
            subprocess.check_call(['rm', '-rf', \
                                os.path.join(ls_ev[i], 'Resp', 'Resp')])
        
        print '\n======================='
        print 'Creating a netCDF file:'
        print os.path.join(ls_ev[i], 'BH_RAW')
        print '======================='
        
        subprocess.check_call(['./obspyNC.py', '--ncCreate', ls_ev[i], \
                                '--data_type', 'corrected'])
########################################################################
########################################################################
########################################################################

if __name__ == "__main__":
    
    t1_pro = time.time()
    status = list_update()
    t_pro = time.time() - t1_pro
    
    print'\n------------'
    print "Total Time:"
    print t_pro
    print'------------\n'
    
    # pass the return of main to the command line.
    sys.exit(status)
