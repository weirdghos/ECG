from matplotlib.pyplot import figure
from numpy.core.records import record
import pywt
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from PyEMD import EMD,CEEMDAN
from nosie_perf import sig
from filter1 import filter

clearsignal,field=wfdb.rdsamp('105',channels=[0])
annotation=wfdb.rdann('105','atr')
clearsignal=clearsignal.flatten()
l=clearsignal[6000:9000]
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

plt.show()
ydata=filter(l,1000)
l_1=ydata.APSM_SVD()
l2=ydata.SSA()
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.title('SVD前后对比')
# plt.plot(l,label='原信号',color='blue')
# plt.plot(l_1,label='滤波信号',color='red')
# plt.legend(loc="right")  #显示标签
# plt.show()
a=sig(l_1[0:len(l)],l)
b=a.SNR()
print(b)
