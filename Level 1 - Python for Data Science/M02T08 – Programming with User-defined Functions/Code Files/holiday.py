# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 20:01:28 2025

@author: juleigar
"""


num_nights = int(input("Enter total number of nights at hotel:"))
cost_hotel = 100

rental_days = int(input("Enter number of days for car rental:"))
cost_car = 50

city_flight = input("Enter a choice of one of these cities, nyc, london, boston: ").lower()

#plane cost function
def plane_cost(a):
    if a =="nyc":
        flight_cost = 200
   
    elif a =="london":
        flight_cost = 1000
    
    else:
        flight_cost = 150
    return flight_cost
    

#hotel cost function
def hotel_cost(a, b):
    total_hotel_cost = a*b
    return total_hotel_cost

#car rental function
def car_rental(a,b):
    total_cost_car_rental = a*b
    return total_cost_car_rental

#holiday cost function
def holiday_cost(num_nights, city_flight,rental_days):
    total_cost_of_holiday = hotel_cost(cost_hotel, num_nights)+plane_cost(city_flight)+car_rental(cost_car, rental_days)
    return total_cost_of_holiday

#Calculate total holiday expense
total_holiday_expense = holiday_cost(num_nights, city_flight, rental_days)
print("Total Holiday Cost for " +str(num_nights) +" nights, and flight to "+city_flight.upper() + " with rental car for "
      + str(rental_days)+" days is " + "$"+str(total_holiday_expense))
