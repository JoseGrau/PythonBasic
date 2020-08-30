#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:14:56 2020

@author: josegrau
"""

#NumpyStackExercise6

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

X = np.random.random((1000,2))
X[:250] -= 1
X[500:750,0] -= 1
X[750:,1] -= 1

Y = np.zeros(1000)
Y[500:] = 1

colores = colors.ListedColormap(['b','r'])

plt.scatter(X[:,0],X[:,1],c=Y,cmap = colores)
plt.show()