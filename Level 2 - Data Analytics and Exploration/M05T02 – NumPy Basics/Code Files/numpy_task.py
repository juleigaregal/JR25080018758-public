# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 09:41:46 2025

@author: juleigar
"""

import numpy as np

# -------------------- Task i --------------------
# Correct way to create a 2D array of floats
print("Task i")
x = np.array([
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)
], dtype=float)

print(f"Number of dimensions: {x.ndim}")
print("Array:\n", x)


# -------------------- Task ii --------------------
print("\nTask ii")
a = np.array([0, 0, 0])      # 1-dimensional
b = np.array([[0, 0, 0]])    # 2-dimensional

print(f"a is {a.ndim} Dimensional")
print(f"b is {b.ndim} Dimensional")


# -------------------- Task iii --------------------
print("\nTask iii")
# Create 3x4x4 array from 1 to 48
array = np.linspace(1, 48, 48).reshape(3, 4, 4)
print(array)

# -------------------- Task iv.1 --------------------
print("\nTask iv.1")
x_1 = array[1, 0, 3]
print(x_1)


# -------------------- Task iv.2 --------------------
print("\nTask iv.2")
x_2 = array[0, 2, :]
print(x_2)


# -------------------- Task iv.3 --------------------
print("\nTask iv.3")
x_3 = array[2, :, :]
print(x_3)


# -------------------- Task iv.4 --------------------
print("\nTask iv.4")
x_4 = array[:, 1, :-2]
print(x_4)


# -------------------- Task iv.5 --------------------
print("\nTask iv.5")
# Reverse columns, then take first two columns of last layer
x_5 = array[:, :, ::-1]
x_5 = x_5[2, :, 0:2]
print(x_5)


# -------------------- Task iv.6 --------------------
print("\nTask iv.6")
# Transpose (swap rows & columns), reverse columns, select first row
x_6 = np.transpose(array, (0, 2, 1))
x_6 = x_6[:, :, ::-1]
x_6 = x_6[:, 0, :]
print(x_6)


# -------------------- Task iv.7 --------------------
print("\nTask iv.7")
# Pick first layer first row (first & last element)
row1 = array[0, 0, [0, -1]]
# Pick last layer last row (first & last element)
row2 = array[-1, -1, [0, -1]]
# Stack into 2x2 array
x_7 = np.vstack([row1, row2])
print(x_7)


# -------------------- Task iv.8 --------------------
print("\nTask iv.8")
# Rows 2-3 from second layer and rows 0-1 from third layer
x_8_part1 = array[1, 2:, :]
x_8_part2 = array[2, 0:2, :]
# Stack vertically to form 4x4 array
x_8 = np.vstack([x_8_part1, x_8_part2])
print(x_8)
