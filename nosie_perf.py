
import numpy as np



class sig():
  def __init__(self,original_signal,reconstructed_signal):
      self.original_signal=     original_signal
      self.reconstructed_signal=reconstructed_signal
  def SNR(self):
     #滤波后的ECG信号/噪声 求分贝
     snr=10*np.log10(np.sum(self.reconstructed_signal**2)/np.sum((self.reconstructed_signal-self.original_signal)**2))
     return snr
  def PRD(self):   #百分比均方根误差
     prd=np.sqrt((self.reconstructed_signal-self.original_signal)**2 /self.reconstructed_signal**2)
     return prd
  def PRD1(self):
     prd1=np.sqrt()
     return prd1
a=np.random.rand(10)
b=np.random.rand(10)
p1=sig(a,b)
print(p1.SNR())


