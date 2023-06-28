import numpy as np
import matplotlib.pyplot as plt

def bisection(f, a, b, tolerance):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at the interval endpoints.")
    
    iterations = 0
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        root = c
        
        iterations += 1
        
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
        print(f"Iteration {iterations}: root = {root}")
    
    return root, iterations

def newton_raphson(f, f_prime, x0, tolerance):
    x = x0
    iterations = 0
    
    while abs(f(x)) > tolerance:
        x = x - f(x) / f_prime(x)
        root = x
        
        iterations += 1
        
        print(f"Iteration {iterations}: root = {root}")
    
    return root, iterations

def secant(f, x0, x1, tolerance):
    x_prev = x0
    x = x1
    iterations = 0
    
    while abs(f(x)) > tolerance:
        x_next = x - f(x) * (x - x_prev) / (f(x) - f(x_prev))
        root = x_next
        
        iterations += 1
        
        x_prev = x
        x = x_next
        
        print(f"Iteration {iterations}: root = {root}")
    
    return root, iterations

def plot_function_and_convergence(f, root, convergence, a, b):
    x = np.linspace(a, b, 1000)
    y = f(x)
    iterations = list(range(1, len(convergence) + 1))
    
    plt.figure(figsize=(10, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(x, y, label="Function")
    plt.plot(root, f(root), marker="o", color="red", label="Root")
    plt.axhline(y=0, color="black", linestyle="--", linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graph of the Function")
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(iterations, convergence, marker="o", alpha=0.5)
    plt.xlabel("Iterations")
    plt.ylabel("Root")
    plt.title("Convergence of Roots")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def f(x):
    return x**3 - x - 1

def f_prime(x):
    return 3 * x**2 - 1

method = input("Enter the method to use (bisection, newton, secant): ")
a = float(input("Enter the lower bound of the range: "))
b = float(input("Enter the upper bound of the range: "))
tolerance = float(input("Enter the tolerance: "))

if method == "bisection":
    root, iterations = bisection(f, a, b, tolerance)
elif method == "newton":
    x0 = float(input("Enter the initial guess: "))
    root, iterations = newton_raphson(f, f_prime, x0, tolerance)
elif method == "secant":
    x0 = float(input("Enter the first initial guess: "))
    x1 = float(input("Enter the second initial guess: "))
    root, iterations = secant(f, x0, x1, tolerance)
else:
    print("Invalid method selected.")
    exit()

print(f"\nRoot: {root}")
print(f"Iterations: {iterations}")

convergence = [root] * iterations

plot_function_and_convergence(f, root, convergence, a, b)
