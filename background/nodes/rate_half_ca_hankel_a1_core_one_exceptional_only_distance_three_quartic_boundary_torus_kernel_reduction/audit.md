# Audit

1. The label is `theta_i=c_i xi_i/lambda_i`, hence
   `xi_iP_Z(xi_i)/lambda_i^2`. Losing the second `lambda_i` changes the
   matrix kernel.
2. The matrix uses `q_e^3`: two powers come from the dual-moment weight and
   one from the derivative-free boundary quotient.
3. The trace is over `D_k` with `k!=i`. The `k=i` term is absent because
   `D_i(a)=0`, not because its denominator is assigned a limiting value.
4. Full rank is sufficient but not necessary for exclusion. A deficient
   kernel can still be excluded when one coordinate is identically zero on
   it, equivalently when the corresponding column is a coloop. The
   rank-deletion equivalence uses `q>e` for the union bound.
5. At `e=3` the matrix has only two rows. The deterministic control has no
   coloop, so failure of a particular `theta` does not exclude all possible
   external labels.
6. The full-rank `e=4,5,7` controls use deterministic subgroup partitions
   and internal labels but do not realize external split designs.
