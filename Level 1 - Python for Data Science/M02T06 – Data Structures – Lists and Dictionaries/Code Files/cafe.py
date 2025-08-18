# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 03:56:51 2025

@author: juleigar
"""
# Defining lists and Dictionaries
menu = ["coffee", "tea", "cake", "muffin"]
stock =  {
    'coffee': 5,
    'tea': 6,
    'cake': 2,
    'muffin': 3
}

price=  {
    'coffee': 3,
    'tea': 2,
    'cake': 4,
    'muffin': 3
}

total_stock=[]
# iterate through the key values
for item in menu:
    item_value = stock[item]*price[item]
    total_stock.append(item_value)
print(total_stock)

        