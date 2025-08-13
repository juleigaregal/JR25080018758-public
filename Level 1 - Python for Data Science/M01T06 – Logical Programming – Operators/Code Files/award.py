# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 08:32:54 2025

@author: juleigar
"""

cycling_time = int(input("Please enter time taken to complete cycling (in minutes):"))
running_time = int(input("Please enter time taken to complete running (in minutes):"))
swimming_time = int(input("Please enter time taken to complete swimming (in minutes):"))

total_time_taken = cycling_time + running_time + swimming_time

print(f"You took {total_time_taken} minutes to complete the Triathlon.")

if total_time_taken <=100:
    print("Congratulations, you received Provincial Colours!")
elif total_time_taken >=101 and total_time_taken <=105:
    print("Congratulations, you received Provincial half colours")
elif total_time_taken >=106 and total_time_taken <=110:
    print("You received Provincial scroll.")
elif total_time_taken >=111:
    print("Unfortunately, you received no award.")
    
    