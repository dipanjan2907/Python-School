import numpy as np
import matplotlib.pyplot as plt


def jacobi_method(A, b, x0, num_iterations):
    n = len(A)
    x = x0.copy()
    x_history = [x0.copy()]
    errors = []

    # Check for diagonal dominance (a condition for convergence)
    is_diagonally_dominant = True
    for i in range(n):
        diag_val = abs(A[i][i])
        sum_off_diag = sum(abs(A[i][j]) for j in range(n) if i != j)
        if diag_val <= sum_off_diag:
            is_diagonally_dominant = False
            break

    if not is_diagonally_dominant:
        print(
            "Warning: The matrix is not diagonally dominant. Jacobi's method may not converge or may converge slowly."
        )

    for k in range(num_iterations):
        x_new = np.zeros(n)

        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s1) / A[i][i]

        error = np.linalg.norm(x_new - x, ord=2)  # L2 norm as error
        errors.append(error)

        x = x_new.copy()
        x_history.append(x.copy())

    return x, np.array(x_history), np.array(errors)


# Define the system of equations Ax = b
A = np.array([[10.0, 1.0, 1.0], [1.0, 10.0, 1.0], [1.0, 1.0, 10.0]])

b = np.array([12.0, 12.0, 12.0])

# Initial guess for x, y, z
x0 = np.array([0.0, 0.0, 0.0])

# Number of iterations
num_iterations = 5

# Perform Jacobi iterations
final_solution, history, jacobi_errors = jacobi_method(A, b, x0, num_iterations)

print("System of equations:")
print("10x + y + z = 12")
print("x + 10y + z = 12")
print("x + y + 10z = 12\n")

print(f"Initial guess: {x0}")
print(f"Number of iterations: {num_iterations}\n")

print("Iteration History:")
for i, sol in enumerate(history):
    print(f"Iteration {i}: x = {sol[0]:.6f}, y = {sol[1]:.6f}, z = {sol[2]:.6f}")

print(
    f"\nFinal solution after {num_iterations} iterations: x = {final_solution[0]:.6f}, y = {final_solution[1]:.6f}, z = {final_solution[2]:.6f}"
)

# Plotting convergence
plt.figure(figsize=(8, 6))
plt.semilogy(range(1, num_iterations + 1), jacobi_errors, marker="o", linestyle="-")
plt.title("Convergence of Jacobi Method")
plt.xlabel("Iteration")
plt.ylabel("Error (L2 Norm)")
plt.grid(True)
plt.show()

print("\nConvergence Data (Error at each iteration):")
for i, error in enumerate(jacobi_errors):
    print(f"Iteration {i+1}: Error = {error:.6e}")
