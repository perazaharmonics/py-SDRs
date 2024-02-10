import numpy as np

# Constants
c = 3e8  # Speed of light (m/s)
f_UL = 6.285e9  # Frequency (Hz)
BW_tr_Hz = 36e6  # Transponder Bandwidth (Hz)
BW_tr_dB = 10 * np.log10(BW_tr_Hz)
R = 38500e3  # Distance (m)
D = 9  # Antenna diameter (m)

K = -228.6  # Boltzmann constant (dBW/K/Hz)
T_sys = 500  # Noise temperature (K)
T_sys_dB = 10 * np.log10(T_sys)

G_sat_dB = 31  # Antenna gain
Aeff_ES = 0.68  # Antenna aperture efficiency
reqCN_up_dB = 26  # Required carrier-to-noise ratio (dB)
L_misc = 0.5  # Clear air atmospheric attenuation and other losses in dB
L_ptr = 2  # Edge of contour Loss in dB
Gr_sat_dB = G_sat_dB - L_ptr

# Calculate wavelength
lambda_ = c / f_UL

# Noise Power Budget (C/N)up = 26 dB
N_dB = K + T_sys_dB + BW_tr_dB  # Power of the Noise in dB
print(f'The noise power is: {N_dB:.2f} dBW')

# Calculate losses
Lp = 20 * np.log10(R) + 20 * np.log10(f_UL) + 20 * np.log10(4 * np.pi / c)  # Path Loss
L_tot_dB = Lp + L_misc
print(f'The total losses are: {L_tot_dB:.2f} dB')

# Calculate antenna gain
Gt_lin = Aeff_ES * (np.pi * D / lambda_)**2
Gt_db = 10 * np.log10(Gt_lin)  # Convert antenna gain to dB
print(f'The antenna gain is: {Gt_db:.2f} dB')

# Calculate required transmitter power
# From CNup_dB = Pt_dB + Gt_db - L_tot_dB, solve for Pt_dB
Pt_dB = reqCN_up_dB - (Gt_db + Gr_sat_dB - Lp - N_dB)
print(f'The required transmitter power is: {Pt_dB:.2f} dBW')

# Convert power to W
Pt_W = 10**(Pt_dB / 10)
print(f'The required transmitter power is: {Pt_W:.2f} W')

# Show Results
print(f'The required transmitter output power during clear sky conditions is: {Pt_W:.2f} Watts ({Pt_dB:.2f} dBW)')
