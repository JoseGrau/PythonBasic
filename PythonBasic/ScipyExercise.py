#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:49:37 2020

@author: josegrau
"""

#Scipy Exercise

from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

#Funciona, no entiendo el error
#!wget https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/cnn_class/lena.png

im = Image.open('lena.png')

gray = np.mean(im, axis=2)

Hx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
Hy = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

Gx = convolve2d(gray,Hx)
Gy = convolve2d(gray,Hy)
G = np.sqrt(Gx**2+Gy**2)

plt.imshow(G, 'gray')

