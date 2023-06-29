import random
import matplotlib.pyplot as plt
import numpy as np

voltage = [value + random.uniform(-0.1, 0.1) for value in np.arange(1,20,0.5)]   

print(voltage)

resistance = 10

current = [v/resistance + random.uniform(-0.02, 0.02) for v in voltage]

print(current)

plt.plot(voltage,current)
plt.title("Current vs. voltage")
plt.show()
