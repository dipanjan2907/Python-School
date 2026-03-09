from sympy import integrate, oo, Symbol
from scipy.integrate import quad

x = Symbol("x")
f_x = 1 / x**2
# a) Test convergence
# For p-series integrals of the form integral(1 to infinity) 1/x^p dx,
# the integral converges if p > 1 and diverges if p <= 1.
# In this case, p = 2, which is greater than 1, so the integral converges.
print(f"a) Testing convergence for integral of {f_x} from 1 to infinity:")
print(
    f"The integral is a p-series integral with p = 2. Since p > 1, the integral converges.\n"
)
# b) Compute symbolically
# The integral is calculated as the limit of the definite integral as the upper limit approaches
# infinity.
# integral(1 to b) 1/x^2 dx = [-1/x] (from 1 to b) = -1/b - (-1/1) = 1 - 1/b
# As b -> oo, 1/b -> 0. So, the integral converges to 1.
symbolic_result = integrate(f_x, (x, 1, oo))
print(f"b) Symbolic computation:")
print(f"The symbolic result of the integral is: {symbolic_result}\n")


# b) Compute numerically
# For numerical integration, the upper limit of infinity needs to be handled.
# The `quad` function from SciPy can handle infinite limits.
def integrand(x):
    return 1 / x**2


numerical_result, error = quad(integrand, 1, oo)
print(f"Numerical computation:")
print(f"The numerical result of the integral is: {numerical_result:.6f}")
print(f"Estimated absolute error: {error:.6f}")
