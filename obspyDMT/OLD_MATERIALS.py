# -----------------------------------------------------------------------
# ------------------------- OLD MATERIALS -------------------------------
# -----------------------------------------------------------------------

# ---------------------------IMPORT PPROCESS
#try:
#    import pprocess
#except Exception as error:
#    print "\n*************************************************************************"
#    print "Unable to import pprocess. Parallel retrieving/processing is not possible"
#    print "Error: %s" % error
#    print "*************************************************************************\n"

#if input['req_parallel'] == 'Y' or input['ic_parallel'] == 'Y':
#    try:
#        import pprocess
#    except Exception as error:
#        print '***************************************************'
#        print 'WARNING:'
#        print 'ppross is not installed on your machine!'
#        print 'for more info: http://pypi.python.org/pypi/pprocess'
#        print '\nobspyDMT will work in Serial mode.'
#        print 'ERROR: %s' % error
#        print '***************************************************'
#        input['req_parallel'] = 'N'
#        input['ic_parallel'] = 'N'

# ---------------------------PARALLEL BULK REQUESTS
#if input['req_parallel'] == 'Y':
#    num_lines=1000; bulk_enum=0; bulk_num_files=1
#    bulkfile_new=open(os.path.join(add_event[i], 'info', 'bulk_split_0.txt'), 'wb')
#    for line in fileinput.FileInput(os.path.join(add_event[i], 'info', 'bulkdata.txt')):
#        bulkfile_new.write(line)
#        bulk_enum+=1
#        if bulk_enum%num_lines==0:
#            bulkfile_new.close()
#            bulk_num_files+=1
#            bulkfile_new=open(os.path.join(add_event[i], 'info', \
#                               "bulk_split_%d.txt"%(bulk_enum/num_lines)), 'wb')
#    bulkfile_new.close()
#
#    print '\nbulkdataselect request is sent for event ' + \
#                            str(i+1) + '/' + str(len(events))
#    parallel_results = pprocess.Map(limit=2)
#    parallel_job = parallel_results.manage(pprocess.MakeParallel(bulk_download_core))
#    for bulk_num in range(0, bulk_num_files):
#        parallel_job(os.path.join(add_event[i], 'info', \
#                "bulk_split_%d.txt"%(bulk_num)), add_event[i])
#    parallel_results.finish()
#    if input['response'] == 'N':
#        input['req_parallel'] = 'N'
#        bulk_parallel_tmp_flag = True
#
#else:
#    print '\nbulkdataselect request is sent for event: ' + \
#                            str(i+1) + '/' + str(len(events))
#    bulk_st = client_iris.bulkdataselect(bulk_file)
#    print 'Saving the retrieved waveforms...',
#    for m in range(0, len(bulk_st)):
#        bulk_st_info = bulk_st[m].stats
#        bulk_st[m].write(os.path.join(add_event[i], 'BH_RAW', \
#            bulk_st_info['network'] + '.' + \
#            bulk_st_info['station'] + '.' + \
#            bulk_st_info['location'] + '.' + \
#            bulk_st_info['channel']), 'MSEED')
#    print 'DONE'

#try:
#    if bulk_parallel_tmp_flag:
#        input['req_parallel'] = 'Y'
#except:
#    pass

# ------------------------- IRIS and ARC parallel pprocess
#parallel_results = pprocess.Map(limit=input['req_np'], reuse=1)
#parallel_job = parallel_results.manage(pprocess.MakeReusable(IRIS_download_core))
#for j in range(len_req_iris):
#    parallel_job(i=i, j=j, dic=dic, type=type, len_events=len(events), events=events, add_event=add_event,
#                 Sta_req=Sta_req, input=input, client_fdsn=client_fdsn)
#parallel_results.finish()

#parallel_results = pprocess.Map(limit=input['req_np'], reuse=1)
#parallel_job = parallel_results.manage(pprocess.MakeReusable(ARC_download_core))
#for j in range(len_req_arc):
#    parallel_job(i=i, j=j, dic=dic, type=type, len_events=len(events), events=events, add_event=add_event,
#                 Sta_req=Sta_req, input=input)
#parallel_results.finish()

