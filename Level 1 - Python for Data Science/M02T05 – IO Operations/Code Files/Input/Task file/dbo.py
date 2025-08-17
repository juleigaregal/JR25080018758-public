# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 07:15:15 2025

@author: juleigar
"""
lines = []

dbo = open("DBO.txt", "r+")

count =0  
#creating a list with the file 2D array
for i in dbo:
    #lines.append(i)  #tried to do this, but hit an error
    parts= i.split()
    lines.append(parts)  #confused about how this works, need some help!
    count += 1 # finding number of rows in file

#Print Names
print("Name") 
for j in range(0,count):
    print(" ".join(lines[j][0:2]))

#Print Birthdate
print(" ")
print("Birthdate")
for j in range(0,count):
    print(" ".join(lines[j][2:5]))

#close file
dbo.close() 