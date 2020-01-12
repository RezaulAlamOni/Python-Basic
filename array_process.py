from __future__ import division
import numpy as np
import matplotlib.pyplot as mlt

points = np.arange(-5,5,0.01)

dx,dy = np.meshgrid(points,points)

z = (np.sin(dx) + np.sin(dy))
mlt.imshow(z)
# print(z)
mlt.show()



