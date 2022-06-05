import math
import numpy as np
import matplotlib.pyplot as plt

"""
# Discretização
delta_phi = 2  # graus
delta_r = 0.0025 # metros
"""

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(0, np.arange(0.03, 0.11, 0.01))
ax.plot(np.deg2rad(40), np.arange(0.03, 0.11, 0.01))
ax.plot(np.arange(0, np.deg2rad(40), 0.01), 0.03)
ax.plot(np.arange(0, np.deg2rad(40), 0.01), 0.11)

ax.set_rmax(0.11)
ax.set_thetamin(0)
ax.set_thetamax(40)

#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()