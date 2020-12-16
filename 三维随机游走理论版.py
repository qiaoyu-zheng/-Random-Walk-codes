from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#This is the codes for 3-D random walk

plt.rcParams['font.family']='SimHei'
fig = plt.figure(figsize=(6,4),dpi=200)
dims = 3
step_n = 5000
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))
# Simulate steps in 3D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]
#Plot the path
fig = plt.figure(figsize=(10,10),dpi=200)
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)
ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.scatter3D(path[:,0], path[:,1], path[:,2], c='blue', alpha=0.25,s=1)
ax.plot3D(path[:,0], path[:,1], path[:,2], c='blue', alpha=0.5, lw=0.5)
ax.plot3D(start[:,0], start[:,1], start[:,2], c='red', marker='*')
ax.plot3D(stop[:,0], stop[:,1], stop[:,2], c='black', marker='*')
plt.title('3D_Random_Walk_理论版')
plt.savefig('3-D_Random_Walk_理论版.png',dpi=250)
plt.show()