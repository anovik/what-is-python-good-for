import random
import matplotlib.pyplot as plt
import numpy as np

voltage = [value + random.uniform(-0.1, 0.1) for value in np.arange(1,20,0.5)]   

print(voltage)

resistance = 10

current = [v/resistance + random.uniform(-0.02, 0.02) for v in voltage]

print(current)

plt.xlabel('Voltage', fontsize=14)
plt.ylabel('Current', fontsize=14)
plt.plot(voltage,current,'o')
plt.title("Current vs. voltage", fontsize=20)
plt.show()


plt.xlabel('Voltage', fontsize=14)
plt.ylabel('Current', fontsize=14)
plt.plot(voltage,current,'o')
plt.plot(voltage, [v/10 for v in voltage], 'r') 
plt.title("Current vs. voltage", fontsize=20)
plt.show()
