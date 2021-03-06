#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:47:55 2020

@author: josegrau
"""

#NumpyStackExercise4

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
idx = np.argsort(y_train)
x_train_sorted = x_train[idx]


x = x_train[y_train == 7]
y = x.mean(axis = 0)

img = np.rot90(y,3)

#h,w = y.shape
#img = np.zeros([h,w])
#for i in range(h):
#    for j in range(w):
#        img[i,j] = y[-j+1,i-1]
#        img = img[0:h,0:w]


plt.imshow(img,cmap = 'gray')
plt.show()
