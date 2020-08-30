#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:00:15 2020

@author: josegrau
"""

#NumpyStackExercise2

import numpy as np
import matplotlib.pyplot as plt

N = 1000
M = 1000
Y = np.zeros(M)

for i in range(M):
    X = np.random.random([N])
    Y[i] = np.sum(X)
    
plt.hist(Y, bins=25)