from matplotlib.pyplot import figure
from numpy.core.records import record
import pywt
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from PyEMD import EMD,CEEMDAN
from nosie_perf import sig
from filter1 import EMGfilter,ECGwander
import test
def get_mixsignal(signal,noise,snr):
    c=1
    mix_signal=[signal[i]+c*noise[i] for i in range(len(signal))]   #list对应元素相加
    a=10*np.log10(np.sum(signal**2)/np.sum((mix_signal-signal)**2))
    mixture=[]
  
    if a==snr:
       mixture=mix_signal
    if a>snr:
        for j in np.linspace(1,5,2000):
           mix_signal1=[signal[i]+j*noise[i] for i in range(len(signal))]
           a=10*np.log10(np.sum(signal**2)/np.sum((mix_signal1-signal)**2))
          
           
           if np.abs(a-snr)<0.01:
             mixture=mix_signal1
             break
    if a<snr:
        for j in np.linspace(1,0.5,2000):
          mix_signal1=[signal[i]+j*noise[i] for i in range(len(signal))]
          a=10*np.log10(np.sum(signal**2)/np.sum((mix_signal1-signal)**2))
          threshold=a
          if np.abs(a-snr)<0.01:
            mixture=mix_signal1
            break
    return mixture
def comparefig(x,y,z):
    plt.rcParams['font.sans-serif']=['SimHei']
    fig=plt.figure()
    plt.title('输入信噪比6db 滤波前后对比')
    ax1=plt.subplot(311)
    ax1.plot(x,label='干净信号')
    plt.legend(loc="right")  
    ax2=plt.subplot(312,sharex=ax1)
    ax2.plot(y,label='含噪信号',color='blue')
    plt.legend(loc="right")  
    ax3=plt.subplot(313,sharex=ax1)
    plt.plot(z,label='滤波信号',color='red')
    plt.legend(loc="right")  #显示标签
    plt.show()
clearsignal,field=wfdb.rdsamp('105',channels=[0])
baseline,fied=wfdb.rdsamp('bw',channels=[0])
msn,fi=wfdb.rdsamp('ma',channels=[0])
annotation=wfdb.rdann('105','atr')
clearsignal=clearsignal.flatten()
msn=msn.flatten()
baseline=baseline.flatten()
# (cA2, cD2), (cA1, cD1)=pywt.swt(l,'db4',level=2)  SWT
# emd = EMD(DTYPE=np.float16,spline_kind='akima',max_imfs=8)  #16位浮点数计算 样条拟合改为akima或分段插值（降低计算量） 插值方面 
# imf=emd(l)
# cemd=CEEMDAN(DTYPE=np.float16,spline_kind='akima')
# imf=cemd(l)
# length=imf.shape[0]
# plt.figure(figsize=(12,9))
# plt.subplot(length+1,1,1)
# plt.plot(l)
# for i in range(length):
#     plt.subplot(length+1,1,i+2)
#     plt.plot(imf[i])
#     plt.ylabel("eIMF %i" %(i+1))
# imf[0]=0
# imf[6:length-1]=0
# re=0
# for i in range(length):
#     re+=imf[i]

#奇异值分解调用
plt.close()
a=clearsignal[7000:9500]
b=msn[4000:6500]
c=baseline[4000:6500]
mixture=get_mixsignal(a,b,8)
mixture=np.array(mixture)
c=ECGwander(mixture)
signal=c.gongpin()

cd=EMGfilter(signal,1000)
x_re=cd.APSM_SVD()
#y=SSR()
plt.plot(x_re)
plt.show()
#comparefig(a,signal,l2)

