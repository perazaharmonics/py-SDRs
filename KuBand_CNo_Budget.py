import numpy as np

# Constants
c = 3e8  # Speed of light (m/s)
f_UL = 14.15e9  # UL Frequency (Hz)
f_DL = 11.45e9  # DL Frequency (Hz)
lambda_ = c / f_DL
R = 38500e3  # distance to sat in meters
D = 9  # Diameter of Earth Station antenna in meters
FEC_dB = 5.5  # Margin created by the FEC
CNup_dB = 30  # Inherited value from Question1 in decibels
CNup_lin = 10 ** (CNup_dB / 10)
CNdn_dB = 17  # Inherited value from Question2 in decibels
CNdn_lin = 10 ** (CNdn_dB / 10)
reqCNo_dB = 17  # required CNo in dB
reqCNo_lin = 10 ** (reqCNo_dB / 10)
BW_Hz = 27e6  # IF Noise Bandwidth (Hz)
BW_dB = 10 * np.log10(BW_Hz)

K = -228.6  # Boltzmann constant (dBW/K/Hz)
To_k = 290  # Average room temp
T_in = 20  # Antenna noise temperature (K)
T_LNA = 110  # LNA noise temperature (K)
T_sys = T_in + T_LNA  # System noise temperature (K)
T_sys_dB = 10 * np.log10(T_sys)

Pt_sat_W = 40  # Saturated output power of the satellite (W)
Pt_sat_dB = 10 * np.log10(Pt_sat_W)
G_sat_dB = 31  # Antenna gain (dB)
Aeff_VSAT = 0.65  # VSAT antenna aperture efficiency
Aeff_ES = 0.68  # Earth Station antenna aperture efficiency

L_ptr = 3  # Edge of contour Loss (dB)
L_misc = 0.5  # Clear air atmospheric attenuation and other losses (dB)
Lp_dB = 197.3215  # Path Loss of the CNo
A_rain_dB = 6  # Rain attenuation

# Part A: (2 dB rain attenuation)
minCNo_dB = 9.5  # Minimum required CNo (dB)
CNo_ca_dB = 17
CNo_rain_dB = CNo_ca_dB - A_rain_dB  # CNo under 6 dB rain attenuation
print(f'The total overall C/N under 6 dB rain attenuation is: {CNo_rain_dB:.2f} dB')

UL_margin_dB = CNo_ca_dB - minCNo_dB
print(f'The UL margin in clear sky conditions is: {UL_margin_dB:.2f} dB')

# Check: when the UL is attenuated by 3.5 dB (margin)
CNup_check_dB = CNup_dB - UL_margin_dB
CNup_check_lin = 10 ** (CNup_check_dB / 10)
CNdn_check_dB = CNdn_dB - UL_margin_dB
CNdn_check_lin = 10 ** (CNdn_check_dB / 10)

# Using the reciprocal formula
invCNo_check_lin = (1 / CNup_check_lin) + (1 / CNdn_check_lin)
CNo_check_lin = 1 / invCNo_check_lin
CNo_check_dB = 10 * np.log10(CNo_check_lin)
print(f'The C/No using the UL Margin is {CNo_check_dB:.2f} dB')

# Part B:
A_ca_b = 0.3
A_rain_dB2 = 5
A_b = A_ca_b + A_rain_dB2
print(f'Total path sky attenuation A: {A_b:.2f} dB')

# Determine the sky noise temperature
T_skyrains_k = (To_k) * (1 - 10 ** (-A_b / 10))
T_sca_k = (To_k) * (1 - 10 ** (-A_ca_b / 10))
print(f'Sky noise temperature under rain T_sky_k: {T_skyrains_k:.2f} K')
print(f'Sky noise temperature under clear skies: {T_sca_k:.2f} K')

# Find the antenna noise temperature
T_sys_rain_k = T_skyrains_k + T_LNA
print(f'Antenna noise temperature T_Ant_k: {T_sys_rain_k:.2f} K')

# Determine the increase in noise power
deltaN_dB = 10 * np.log10(T_sys_rain_k / T_sys)
print(f'Increase in receiver noise power deltaN_dB: {deltaN_dB:.2f} dB')

# Calculate the effect on (C/N)rain
linkM_dB = A_rain_dB2 + deltaN_dB
CNdn_rain_dB_b = CNdn_dB - linkM_dB
CNdn_rain_lin_b = 10 ** (CNdn_rain_dB_b / 10)
CNo_rain_lin = 1 / ((1 / CNup_lin) + (1 / CNdn_rain_lin_b))
CNo_rain_dB_b = 10 * np.log10(CNo_rain_lin)

# Print results
print(f'Overall C/N with 5-dB of rain attenuation is: {CNo_rain_dB_b:.2f} dB (or {CNo_rain_dB_b + FEC_dB:.2f} dB with FEC)')
