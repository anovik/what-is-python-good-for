import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4*np.pi,4*np.pi,0.1)   
y = np.sin(x)

plt.plot(x,y)
plt.title("The graph of sin(x)")
plt.show()

x = np.arange(1,10,0.1)   
f1 = x
f2 = x**2

plt.plot(x, f1, 'r')
plt.plot(x, f2, 'g')
plt.title("The graphs of several functions")
plt.legend(['x', 'x^2'])
plt.show()