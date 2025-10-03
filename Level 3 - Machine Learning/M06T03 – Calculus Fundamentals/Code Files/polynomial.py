# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:48:27 2025

@author: juleigar
"""
try:
    coefficient = int(input("Enter coefficient: "))
    power_n = int(input("Enter the power to raise: "))
    x = int(input("Enter the x-coordinate of the point where you would like to calculate the gradient: "))

    # derivative calculation
    derivative_coeff = coefficient * power_n
    derivative_power = power_n - 1
    gradient = derivative_coeff * (x ** derivative_power)

    # format derivative nicely (e.g. 6x^2)
    if derivative_power == 0:
        derivative_str = f"{derivative_coeff}"
    elif derivative_power == 1:
        derivative_str = f"{derivative_coeff}x"
    else:
        derivative_str = f"{derivative_coeff}x^{derivative_power}"

    # polynomial string
    if power_n == 0:
        poly_str = f"{coefficient}"
    elif power_n == 1:
        poly_str = f"{coefficient}x"
    else:
        poly_str = f"{coefficient}x^{power_n}"

    print(
        f"The derivative of the polynomial {poly_str} is {derivative_str}. "
        f"The gradient at the point x = {x} is {gradient}."
    )

except ValueError:
    print("Invalid input! Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero occurred (check negative powers at x=0).")
except Exception as e:
    print("An unexpected error occurred:", e)
