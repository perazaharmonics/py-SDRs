import numpy as np

# Constants
c = 3e8  # Speed of light (m/s)
f_UL = 14.15e9  # Frequency (Hz)
BW_tr_Hz = 36e6  # Transponder Bandwidth (Hz)
BW_tr_dB = 10 * np.log10(BW_tr_Hz)
R = 38500e3  # Distance (m)
D = 5  # Antenna diameter (m)

K = -228.6  # Boltzmann constant (dBW/K/Hz)
T_sys = 500  # Noise temperature (K)
T_sys_dB = 10 * np.log10(T_sys)

Pt_sat_W = 40  # Saturated output power of the satellite
Pt_sat_db = 10 * np.log10(Pt_sat_W)
G_sat_dB = 31  # Antenna gain
G_sat_lin = 10 ** (G_sat_dB / 10)
FEC_dB = 5.5

Aeff_ES = 0.68  # Antenna aperture efficiency
reqCN_up_dB = 30  # Required carrier-to-noise ratio (dB)
L_ptr = 2  # Edge of contour Loss in dB
L_misc = 1  # Clear air atmospheric attenuation and other losses in dB
Gr_sat_dB = G_sat_dB - L_ptr

# Calculate wavelength
lambda_ = c / f_UL

# 1. Noise Power Budget (C/N)up = 26 dB
N_dB = K + T_sys_dB + BW_tr_dB  # Power of the Noise in dB
print(f'The noise power is: {N_dB:.2f} dBW')
Pr_sat_dB = N_dB + reqCN_up_dB  # The received power level must be 26 dB greater than the noise power
print(f'The required satellite received power is: {Pr_sat_dB:.2f} dBW')

# Calculate losses
Lp = 20 * np.log10(R) + 20 * np.log10(f_UL) + 20 * np.log10(4 * np.pi / c)
print(f'The free-space path loss is: {Lp:.2f} dB')
L_tot_dB = Lp + L_misc
print(f'The total loss is: {L_tot_dB:.2f} dB')

# Calculate antenna gain
Gt_lin = Aeff_ES * (np.pi * D / lambda_)**2
print(f'The linear antenna gain is: {Gt_lin:.2f}')

# Convert antenna gain to dB
Gt_db = 10 * np.log10(Gt_lin)
print(f'The antenna gain in dB is: {Gt_db:.2f} dB')

# Calculate required transmitter power
Pt_dB = reqCN_up_dB + Pr_sat_dB - (Gt_db + Gr_sat_dB + L_tot_dB)
print(f'The required transmitter power is: {Pt_dB:.2f} dBW')

# Convert power to W
Pt_W = 10 ** (Pt_dB / 10)
print(f'The required transmitter power is: {Pt_W:.2f} W')

# Get (C/N)up
CN_up = Pt_dB + Gt_db - L_tot_dB - N_dB
print(f'The carrier-to-noise ratio (C/N) uplink is: {CN_up:.2f} dB')

# Show Results
print(f'The required transmitter output power during clear sky conditions is: {Pt_W:.2f} Watts ({Pt_dB:.2f} dBW)')
