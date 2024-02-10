import numpy as np

# Constants
c = 3e8  # Speed of light (m/s)
f_UL = 6.285e9  # UL Frequency (Hz)
f_DL = 4.06e9  # DL Frequency (Hz)
lambda_ = c / f_DL
R = 38500e3  # distance to sat in meters

FEC_dB = 5.5  # Margin added by FEC coding
CNup_dB = 26  # Assumed value in decibels
CNup_lin = 10 ** (CNup_dB / 10)
reqCNo_dB = 13  # required CNo in dB
reqCNo_lin = 10 ** (reqCNo_dB / 10)
BO = 1
BWn_Hz = 27e6  # IF Noise Bandwidth (Hz)
BWn_dB = 10 * np.log10(BWn_Hz)

K = -228.6  # Boltzmann constant (dBW/K/Hz)
T_in = 20  # Antenna noise temperature (K)
T_LNA = 55  # LNA noise temperature (K)
T_sys = T_in + T_LNA  # System noise temperature (K)
T_sys_dB = 10 * np.log10(T_sys)

Pt_sat_W = 40  # Saturated output power of the satellite (W)
Pt_sat_dB = 10 * np.log10(Pt_sat_W)
G_sat_dB = 31  # Antenna gain (dB)
Aeff = 0.65  # Antenna aperture efficiency

L_ptr = 3  # Edge of contour Loss (dB)
L_misc = 0.5  # Clear air atmospheric attenuation and other losses (dB)
Lp_up = 200.1
Gt_sat_dB = G_sat_dB - L_ptr

# 1. Calculate CNo of the DL that will provide (CNo) of 13 dB
invCNdn_lin = (1 / reqCNo_lin) - (1 / CNup_lin)
CNdn_lin = 1 / invCNdn_lin  # CN DL linear units
CNdn_dB = 10 * np.log10(CNdn_lin)

print(f'Calculated C/N for Downlink: {CNdn_dB:.2f} dB')

# 2. Downlink Noise Power Budget
N_dB = K + T_sys_dB + BWn_dB  # Power of the Noise in dB
Pr_ES_dB = CNdn_dB + N_dB  # The received power level must be

print(f'The noise power is: {N_dB:.2f} dBW')
print(f'The required power at the Earth Station is: {Pr_ES_dB:.2f} dBW')

# 3. Calculate losses
Lp = Lp_up + 20 * np.log10(f_DL / f_UL)

print(f'The free-space path loss is: {Lp:.2f} dB')

# 4. Downlink Power Budget
Gr_ES_dB = (Pr_ES_dB - Pt_sat_dB - Gt_sat_dB + Lp)
Gr_ES_lin = 10 ** (Gr_ES_dB / 10)

print(f'The Gain of Earth Station RCV antenna is: {Gr_ES_dB:.2f} dB')

# 5. Diameter of the antenna
D_m = (lambda_) * np.sqrt(Gr_ES_lin / (Aeff * (np.pi ** 2)))

print(f'The required Diameter of Earth Station RCV antenna is: {D_m:.2f} m')
