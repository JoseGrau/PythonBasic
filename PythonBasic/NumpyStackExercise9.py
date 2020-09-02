#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:24:50 2020

@author: josegrau
"""

#NumpyStackExercise9

import pandas as pd

#Usando el ejercicio 8 anterior
import NumpyStackExercise8 as ex

x = ex.x
y = ex.y

df = pd.DataFrame({'x1' : x[0,:], 'x2' : x[1,:], 'y' : y})

df.to_csv('NumpyStackExercise9.csv', index = False)