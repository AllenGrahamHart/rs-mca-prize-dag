# ATTACK - e22_cofactor_common_tail_kernel_invariance

This is now an assembly node. The live E22 cofactor-structure leaf is
`e22_common_tail_invariance_payload`.

The proved `e22_kernel_invariance_full_fiber_criterion` shows that local
full-fiber structure follows from kernel invariance. What remains is to prove
that invariance from the actual cofactor divisibility constraints.

Needed output at the payload:

- identify a common tail `B` for all touched-petal divisors;
- prove `|B| < min_i M_i`;
- choose dyadic local moduli `M_i>t`;
- prove `T_i\B` is closed under multiplication by the `M_i`-th roots of
  unity.

Once this is known, the full-fiber structure and quotient-factor passthrough
are formal.
