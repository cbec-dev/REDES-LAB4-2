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

if __name__ == '__main__':

	F1 = 25
	F2 = 5
	A = 3
	t = np.arange(0, 1, 0.001)
	x = A*np.sin(2*np.pi*F1*t)+(A/2)
	u = (A/2)*signal.square(2*np.pi*F2*t)+(A/2)
	v = x*u

	f, axarr = matplot.subplots(3)
	axarr[0].set_title('Carrier')
	axarr[0].plot(t, x)
	axarr[0].set_xlabel('Tiempo (s)')
	axarr[0].set_ylabel('Amplitud')
	axarr[1].set_title('Pulsos cuadrados')
	axarr[1].plot(t, u)
	axarr[1].set_xlabel('Tiempo (s)')
	axarr[1].set_ylabel('Amplitud')
	axarr[2].set_title('Señal ASK')
	axarr[2].plot(t, v)
	axarr[2].set_xlabel('Tiempo (s)')
	axarr[2].set_ylabel('Amplitud')
	matplot.tight_layout()
	matplot.show()