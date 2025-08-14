# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 19:17:02 2025

@author: juleigar
"""

#Code needs to create a pattern that looks like an arrow
#use for loop, if and else statements
stars =0 #set variable to 0

#start of for loop
for i in range(0,10):
    if i<=5:
        #want each row to increase by 1 until 5 stars in a row
        stars =  '*'*i
        print(stars) #prints the stars as it goes through the loop until condition no longer met
       
    else:
        #now we want to print out the max number of stars -1 each time from the total to get the arrow, need 4, 3, 2 and 1 row to be produced
        print(stars[0:len(stars)-i])
        
       
      
        
        
        
        
        