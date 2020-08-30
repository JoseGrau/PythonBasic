#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:42:53 2020

@author: josegrau
"""

#NumpyStackExercise5

import numpy as np

def is_symmetric_loop(matrix):
    ans = True
    if len(matrix) != len(matrix[0]):
        print("La matriz no es cuadrada")
        return False
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):  
                if (matrix[i,j] != matrix[j,i]):
                    ans = False
    return ans

def is_symmetric(matrix):
    if np.array_equal(matrix, np.transpose(matrix)):
        return True
    else:
        return False

matrix = np.array([[1,1],[2,1]])
print(is_symmetric(matrix))


