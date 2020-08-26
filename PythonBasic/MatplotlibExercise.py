#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:29:21 2020

@author: josegrau
"""

#Matplotlib Exercise

import numpy as np
import matplotlib.pyplot as plt

X = np.random.random((1000,2))
X[:250] -= 1
X[500:750,0] -= 1
X[750:,1] -= 1

Y = np.zeros(1000)
Y[500:] = 1

plt.scatter(X[:,0],X[:,1],c=Y)
plt.show()