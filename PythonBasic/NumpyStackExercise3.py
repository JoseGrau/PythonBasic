#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:10:14 2020

@author: josegrau
"""

#NumpyStackExercise3

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
idx = np.argsort(y_train)
x_train_sorted = x_train[idx]

for i in range(10):
    x = x_train[y_train == i]
    y = x.mean(axis = 0)
    plt.imshow(y,cmap = 'gray')
    plt.show()




