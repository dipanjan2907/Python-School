import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(func_str, func_prime_str, x0, tol=1e-6, max_iter=100):
    f = lambda x: eval(func_str)
    f_prime = lambda x: eval(func_prime_str)

    if f_prime(x0) == 0:
        print("Derivative is zero at initial guess.")
        return None, None, None

    iterations = [x0]
    errors = []
    x_old = x0

    for i in range(max_iter):

        if f_prime(x_old) == 0:
            print(f"Derivative is zero at x = {x_old}. Cannot continue Newton-Raphson.")
            return x_old, iterations, errors

        x_new = x_old - f(x_old) / f_prime(x_old)
        iterations.append(x_new)

        error = abs(x_new - x_old)
        errors.append(error)

        if error < tol:
            return x_new, iterations, errors

        x_old = x_new

    print("Maximum iterations reached.")
    return x_old, iterations, errors


# User defined function string (from previous context)
user_func_str = "x**3 - x - 2"
user_func_prime_str = "3*x**2 - 1"

# Define initial guess for Newton-Raphson
x0 = 1.5  # A reasonable guess based on the bisection interval [1, 2]

# Calculate the root using Newton-Raphson method
root_newton, iter_newton, errors_newton = newton_raphson(
    user_func_str, user_func_prime_str, x0
)

if root_newton is not None:
    print(f"\nNewton-Raphson Method:")
    print(f"The approximate root is: {root_newton}")
    print(f"Number of iterations: {len(iter_newton) - 1}")

# Plotting for Newton-Raphson
x_vals_newton = np.linspace(min(iter_newton) - 1, max(iter_newton) + 1, 100)

y_vals_newton = [eval(user_func_str) for x in x_vals_newton]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_vals_newton, y_vals_newton, label=user_func_str)
plt.axhline(0, color="red", linestyle="--", label="y=0")
plt.scatter(
    [root_newton],
    [eval(user_func_str.replace("x", str(root_newton)))],
    color="purple",
    marker="o",
    s=50,
    label="Root (Newton-Raphson)",
)
plt.title("Function Plot (Newton-Raphson)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.semilogy(
    range(len(errors_newton)),
    errors_newton,
    marker="o",
    linestyle="-",
    color="purple",
    label="Newton-Raphson",
)


plt.title("Convergence Comparison (Error vs. Iteration)")
plt.xlabel("Iteration")
plt.ylabel("Absolute Error")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Display convergence information for Newton-Raphson
print("\nConvergence Information (Newton-Raphson):")
print("Iteration | Approximation | Error")
print("---------------------------------")

for i in range(len(errors_newton)):
    print(f"{i+1:<9} | {iter_newton[i+1]:<13.8f} | {errors_newton[i]:<.8e}")
