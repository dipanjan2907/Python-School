import numpy as np


def newton_forward_interpolation(x_data, y_data, x_estimate):
    n = len(x_data)

    # Create a forward difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_data

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]

    # Calculate the interpolated value
    # The formula is P(x) = y0 + (s C 1) * Delta y0 + (s C 2) * Delta^2 y0 + ...
    # where s = (x - x0) / h

    # Check for equally spaced intervals for h, or use a general formula for s
    if len(x_data) > 1 and np.allclose(np.diff(x_data), x_data[1] - x_data[0]):
        h = x_data[1] - x_data[0]
    else:
        print(
            "Warning: x-values are not equally spaced. Newton's Forward Interpolation might not be suitable."
        )
        # For non-equally spaced points, Newton's Divided Difference is generally used.
        # For forward interpolation, we usually assume equally spaced. Let's proceed with first interval h.
        h = x_data[1] - x_data[0] if len(x_data) > 1 else 1  # Fallback h

    s = (x_estimate - x_data[0]) / h

    # Calculate binomial coefficients (s C k)
    def nCr_s(s_val, k):
        res = 1
        for i in range(k):
            res = res * (s_val - i) / (i + 1)
        return res

    interpolated_value = diff_table[0, 0]  # y0

    for k in range(1, n):
        interpolated_value += nCr_s(s, k) * diff_table[0, k]

    return interpolated_value


# Get data from user input
x_input_str = input("Enter x-coordinates (comma-separated, e.g., 0,1,2,3): ")
y_input_str = input("Enter y-coordinates (comma-separated, e.g., 1,2,4,8): ")

try:
    x_data = np.array([float(x.strip()) for x in x_input_str.split(",")])
    y_data = np.array(
        [float(val.strip()) for val in y_input_str.split(",")]
    )  # Fixed: changed 'x' to 'val'
except ValueError:
    print(
        "Invalid input for data points. Please enter numerical values separated by commas."
    )
    exit()

if len(x_data) < 2 or len(x_data) != len(y_data):
    print(
        "Number of x-coordinates must match the number of y-coordinates and be at least 2."
    )
    exit()

x_estimate_str = input("Enter the x-value to estimate (e.g., 2.5): ")

try:
    x_estimate = float(x_estimate_str.strip())
except ValueError:
    print("Invalid input for x-value to estimate. Please enter a numerical value.")
    exit()

# Check for equally spaced intervals and warn if not.
# This check is also inside the function, but a clear warning upfront is good.
if not np.allclose(np.diff(x_data), x_data[1] - x_data[0]):
    print(
        "\nWarning: Newton's Forward Interpolation works best with equally spaced x-values."
    )
    print(
        "The calculation will proceed using the first interval's spacing, but results might be less accurate."
    )

estimated_y = newton_forward_interpolation(x_data, y_data, x_estimate)

print(f"\nData points: x = {x_data}, y = {y_data}")
print(f"Estimating y({x_estimate})")
print(f"Estimated value y({x_estimate}) = {estimated_y:.4f}")
