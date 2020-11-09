import pywt
import wfdb
import matplotlib.pyplot as plt


record,filed=wfdb.rdsamp('100',sampfrom=0,sampto=1023,channels=[0])
print(record.flatten())
a,b=pywt.swt(record,'db4',level=1,axis=-1)

plt.plot(a)
plt.plot(b)
plt.show()