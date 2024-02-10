import numpy as np

# Under conditions of heavy rain, the C-Band 
# path from the transmitting station suffers an attenuation of 2-dB. Calculate
# overall C/N at the earth station in a bandwidth of 27 MHz under these conditions
# and find the link margin. Reminder: The uplink margin is the number of dB of attenuation that
# can occur on the uplink before the receiver overall C/N reaches the limit of 9.5 dB

# Parameters
c = 3e8  # Speed of light (m/s)
f_UL = 6.285e9  # UL Frequency (Hz)
f_DL = 4.06e9  # DL Frequency (Hz)
lambda_ = c / f_DL
R = 38500e3  # distance to sat in meters
D = 9  # Diameter of Earth Station antenna in meters

BW_Hz = 27e6  # IF Noise Bandwidth (Hz)
BW_dB = 10 * np.log10(BW_Hz)

K = -228.6  # Boltzmann constant (dBW/K/Hz)
To_k = 290  # Average room temp
T_in = 20  # Antenna noise temperature (K)
T_LNA = 55  # LNA noise temperature (K)
T_sys = T_in + T_LNA  # System noise temperature (K)
T_sys_dB = 10 * np.log10(T_sys)

Pt_sat_W = 40  # Saturated output power of the satellite (W)
Pt_sat_dB = 10 * np.log10(Pt_sat_W)
G_sat_dB = 31  # Antenna gain (dB)
Aeff_VSAT = 0.65  # VSAT antenna aperture efficiency
Aeff_ES = 0.68  # Earth Station antenna aperture efficiency

BO = 1  # Back off (dB)
T_grnd_k = 12  # Assumed ground temperature due to sidelobes in Kelvin degrees

L_ptr = 3  # Edge of contour Loss (dB)
L_misc = 0.5  # Clear air atmospheric attenuation and other losses (dB)
Lp_dB = 197.3215  # Path Loss of the CNo
A_rain_dB = 2  # Rain attenuation
FEC_dB = 5.5  # FEC Gain        

Pt_dB = 17.7932  # Power of the Earth Station Antenna
A_ca = 0.5  # Clear sky attenuation dB
Nca_dB = -126.0473  # Clear sky Noise Power

# Part A: (2 dB rain attenuation)

# Required overall (C/N)_rain
minCNo_dB = 9.5  # Minimum required CNo (dB)
CNup_dB = 26  # Inherited value from Question1 in decibels
CNup_lin = 10 ** (CNup_dB / 10)
CNdn_dB = 13.2  # Inherited value from Question2 in decibels
CNdn_lin = 10 ** (CNdn_dB / 10)
CNo_ca_dB = 13
CNo_rain_dB = CNo_ca_dB - A_rain_dB  # CNo in dB under rain

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

print(f' The C/No using the UL Margin is {CNo_check_dB:.2f} dB')

# Part B:

A_ca_b = 0.3
A_rain_dB2 = 1.5
A_b = A_ca_b + A_rain_dB2
print(f'Total path sky attenuation A: {A_b:.2f} dB')

# Determine the sky noise temperature
T_skyrains_k = To_k * (1 - 10 ** (-A_b / 10))
T_sca_k = To_k * (1
