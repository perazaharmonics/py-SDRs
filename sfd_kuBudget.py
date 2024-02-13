import math
import numpy as np

"""
Example 12.10: An Earth-Station Uplink operates at 14 GHz, and the flux density required to saturate the 
the transponder is -120 db(W/m^2). The FSPL 207 dB and the other propagation loss amounts to 2 dB. Calculate
the earth-station [EIRP] required for saturation, assuming clear-sky conditions. Assume [RFL] is negligible.
"""

ul_freq = 14 # GHz
gamma = -120 # dB(W/m^2)
FSPL = 207 # dB
AL = 2 # dB
RFL = -(FSPL + AL)

A0 = -(20*np.log10(4*np.pi) + 20*np.log10(ul_freq))
print("Effective Area of a Isotropic Antenna: ", A0, "dB(W)")

EIRP_S_ul = gamma + A0 - RFL
print("EIRP_S_ul = ", EIRP_S_ul, "dB(W)")
