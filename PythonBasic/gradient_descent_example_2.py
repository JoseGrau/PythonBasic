#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:12:30 2020

@author: josegrau
"""

#Ejemplo de gradient descent para la funcion J = w1^2 + w2^4

#dJ/dw1 = 2*w1, dJ/dw2=4*w2^3



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
#Empezamos en w1,w2 = algún valor , y sabemos que queremos llegar al valor w = 0
w1 = -42
w2 = 12
dw1 = 2*w1
dw2 = 4*w2**3
#Fijamos el paso y el número de iteraciones
rate = 0.003
steps = 10000

p1 = np.zeros(steps+1)
p2 = np.zeros(steps+1)
p1[0] = w1
p2[0] = w2
#Probamos el método
for i in range(steps):
    w1 -= rate*dw1
    w2 -= rate*dw2
    dw1 = 2*w1
    dw2 = 4*w2**3
    p1[i+1] = w1
    p2[i+1] = w2

print(w1)
print(w2)

fig = plt.figure()
ax = plt.axes(projection="3d")

x = np.linspace(-50, 50, 100)
y = np.linspace(-50, 50, 1000)

X, Y = np.meshgrid(x, y)
Z = X**2+Y**4

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.view_init(elev=30, azim=15)
ax.plot_wireframe(X, Y, Z, alpha = 0.2)

ax = plt.gca()


ax.scatter(p1, p2, p1**2+p2**4, color="red")