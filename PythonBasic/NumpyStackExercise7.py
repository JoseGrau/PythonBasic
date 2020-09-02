#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:24:50 2020

@author: josegrau
"""

#NumpyStackExercise7

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

size = 1000
rad = np.random.random(size) * 250
mod = np.random.randn(size) + 10

x0= mod * np.cos(rad)
x1= mod * np.sin(rad)
x = np.vstack((x0,x1))

rad = np.random.random(size) * 250
mod = np.random.randn(size) + 20
x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)

y = np.zeros(2000)
y[1000:] = 1

colores = colors.ListedColormap(['b','r'])

plt.scatter(x[0,:],x[1,:], c = y, cmap=colores)





