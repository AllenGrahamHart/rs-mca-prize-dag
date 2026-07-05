# ATTACK - e22_local_quotient_factor_extraction

This is now an assembly node after separating the formal tail-removal
passthrough lemma.

Input:

```text
L_{T_i} | H_i,
H_i = U L_{Z\C} - a_i L_{C\Z}.
```

Known:

- `e22_tail_removed_quotient_factor_passthrough` proves that, once the common
  tail and quotient-fiber root sets are known, the quotient factors
  `X^{M_i}-z` divide the tail-removed cofactors formally.

Remaining task:

- one common exceptional tail `B`;
- a proof that `|B| < min_i M_i`;
- dyadic local moduli `M_i > t`;
- full-fiber structure of every non-tail root forced by each touched-petal
  divisor.

Once these quotient factors are available, `e22_fiber_locator_saturation`
turns them into local full-fiber blocks, and
`e22_dyadic_local_to_common_saturation` glues the blocks to one modulus.
