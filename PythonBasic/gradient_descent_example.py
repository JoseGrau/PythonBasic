#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:02:11 2020

@author: josegrau
"""

#Ejemplo de gradient descent para la funcion J = w^2 (dJ = 2*w)

import numpy as np
import matplotlib.pyplot as plt

#Empezamos en w = 20, y sabemos que queremos llegar al valor w = 0
w = 20
#Fijamos el paso y el número de iteraciones
rate = 0.1
steps = 100

p = np.zeros(steps)
#Probamos el método
for i in range(steps):
    w -= rate*2*w
    p[i] = w
    print(w)
    
#visualización
x = np.arange(39)-19

plt.plot(x,x**2,'k',p,p**2,'bo')