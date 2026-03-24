import numpy as np
import matplotlib.pyplot as plt


def bisection_method(func_str, a, b, tol=1e-6, max_iter=100):
    f = lambda x: eval(func_str)
    if f(a) * f(b) >= 0:
        print("Bisection method may not work. f(a) and f(b) must have opposite signs.")
        return None, None, None

    iterations = []
    errors = []

    for i in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        error = abs(b - a) / 2
        errors.append(error)

        if abs(f(c)) < tol or error < tol:
            return c, iterations, errors

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    print("Maximum iterations reached.")
    return (a + b) / 2, iterations, errors


user_func_str = "x**3 - x - 2"
# User input function string (already defined in kernel state)
# user_func_str = 'x**3 - x - 2'

# Define initial interval for bisection method
a = 1
b = 2

# Calculate the root using bisection method
root, iter_bisection, errors_bisection = bisection_method(user_func_str, a, b)

if root is not None:
    print(f"The approximate root is: {root}")
    print(f"Number of iterations: {len(iter_bisection)}")

# Plotting the function
x_vals = np.linspace(a, b, 100)
y_vals = [eval(user_func_str) for x in x_vals]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, label=user_func_str)
plt.axhline(0, color="red", linestyle="--", label="y=0")
plt.scatter(
    [root],
    [eval(user_func_str.replace("x", str(root)))],
    color="green",
    marker="o",
    s=50,
    label="Root",
)
plt.title("Function Plot")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

# Plotting convergence
plt.subplot(1, 2, 2)
plt.semilogy(
    range(len(errors_bisection)),
    errors_bisection,
    marker="o",
    linestyle="-",
    color="blue",
)
plt.title("Convergence of Bisection Method (Error vs. Iteration)")
plt.xlabel("Iteration")
plt.ylabel("Absolute Error")
plt.grid(True)

plt.tight_layout()
plt.show()

# Display convergence information
print("\nConvergence Information:")
print("Iteration | Approximation | Error")
print("---------------------------------")

for i in range(len(iter_bisection)):
    print(f"{i+1:<9} | {iter_bisection[i]:<13.8f} | {errors_bisection[i]:<.8e}")
