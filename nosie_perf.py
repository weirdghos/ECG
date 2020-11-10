
import numpy as np
from scipy import stats
class sig():
  def __init__(self,original_signal,reconstructed_signal):
      self.original_signal=     original_signal          #b表示干净信号
      self.reconstructed_signal=reconstructed_signal     #去噪后的信号
  def SNR(self):
     #滤波后的ECG信号/噪声 求分贝
     snr=10*np.log10(np.sum(self.original_signal**2)/np.sum((self.reconstructed_signal-self.original_signal)**2))
     return snr
  def PRD(self):   #百分比均方根误差
     prd=np.sqrt((self.reconstructed_signal-self.original_signal)**2 /self.original_signal)   #公式可能有问题 再找一哈
     return prd
  def MSE(self): #均方误差
     mse=(np.sum((self.original_signal-self.reconstructed_signal)**2))/len(self.original_signal)
     return mse
  def corelete(self):  #皮尔森相关系数
     pccs=stats.pearsonr(self.original_signal,self.reconstructed_signal)
     return pccs


