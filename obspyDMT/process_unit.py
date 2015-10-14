# Required Python and Obspy modules will be imported in this part.
from obspy.core import read
from obspy import read_inventory
from utils.resample_handler import resample_unit
try:
    from obspy.io.xseed import Parser
except Exception, e:
    from obspy.xseed import Parser
import os

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ===================== YOU CAN CHANGE THE FOLLOWING FUNCTION
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ********* process_unit has the following arguments:
# 1. tr_add: address of one trace in your directory.
# 2. target_path: address of the event that we want to process.
# 3. input_dics: dictionary that contains all the inputs.

# IMPORTANT:
# change the following function as you want. This function will be
# automatically applied to all traces in your database.


def process_unit(tr_add, target_path, input_dics, staev_ar):
    """
    processing unit, adjustable by the user
    :param tr_add: address of one trace in your directory.
    :param target_path: address of the event that we want to process.
    :param input_dics: dictionary that contains all the inputs.
    :return:
    """
    # read the waveform and create an ObsPy Stream object
    st = read(tr_add)

    # in case that there are more than one waveform in the Stream,
    # merge them and create a 'waveform_gap.txt'
    if len(st) > 1:
        st.merge(method=1, fill_value=0, interpolation_samples=0)
        gap_fio = open(os.path.join(target_path, 'info',
                                    'waveform_gap.txt'), 'a+')
        gap_msg = '%s.%s.%s.%s\t%s\n' % (st[0].stats.network,
                                         st[0].stats.station,
                                         st[0].stats.location,
                                         st[0].stats.channel,
                                         'instrument_correction')
        gap_fio.writelines(gap_msg)
        gap_fio.close()

    # Now, there is only one waveform, create a Trace
    tr = st[0]

    corr_unit = input_dics['corr_unit']
    if not os.path.isdir(os.path.join(target_path, 'BH_%s' % corr_unit)):
        os.mkdir(os.path.join(target_path, 'BH_%s' % corr_unit))
    save_path = os.path.join(target_path, 'BH_%s' % corr_unit, tr.id)

    # Resample the data
    if input_dics['resample_corr']:
        print("resampling for: %s" % tr.id)
        tr = resample_unit(tr,
                           des_sr=input_dics['resample_corr'],
                           resample_method=input_dics['resample_method'])
        tr.write(save_path, format='mseed')

    # apply instrument correction
    if input_dics['instrument_correction']:
        instrument_correction(tr, target_path, save_path,
                              input_dics['corr_unit'], input_dics['pre_filt'],
                              input_dics['water_level'])

    if input_dics['waveform_format']:
        waveform_format(save_path, target_path, staev_ar)

# ##################### instrument_correction #################################

def instrument_correction(tr, target_path, save_path, corr_unit, pre_filt,
                          water_level):
    """
    find DATALESS or STXML file for one trace and apply instrument correction
    :param tr:
    :param target_path:
    :param save_path:
    :param corr_unit:
    :param pre_filt:
    :param water_level:
    :return:
    """
    resp_file = os.path.join(target_path, 'Resp', 'DATALESS.%s' % tr.id)
    stxml_file = os.path.join(target_path, 'Resp', 'STXML.%s' % tr.id)

    if os.path.isfile(stxml_file):
        obspy_fullresp_stxml(tr, stxml_file, save_path,
                             corr_unit, pre_filt, water_level,
                             debug=False)
    elif os.path.isfile(resp_file):
        obspy_fullresp_resp(tr, resp_file, save_path,
                            corr_unit, pre_filt, water_level,
                            debug=False)
    else:
        print "%s -- StationXML or Response file does not exist!" % tr.id

# ##################### obspy_fullresp_stxml #################################


