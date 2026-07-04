# ejm_joint_moment conditional proof
## Predicate node
- `dli_dirichlet_log_integral`
## Claim
DLI_j(eps_j) implies EJM_2(j, eta_j) with eta_j <= eps_j + O(1).
## Proof (Pro D4 section 8, verified)
Pointwise: DLI gives |F_M(lambda)|^2 <= q^{-2(L-eps)+O(1)} for every nonzero
lambda; summing over < q^L frequencies gives J_2 <= q^{-L+2eps+O(1)}, the
EJM_2 scale. Collision equivalent: DWE_2. Calibration replayed (3 rows
exact); the collision identity 1 + J_2m = q^L Pr[VZ=0] verified by DP.
