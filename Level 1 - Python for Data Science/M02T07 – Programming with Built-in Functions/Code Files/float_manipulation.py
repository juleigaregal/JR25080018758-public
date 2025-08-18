# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:59:07 2025

@author: juleigar
"""

import math 
from statistics import mean, median

stored_numbers = []
total_numbers = 0
#Iterate through the inputs, store the data in a list and add each value
for i in range(0,10):
    items = float(input("Enter a float number:"))
    stored_numbers.append(items)
    total_numbers+=items
    
#print the output
print(f"The total is {total_numbers}")
print(f"The minimum is {min(stored_numbers)}")
print(f"The maximum is {max(stored_numbers)}")
print(f"The mean is {mean(stored_numbers)}")
print(f"The median is {median(stored_numbers)}")
