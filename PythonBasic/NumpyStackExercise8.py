#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:24:50 2020

@author: josegrau
"""

#NumpyStackExercise8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

size = 100
noise= 0.3
t = (np.random.random(size))
rad = t + np.random.random(size)*noise
mod = t


x0= mod * np.cos(rad)
x1= mod * np.sin(rad)
x = np.vstack((x0,x1))

t = (np.random.random(size))
rad = t+2 +np.random.random(size)*noise
mod = t


x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)

t = (np.random.random(size))
rad = t+4 +np.random.random(size)*noise
mod = t


x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)

t = (np.random.random(size))
rad = t+1 +np.random.random(size)*noise
mod = t


x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)

t = (np.random.random(size))
rad = t+3 +np.random.random(size)*noise
mod = t


x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)


t = (np.random.random(size))
rad = t+5 +np.random.random(size)*noise
mod = t


x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)


y = np.zeros(6*size)
y[3*size:] = 1

colores = colors.ListedColormap(['b','r'])

plt.scatter(x[0,:],x[1,:], c = y, cmap=colores)