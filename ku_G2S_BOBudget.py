import math
import numpy as np

"""
Example 12.11: An uplink at 14 GHz requires a saturations flux density of -91.4 dBW/m^2 and an input BO of 11 dB.
The atellite [G/T] is -6.7 dB/K and receiver feeder losses amount to 0.6 dB. Calculate the the carrier to noise density ratio.
"""
sfd = -91.4
A0 = -44.4
GT = -6.7
input_bo = -11
k =  - 228.6
RFL = -0.6

# Carrier to noise density ratio
CNR = sfd + A0 - input_bo + GT - k - RFL
print(f"The carrier to noise density ratio is {CNR} dB")
