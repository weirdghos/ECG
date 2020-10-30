import numpy as np
import scipy.signal as signal
import wfdb
import matplotlib.pyplot as plt
def pan_detectors(n,data):
    global location
    fs=360
    location=[]
    processed_data=np.convolve(np.power(np.diff(data),2),np.ones(n)/n,mode='full')
    pks,_=signal.find_peaks(processed_data,distance=0.2*fs)      #在距离0.2*fs寻找峰值 可以遍历比较值大小 距离内存在多个最大值则消除
    pks=[x for x in pks if processed_data[x] > np.max(processed_data[x:x + 2 * fs]) * 1 / 2]
    print(len(pks))
    pkstemp=[]
    pksmisstemp=[]
    location_temp=[]
    the_noise=np.mean(processed_data[0:2*fs])*1/2
    for i in range(0,len(pks)-1):
       if pks[0]>160:
          pks_first=np.argmax(processed_data[0:pks[0]-int(0.2*fs)])
          slope1=np.mean(np.diff(processed_data[pks_first-int(0.075*fs):pks_first]))
          slope2=np.mean(np.diff(processed_data[pks[0]-int(0.075 * fs):pks[0]]))
          if slope1>slope2:
              pksmisstemp.append(pks_first)
              location.append(pks_first)
       if pks[i]-60>0 and pks[i]<len(processed_data):                                #寻找原信号中的峰值
          jkl=np.argmax(data[pks[i]-60:pks[i]])
          location.append(jkl+pks[i]-60)
          if len(location)>1 and np.diff(location[i-1:i])<0.36*fs:
             slope_cur_pdata  =np.mean(np.diff(processed_data[pks[i]-int(0.075 * fs) : pks[i]]))
             slope_prev_pdata =np.mean(np.diff(processed_data[pks[i-1]- int(0.075 * fs):pks[i-1]]))
             if slope_cur_pdata < 0.5 * slope_prev_pdata:
               pkstemp.append(pks[i])
          if len(location)>9:
             RR_means=np.mean(np.diff(location[i-9:i]))                                #get 8 means of RR in ECG
             cur_RR=np.diff(location[i-1:i])                                           #current location RR
             if cur_RR>1.50*RR_means:
              index_pdata=np.argmax(processed_data[pks[i-1]+0.2*fs:pks[i]-0.2*fs])     #在绝对不应期外寻找漏掉峰值
              pks_temp=processed_data[index_pdata+pks[i-1]+0.2*fs]                     #平滑信号中寻找最大值
              pks_index=index_pdata+pks[i-1]+0.2*fs
              pksmisstemp.append(pks_index)                                            #插入pks[i]
              if processed_data[pks_index]>the_noise:
                  index_odata=np.argmax(data[pks_index-60:pks_index])
                  locationvalue= data[index_odata+pks_index-60]                         #寻找原信号中漏掉的R峰索引
                  location_temp.append(index_odata+pks_index-60)

    return location