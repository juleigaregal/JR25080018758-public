# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 08:15:28 2025

@author: juleigar
"""

#will need to store the user inputs
#this code calculates the average value after user is asked to repeatedly enter numbers
#in this code they only exit after they enter a negative number but there should be some other type of check
number =0 #set number to 0
total_numbers  = 0 #will be used in the loop, and will add numbers as the user enters the data
count = 0  #set the counter, this is required to track total number of times the number was entered, and hence can calculate the average
while number >= 0:
    number = int(input("Please enter number: "))
    total_numbers += number #adds numbers together as user enters them

    if number == 0: #if user enters 0
        count -= 1 #deduct this count from the count
    else:
        count += 1

    if number < 0:
        # Remove the negative number's effect on the total
        total_numbers += abs(number)
        count -= 1
        break  # Exit the loop
if count>0:
    #ensures that no calculations happens if the count is zero, in this case user enters zeros repeatedly
    print(total_numbers/count)       
else:
    print("no valid numbers entered")
    
   
