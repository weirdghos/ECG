from numba.np.ufunc import parallel
import numpy as np
import scipy
from wfdb import processing
from matplotlib import pyplot as plt
from scipy import stats
from numba import jit,types,typed

class EMGfilter():
    def __init__ (self,x,L):  #  x为传入需要滤波数据
        self.x=x
        self.L=L
    def APSM_SVD(self):        #自适应周期轨迹矩阵去除EMG
        ann=self.detectR()
        length=len(ann)
        meanRR=np.mean(np.diff(ann))                #求取RR波均值 确定轨迹矩阵长度
        z=np.int(2/3*meanRR)
        signal=self.x[:]                            #浅拷贝
        length_first=len(self.x[:ann[0]])
        print(length_first)
        length_last=len(self.x[ann[length-1]:ann[length-1]+z])
        if length_last<z:
            signal=np.pad(signal,[0,z-length_last],mode='symmetric')
        matrx=np.zeros((length,2*z))
        matrx[0,ann[0]:ann[0]+z]=signal[ann[0]:ann[0]+z]
        print(z)
        for i in range(1,length):                   #构建轨迹矩阵
            matrx[i,:]=signal[ann[i]-z:ann[i]+z]
        u,s,v=np.linalg.svd(matrx)                  #奇异值分解
        matrx_re=(u[:,0:1]).dot(np.diag(s[0:1])).dot(v[0:1,:])
        matrx_re=matrx_re.reshape((length,2*z))     #形状变换
        x_re=np.zeros(len(signal))                  #分解后数据返回
        x_re[ann[0]:ann[0]+z]=matrx_re[0,z:]
        for i in range(1,length):
            x_re[ann[i]-z:ann[i]+z]=matrx_re[i,:]
                                           #未滤波段使用原值填充                                  
        index=np.where(x_re==0)
        x_re[index]=self.x[index]
        return x_re
    def SSA(self):             #奇异谱分析去除EMG
        ann=self.detectR()
        length=len(self.x)
        if self.L>length/2:
            window=length-self.L
        else:
            window=self.L 
        K=length-window+1
        A=np.zeros((window,K))
        for i in range(K):
            A[0:window,i]=self.x[i:window+i]
        u,s,v=np.linalg.svd(A)
        index=np.where(s/np.sum(s)>0.005)[0]                  #x系数大于0.001特征向量
        Traix=np.zeros((window,length))                    #存储前index个特征向量重构的序列
        u1=np.zeros((u.shape[0],u.shape[1]))
        for i in range(len(index)):                        #便于后面重构每个分量
            u1[:,i]=u[:,i]*s[i]                            #将u的每一列乘上对应的特征值
        for i in range(len(index)):
            base=np.array(u[:,i].reshape((window,1)).dot(v[i,:].reshape((1,K))))
            for j in range(window):
              for m in range(j):
                Traix[i,j]=base[m,j-m]+Traix[i,j]
              Traix[i,j]=Traix[i,j]/(j+1)
            for j in range(window,K):
              for m in range(window):
                Traix[i,j]=base[m,j-m]+Traix[i,j]
              Traix[i,j]=Traix[i,j]/window
            for j in range(K,length):
              for m in range(length-j):
                Traix[i,j]=base[m+1,K-m-1]+Traix[i,j]
              Traix[i,j]=Traix[i,j]/(length-j)
        for i in range(10,20):
            ax=plt.subplot(10,1,i+1-10)
            ax.plot(Traix[i,:])
        plt.show()
    def detectR(self):
        xqrs=processing.XQRS(self.x,360)
        xqrs.detect()
        ann=xqrs.qrs_inds
        return ann            
    def wavlvt(self):          #使用小波去粗EMG 
        a=1
    def double_period(self):
        ann=self.detectR(self.x)
        RR_length=len(ann)
        mean_RR=np.mean(np.diff(ann))
        z=2/3
class ECGwander():
    def __init__(self,x) :
        self.x=x
    def dwt(self):
        b=1
    def emd(self):
        b=1
    def lowpass(self):
        b=1
    def gongpin(self):
        b,a=scipy.signal.butter(4,[0.015,0.30],'bandpass')
        data=scipy.signal.filtfilt(b,a,self.x,axis=0)
        return data
