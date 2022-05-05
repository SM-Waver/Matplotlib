import matplotlib.pyplot as plt
import numpy as np

plt.title("Basic matplotlib")

x = np.array([7, 8 ,1 ,5])
y = np.array([4, 3, 7, 9])

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x, y)
plt.show()