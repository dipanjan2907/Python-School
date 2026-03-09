# LAGRANGE'S MEAN VALUE THEOREM
from sympy import Eq, N, diff, solve, symbols, sympify
import numpy as np
import matplotlib.pyplot as plt


# 1. Symbols
x = symbols("x")
c = symbols("c")

# 2. Input points
a = int(input("Enter the first point: "))
b = int(input("Enter the second point: "))

if a == b:
    raise ValueError("The two points must be different.")

# 3. Input expression
user_expr = input("Enter the expression in terms of x: ")
expression = sympify(user_expr)

# 4. Derivative
derivative = diff(expression, x)
derivative_with_c = derivative.subs(x, c)


# 5. Secant slope
def expr(value):
    return expression.subs(x, value)


secant_slope = (expr(b) - expr(a)) / (b - a)
print(f"Derivative in terms of c: {derivative_with_c} = {secant_slope}")

# 6. Solve for c (Mean Value Theorem)
equation = Eq(derivative_with_c, secant_slope)
solutions = solve(equation, c)
solutions = [sol for sol in solutions if sol.is_real and a < N(sol) < b]

if not solutions:
    raise ValueError(
        "No real c in (a, b) satisfies Lagrange's Mean Value Theorem equation."
    )

c_value = float(solutions[0])
print("Value of c:", c_value)

# 7. Prepare plotting
x_vals = np.linspace(a, b, 200)
f_vals = [float(expression.subs(x, val)) for val in x_vals]

# Secant line
secant_vals = float(expr(a)) + float(secant_slope) * (x_vals - a)

# Tangent line at c
tangent_slope = float(derivative.subs(x, c_value))
tangent_vals = float(expression.subs(x, c_value)) + tangent_slope * (x_vals - c_value)

# 8. Plot
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_vals, label="Function f(x)", color="blue")
plt.plot(x_vals, secant_vals, label="Secant line", color="green", linestyle="--")
plt.plot(x_vals, tangent_vals, label="Tangent at c", color="black", linestyle="-.")

# Points
points_x = [a, b, c_value]
points_y = [float(expr(a)), float(expr(b)), float(expression.subs(x, c_value))]
plt.scatter(points_x, points_y, color="black", zorder=5)

# Label the points with literal expressions
labels = ["[a,f(a)]", "[b,f(b)]", "[c,f(c)]"]
for px, py, label in zip(points_x, points_y, labels):
    plt.text(
        px,
        py,
        label,
        fontsize=10,
        fontweight="bold",
        color="purple",
        verticalalignment="bottom",
        horizontalalignment="right",
    )

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function, Secant, and Tangent with Point Labels [a,f(a)] etc.")
plt.legend()
plt.grid(True)
plt.show()
