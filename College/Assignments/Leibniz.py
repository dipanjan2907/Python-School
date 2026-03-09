from sympy import integrate, diff, exp, Symbol

# Define symbolic variables
x, a = Symbol("x"), Symbol("a")
# Define the integrand f(x, a)
f_xa = exp(-a * x)
# a) Differentiate under the integral sign (Leibniz Rule)
# The Leibniz rule for d/da [integral(from c to d) f(x, a) dx] is integral(from c to d) [df/da(x, a)] dx
# Step 1: Differentiate f(x, a) with respect to 'a'
df_da = diff(f_xa, a)
print(
    f"a) Differentiating under the integral sign for I(a) = integral(0 to 1) e^(-ax) dx"
)
print(f" 1. Partial derivative of f(x,a) = e^(-ax) with respect to a: {df_da}")
# Step 2: Integrate df_da with respect to 'x' from 0 to 1
dI_da_leibniz = integrate(df_da, (x, 0, 1))
print(f"2. Integrating the result from 0 to 1: {dI_da_leibniz}")
# b) Verify by integrating first, then differentiating
# Step 1: Integrate I(a) with respect to 'x' from 0 to 1
I_a_integrated = integrate(f_xa, (x, 0, 1))
print(f"b) Verifying by integrating first, then differentiating:")
print(f" 1. Integrating e^(-ax) with respect to x from 0 to 1: {I_a_integrated}")
# Step 2: Differentiate the result with respect to 'a'
dI_da_verify = diff(I_a_integrated, a)
print(f"2. Differentiating the result with respect to a: {dI_da_verify}")
# Compare the two results
print(f"Comparison of results:")
print(f"From Leibniz rule: {dI_da_leibniz}")
print(f"From integrating first, then differentiating: {dI_da_verify}")
print(f"Are the results equal? {dI_da_leibniz == dI_da_verify}")
