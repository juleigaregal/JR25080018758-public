# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 09:11:29 2025

@author: juleigar
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from 0 to 100 in intervals of 0.5
start_val = 0
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

params = np.array([2, -5])

"""
-----------------
Task 1
------------------

Plot f(x) = P.X, where p is your params
"""
y =params[0] * X + params[1]
plt.plot(X, y, color = 'blue')
plt.title("f(y) = 2x - 5")
plt.xlabel("X")
plt.ylabel("y")