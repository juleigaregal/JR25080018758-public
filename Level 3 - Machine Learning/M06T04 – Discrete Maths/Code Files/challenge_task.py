import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from -100 to 100 in intervals of 0.5
start_val = -100
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

params = [1.2, 0.5, 2, -5]

"""
-----------------
Optional Task
------------------

Plot f(x) = P.X, where p is your params
"""
y = params[0] * X**3 + params[1] * X**2 + params[2] * X + (params[3])

plt.plot(X, y, color="blue")
plt.title(f"f(x) = {params[0]}x³ + {params[1]}x² + {params[2]}x - {abs(params[3])}")
plt.ylabel("y")
plt.xlabel("X")
plt.grid(True)
plt.show()