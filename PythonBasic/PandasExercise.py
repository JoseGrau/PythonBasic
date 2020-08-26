#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:24:50 2020

@author: josegrau
"""

#Pandas Exercise

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

size = 1000
rad = np.random.random(size) * 250
mod = np.random.randn(size) + 5

x0= mod * np.cos(rad)
x1= mod * np.sin(rad)
x = np.vstack((x0,x1))

rad = np.random.random(size) * 250
mod = np.random.randn(size) + 10
x0= mod * np.cos(rad)
x1= mod * np.sin(rad)

x3 = np.vstack((x0,x1))
x = np.concatenate((x,x3), axis=1)

y = np.zeros(2000)
y[1000:] = 1

plt.scatter(x[0,:],x[1,:], c = y)

df = pd.DataFrame({'x1' : x[0,:], 'x2' : x[1,:], 'y' : y})

#aqui hay un problema
df['x1^2'] = df.x1**2
df['x2^2'] = df.x2**2
df['x1*x2'] = df.x1*df.x2

df = df[['x1', 'x2', 'x1^2', 'x2^2', 'x1*x2', 'y']]



df.to_csv('PandasExercise.csv', index = False)