import math
import numpy as np

"""
Example 12.3: A QPSK signal is transmitted by a satellite. Raised-cosine filtering is used, for which the roll-off factor is 0.2
and a BER of 10^-5 is required. For the satellite downlink, the losses amount to 200 dB, the receiving earth-station G/T ratio is 32 dB/K
and the transponder bandwidth is 36 MHz.
Calculate:

A) the bit rate which can be accomodated
B) the required EIRP

"""

# Constants
rho = 0.2 # roll-off factor
BER = 1e-5 # required BER
LOSSES = 200 # dB
rcv_GT = 32 # dB/K G/T of the Ground Station
BW = 36e6 # Hz Transponder Bandwidth
k = -228.6 # dBJ/K Boltzmann's constant

bit_rate = (2*BW) / (1 + rho) # bits per second
print(f"A) The bit rate which can be accomodated is {bit_rate} bps")

bit_rate_log = 10*np.log10(bit_rate / 1) # dBbps

# For a BER of 10^-5, the [EbNo] = 9.6 dB

EbNo = 9.6 # dB

CNo_d = EbNo + bit_rate_log # dB Downlink Carrier-to-Noise Density ratio
print(f"The Carrier-to-Noise Density ratio is {CNo_d} dB")

EIRP_dl = CNo_d - rcv_GT + LOSSES + k # dB
print(f"B) The required EIRP is {EIRP_dl} dB") # dB
