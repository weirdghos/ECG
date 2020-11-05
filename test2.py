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
record=wfdb.rdrecord('101',physical=False,channels=[0,1]).d_signal.flatten() #原数据为单独列表，并不是一个list，卡2天

plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 500 #分辨率
data=record[0:2000]

plt.plot(data)
plt.show()






# plt.plot(data1[1:2000],color='#008000')
# plt.plot(data2[1:2000],color='#FF0000')
# plt.show()

# w,h=signal.freqz(ba)
# plt.plot(w,20*np.log10(abs(h)),'b')
# plt.show()













