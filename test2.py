import wfdb
from scipy.fft import fft
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import pywt
import scipy.interpolate as interpol
from sklearn import decomposition
pca=decomposition.PCA

fs=360
record=wfdb.rdrecord('101',physical=False,channels=[0]).d_signal.flatten() #原数据为单独列表，并不是一个list，卡2天


coffee=pywt.wavedec(data=record,wavelet='db8',level=9)
A9,D9,D8,D7,D6,D5,D4,D3,D2,D1=coffee

A9.fill(0)
rdata = pywt.waverec(coeffs=coffee, wavelet='db8')
coffee1=pywt.wavedec(data=record,wavelet='db8',level=8)
a8,d8,d7,d6,d5,d4,d3,d2,d1=coffee1
a8.fill(0)
rdata1=pywt.waverec(coeffs=coffee1,wavelet='db8')
plt.plot(record[30000:40000])
plt.plot(rdata[30000:40000],color='red')
plt.plot(rdata1[30000:40000])
plt.show()
# plt.plot(data1[1:2000],color='#008000')
# plt.plot(data2[1:2000],color='#FF0000')
# plt.show()

# w,h=signal.freqz(ba)
# plt.plot(w,20*np.log10(abs(h)),'b')
# plt.show()













