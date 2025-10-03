# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 15:36:16 2025

@author: juleigar
"""
import matplotlib.pyplot as plt


# NumPy is our numerical computational framework
import numpy as np

X = np.array([1, 2.5, 3, 3.25, 6, 8, 9.4])
y = np.array([0, 5, 7, 6.5, 9.5, 23.5, 18.7])

def model(x, m):
    """
    Our model f(x) = mx
    Receives: a data point x and the line gradient m
    Returns: a prediction for y
    """
      
    return m * x
    

def error_function(m):
    """
    Our error function J(m)
    This is done using the Mean Square Error (MSE) between our model and the data
    Receives: m, the gradient of the line
    Returns: J(m), the Mean Squared Error between the model and the data
    Hint: you can use the data itself (X and y) from this function
    
    """
    predictions = model(X, m)
    errors = y - predictions
    return np.mean(errors ** 2)

    

def derivative(m):
    """
    The derivation of the error_function J(m)
    Receives: m, the gradient of the line
    Returns: dJ/dm, the derivative of the error function with respect to m
    """
    predictions = model(X, m)
    errors = y - predictions
    return (-2 / len(X)) * np.sum(X * errors)
    

def update_step(m, learning_rate=0.01):
    """
    Update the gradient m using the derivative of J(m)
    Receives: m, the gradient of the line
    Returns: a new and updated m
    """
    gradient_descent = m - learning_rate * derivative(m)
    return gradient_descent
    pass # Remove when function is written

m = -6
n_epochs = 5 # This is just the number of update steps you take

# Iterate for n epochs
for epoch in range(n_epochs):
    # Update and print m
    m = update_step(m)
    print(f'Epoch {epoch + 1}: m = {round(m,2)} and loss = {round(error_function(m), 2)}')

# Print Final Results
print("-----------------")
print("FINAL RESULTS")
print("-----------------")

print(f'm = {round(m,2)} and loss = {round(error_function(m), 2)}')


print("-----------------")

#plotting fitted line with final slope

# Final slope from gradient descent
m_final = 2.14

# Line using the final slope
y_pred = m_final * X

# Plotting
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Data Points')       # Original data
plt.plot(X, y_pred, color='red', label=f'Fitted Line: y={m_final:.2f}x') # Fitted line
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Fit using Gradient Descent')
plt.legend()
plt.grid(True)
plt.show()

