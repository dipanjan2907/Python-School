import numpy as np
import matplotlib.pyplot as plt


def gauss_seidel_method(A, b, x0, num_iterations):
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
            "Warning: The matrix is not diagonally dominant. Gauss-Seidel method may not converge or may converge slowly."
        )
    for k in range(num_iterations):
        x_new = x.copy()

        for i in range(n):
            s1 = sum(
                A[i][j] * x_new[j] for j in range(i)
            )  # Use new values for x[0] to x[i-1]
            s2 = sum(
                A[i][j] * x[j] for j in range(i + 1, n)
            )  # Use old values for x[i+1] to x[n-1]
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        error = np.linalg.norm(x_new - x, ord=2)  # L2 norm as error
        errors.append(error)

        x = x_new.copy()
        x_history.append(x.copy())

    return x, np.array(x_history), np.array(errors)


jacobi_errors = [2.078461e00, 4.156922e-01, 8.313844e-02, 1.662769e-02, 3.325538e-03]
# Define the system of equations Ax = b
A = np.array([[10.0, 1.0, 1.0], [1.0, 10.0, 1.0], [1.0, 1.0, 10.0]])
b = np.array([12.0, 12.0, 12.0])
# Initial guess for x, y, z
x0 = np.array([0.0, 0.0, 0.0])
# Number of iterations
num_iterations = 5
# Perform Gauss-Seidel iterations
final_solution_gs, history_gs, gs_errors = gauss_seidel_method(A, b, x0, num_iterations)
print("\n--- Gauss-Seidel Method ---")
print("Iteration History (Gauss-Seidel):")
for i, sol in enumerate(history_gs):
    print(f"Iteration {i}: x = {sol[0]:.6f}, y = {sol[1]:.6f}, z = {sol[2]:.6f}")
print(
    f"\nFinal solution after {num_iterations} iterations (Gauss-Seidel): x = {final_solution_gs[0]:.6f}, y = {final_solution_gs[1]:.6f}, z = {final_solution_gs[2]:.6f}"
)
print("\nConvergence Data (Error at each iteration - Gauss-Seidel):")
for i, error in enumerate(gs_errors):
    print(f"Iteration {i+1}: Error = {error:.6e}")

# Retrieve Jacobi errors from kernel state for comparison
# Assuming jacobi_errors is available from the previous run

print("\n--- Comparison of Convergence ---")
plt.figure(figsize=(10, 6))
plt.semilogy(
    range(1, num_iterations + 1),
    jacobi_errors,
    marker="o",
    linestyle="-",
    color="blue",
    label="Jacobi Method",
)
plt.semilogy(
    range(1, num_iterations + 1),
    gs_errors,
    marker="x",
    linestyle="--",
    color="red",
    label="Gauss-Seidel Method",
)
plt.title("Convergence Comparison (Jacobi vs. Gauss-Seidel)")
plt.xlabel("Iteration")
plt.ylabel("Error (L2 Norm)")
plt.legend()
plt.grid(True)
plt.show()
