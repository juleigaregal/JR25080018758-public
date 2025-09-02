# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 19:20:55 2025

@author: juleigar
"""

def sum_recursion(num_list,index_point):
  
   
    if index_point==0:
        
        return(num_list[0])
       
        
     
      
    else:
        
        return num_list[index_point] +(sum_recursion(num_list,index_point-1))
   
        

a_list = [1,3,4,5,7]
index = 3
x=sum_recursion(a_list, index)
print(x)

    