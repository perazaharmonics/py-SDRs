import numpy as np
import matplotlib.pyplot as plt
"""
Description: This script calculates the PSD of a signal using the a windowed FFT

1. Take the FFT of our samples. If we have x samples, the FFT size will be the length of x by default. Let’s use the first 1024 samples as an example to create a 1024-size FFT. The output will be 1024 complex floats.

2. Take the magnitude of the FFT output, which provides us 1024 real floats.

3. Square the resulting magnitude to get power.

4. Normalize: divide by the FFT size (N) and sample rate (Fs).

5. Convert to dB using 10 \log_{10}(); we always view PSDs in log scale.

6. Perform an FFT shift, covered in the previous chapter, to move “0 Hz” in the center and negative frequencies to the left of center.
"""

Fs = 2800 #sample rate
Ts = 1 / Fs # sample period
N = int(4096/2) # number of samples to take the FFT of
t = Ts*np.arange(N)
x = np.exp(1j*2*np.pi*777*t) # simulates sinusoid at 50 Hz
x = x[0:N] # we will only take the FFT of the first 1024 samples
# add the following line after doing x = x[0:1024]
x = x * np.hamming(len(x)) # apply a Hamming window
# Get the PSD
PSD = np.abs(np.fft.fft(x))**2 / (N*Fs)
PSD_log = 10.0*np.log10(PSD)
# Shift the PSD to have 0 Hz in the center
PSD_shifted = np.fft.fftshift(PSD_log)

# In Python, shifting the observation window will look like:
center_freq = 2.4e9
f = np.arange(-Fs/2, Fs/2, Fs/N) #start, stop, step. centered around 0 Hz
f+= center_freq # shift the observation window to 2.4 GHz by adding center_freq to f

plt.plot(f, PSD_shifted)
plt.show()