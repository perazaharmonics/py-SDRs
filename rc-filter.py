# Create and plot a baseband Raised-Cosine filter of a QPSK signal with a given roll-off factor of 0.2

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Parameters
N = 77  # Number of taps
roll_off_set = [0.2, 0.3 ,0.5 ,0.7 ,1.0 ]  # Roll-off factor
colors = ['b', 'g', 'r', 'c', 'm']  # Colors for the plot
fs = 50  # Sampling frequency
T = 1/fs  # Sampling period
f_cutoff = 100  # Cutoff frequency
t = np.linspace(-N/2, N/2, N) * T


# Create the filter
def rc_filt(num_taps, beta, sampling_rate, symbol_rate):
    """
    Raised Cosine (RC) filter.

    Parameters:
    num_taps (int): Number of filter taps.
    beta (float): Roll-off factor (0 <= beta <= 1).
    sampling_rate (float): Sampling frequency.
    symbol_rate (float): Symbol rate (frequency).
    
    Returns:
    numpy.ndarray: Coefficients of the RC filter.
    """
    # Create the time vector
    t = np.arange(-num_taps/2, num_taps/2) / sampling_rate
    Ts = 1/symbol_rate  # Symbol period
    h_rc = np.zeros(num_taps)

    for i, ti in enumerate(t):
        if ti == 0.0:
            h_rc[i] = 1.0
        elif beta != 0 and (ti == Ts/(2*beta) or ti == -Ts/(2*beta)):
            h_rc[i] = (np.pi/4) * np.sinc(1/(2*beta))
        else:
            numerator = np.sin(np.pi*ti/Ts) * np.cos(np.pi*beta*ti/Ts)
            denominator = (np.pi*ti/Ts) * (1-(2*beta*ti/Ts)**2)
            h_rc[i] = numerator / denominator

    # Normalize the filter coefficients
    h_rc /= np.sum(h_rc)

    return h_rc

for i, roll_off in enumerate(roll_off_set):
    h = rc_filt(N, roll_off, fs, 1/T)
    w, h_freq = freqz(h, worN=1024)
    plt.plot(fs*w/np.pi, 20*np.log10(np.abs(h_freq)), color=colors[i], label=f'Roll-off: {roll_off}')
    plt.grid(True)
    plt.title('Magnitude Response')
    plt.legend()

# Plot the filter
plt.figure()
plt.stem(t, h)
plt.title('Raised-Cosine Filter')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the frequency response
w, h_freq = freqz(h, worN=1024)
# Generate a frequency vector that is symmetric around 0
freqs = np.fft.fftfreq(len(w), d=1/fs)

# Shift the frequency vector and freq response to put the zero frequncy in the center
freqs_shift = np.fft.fftshift(freqs)
h_shift = np.fft.fftshift(h_freq)

# Calculate the phase response
phase_response = np.angle(h_shift)

# Unwrap the phase response
# Calculate the unwrapped phase response
unwrapped_phase = np.unwrap(np.angle(h_shift))

# Add a Bode plot
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(fs*w/np.pi, 20*np.log10(np.abs(h_freq)))
plt.title('Bode Plot')
plt.ylabel('Gain [dB]')
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(fs*w/np.pi, unwrapped_phase)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [radians]')
plt.grid(True)
plt.show()
