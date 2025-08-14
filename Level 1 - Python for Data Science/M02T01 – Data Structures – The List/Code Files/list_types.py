# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 06:25:32 2025

@author: juleigar
"""

#Create a new Python fi le in this folder called list_types.py.
# Imagine you want to store the names of three of your friends in a list of strings. Create a list variable called friends_names, and write the syntax to store the full names of three of your friends.
# Now, write statements to print out the name of the fi rst friend, then the name of the last friend, 
#and fi nally the length of the list. 7
# Now, defi ne a list called friends_ages that stores the age of each of your friends in a corresponding manner, i.e., the fi rst entry of this list is the age of the friend named fi rst in the other list.
# Print each friend’s name and age in a sentence similar to this:
#Sophia is 25 years old

friends_names = ["Jane", "Harry", "Kate"]  #list storing names of friends
print(f"Name of my first friend is {friends_names[0]}.") #print first friend using index
print(f"Name of my first friend is {friends_names[-1]}.") #print last friend using index
print("Number of friends in the list is :" + str(len(friends_names)))

friends_ages = [20,25,23]

for i in range(0,3): # creating a range that has the same number of elements as friends_names and friends_age to loop through printing the names and ages in sentence
    print(f"{friends_names[i]} is {friends_ages[i]} years old.") # the loop makes this more efficient than having to code a line for each sentence