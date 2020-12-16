from matplotlib import pyplot as plt
import numpy as np

#This is the codes for 2-D random walk

dims = 2
step_n = 50000
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))
# Simulate steps in 2D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]
# Plot the path image
fig = plt.figure(figsize=(6,4),dpi=200)
ax = fig.add_subplot(111)
ax.scatter(path[:,0], path[:,1],c='blue',alpha=0.25,s=0.05)
ax.plot(path[:,0], path[:,1],c='blue',alpha=0.5,lw=0.25,ls='-')
ax.plot(start[:,0], start[:,1],c='red', marker='*')
ax.plot(stop[:,0], stop[:,1],c='black', marker='*')
plt.title('2D Random Walk_Brown')
plt.tight_layout(pad=0)
plt.savefig('2-D Random_Walk_Brown.png',dpi=250)
plt.show()

