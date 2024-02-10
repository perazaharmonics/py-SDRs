import numpy as np
import matplotlib.pyplot as plt

num_symbols = 64000

x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_degrees = x_int*360/4.0 + 45 # 45, 135, 225, 315 degrees

x_radians = x_degrees*np.pi/180.0 # sin() and cos() takes in radians
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # this produces our QPSK symbols

plt.plot(np.real(x_symbols), np.imag(x_symbols), '*')
plt.grid(True)
plt.show()

noise = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2) # AWGN with unity power

noise_power = 0.01
rcv = x_symbols + noise*np.sqrt(noise_power)
plt.plot(np.real(rcv), np.imag(rcv), '.')
plt.grid(True)
plt.show()

# to simulate phase noise, which could result from phase jitter within the LO, we replace rcv with:
phase_noise = np.random.randn(len(x_symbols)) * (noise_power * 10)
rcv = x_symbols * np.exp(1j*phase_noise) + noise*np.sqrt(noise_power)

plt.plot(np.real(rcv), np.imag(rcv), '.')
plt.grid(True)
plt.show()
