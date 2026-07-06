# spi_point_counting conditional proof
## Predicate nodes
- `conj_f`
- `hankel_slope_large_sieve`
## Claim
R2: #(D_j cap X_{u,v} \ Paid) <= n^B max(1, C(n,j) q^{-(t-1)}), B = C_F + C_Sigma.
## Proof (Pro Theorem J, refereed)
N_unp = sum over supported slopes of the unpaid fiber size. Each unpaid fiber
is a linear-plane section of D_j, so conj_f (PROVED) bounds it by n^{C_F}.
The sieve bounds #Sigma_unp by n^{C_Sigma} max(1, C(n,j)/q^{t-1}). Multiply.
Vertical/degenerate slopes: rank-profile packet + noncontainment gate.
Non-circular; converse noted (R2 => sieve), so the sieve is exactly the
residual content.
