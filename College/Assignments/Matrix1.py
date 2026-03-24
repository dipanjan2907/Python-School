import numpy as np
import matplotlib.pyplot as plt

# Get user input for the 2x2 matrix A
print("Enter the elements of the 2x2 matrix A:")

while True:
    try:
        a11 = float(input("Enter element A[0,0]: "))
        a12 = float(input("Enter element A[0,1]: "))
        a21 = float(input("Enter element A[1,0]: "))
        a22 = float(input("Enter element A[1,1]: "))
        A = np.array([[a11, a12], [a21, a22]])
        break
    except ValueError:
        print("Invalid input. Please enter numerical values for the matrix elements.")

print("Matrix A:")
print(A)
print("\n")

# a) Compute eigenvalues and eigenvectors using NumPy
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
print("\n")

print("Eigenvectors (columns correspond to eigenvalues):")
print(eigenvectors)
print("\n")

# b) Plot eigenvectors
plt.figure(figsize=(6, 6))
plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.grid(True, linestyle="--", alpha=0.6)

# Plot each eigenvector
for i in range(eigenvectors.shape[1]):
    vector = eigenvectors[:, i]
    plt.quiver(
        0,
        0,
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=f"C{i}",
        label=f"Eigenvector {i+1} (λ={eigenvalues[i]:.2f})",
    )

    plt.text(
        vector[0] * 1.1,
        vector[1] * 1.1,
        f"({vector[0]:.2f}, {vector[1]:.2f})",
        color=f"C{i}",
        fontsize=9,
    )

plt.xlim(
    [-max(abs(eigenvectors.flatten())) * 1.5, max(abs(eigenvectors.flatten())) * 1.5]
)

plt.ylim(
    [-max(abs(eigenvectors.flatten())) * 1.5, max(abs(eigenvectors.flatten())) * 1.5]
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Eigenvectors of Matrix A")
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")
plt.show()
