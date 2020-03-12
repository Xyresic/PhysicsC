import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np


x = np.array(list(range(1,22,2))*9)
y = np.array(sum([[i]*11 for i in range(1,19,2)],[]))
z = sum([l.strip().split(',') for l in open('voltages.csv','r').readlines()],[])
z = [float(i) for i in z]

x_grid = np.linspace(1,22,500)
y_grid = np.linspace(1,18,500)
m_x, m_y = np.meshgrid(x_grid,y_grid,indexing='xy')
z_interpolated = np.zeros((99,99))

spline = interpolate.Rbf(x,y,z)
z_interpolated = spline(m_x,m_y)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(m_x, m_y, z_interpolated, cmap=plt.cm.RdBu, linewidth=0.2)
ax.set_xlabel('X coordinate (cm)')
ax.set_ylabel('Y coordinate (cm)')
ax.set_zlabel('Voltage (V)')

fig.colorbar(surf)

plt.title('Electric Potential Scalar Field')
plt.show()