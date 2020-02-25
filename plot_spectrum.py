import matplotlib.pyplot as plt
import numpy as np

wav, inc, trn, ref = np.loadtxt('spectrum.txt', skiprows=1, unpack=True)

plt.plot(wav, inc, label='Incident')
plt.plot(wav, trn, label='Transmitted')
plt.plot(wav, ref, label='Reflected')
plt.legend(loc='best')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')

plt.show()