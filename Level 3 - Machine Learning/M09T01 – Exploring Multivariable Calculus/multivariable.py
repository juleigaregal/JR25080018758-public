# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 05:35:48 2025

@author: juleigar

This program calculates the gradient vector (∇f) of a
two-variable function using partial derivatives.

"""



# Import the sympy library for symbolic mathematics
import sympy as sp


def main():
    """
    Main function to calculate the gradient of a user-defined
    two-variable function.
    """
    # Define the variables used in the function
    x, y = sp.symbols('x y')

    # Request user input for the function
    user_input = input("Enter a multivariable function in terms of x and y e.g(x**2+y**3): ")

    # Convert the user input string into a sympy expression
    f = sp.sympify(user_input)

    # Calculate the partial derivative of f with respect to x
    df_dx = sp.diff(f, x)

    # Calculate the partial derivative of f with respect to y
    df_dy = sp.diff(f, y)

    # Create the gradient vector from the partial derivatives
    gradient = (df_dx, df_dy)

    # Display the result using the nabla (∇) symbol
    print(f"The gradient vector of the function f = {f} is \u2207f = {gradient}.")


# Run the program only if it is executed directly
if __name__ == "__main__":
    main()
