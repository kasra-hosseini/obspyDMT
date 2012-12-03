import sys
from obspy.core import read
import matplotlib.pyplot as plt
import numpy as np
from obspy.signal.util import prevpow2

tr = read(sys.argv[1])[0]
#tr.resample(20.0)
#tr.filter('lowpass', freq = 2.0)
#tr.filter('highpass', freq = 0.001)

samp_rate = tr.stats.sampling_rate
nyquist = samp_rate/2.

#tr_fft = np.fft.fft(tr.data)
#fft_power_amp = tr_fft.real**2 + tr_fft.imag**2
#fft_amp = np.sqrt(fft_power_amp)
#tr.data -= tr.data.mean()

num = prevpow2((len(tr.data)))
fft_amp_new = np.fft.rfft(tr.data, n = num)
freq = np.linspace(0, samp_rate, num)

#plt.plot(np.log10(freq[0:(len(freq)/2)]), np.log10(fft_amp[0:(len(freq)/2)]))
#plt.plot(np.log10(freq[0:(len(freq)/2)]), abs(fft_amp_new[0:(len(freq)/2)]))
plt.plot(np.log10(freq[0:(len(freq)/2)]), np.log10(abs(fft_amp_new[0:(len(freq)/2)])))
plt.show()