# ------------------------- IC parallel pprocess
# Following methods can also be used:
#parallel_results = pprocess.Queue(limit=input['req_np'])
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IC_core))
#parallel_results = pprocess.Map(limit=input['req_np'], continuous=1)
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IC_core))

# ------------------------- Instrument Correction:
## Removing the trend
# rt_c = RTR(stream = ls_saved_stas, degree = 2)
# tr = read(ls_saved_stas)[0]
# tr.data = rt_c

## Tapering
#taper = invsim.cosTaper(len(tr.data))
#tr.data *= taper

#        if input['ic_sac_full'] == 'Y':
#
#            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
#                                        ls_saved_stas.split('/')[-1])
#
#            SAC_fullresp(trace = ls_saved_stas, resp_file = resp_file, \
#                address = address, BH_file = BH_file, unit = input['corr_unit'], \
#                BP_filter = input['pre_filt'], inform = inform)
#
#        if input['ic_paz'] == 'Y':
#            """
#            paz_file = os.path.join(address, 'Resp', 'PAZ' + '.' + \
#                                ls_saved_stas.split('/')[-1] + '.' + 'full')
#
#            SAC_PAZ(trace = ls_saved_stas, paz_file = paz_file, \
#                address = address, BH_file = BH_file, unit = input['corr_unit'], \
#                BP_filter = input['pre_filt'], inform = inform)
#            """
#            """
#            rt_c = RTR(stream = ls_saved_stas, degree = 2)
#            tr = read(ls_saved_stas)[0]
#            tr.data = rt_c
#
#            # Tapering
#            taper = invsim.cosTaper(len(tr.data))
#            tr.data *= taper
#
#            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
#                                        ls_saved_stas.split('/')[-1])
#
#            obspy_PAZ(trace = tr, resp_file = resp_file, \
#                Address = os.path.join(address, BH_file), \
#                clients = clients, unit = input['corr_unit'], \
#                BP_filter = input['pre_filt'], inform = inform)
#            """
#
#            #if clients == 'iris':
#            #    paz_file = os.path.join(address, 'Resp', 'PAZ' + '.' + \
#            #                    ls_saved_stas.split('/')[-1] + '.' + 'full')
#
#            #    SAC_PAZ(trace = ls_saved_stas, paz_file = paz_file, \
#            #        address = address, BH_file = BH_file, unit = input['corr_unit'], \
#            #        BP_filter = input['pre_filt'], inform = inform)
#
#            #if clients == 'arc':
#
#            print "instrument correction using PAZ"
#            rt_c = RTR(stream = ls_saved_stas, degree = 2)
#            tr = read(ls_saved_stas)[0]
#            tr.data = rt_c
#
#            # Tapering
#            taper = invsim.cosTaper(len(tr.data))
#            tr.data *= taper
#
#            resp_file = os.path.join(address, 'Resp', 'RESP' + '.' + \
#                                        ls_saved_stas.split('/')[-1])
#
#            obspy_PAZ(trace = tr, resp_file = resp_file, \
#                Address = os.path.join(address, BH_file), \
#                clients = clients, unit = input['corr_unit'], \
#                BP_filter = input['pre_filt'], inform = inform)
#
#            """
#            rt_c = RTR(stream = ls_saved_stas, degree = 2)
#            tr = read(ls_saved_stas)[0]
#            tr.data = rt_c
#
#            # Tapering
#            taper = invsim.cosTaper(len(tr.data))
#            tr.data *= taper
#
#            paz_file_open = open(os.path.join(address, 'Resp', 'PAZ' + '.' + \
#                            ls_saved_stas.split('/')[-1] + '.' + 'paz'))
#            paz_file = pickle.load(paz_file_open)
#
#            paz_dic = {\
#            'poles': paz_file['poles'], \
#            'zeros': paz_file['zeros'], \
#            'gain': paz_file['gain']}
#
#            obspy_PAZ(trace = tr, paz_dic = paz_dic, \
#                Address = os.path.join(address, BH_file), unit = input['corr_unit'], \
#                BP_filter = input['pre_filt'], inform = inform)
#            """
#

