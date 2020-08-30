#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:46:54 2020

@author: josegrau
"""

#NumpyStackExercise1

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0.3,0.6,0.1],[0.5,0.2,0.3],[0.4,0.1,0.5]])
v = np.array([1/3,1/3,1/3])
x = np.ones(25)

for i in range(25):
    v1 = np.dot(v,A)
    x[i] = np.linalg.norm(v-v1)
    v = v1
    
plt.plot(x)
