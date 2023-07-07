import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_surface(data):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(data, Y=data, Z=data, cmap='jet')
  plt.show()

data = np.random.rand(100, 10)

plot_surface(data)