####################### RTR #############################################
#
#
#def RTR(stream, degree = 2):
#    """
#    Remove the trend by Fitting a linear function to the trace
#    with least squares and subtracting it
#    """
#
#    raw_f = read(stream)
#    t = []
#    b0 = 0
#    inc = []
#
#    b = raw_f[0].stats['starttime']
#
#    for i in range(0, raw_f[0].stats['npts']):
#        inc.append(b0)
#        b0 = b0+1.0/raw_f[0].stats['sampling_rate']
#        b0 = round(b0, 4)
#
#    A = np.vander(inc, degree)
#    (coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, raw_f[0].data)
#
#    f = np.poly1d(coeffs)
#    y_est = f(inc)
#    rt_c = raw_f[0].data-y_est
#
#    return rt_c

####################### SAC_fullresp ####################################
#
#def SAC_fullresp(trace, resp_file, address, BH_file = 'BH', unit = 'DIS', \
#                    BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
#
#    """
#    This script runs SAC program for instrument correction
#    Instrument Correction will be done for all waveforms in the BH_RAW folder
#    Response files will be loaded from Resp folder
#
#    Instrument Correction has three main steps:
#    1) RTR: remove the trend
#    2) tapering
#    3) pre-filtering and deconvolution of Resp file from Raw counts
#    """
#
#    try:
#
#        trace_info = trace.split('/')[-1].split('.')
#
#        if unit.lower() == 'dis':
#            unit_sac = 'NONE'
#        if unit.lower() == 'vel':
#            unit_sac = 'VEL'
#        if unit.lower() == 'acc':
#            unit_sac = 'ACC'
#
#        BP_filter_tuple = eval(BP_filter)
#        freqlim = str(BP_filter_tuple[0]) + ' ' +  str(BP_filter_tuple[1]) \
#                    + ' ' + str(BP_filter_tuple[2]) + ' ' + \
#                    str(BP_filter_tuple[3])
#
#        pwd = commands.getoutput('pwd')
#        os.chdir(os.path.join(address, BH_file))
#
#        p = subprocess.Popen(['sac'],
#                             stdout = subprocess.PIPE,
#                             stdin  = subprocess.PIPE,
#                             stderr = subprocess.STDOUT )
#
#        s = \
#        'setbb resp ../Resp/' + resp_file.split('/')[-1] + '\n' + \
#        'read ../BH_RAW/' + trace.split('/')[-1] + '\n' + \
#        'rtrend' + '\n' + \
#        'taper' + '\n' + \
#        'rmean' + '\n' + \
#        'trans from evalresp fname %resp to ' + unit_sac + ' freqlim ' + freqlim + '\n' + \
#        'write ' + unit.lower() + '.' + trace_info[1] + '.' + trace_info[2] + \
#                                            '.' + trace_info[3] + '\n' + \
#        'quit\n'
#
#        out = p.communicate(s)
#        print out[0]
#        if input['mseed'] == 'Y':
#            tr_mseed = read('%s.%s.%s.%s' %(unit.lower(), trace_info[1],
#                                                trace_info[2], trace_info[3]))
#            tr_mseed.write('%s.%s.%s.%s' %(unit.lower(), trace_info[1],
#                                                trace_info[2], trace_info[3]),
#                                                format='MSEED')
#        os.chdir(pwd)
#
#        if unit.lower() == 'dis':
#            unit_print = 'displacement'
#        if unit.lower() == 'vel':
#            unit_print = 'velocity'
#        if unit.lower() == 'acc':
#            unit_print = 'acceleration'
#
#        print inform + ' -- Instrument Correction to ' + unit_print + \
#                        ' for: ' + trace_info[0] + '.' + trace_info[1] + \
#                        '.' + trace_info[2] + '.' + trace_info[3]
#        print "-----------------------------------"
#
#    except Exception as e:
#        print inform + ' -- ' + str(e)
#
####################### readRESP ########################################
#
#def readRESP(resp_file, unit):
#
#    resp_open = open(resp_file)
#    resp_read = resp_open.readlines()
#
#    check_resp = []
#
#    for resp_line in resp_read:
#        if "velocity in meters per second" in resp_line.lower() or \
#            "velocity in meters/second" in resp_line.lower() or \
#            "m/s -" in resp_line.lower():
#            check_resp.append('M/S')
#
#        elif "m/s**2 - acceleration" in resp_line.lower():
#            check_resp.append('M/S**2')
#
#    if check_resp == []:
#        print '\n***************************************************************'
#        print 'The response file is not in the right dimension (M/S) or (M/S**2)'
#        print 'This could cause problems in the instrument correction.'
#        print 'Please check the response file:'
#        print resp_file
#        print '*****************************************************************'
#        sys.exit()
#
#    gain_num = []
#    A0_num = []
#    poles_num = []
#    poles = []
#    zeros = []
#    zeros_num = []
#    #if clients == 'iris':
#    if resp_read[0].find('obspy.xseed') == -1:
#        for i in range(0, len(resp_read)):
#            if resp_read[i].find('B058F04') != -1:
#                gain_num.append(i)
#            if resp_read[i].find('B053F07') != -1:
#                A0_num.append(i)
#            if resp_read[i].find('B053F10-13') != -1:
#                zeros_num.append(i)
#            if resp_read[i].find('B053F15-18') != -1:
#                poles_num.append(i)
#
#    #elif clients == 'arc':
#    elif resp_read[0].find('obspy.xseed') != -1:
#        for i in range(0, len(resp_read)):
#            if resp_read[i].find('B058F04') != -1:
#                gain_num.append(i)
#            if resp_read[i].find('B043F08') != -1:
#                A0_num.append(i)
#            if resp_read[i].find('B043F11-14') != -1:
#                zeros_num.append(i)
#            if resp_read[i].find('B043F16-19') != -1:
#                poles_num.append(i)
#
#    list_sensitivity = resp_read[gain_num[-1]].split('\n')[0].split(' ')
#    list_new_sensitivity = [x for x in list_sensitivity if x]
#    sensitivity = eval(list_new_sensitivity[-1])
#
#    list_A0 = resp_read[A0_num[0]].split('\n')[0].split(' ')
#    list_new_A0 = [x for x in list_A0 if x]
#    A0 = eval(list_new_A0[-1])
#
#
#    for i in range(0, len(poles_num)):
#
#        list_poles = resp_read[poles_num[i]].split('\n')[0].split(' ')
#        list_new_poles = [x for x in list_poles if x]
#
#        poles_r = eval(list_new_poles[-4])
#        poles_i = eval(list_new_poles[-3])
#        poles.append(complex(poles_r, poles_i))
#
#    for i in range(0, len(zeros_num)):
#
#        list_zeros = resp_read[zeros_num[i]].split('\n')[0].split(' ')
#        list_new_zeros = [x for x in list_zeros if x]
#
#        zeros_r = eval(list_new_zeros[-4])
#        zeros_i = eval(list_new_zeros[-3])
#        zeros.append(complex(zeros_r, zeros_i))
#
#    if check_resp[0] == 'M/S':
#        if unit.lower() == 'dis':
#            zeros.append(0j)
#        #if unit.lower() == 'vel':
#        #    zeros = [0j, 0j]
#        #if unit.lower() == 'acc':
#        #    zeros = [0j]
#    elif check_resp[0] == 'M/S**2':
#        if unit.lower() == 'dis':
#            zeros.append(0j)
#            zeros.append(0j)
#
#    paz = {\
#    'poles': poles,
#    'zeros': zeros,
#    'gain': A0,
#    'sensitivity': sensitivity\
#    }
#
#    return paz
#
####################### obspy_PAZ #######################################
#
#def obspy_PAZ(trace, resp_file, Address, clients, unit = 'DIS', \
#            BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
#
#    try:
#
#        paz = readRESP(resp_file, unit)
#
#        trace.data = seisSim(data = trace.data, \
#            samp_rate = trace.stats.sampling_rate,paz_remove=paz, \
#            paz_simulate = None, remove_sensitivity=True, \
#            simulate_sensitivity = False, water_level = 600.0, \
#            zero_mean = True, taper = False, pre_filt=eval(BP_filter), \
#            seedresp=None, pitsasim=False, sacsim = True)
#
#        trace.data *= 1.e9
#
#        trace_identity = trace.stats['station'] + '.' + \
#                trace.stats['location'] + '.' + trace.stats['channel']
#        if input['mseed'] == 'N':
#            trace.write(os.path.join(Address, unit.lower() + '.' +
#                                        trace_identity), format = 'SAC')
#        else:
#            trace.write(os.path.join(Address, unit.lower() + '.' +
#                                        trace_identity), format = 'MSEED')
#
#        if unit.lower() == 'dis':
#            unit_print = 'displacement'
#        if unit.lower() == 'vel':
#            unit_print = 'velocity'
#        if unit.lower() == 'acc':
#            unit_print = 'acceleration'
#
#        print inform + ' -- Instrument Correction to ' + unit_print + \
#                                            ' for: ' + trace_identity
#
#    except Exception as e:
#        print inform + ' -- ' + str(e)
#
####################### SAC_PAZ #########################################
#
#def SAC_PAZ(trace, paz_file, address, BH_file = 'BH', unit = 'DIS', \
#                    BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
#
#    """
#    This script runs SAC program for instrument correction (PAZ)
#    Instrument Correction will be done for all waveforms in the BH_RAW folder
#    PAZ files will be loaded from Resp folder
#
#    Instrument Correction has three main steps:
#    1) RTR: remove the trend
#    2) tapering
#    3) pre-filtering and deconvolution of PAZ from Raw counts
#    """
#
#    try:
#
#        trace_info = trace.split('/')[-1].split('.')
#
#        if unit.lower() == 'dis':
#            unit_sac = 'NONE'
#        if unit.lower() == 'vel':
#            unit_sac = 'VEL'
#        if unit.lower() == 'acc':
#            unit_sac = 'ACC'
#
#        BP_filter_tuple = eval(BP_filter)
#        freqlim = str(BP_filter_tuple[0]) + ' ' +  str(BP_filter_tuple[1]) \
#                    + ' ' + str(BP_filter_tuple[2]) + ' ' + \
#                    str(BP_filter_tuple[3])
#
#        pwd = commands.getoutput('pwd')
#        os.chdir(os.path.join(address, BH_file))
#
#        p = subprocess.Popen(['sac'],
#                             stdout = subprocess.PIPE,
#                             stdin  = subprocess.PIPE,
#                             stderr = subprocess.STDOUT )
#
#        s = \
#        'setbb pzfile ../Resp/' + paz_file.split('/')[-1] + '\n' + \
#        'read ../BH_RAW/' + trace.split('/')[-1] + '\n' + \
#        'rtrend' + '\n' + \
#        'taper' + '\n' + \
#        'rmean' + '\n' + \
#        'trans from polezero s %pzfile to ' + unit_sac + ' freqlim ' + freqlim + '\n' + \
#        'MUL 1.0e9' + '\n' + \
#        'write ' + unit.lower() + '.' + trace_info[1] + '.' + trace_info[2] + \
#                                            '.' + trace_info[3] + '\n' + \
#        'quit\n'
#
#        out = p.communicate(s)
#        print out[0]
#        if input['mseed'] == 'Y':
#            tr_mseed = read('%s.%s.%s.%s' %(unit.lower(), trace_info[1],
#                                                trace_info[2], trace_info[3]))
#            tr_mseed.write('%s.%s.%s.%s' %(unit.lower(), trace_info[1],
#                                                trace_info[2], trace_info[3]),
#                                                format='MSEED')
#        os.chdir(pwd)
#
#        if unit.lower() == 'dis':
#            unit_print = 'displacement'
#        if unit.lower() == 'vel':
#            unit_print = 'velocity'
#        if unit.lower() == 'acc':
#            unit_print = 'acceleration'
#
#        print inform + ' -- Instrument Correction to ' + unit_print + \
#                        ' for: ' + trace_info[0] + '.' + trace_info[1] + \
#                        '.' + trace_info[2] + '.' + trace_info[3]
#
#    except Exception as e:
#        print inform + ' -- ' + str(e)
#"""
####################### obspy_PAZ #######################################
#
#def obspy_PAZ(trace, paz_dic, Address, unit = 'DIS', \
#            BP_filter = (0.008, 0.012, 3.0, 4.0), inform = 'N/N'):
#
#    date = trace.stats['starttime']
#
#    try:
#
#        trace.data = seisSim(data = trace.data, \
#            samp_rate = trace.stats.sampling_rate,paz_remove=paz_dic, \
#            paz_simulate = None, remove_sensitivity=False, \
#            simulate_sensitivity = False, water_level = 600.0, \
#            zero_mean = True, taper = False, pre_filt=eval(BP_filter), \
#            seedresp=None, pitsasim=False, sacsim = False)
#
#        trace_identity = trace.stats['station'] + '.' + \
#                trace.stats['location'] + '.' + trace.stats['channel']
#        trace.write(os.path.join(Address, unit.lower() + '.' + \
#                                        trace_identity), format = 'SAC')
#
#        if unit.lower() == 'dis':
#            unit_print = 'displacement'
#        if unit.lower() == 'vel':
#            unit_print = 'velocity'
#        if unit.lower() == 'acc':
#            unit_print = 'acceleration'
#
#        print inform + ' -- Instrument Correction to ' + unit_print + \
#                                            ' for: ' + trace_identity
#
#    except Exception, e:
#        print inform + ' -- ' + str(e)
#"""
# ------------------------- END Instrument Correction:

