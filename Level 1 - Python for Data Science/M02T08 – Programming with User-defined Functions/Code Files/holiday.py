# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 10:51:05 2025

@author: juleigar

Calculate the total cost of a holiday
including flights, hotel, and car rental.
"""


def plane_cost(city_flight):
    """
    Returns the flight cost based on the chosen city.
    """
    if city_flight == "nyc":
        return 200
    elif city_flight == "london":
        return 1000
    elif city_flight == "boston":
        return 150


def hotel_cost(num_nights):
    """
    Returns the total hotel cost.
    Cost per night = £100
    """
    cost_hotel_per_night = 100
    return num_nights * cost_hotel_per_night


def car_rental(rental_days):
    """
    Returns the total car rental cost.
    Cost per day = £50
    """
    cost_car_per_day = 50
    return rental_days * cost_car_per_day


def holiday_cost(city_flight, num_nights, rental_days):
    """
    Calculates and returns all individual costs
    and the total holiday cost.
    """
    flight = plane_cost(city_flight)
    hotel = hotel_cost(num_nights)
    car = car_rental(rental_days)
    total_holiday_cost = flight + hotel + car
    return hotel, flight, car, total_holiday_cost



# Main Code

# List of valid cities
travel_cities = ["nyc", "london", "boston"]

# Ensure code can handle exceptions, so that the user is prompted to enter correc info
city_flight = ""
while city_flight not in travel_cities:
    city_flight = input("Enter a choice of one of these cities, nyc, london, boston:  ").lower()
    if city_flight not in travel_cities:
        print("Invalid choice. Please try again.")

# User inputs
num_nights = int(input("Enter total number of nights at hotel: "))
rental_days = int(input("Enter number of days for car rental: "))

# Calculate costs
hotel, flight, car, total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

# Display Holiday Information
print(f"\nHoliday Details:")
print(f"Destination: {city_flight}")
print(f"Hotel cost for {num_nights} nights: £{hotel}")
print(f"Flight cost to {city_flight}: £{flight}")
print(f"Car rental for {rental_days} days: £{car}")
print(f"Total holiday cost: £{total_holiday_cost}")
