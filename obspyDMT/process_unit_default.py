# ------------- required Python and obspy modules are imported in this part
from obspy.core import read
import os
import errno

from .utils.instrument_handler import instrument_correction
from .utils.resample_handler import resample_unit
from .utils.utility_codes import convert_to_sac
# -----------------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ===================== YOU CAN CHANGE THE FOLLOWING FUNCTION =================
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# * IMPORTANT *
# The following function (process_unit) is in the waveform level.
# This means that you can write your process unit for one trace, and
# obspyDMT uses this function to pre-process all your waveforms,
# either right after retrieval or as a separate step:
# obspyDMT --datapath /your/dataset --local

# ========== process_unit has the following arguments:
# Use the following parameters to write your process_unit:
# 1. tr_add: address of one trace in your dataset. You can use that to
# read in the data.
# 2. target_path: address of the event that should be processed.
# 3. input_dics: dictionary that contains all the inputs.
# 4. staev_ar: an array that contains the following information:
# net, sta, loc, cha, station latitude, station longitude, station elevation,
# station depth


def process_unit(tr_add, target_path, input_dics, staev_ar):
    """
    processing unit, adjustable by the user
    :param tr_add: address of one trace in your dataset. You can use that to
    read in the data.
    :param target_path: address of the event that should be processed.
    :param input_dics: dictionary that contains all the inputs.
    :param staev_ar: an array that contains the following information:
           net, sta, loc, cha, station latitude, station longitude,
           station elevation, station depth
    :return:
    """
    # -------------- read the waveform, deal with gaps ------------------------
    # 1. read the waveform and create an obspy Stream object
    try:
        st = read(tr_add)
    except Exception as error:
        print('WARNING: %s' % error)
        return False
    # 2. in case that there are more than one waveform in a Stream (this can
    # happen due to some gaps in the waveforms) merge them.
    if len(st) > 1:
        try:
            st.merge(method=1, fill_value=0, interpolation_samples=0)
        except Exception as error:
            print('WARNING: %s' % error)
            return False
    # 3. Now, there is only one waveform, create a Trace
    tr = st[0]

    # -------------- path to save the processed waveform ----------------------
    # Before entering to the actual processing part of the code,
    # we define some paths to be used later:
    # you can adjust it as you want, here is just one example
    
    # If pathlib is installed, one can use: (suggested by ghraecakter)
    # pathlib.Path(os.path.join(target_path, 'processed')).mkdir(exist_ok=True)
    try:
        os.mkdir(os.path.join(target_path, 'processed'))
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    # save_path is the address that will be used to save the processed data
    save_path = os.path.join(target_path, 'processed', tr.id)
    if os.path.isfile(save_path) and (not input_dics['force_process']):
        return False

    # -------------- PROCESSING -----------------------------------------------
    # * resample the data
    # input_dics['sampling_rate'] determines the desired sampling rate
    if input_dics['sampling_rate']:
        print("resample %s from %s to %sHz" % (tr.id,
                                               tr.stats.sampling_rate,
                                               input_dics['sampling_rate']))
        tr = resample_unit(tr,
                           des_sr=input_dics['sampling_rate'],
                           resample_method=input_dics['resample_method'])

    # * apply instrument correction which consists of:
    # 1. removing the trend of the trace (remove_trend)
    # 2. remove the mean (zero_mean)
    # 3. taper (taper, taper_fraction [e.g., 0.05: 5%])
    # 4. apply pre-filter based on input_dics['pre_filt']
    # 5. apply instrument correction
    # all the above parameters are adjustable
    if input_dics['instrument_correction']:
        tr = instrument_correction(tr, target_path, save_path,
                                   input_dics['corr_unit'],
                                   input_dics['pre_filt'],
                                   input_dics['water_level'],
                                   zero_mean=True,
                                   taper=True,
                                   taper_fraction=0.05,
                                   remove_trend=True)

    # -------------- OUTPUT ---------------------------------------------------
    if not tr:
        pass
    elif input_dics['waveform_format'] == 'sac':
        tr = convert_to_sac(tr, save_path, staev_ar)
        tr.write(save_path, format='SAC')
    else:
        tr.write(save_path, format='mseed')
