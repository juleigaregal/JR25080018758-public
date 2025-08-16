# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 14:09:07 2025

@author: juleigar
"""

count =0
age =[20,35,30]

for i in age:
    if i >30:
        print("I am younger than 30 years old")
    else:
        break
        print("You are not in the age range")  #logically the break statement should come before the print statement
    