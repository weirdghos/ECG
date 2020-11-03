import pywt
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
import scipy.signal as signal
import QRS_detector1
from wfdb import processing
def read_data(filename):#读取心电数据
    # record=wfdb.rdrecord(filename,physical=False,channels=[0]).d_signal.flatten()  #原始数据单个元素存在中括号，使用flatten
    record,field=wfdb.rdsamp(filename,channels=[0])
    record=record.flatten()
    return record,field
def draw_spectrum(x):  #画频谱函数
    y = np.abs(fft(x) / len(x))
    y1 = y[1:int(len(x) / 2)+1]
    freqs=np.linspace(0, 180, int(len(x)/2))
    plt.plot(freqs,y1)
    plt.show()
def wavelet(x):
    coffee=pywt.wavedec(data=x,wavelet='db8',level=8)
    A8,D8,D7,D6,D5,D4,D3,D2,D1=coffee
    # cof=coffee
    # for i in range(0,len(cof)-3):
    #     cof[i].fill(0)
    # 画出具体某一个小波分量
    # cof[7].fill(0)
    # cof[8].fill(0)
    # basline=pywt.waverec(coeffs=cof,wavelet='db8')
    D2.fill(0)
    D1.fill(0)
    A8.fill(0)
    threshold = (np.median(np.abs(D1)) / 0.6745) * (np.sqrt(2 * np.log(len(D1))))
    for i in range(1, len(coffee) - 2):
        coffee[i] = pywt.threshold(coffee[i], threshold)
    rdata = pywt.waverec(coeffs=coffee, wavelet='db8')
    return rdata
def R_peaks(x):
    peaks=processing.XQRS(x,fs=360)
    peaks.detect()
    return peaks
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
    plt.rcParams['figure.dpi'] = 300
      # 分辨率
    x='101'
    record,field=read_data(x)
    band_filter(record,55,65,True)
    data[0:100]=min(data[100:300])
    rdata=wavelet(data)
    peak=R_peaks(radta)
    print(len(peak.qrs_inds))
    # d=QRS_detectorpan_detectors(32,data)
    #plt.plot(d[0:20],data[d[0:20]],'or')
    # plt.plot(data[0:10000])
    # plt.show()