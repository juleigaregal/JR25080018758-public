# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 13:48:27 2025

@author: juleigar
"""

def main():
    try:
        # Get user input
        coefficient = int(input("Enter coefficient of x: "))
        power_n = int(input("Enter the power to raise x: "))
        x = int(input("Enter the x-coordinate of the point where you would like to calculate the gradient: "))

        # Apply power rule: derivative = (coefficient * power) * x^(power-1)
        derivative_coeff = coefficient * power_n
        derivative_power = power_n - 1

        # Gradient at the given x
        gradient = derivative_coeff * (x ** derivative_power)

        # Output
        print(f"The derivative of the polynomial {coefficient}x^{power_n} is {derivative_coeff}x^{derivative_power}.")
        print(f"The gradient at the point x = {x} is {gradient}.")

    except ValueError:
        print("Error: Please enter valid integers for coefficient, power, and x.")

if __name__ == "__main__":
    main()
