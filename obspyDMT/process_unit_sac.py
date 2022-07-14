# ------------- required Python and obspy modules are imported in this part
from obspy.core import read
import os
import subprocess
import sys
import errno

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
    tr = convert_to_sac(tr, save_path, staev_ar)
    tr.write(save_path, format='SAC')

    p = subprocess.Popen(['sac'],
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    s = \
        'read ' + save_path + '\n' + \
        'rmean' + '\n' + \
        'rtrend' + '\n' + \
        'taper' + '\n' + \
        'fft' + '\n' + \
        'keepam' + '\n' + \
        'p1' + '\n' + \
        'loglog' + '\n' + \
        'xlim 1e-5 100' + '\n' + \
        'p1' + '\n' + \
        'saveimg ' + save_path + '.pdf\n' + \
        'quit\n'

    if sys.version_info > (3, 0):
        out = p.communicate(bytes(s, "utf-8"))
    else:
        out = p.communicate(bytes(s))
    print(out[0])
