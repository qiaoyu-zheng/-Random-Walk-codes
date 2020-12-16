import random
import numpy as np 
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(6,4),dpi=200)
plt.rcParams['font.family']='SimHei'
plt.title("2D Random Walk_理论版")
N=1000
d=1
x=np.zeros(N+1)
y=np.zeros(N+1)
x[0]=0
y[0]=0

for i in range(N):
    r=random.random()
    if 0<=r<0.25:
        y[i+1]=y[i]+d
        x[i+1]=x[i]
    elif 0.25<=r<0.5:
        y[i+1]=y[i]
        x[i+1]=x[i]+d
    elif 0.5<=r<0.75:
        y[i+1]=y[i]-d
        x[i+1]=x[i]
    else:
        y[i+1]=y[i]
        x[i+1]=x[i]-d

ax = fig.add_subplot(111)
plt.plot(x,y,'r--',x[0],y[0],x[-1],y[-1],c='blue')
ax.plot(0, 0, c='red', marker='*')
ax.plot(x[N], y[N], c='black', marker='*')
plt.xlabel('East->')
plt.ylabel('North->')
#fig = plt.figure(figsize=(6,4),dpi=200)
plt.savefig("2-D_Random_Walk_理论版")
plt.show()