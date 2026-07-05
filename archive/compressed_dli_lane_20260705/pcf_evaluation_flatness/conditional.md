# pcf_evaluation_flatness conditional proof
## Predicate node
- `ejm_joint_moment`
## Claim
EJM_{2m} implies the evaluation-form flatness B_j(M) <= q^{-L_j+eta_j} U_j(M).
## Proof (Pro D3, verified: Fourier identity + Holder on toy cases, PASS)
Character orthogonality: rho_j = sum_lambda F_M(lambda) = 1 + sum_{lambda!=0}.
Holder with exponent 2m: sum_{lambda!=0}|F| <= (q^L-1)^{1-1/2m} J_2m^{1/2m};
under EJM the exponents cancel exactly (L(1-1/2m) - (2m-1)L/2m = 0), giving
sum_{lambda!=0}|F| <= q^{eta_j} - 1, hence rho_j <= q^{eta_j}. The cascade
then gives C_central <= q^{-t+H} W_cen as before.