def obspy_fullresp_stxml(trace, stxml_file, save_path, unit,
                         bp_filter, water_level, debug=False):
    """
    Apply instrument correction by using StationXML file
    :param trace:
    :param stxml_file:
    :param save_path:
    :param unit:
    :param bp_filter:
    :param water_level:
    :param debug:
    :return:
    """

    if 'dis' in unit.lower():
        unit = 'DISP'
    elif 'vel' in unit.lower():
        unit = 'VEL'
    elif 'acc' in unit.lower():
        unit = 'ACC'
    else:
        unit = unit.upper()
    try:
        if debug:
            print 20*'='
            print 'stationXML file: %s' % stxml_file
            print 'tarce: %s' % trace.id
            print 'save path: %s' % save_path

        # remove the trend
        trace.detrend('linear')
        inv = read_inventory(stxml_file, format="stationxml")
        trace.attach_response(inv)
        trace.remove_response(output=unit,
                              water_level=water_level,
                              pre_filt=eval(bp_filter), zero_mean=True,
                              taper=True, taper_fraction=0.05)
        # Remove the following line to keep the units
        # as it is in the stationXML
        # trace.data *= 1.e9
        trace.write(save_path, format='mseed')

        if unit.lower() == 'disp':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'

        print 'instrument correction to %s for: %s' % (unit_print, trace.id)

    except Exception as error:
        print '[EXCEPTION] %s -- %s' % (trace.id, error)

# ##################### obspy_fullresp_resp ##################################


def obspy_fullresp_resp(trace, resp_file, save_path, unit,
                        bp_filter, water_level, debug=False):
    """
    Apply instrument correction by using response file
    :param trace:
    :param resp_file:
    :param save_path:
    :param unit:
    :param bp_filter:
    :param water_level:
    :param debug:
    :return:
    """

    dataless_parser = Parser(resp_file)
    seedresp = {'filename': dataless_parser, 'units': unit}
    if debug:
        print 20*'='
        print 'stationXML file: %s' % resp_file
        print 'tarce: %s' % trace.id
        print 'save path: %s' % save_path
    # remove the trend
    trace.detrend('linear')
    try:
        trace.simulate(seedresp=seedresp, paz_remove=None, paz_simulate=None,
                       remove_sensitivity=True, simulate_sensitivity=False,
                       water_level=water_level,
                       zero_mean=True, taper=True,
                       taper_fraction=0.05, pre_filt=eval(bp_filter),
                       pitsasim=False, sacsim=True)
        # Remove the following line since we want to keep
        # the units as it is in the stationXML
        # trace.data *= 1.e9
        trace.write(save_path, format='mseed')

        if unit.lower() == 'dis':
            unit_print = 'displacement'
        elif unit.lower() == 'vel':
            unit_print = 'velocity'
        elif unit.lower() == 'acc':
            unit_print = 'acceleration'
        else:
            unit_print = 'UNKNOWN'
        print 'instrument correction to %s for: %s' % (unit_print, trace.id)

    except Exception as error:
        print '[EXCEPTION] %s -- %s' % (trace.id, error)

def waveform_format(tr_add, target_path, sta_ev_arr):
    # read the waveform and create an ObsPy Stream object
    st = read(tr_add)

    # in case that there are more than one waveform in the Stream,
    # merge them and create a 'waveform_gap.txt'
    if len(st) > 1:
        st.merge(method=1, fill_value=0, interpolation_samples=0)
        gap_fio = open(os.path.join(target_path, 'info',
                                    'waveform_gap.txt'), 'a+')
        gap_msg = '%s.%s.%s.%s\t%s\n' % (st[0].stats.network,
                                         st[0].stats.station,
                                         st[0].stats.location,
                                         st[0].stats.channel,
                                         'format_converter')
        gap_fio.writelines(gap_msg)
        gap_fio.close()

    # Now, there is only one waveform, create a Trace
    tr = st[0]
    tr.write(tr_add, format='SAC')
    tr = read(tr_add)[0]
    try:
        tr.stats.sac.stla = float(sta_ev_arr[4])
    except Exception, e:
        pass
    try:
        tr.stats.sac.stlo = float(sta_ev_arr[5])
    except Exception, e:
        pass
    try:
        tr.stats.sac.stel = float(sta_ev_arr[6])
    except Exception, e:
        pass
    try:
        tr.stats.sac.stdp = float(sta_ev_arr[7])
    except Exception, e:
        pass
    try:
        tr.stats.sac.evla = float(sta_ev_arr[9])
    except Exception, e:
        pass
    try:
        tr.stats.sac.evlo = float(sta_ev_arr[10])
    except Exception, e:
        pass
    try:
        tr.stats.sac.evdp = float(sta_ev_arr[11])
    except Exception, e:
        pass
    try:
        tr.stats.sac.mag = float(sta_ev_arr[12])
    except Exception, e:
        pass
    tr.write(tr_add, format='SAC')
