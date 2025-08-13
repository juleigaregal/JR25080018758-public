# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 14:58:04 2025

@author: juleigar
"""
#Code calculate interest on investment or home repayment per month
#user has to enter details regarind investment or bond
#output of code is interest on investment or bond repayment per month
#I am having issues for exiting the code if user doesn't input simple or compound, it should give the user a message but can't figure it out
import math

print("Investment - to calculate the amount of interest you'll earn on your investment: ")

print("Bond - to calculate the amount you'll have to pay on a home loan: ")

investment_type = input("Enter either “investment” or “bond” from the menu above to proceed: ").lower()


if investment_type =="investment":  #user chooses investment as the option
    P = int(input("Enter Amount depositing:"))
    r = float(input("Enter interest between 1 and 100: "))/100
    t = int(input("Number of years investing:"))
    type_of_interest= input("Enter simple or compound interest:").lower()
    if type_of_interest == "simple": #input from user is either simple or compound and calcs are based on this
        A = P*(1+r*t)
    elif type_of_interest == "compound":
        A = P*math.pow((1+r),t)
    print(f"Interest on investment after {t} years is {A}")
elif investment_type =="bond":
    P= int(input("Value of the bond: "))
    i = float(input("Enter interest rate: "))/100/12
    
    n = int(input("Enter number of months to pay off bond "))
    Repayment = (i*P)/(1-(1+i)**(-n))
    print(f"Your monthly repayment amount is {Repayment} on your bond")
else:
    print("You did not enter a valid product type or interest type")