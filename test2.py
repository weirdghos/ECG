import wfdb
from scipy.fft import fft
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import pywt
import scipy.interpolate as interpol
from PyEMD import EMD,EEMD,CEEMDAN   #导入ENMD相关包
fs=360
record=wfdb.rdrecord('101',physical=False,channels=[0]).d_signal.flatten() #原数据为单独列表，并不是一个list，卡2天
f1=0.083
f2=0.13
f3=0.32
f4=0.34
ba=signal.firwin(101,[f1,f2],window='hann',pass_zero=False)
b2=signal.firwin(101,[f3,f4],window='hann',pass_zero=True)
b3=signal.firwin(101,0.017,pass_zero=False)
data1=signal.lfilter(ba,1,record)
data2=signal.lfilter(b2,1,record)
data3=signal.lfilter(b3,1,data2)
# coffees=pywt.wavedec(data2,wavelet='db10',level=8)
# print(coffees[7])


plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 500 #分辨率
data3[0:100]=min(data3[200:600])
locmin=signal.argrelmin(data2,order=100)
locmin=locmin[0]
x=np.linspace(0,len(data2)-1)
curve=interpol.interp1d(locmin,data2[locmin])
a,d=pywt.dwt(data2,'db8','constant')
plt.plot(d)
plt.show()



# plt.plot(data1[1:2000],color='#008000')
# plt.plot(data2[1:2000],color='#FF0000')
# plt.show()

# w,h=signal.freqz(ba)
# plt.plot(w,20*np.log10(abs(h)),'b')
# plt.show()













