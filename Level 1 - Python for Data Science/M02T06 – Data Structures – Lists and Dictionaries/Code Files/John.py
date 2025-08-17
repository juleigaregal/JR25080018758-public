# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 19:28:43 2025

@author: juleigar
"""

correct_name = "John"
name_list =[]
incorrect_name=[]

while name_list != correct_name.lower():
        name_list= input("Enter your name: ")
        #only append names if they are not John
        if name_list!=correct_name.lower():
            incorrect_name.append(name_list)
        #once user enters john, then stop
        else:
            break
#print
print(f"Inncorrect names: {incorrect_name}")  

