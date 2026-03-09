import math
from scipy.special import beta

# a) Evaluate Gamma(5)
# For positive integer n, Gamma(n) = (n-1)!
gamma_5 = math.gamma(5)
print(f"a) Gamma(5) = {gamma_5}")
print(f" (which is 4! = {math.factorial(4)})\n")
# b) Verify B(p,q) = Gamma(p)Gamma(q)/Gamma(p+q) for p=2, q=3
p = 2
q = 3
# Calculate Gamma values
gamma_p = math.gamma(p)
gamma_q = math.gamma(q)
gamma_p_plus_q = math.gamma(p + q)
# Calculate B(p,q) directly
beta_pq_direct = beta(p, q)
# Calculate B(p,q) using the Gamma function relationship
beta_pq_relationship = (gamma_p * gamma_q) / gamma_p_plus_q
print(f"b) Verifying B(p,q) = Gamma(p)Gamma(q)/Gamma(p+q) for p={p}, q={q}:")
print(f" Gamma({p}) = {gamma_p}")
print(f" Gamma({q}) = {gamma_q}")
print(f" Gamma({p+q}) = {gamma_p_plus_q}")
print(f"\n B({p},{q}) (direct calculation) = {beta_pq_direct}")
print(f" (Gamma({p}) * Gamma({q})) / Gamma({p+q}) = {beta_pq_relationship}")
# Check if the values are approximately equal due to potential floating-point precision
# differences
is_equal = math.isclose(beta_pq_direct, beta_pq_relationship)
print(f"\n The relationship holds true: {is_equal}")
