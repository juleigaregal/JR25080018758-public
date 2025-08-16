# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 14:40:34 2025

@author: juleigar
"""
#code needs to alternate between upper and lower case
#need to find the characters in the index to change, for loop used with if statement would work
#store the updated characters in a list
#use join to then add the characters back together to form HeLlO WoRlD
string_name = "Hello World"
string_name_stored = []
string_name_split = string_name.split()
string_alternate_word =[] #variable will hold the final output for second part of question

#loops through the entire string, and uses len to find what the ranage should be
for i in range(0,len(string_name)):
    if i % 2 ==0:
        string_name_stored +=string_name[i].upper()
        #print(string_name_stored)
    else:
        string_name_stored +=string_name[i].lower()
print("".join(string_name_stored))       

#we want to do the same as above but for each word not each letter
#split function would work here

for i in range(0,len(string_name_split)):
    if i % 2 ==0:
        string_alternate_word +=string_name_split[i].upper()+ " "
        #print(string_name_stored)
    else:
        string_alternate_word +=string_name_split[i].lower()
print("".join(string_alternate_word))   