import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - np.tan(x)

def bisection_method(a, b, max_iterations):
    c = (a + b) / 2
    iterations = 0
    while iterations < max_iterations:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        iterations += 1
        print("Iteration:", iterations)
        print("Root:", c)
        print("Value:", f(c))
        print()
    return c, iterations

# Define the interval [a, b]
a = float(input("Enter the lower bound of the range: "))
b = float(input("Enter the upper bound of the range: "))

# Set the maximum number of iterations
max_iterations = int(input("Enter the maximum number of iterations: "))

# Apply the bisection method
root_bisection, iterations_bisection = bisection_method(a, b, max_iterations)

# Print the final result
print("Bisection Method:")
print("Root:", root_bisection)
print("Iterations:", iterations_bisection)

# Plot the function
x = np.linspace(a, b, 100)
plt.plot(x, f(x))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(root_bisection, color='red', linestyle='--', label='Root (Bisection)')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x - tan(x)')
plt.grid(True)
plt.show()
