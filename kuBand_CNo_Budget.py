import math
import numpy as np

"""
Example 12.9: In a Ku-Band Link Budget calculation at 12 GHz, the following parameters are given:
Free-Space Path Loss = 206 dB
Atmospheric Absorption Loss = 2 dB
Off-pointing Loss = 1 dB
Receiver Feeder Loss = 1 dB
Polarization mismatch Loss = 0 dB
Receiver G/T ratio = 19.5 dB/K
EIRP = 48 dBW
k = 228.6 dB

"""

FSPL = 206
AAL = 2
OPL = 1
RFL = 1
PML = 0
rGT = 19.5
EIRP = 48
k = -228.6

LOSSES = FSPL + AAL + OPL + RFL + PML
CNo = EIRP + rGT - LOSSES - k
print("The Carrier to Noise ratio is: ", CNo, "dB-Hz")
