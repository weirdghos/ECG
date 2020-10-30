import pywt
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
import scipy.signal as signal
import QRS_detector1
def read_data(filename):#读取心电数据
    global record
    record=wfdb.rdrecord(filename,physical=False,channels=[0]).d_signal.flatten()  #原始数据单个元素存在中括号，使用flatten
    return record
def draw_spectrum(x):  #画频谱函数
    y = np.abs(fft(x) / len(x))
    y1 = y[1:int(len(x) / 2)+1]
    freqs=np.linspace(0, 180, int(len(x)/2))
    plt.plot(freqs,y1)
    plt.show()
def wavelet(x):
    coffee=pywt.wavedec(data=x,wavelet='db8',level=10)
    A10,D10,D9,D8,D7,D6,D5,D4,D3,D2,D1,D0=coffee
    D0.fill(0)
    D1.fill(0)
    A10.fill(0)
    threshold=np.median(np.abs(D0)/len)

    plt.plot(coffee[3])
    plt.show()
def band_filter(x,start,end,type):
    global data
    f1=start/180
    f2=end/180
    band=signal.firwin(101,[f1,f2],window='hann',pass_zero=type)    #可以使用firwin构建滤波器 freqs画频率响应
    data = signal.lfilter(band,1,x)
    data[0:50]=0
    return data
def draw_time(x,y,start,end):
    if y==0:
        plt.plot(x[start:end])
        plt.show()
    else:
        plt.plot(x[start:end],y[start:end],'or')
        plt.show()
if __name__=="__main__":
    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    x='101'
    read_data(x)
    band_filter(record,55,65,True)
    data[0:100]=min(data[100:300])
    wavelet(data)
    # d=QRS_detector1.pan_detectors(32,data)
    #plt.plot(d[0:20],data[d[0:20]],'or')
    # plt.plot(data[0:10000])
    # plt.show()