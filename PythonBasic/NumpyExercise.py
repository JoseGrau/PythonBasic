#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:27:10 2020

@author: josegrau
"""

#Numpy exercise
#speed test matrix multiplication for list and vs for np function
#Bonus: how does time increase wrt input size?
#Answer:
#for 3x3: around 10
#for 10x10: around 200
#for 100x100: around ??? too much time to compile

import numpy as np
from datetime import datetime

# note: you can also use %timeit

A = np.random.random((100,100))
B = np.random.random((100,100))
T = 100000

def slow_dot_product(A, B):
	result = np.zeros((len(A), len(B[0])))
	for i in range(len(A)):
            for e, f in zip(A[0], B[:,0]):
                result += e*f
	return result

t0 = datetime.now()
for t in range(T):
	slow_dot_product(A, B)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
	A.dot(B)
dt2 = datetime.now() - t0

print("dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds())