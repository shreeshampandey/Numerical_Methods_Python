import math
import matplotlib.pyplot as plt
import numpy as np

def find_root(k, iterations):
    x = k * math.pi
    for _ in range(iterations):
        x = math.atan(x) + k * math.pi
    return x

def solve_equation(start_k, end_k, iterations):
    roots = []
    k_values = np.arange(start_k, end_k + 1)
    for k in k_values:
        root = find_root(k, iterations)
        roots.append(root)
        print(f"Root for k={k}: {root}")
    
    # Plot the function x - tan(x)
    x_values = np.linspace(start_k * math.pi, end_k * math.pi, 1000)
    y_values = x_values - np.tan(x_values)
    plt.plot(x_values, y_values, label='x - tan(x)')
    
    # Plot the calculated roots
    plt.plot(roots, [0] * len(roots), 'ro', label='Roots')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of x - tan(x) with Calculated Roots')
    plt.legend()
    plt.grid(True)
    plt.show()

start_k = int(input("Enter the starting value of k: "))
end_k = int(input("Enter the ending value of k: "))
iterations = int(input("Enter the number of iterations: "))

solve_equation(start_k, end_k, iterations)