# ###################### XML_list_avail ##################################
#
#
# def XML_list_avail(xmlfile):
#
#     """
#     This module changes the XML file got from availability to a list
#     """
#
#     sta_obj = objectify.XML(xmlfile)
#     sta_req = []
#
#     for i in range(0, len(sta_obj.Station)):
#
#         station = sta_obj.Station[i]
#         net = station.get('net_code')
#         sta = station.get('sta_code')
#
#         lat = str(station.Lat)
#         lon = str(station.Lon)
#         ele = str(station.Elevation)
#
#         for j in range(0, len(station.Channel)):
#             cha = station.Channel[j].get('chan_code')
#             loc = station.Channel[j].get('loc_code')
#
#             sta_req.append([net, sta, loc, cha, lat, lon, ele])
#
#     return sta_req


# ------------------------- TRASH:
# ------------------------- Parallel methods
#!! Still do not know which one is the best:
#parallel_results = pprocess.Queue(limit=input['req_np'])
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IRIS_download_core))
#parallel_results = pprocess.Map(limit=input['req_np'])
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IRIS_download_core))
#parallel_results = pprocess.Map(limit=input['req_np'], continuous=1)
#parallel_job = parallel_results.manage(pprocess.MakeParallel(IRIS_download_core))

#parallel_len_req_iris = range(0, len_req_iris)
#lol = [parallel_len_req_iris[n:n+input['req_np']] for n in range(0, len(parallel_len_req_iris), input['req_np'])]
#import ipdb; ipdb,set_trace()
#jobs = []
#for j in range(0, len_req_iris):
#    p = multiprocessing.Process(target=IRIS_download_core,\
#                args=(i, j, dic, type, \
#                        len_events, \
#                        events, add_event, \
#                        Sta_req, input,))
#    jobs.append(p)
#
#for l in range(0, len(lol)):
#    for ll in lol[l]:
#        jobs[ll].start()
#    jobs[ll].join()
#
# ------------------------- END Parallel methods
# ------------------------- END TRASH: