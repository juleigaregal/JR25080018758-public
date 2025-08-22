# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 21:50:14 2025

@author: juleigar
"""

# Create a calculator
calculation_output =[]
application_list =['+', '-', '/', '*']
type_of_calculation =[]
x = []
y = []
print_yes_no = []


while True:
    try:
        x = int(input("Enter first integer: "))
        break
    except Exception:
        print("oops please try again: ")

while True:
    try:
        y = int(input("Enter second integer: "))
        break
    except Exception:
        print("oops please try again")
    

while type_of_calculation not in application_list:
    type_of_calculation = input("Enter add, minus, divide or multiply: ")
    if type_of_calculation not in application_list:
        print("please try again and enter a valid option")
   
    elif type_of_calculation == '+':
        calculation_output = x+y
    
    elif type_of_calculation == '-':
        calculation_output = x-y
    
    elif type_of_calculation == '/':
        calculation_output = x/y
    
    elif type_of_calculation == '*':
        calculation_output = x*y
  
        
  
with open("equation.txt", "a") as f:
    f.write(f"{x}{type_of_calculation}{y}={calculation_output} \n")

does_user_want_to_print = input("Do you want to print a history of all calculations?: ")

if does_user_want_to_print=='y':
   with open("equation.txt", "r+") as  file:
    lines =  file.readlines()
    print(lines)
else:
    print("good bye")
