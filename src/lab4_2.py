import scipy.io.wavfile as wav
import scipy.signal as signal
import matplotlib.pyplot as matplot
import matplotlib.patches as mpatches
import numpy as np
import math
from scipy import fftpack, integrate
from scipy.interpolate import interp1d
import warnings
#warnings.filterwarnings('ignore')

def getBinSignal(s):
	n = np.size(s)
	sbin = 0
	for i in range(n):
		aux = '{0:016b}'.format(s[i])
		for j in range(16):
			if(j==0):
				if(aux[j]=='-'):
					sbin = np.append(sbin, 1)
				else:
					sbin = np.append(sbin, 0)
			else:
				sbin = np.append(sbin, float(aux[j]))


	sbin = sbin[1:np.size(sbin)].ravel()
	sbin = np.array(sbin)
	return sbin


def ASKmod(s, fs):
	fs = 16*fs
	A = 5
	B = 10
	n = np.size(s)
	#T = n/fs     #Tiempo
	t = np.arange(0, 1, 1/n)
	c1 = A*np.cos(2*np.pi*fs*t)
	c2 = B*np.cos(2*np.pi*fs*t)
	smod = 0

	for i in range(n):
		if s[i]==0:
			smod = np.append(smod, c1[i]*s[i])
		else:
			smod = np.append(smod, c2[i]*s[i])
	smod = smod[1:np.size(smod)].ravel()
	smod = np.array(smod)


	f, axarr = matplot.subplots(3)
	axarr[0].set_title('Señal Digital Original')
	axarr[0].step(t, s)
	axarr[0].set_ylabel('Amplitud')
	axarr[1].set_title('Portadoras')
	axarr[1].plot(t, c1, color='red')
	axarr[1].plot(t, c2, color='blue')
	blue_patch = mpatches.Patch(color='blue', label='Portadora 1')
	red_patch = mpatches.Patch(color='red', label='Portadora 2')
	axarr[1].legend(handles=[blue_patch, red_patch])
	axarr[1].set_ylabel('Amplitud')
	axarr[2].set_title('Señal ASK')
	axarr[2].plot(t, smod)
	axarr[2].set_ylabel('Amplitud')
	matplot.tight_layout()
	matplot.show()

	return smod

def deMOD(smod, A, B):
	n = np.size(smod)
	sdemod = 0.0
	for i in range(n):
		if abs(smod[i])>A:
			sdemod = np.append(sdemod, 1)
		else:
			sdemod = np.append(sdemod, 0)
	sdemod = sdemod[1:np.size(sdemod)].ravel()
	sdemod = np.array(sdemod)
	return sdemod 

if __name__ == '__main__':

	# Se leen eñ archivo de audio, se guarda la frecuencia en f y las muestras en signal
	f, s = wav.read('handel.wav')
	Amax = np.amax(abs(s))
	s = s[5000:5100]
	sbin = getBinSignal(s)

	smod = ASKmod(sbin, f)

	sdemod = deMOD(smod, 5, 10)

	print(sbin[0:16])
	print(smod[0:16])
	print(sdemod[0:16])






	# F1 = 10000
	# F2 = 50
	# A = 5
	# B = 10
	# n = np.size(s)
	# t = np.arange(0, n, 1)
	# #c = A*np.sin(2*np.pi*F1*t)+(A/2)
	# c1 = A*np.cos(2*np.pi*F1*t)
	# c2 = B*np.cos(2*np.pi*F1*t)
	# u = (A/2)*signal.square(2*np.pi*F2*t)+(A/2)
	# v = c1*u

	# f, axarr = matplot.subplots(4)
	# axarr[0].set_title('Señal')
	# axarr[0].step(t, s)
	# axarr[1].set_title('Señal Cuadrada')
	# axarr[1].step(t, u)
	# axarr[1].set_xlabel('Tiempo (s)')
	# axarr[1].set_ylabel('Amplitud')
	# axarr[2].set_title('Carrier 1')
	# axarr[2].plot(t, c1)
	# axarr[2].set_xlabel('Tiempo (s)')
	# axarr[2].set_ylabel('Amplitud')
	# axarr[3].set_title('Señal ASK')
	# axarr[3].plot(t, v)
	# axarr[3].set_xlabel('Tiempo (s)')
	# axarr[3].set_ylabel('Amplitud')
	# matplot.tight_layout()
	# matplot.show()

	# sbin = getBinSignal(s)
	# print('{0:016b}'.format(s[0]))
	# print('{0:016b}'.format(s[1]))
	

	# print(sbin[0:16])
	# print(sbin[16:32])

	# matplot.step(range(32), sbin[0:32])
	# matplot.show()
