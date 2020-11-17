import numpy as np
from wfdb import processing
from matplotlib import pyplot as plt
import test
class filter():
    def __init__ (self,x,L):  #  x为传入需要滤波数据
        self.x=x
        self.L=L
    def APSM_SVD(self):        #自适应周期轨迹矩阵去除EMG
        xqs=processing.XQRS(self.x,fs=360)       #XQRS检测R波 后面可自己更改
        xqs.detect()
        ann=xqs.qrs_inds
        length=len(ann)
        print(length)
        meanRR=np.mean(np.diff(ann))                #求取RR波均值 确定轨迹矩阵长度
        z=np.int(2/3*meanRR)
        signal=self.x[:]                            #浅拷贝
        length_first=len(self.x[ann[0]-z:ann[0]])
        length_last=len(self.x[ann[length-1]:ann[length-1]+z])
        if length_first!=z:
            signal=np.pad(signal,(z-length_first,0),mode='symmetric')
        if length_last!=z:
            signal=np.pad(signal,[0,z-length_last],mode='symmetric')
        matrx=np.zeros((length,2*z))
        for i in range(length):                    #构建轨迹矩阵
            matrx[i,:]=signal[ann[i]-z:ann[i]+z]
        u,s,v=np.linalg.svd(matrx)                  #奇异值分解
        matrx_re=(u[:,0:1]).dot(np.diag(s[0:1])).dot(v[0:1,:])
        matrx_re=matrx_re.reshape((length,2*z))     #形状变换
        x_re=np.zeros(len(signal))                             #分解后数据返回
        for i in range(length):
            x_re[ann[i]-z:ann[i]+z]=matrx_re[i]
        index=np.where(x_re==0)                     #未滤波段使用原值填充
        x_re[index]=signal[index]
        return x_re
    def SSA(self):             #奇异谱分析去除EMG
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
        print(len(s))
        index=np.where(s/sum(s)>0.001)              #x系数大于0.001特征向量
        s1=s[index]
        print(len(s1))
        C=(u[:,200:210]).dot(np.diag(s[200:210])).dot(v[200:210,:])
        C=C.reshape((window,K))
        signal1=np.zeros(length)
        for i in range(K):
            signal1[i:i+window]=C[:,i]
        plt.plot(signal1)
        plt.show()
        for i in range(len(s1)):
          B=(u[:,i:i+1]).dot(np.diag(s[i:i+1])).dot(v[i:i+1,:])  #重构每一个奇异值对应的分量 判断功率谱
          B=A.reshape((window,K))
          signal=np.zeros((length))
          for j in range(K):
             signal[j:j+window]=B[:,j] 

        