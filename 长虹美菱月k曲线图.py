from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.tsa.stattools as ts

yarray=[5.72,5.17,5.07,4.7,4.19,4.35,4.2,4.11,3.84,3.81,3.28,3.33,2.92,3.31,2.96,3.01,3.7,3.89,3.89,3.49,3.56,3.47,\
    3.32,3.24,3.35,3.26,3.43,3.31,3.23,3.24,2.82,2.98,2.94,3.89,3.32,3.06,3.09,3.3,4.59]
xarray=range(1,40)
fig = plt.figure(figsize=(6,4),dpi=200)
plt.rcParams['font.family']='SimHei'
plt.suptitle("长虹美菱月k",fontsize=16)
plt.ylabel("收盘价/元")
plt.xlabel("时间间隔/月")
plt.plot(xarray,yarray,c='blue')
plt.savefig("长虹美菱月k")
plt.show()
result = ts.adfuller(yarray, 1)
print(result)














