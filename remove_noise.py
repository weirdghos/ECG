from matplotlib.pyplot import figure
from numpy.core.records import record
import pywt
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from PyEMD import EMD
from nosie_perf import sig


clearsignal,field=wfdb.rdsamp('105',channels=[0])
annotation=wfdb.rdann('105','atr')
clearsignal=clearsignal.flatten()
l=clearsignal[0:1500]
# (cA2, cD2), (cA1, cD1)=pywt.swt(l,'db4',level=2)  SWT
# emd = EMD(DTYPE=np.float16,spline_kind='akima',max_imfs=8)  #16位浮点数计算 样条拟合改为akima或分段插值（降低计算量） 插值方面 
# imf=emd(l)
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



index=annotation.sample  #sample R波位置  symbol 心拍类型
index2=index[1:6]
meanRR=np.round(np.mean(np.diff(index2)))
z=np.int(2/3*meanRR)
matrx=[]
for i in range(5):
   matrx.append(l[index2[i]-z:index2[i]+z])

matrx=np.array(matrx)
matrx=matrx.reshape((5,340))
u,s,v=np.linalg.svd(matrx)
s[1:len(s)]=0
matrx_reconsructed=(u[:,0:1]).dot(np.diag(s[0:1])).dot(v[0:1,:])
lsit=matrx_reconsructed.reshape((5,340))
plt.plot(lsit[0])
plt.plot(matrx[0])
plt.show()
a=sig(lsit[0],matrx[0])
b=a.SNR()
print(b)
# for i in range(len(index)):
#     meanRR=np.mean(index[i:i+5])