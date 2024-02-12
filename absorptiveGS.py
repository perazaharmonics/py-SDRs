import math
import numpy as np

""" For the system shown in Figure 12.6a, the receiver noise figure is 12 dB, the cable loss is 5 dB, the LNA gain is 50 dB
and its noise temperature is 150 K. The antenna noise temperature is 35 K. 
Calculate the noise temperature referred to the input of the LNA
"""

NF_rcvr = 12
cable_loss = 5
LNA_gain = 50
LNA_noise_temp = 150
antenna_noise_temp = 35

F = 10**(NF_rcvr/10)
G = 10**(LNA_gain/10)
T0 = 290
Loss = 10**(cable_loss/10)

T_system = antenna_noise_temp + LNA_noise_temp + ((Loss - 1)*T0/G) + (Loss*T0*(F-1)/G)
print("The noise temperature referred to the input of the LNA is", T_system, "K")

