import matplotlib.pyplot as plt

def nth_root(number, n, precision):
    """
    Approximates the nth root of a number up to a given number of significant digits.
    Returns the approximate root and a list of intermediate approximations.
    """
    guess = number / n  # Initial guess
    approximations = [guess]  # List to store intermediate approximations

    while True:
        next_guess = ((n - 1) * guess + number / (guess ** (n - 1))) / n  # Newton's method
        approximations.append(next_guess)
        if round(next_guess, precision) == round(guess, precision):
            return round(next_guess, precision), approximations
        guess = next_guess


# Take user input
number = float(input("Enter a number: "))
n = int(input("Enter the order of the root: "))
precision = int(input("Enter the number of significant digits: "))

# Calculate the approximate nth root and get intermediate approximations
result, approximations = nth_root(number, n, precision)

# Print the result
print(f"The approximate {n}th root of {number} is: {result}")

# Plot the convergence
iterations = range(len(approximations))
plt.plot(iterations, approximations, 'b.-')
plt.xlabel('Iteration')
plt.ylabel('Approximation')
plt.title('Convergence of Newton-Raphson')
plt.grid(True)
plt.show()
