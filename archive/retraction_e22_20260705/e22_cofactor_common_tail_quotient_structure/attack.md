# ATTACK - e22_cofactor_common_tail_quotient_structure

This is now an assembly node.

The formal tail-removal and quotient-factor passthrough is proved in
`e22_tail_removed_quotient_factor_passthrough`, and the full-fiber criterion
is proved in `e22_kernel_invariance_full_fiber_criterion`. What remains is the
E22-specific kernel-invariance structure forced by

```text
L_{T_i} | U L_{Z\C} - a_i L_{C\Z}.
```

Remaining task:

- identify one tail `B` shared by all touched-petal divisors;
- prove `|B| < min_i M_i`;
- choose dyadic local moduli `M_i>t`;
- prove that every non-tail root set forced by `L_{T_i}|H_i` is invariant
  under the corresponding `M_i`-th-root kernel.

Once this structure is supplied, the kernel-invariance criterion gives full
fibers, and the proved passthrough lemma turns them into the actual quotient
factors `X^{M_i}-z` in the cofactors.
