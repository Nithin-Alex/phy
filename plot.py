import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('2016-07-11_ipm_data.txt')
max_index = np.argmax(data)
max_value = data[max_index]
plt.plot(data, color='blue')
plt.scatter(max_index, max_value, color='red')
plt.grid(color='black', linestyle='-', linewidth=0.5, alpha=0.5)
plt.savefig('plot.png')
plt.show()
