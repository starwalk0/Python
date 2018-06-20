# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:59:47 2018

@author: starw_hyrtn4v
"""

import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('title')

#%%

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])

ax1.plot(x,y, color='red')
ax2.plot(x,y, color='red')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
#%%

fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])

ax1.plot(x,z)
ax2.plot(x,y)

ax1.set_xlabel('X')
ax1.set_ylabel('Z')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Zoom')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])

#%%

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (12,2))


axes[0].plot(x,y, color='blue', linewidth=3, linestyle='-')
axes[1].plot(x,z, color='red', linewidth = 3, linestyle='--')