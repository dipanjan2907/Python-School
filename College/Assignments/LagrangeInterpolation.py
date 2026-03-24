import numpy as np
from scipy.interpolate import lagrange

# Get points from user input
x_input_str = input("Enter x-coordinates (comma-separated, e.g., 0,1,2): ")
y_input_str = input("Enter y-coordinates (comma-separated, e.g., 1,3,2): ")

try:
    x_points = np.array([float(x.strip()) for x in x_input_str.split(",")])
    y_points = np.array([float(y.strip()) for y in y_input_str.split(",")])
except ValueError:
    print("Invalid input. Please enter numerical values separated by commas.")
    exit()

if len(x_points) != len(y_points):
    print("Number of x-coordinates must match the number of y-coordinates.")
    exit()

# a) Construct the Lagrange polynomial
poly = lagrange(x_points, y_points)

print(f"Lagrange Polynomial coefficients (from highest to lowest power): {poly.coeffs}")

# Optionally, to display the polynomial in a more readable form:
# For a polynomial p(x) = a_n*x^n + ... + a_1*x + a_0
# poly.coeffs gives [a_n, ..., a_1, a_0]

polynomial_str = "Polynomial P(x) = "

for i, coeff in enumerate(poly.coeffs[::-1]):  # Iterate from a_0 to a_n
    if i == 0:
        polynomial_str += f"{coeff:.4f}"
    else:
        if coeff >= 0:
            polynomial_str += f" + {coeff:.4f}*x^{i}"
        else:
            polynomial_str += f" - {-coeff:.4f}*x^{i}"

print(polynomial_str)

# b) Estimate value at x=1.5
x_estimate_str = input("Enter the x-value to estimate (e.g., 1.5): ")

try:
    x_estimate = float(x_estimate_str.strip())
except ValueError:
    print("Invalid input for x-value. Please enter a numerical value.")
    exit()

y_estimate = poly(x_estimate)

print(f"Estimated value at x={x_estimate}: {y_estimate:.4f}")
