# dli_dirichlet_log_integral
- **status:** CONDITIONAL
## Statement
DLI_j(eps_j): for every central profile M and every nonzero frequency lambda,
-sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2 >= 2(L_j - eps_j) log q - O(1)
— i.e. low-degree odd evaluations on the square-root section have near-
log-integral (GEOMETRIC-mean) Dirichlet distribution; the exact circle
constant is int_0^1 log|cos(2pi x)|^2 dx = -2 log 2. Then J_2 <=
q^{-L_j + 2 eps_j + O(1)}, so EJM_2 holds with eta_j <= eps_j + O(1); sum
eps_j = o(t) closes the primitive core through the banked cascade. PROVED
en route (D4): the exact collision identity 1 + J_2m = q^L Pr[VZ = 0]; the
seen-coordinate lever (>= 255L+1) is TRUE but INSUFFICIENT (Dirichlet peaks;
even degree-preimage refinement leaves ~129 near-peak residues); arithmetic
average gives only q^{-L} — geometric behavior is required. CALIBRATION
(verified, 3 rows reproduced exactly): no falsifier at the section toys;
mu_32 ternary eta*/L = 3.6e-7 (essentially flat); signed midpoint is the
stress case (eta*/L = 0.019 at mu_32, decreasing with N); m = 1 optimal for
signed domains (the Z_y zero-atom).

## Conditional decomposition

This node is conditional on `dli_log_integral_equidistribution`.

The exact circle constant is closed by `dli_circle_log_integral_constant`.
The remaining analytic input below the log-integral predicate is
`dli_odd_evaluation_discrepancy`.
