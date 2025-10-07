# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 08:06:19 2025

@author: juleigar
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from -100 to 100 in intervals of 0.5
start_val = -100
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

params = [1.2, 0.5, 2, -5]

"""
-----------------
Optional Task
------------------

Plot f(x) = P.X, where p is your params
"""
y = params[0] * X**3 + params[1] * X**2 + params[2] * X + params[3]
plt.plot(X, y, color="blue")

# Format the equation dynamically with correct signs
sign2 = '+' if params[1] >= 0 else '-'
sign3 = '+' if params[2] >= 0 else '-'
sign4 = '+' if params[3] >= 0 else '-'

plt.title(
    f"f(x) = {params[0]:.1f}x³ {sign2} {abs(params[1]):.1f}x² "
    f"{sign3} {abs(params[2]):.1f}x {sign4} {abs(params[3]):.1f}"
)

plt.ylabel("y")
plt.xlabel("X")
plt.grid(True)
plt.show()
