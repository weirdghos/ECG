import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit


def SSR1(x):
  L=500
  N=len(x)
  K=N-L+1
  A=np.zeros((L,K))
  for i in range(K):
      A[0:L,i]=x[i:i+L]
  u,s,v=np.linalg.svd(A)
  u1=np.zeros((u.shape[0],u.shape[1]))
  for i in range(u.shape[1]):   #先将特征值乘上 
    u1[:,i]=u[:,i]*s[i]
  x=np.zeros((L,len(x)))
  for i in range(L):
    b=u1[:,i].copy().reshape((-1,1)).dot(v[i,:].copy().reshape(1,-1))
    for j in range(L):
        for m in range(j):
          x[i,j]=b[m,j-m]+x[i,j]
        x[i,j]=x[i,j]/(j+1)
    for j in range(L,K):
        for m in range(L):
          x[i,j]=b[m,j-m]+x[i,j]
        x[i,j]=x[i,j]/L
    for j in range(K,N):
        for m in range(N-j):
          x[i,j]=b[m+1,K-m-1]+x[i,j]
        x[i,j]=x[i,j]/(N-j)
    return x

def SSR(x):
  L=500
  N=len(x)
  K=N-L+1
  A=np.zeros((L,K))
  for i in range(K):
      A[0:L,i]=x[i:i+L]
  u,s,v=np.linalg.svd(A)
  aver(u,v,s,L,K)
@jit(nopython=True)
def aver(u,v,s,L,K):
  u1=np.zeros((u.shape[0],u.shape[1]))
  N=L+K-1
  for i in range(u.shape[1]):   #先将特征值乘上 
    u1[:,i]=u[:,i]*s[i]
  x=np.zeros((L,L+K-1))
  for i in range(L):
    b=u1[:,i].copy().reshape((-1,1)).dot(v[i,:].copy().reshape(1,-1))
    for j in range(L):
        for m in range(j):
          x[i,j]=b[m,j-m]+x[i,j]
        x[i,j]=x[i,j]/(j+1)
    for j in range(L,K):
        for m in range(L):
          x[i,j]=b[m,j-m]+x[i,j]
        x[i,j]=x[i,j]/L
    for j in range(K,N):
        for m in range(N-j):
          x[i,j]=b[m+1,K-m-1]+x[i,j]
        x[i,j]=x[i,j]/(N-j)
    return x
x=np.random.randn(2000)
a=time.time()
SSR(x)
b=time.time()
a1=time.time()
SSR1(x)
b1=time.time()
print(b-a)
print(b1-a1)


