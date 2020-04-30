import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

plt.plot(x, y, 'r-')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')

plt.subplot(1,2,1)
plt.plot(x, y, 'r')

plt.subplot(1,2,2)
plt.plot(y, x, 'b')

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel('X Label')
axes.set_title('Set Title')

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes1.set_title('LARGER PLOT')

axes2.plot(y, x)
axes2.plot('SMALLER PLOT')

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.show()