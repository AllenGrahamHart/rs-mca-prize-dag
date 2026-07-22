# Audit

1. The gcd is multiplied into the complement. Omitting it produces a
   rational function and incorrectly reuses the zero-tail degree `e`.
2. `K_u` is the complement of the union of the two row root sets, so its
   degree is `e+d_u`, not `e-d_u`.
3. `I(gamma)` is nonzero because external and internal slopes are disjoint.
4. The determinant uses two polynomial coefficient blocks of length `t+1`.
   Its size is therefore `2(t+1)`, and its degree bound is the same number.
5. Identically zero determinants are not counted with the polynomial root
   bound. They are isolated explicitly as the remaining obstruction.
6. The outside-orbit count pays all `2t` tail roots, all five boundary rows,
   up to two reciprocal fixed points, and the one possible identical orbit.
7. The official rational percentages are exact integer comparisons, not
   floating-point estimates.
8. The incidence theorem is useful only after tail rigidity. At the coarse
   `t=40` loss, the subset-size penalty would exceed the official scale.
9. Tail locator norms are arbitrary nonzero quadratics. Only the good
   `e-t` indices give squares `(U-u_i)^2`; the circuit argument uses
   quadraticity, not a false square assumption at the tails.
