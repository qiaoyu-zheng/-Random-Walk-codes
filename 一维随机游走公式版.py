import matplotlib.pyplot as plt
import numpy as np

#rect=[0.1,5.0,0.1,0.1]
plt.rcParams['font.family']='SimHei'
fig=plt.figure()
 #time span
T=20
#drift factor飘移率
mu=0.1 
#volatility波动率
sigma=0.04 
#t=0初试价
S0=50
#length of steps
dt=0.01 
N=round(T/dt)
t=np.linspace(0,T,N)
fig = plt.figure(figsize=(6,4),dpi=200)
ax = fig.add_subplot(111)
#布朗运动
W=np.random.standard_normal(size=N)
W=np.cumsum(W)*np.sqrt(dt)
X=(mu-0.5*sigma**2)*t+sigma*W

S=S0*np.exp(X)
ax.plot(0,50 ,c='red', marker='*')
#ax.plot(S,20, c='black', marker='*')
plt.plot(t,S,c='blue',lw=2)
plt.title('1D Random Walk_公式版')
plt.savefig("1-D_Random_Walk_公式版.png")
plt.show()