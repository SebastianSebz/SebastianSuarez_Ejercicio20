import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('DataEvol.txt')

x = data[:,0]
y = data[:,1]

plt.figure()
plt.plot(x, y, color = 'g',lw = 5)

plt.savefig('Graph.png')
