#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:26:42 2020

@author: guilhermearanha
"""

import matplotlib.pyplot as plt
import numpy as np

fig, window = plt.subplots()

x = [1]
a = [1]
b = [1]
c = [1]

for i in range(99):
    x.append(1+i*0.05)
    a.append(a[i] +1)
    b.append(b[i] *1.05)
    c.append(0.1 + c[i] **1.01)
    
#print(a)
#print(b)
#print(c)

window.plot(x, a, label = 'a')
window.plot(x, b, label = 'b')
window.plot(x, c, label = 'c')

window.legend()

