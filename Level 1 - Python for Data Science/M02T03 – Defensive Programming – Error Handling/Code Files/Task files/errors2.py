# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 14:04:06 2025

@author: juleigar
"""

# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error missing qoutation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth") #syntax error and logical error the variables in wrong order, need to use {} to add the avariable

print(full_spec) #synax error missing the brackets