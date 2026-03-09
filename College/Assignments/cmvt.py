# CAUCHY'S MEAN VALUE THEOREM
from sympy import Eq, N, diff, lambdify, solve, symbols, sympify
import numpy as np
import matplotlib.pyplot as plt


# 1. Symbols
x = symbols('x')
c = symbols('c')

# 2. Input points
a = int(input("Enter the first point: "))
b = int(input("Enter the second point: "))

if a == b:
	raise ValueError("The two points must be different.")

# 3. Input expressions
f_x = input("Enter the first expression in terms of x: ")
expression1 = sympify(f_x)
g_x = input("Enter the second expression in terms of x: ")
expression2 = sympify(g_x)

# 4. Derivatives
f_prime = diff(expression1, x)
f_prime_c = f_prime.subs(x, c)
g_prime = diff(expression2, x)
g_prime_c = g_prime.subs(x, c)

# 5. CMVT right-hand side
denominator = expression2.subs(x, b) - expression2.subs(x, a)
if denominator == 0:
	raise ValueError("g(b) - g(a) is zero; CMVT ratio is undefined.")

rhs = (expression1.subs(x, b) - expression1.subs(x, a)) / denominator

print("----------------- The Equation is -----------------")
print("Equation: f'(c)/g'(c) =", f_prime_c, "/", g_prime_c, "=", rhs)

# CMVT equation and c in (a, b)
equation = Eq(f_prime_c / g_prime_c, rhs)
solutions = solve(equation, c)
solutions = [sol for sol in solutions if sol.is_real and a < N(sol) < b]

if not solutions:
	raise ValueError("No real c in (a, b) satisfies the CMVT equation.")

c_value = float(N(solutions[0]))
print("c =", solutions, "-> using", c_value)

# -------------------------------------------------
# Plotting
# -------------------------------------------------
print("--------------- The Plot is --------------------")

f_func = lambdify(x, expression1, "numpy")
g_func = lambdify(x, expression2, "numpy")

x_vals = np.linspace(a, b, 400)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_func(x_vals), label='f(x)', color='blue')
plt.plot(x_vals, g_func(x_vals), label='g(x)', color='green')

points_x = [a, b, c_value]
points_y = [
	float(expression1.subs(x, a)),
	float(expression1.subs(x, b)),
	float(expression1.subs(x, c_value)),
]
plt.scatter(points_x, points_y, color='red', zorder=5)
plt.text(c_value, float(expression1.subs(x, c_value)), ' c', fontsize=12)

plt.title("Cauchy Mean Value Theorem Visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()