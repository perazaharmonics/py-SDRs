import math
import numpy as np

""" 
Example 12.12: A satellite TV signal occupies the full transponder bandwidth of 36 MHz, and it must provide a C/N ratio at the destination earth station
of 22 dB. Given that the total transmission path loss is 200 dB, and the destination Earth Station G/T ratio is 31 dB/K,
Calculate the EIRP required at the satellite.
"""

CN_d=22 # dB
GT = 31 # [G/T] dB/K
LOSSES = 200 # dB
k = -228.6 # dB
B= 75.6 # MHz
EIRP = CN_d - GT + LOSSES + k + B

print(f"The EIRP required at the satellite is {EIRP} dBW")
