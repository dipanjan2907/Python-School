import numpy as np


def trapezoidal_rule(func_str, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)

    try:
        y = np.array([eval(func_str, {"x": val, "np": np}) for val in x])
    except Exception as e:
        print(f"Error evaluating the function: {e}")
        return None

    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral


func_str_input = input("Enter the function to integrate (e.g., 'x**2 + 1'): ")

try:
    lower_limit = float(input("Enter the lower limit of integration (e.g., 0): "))
    upper_limit = float(input("Enter the upper limit of integration (e.g., 2): "))
    num_subintervals = int(input("Enter the number of subintervals (n, e.g., 10): "))
except ValueError:
    print(
        "Invalid input for limits or number of subintervals. Please enter numerical values."
    )
    exit()

if num_subintervals <= 0:
    print("Number of subintervals must be a positive integer.")
    exit()

approximated_integral = trapezoidal_rule(
    func_str_input, lower_limit, upper_limit, num_subintervals
)

if approximated_integral is not None:
    print(f"\nFunction: f(x) = {func_str_input}")
    print(f"Integration limits: [{lower_limit}, {upper_limit}]")
    print(f"Number of subintervals (n): {num_subintervals}")
    print(f"Approximation using Trapezoidal Rule: {approximated_integral:.6f}")
