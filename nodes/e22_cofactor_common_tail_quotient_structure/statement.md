# e22_cofactor_common_tail_quotient_structure

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For E22 mixed/full-petal challengers satisfying the cofactor divisor
constraints

```text
L_{T_i}(X) | H_i(X),
H_i(X) = U(X)L_{Z\C}(X) - a_i L_{C\Z}(X),
```

construct:

- one common exceptional tail `B`;
- dyadic local moduli `M_i>t`;
- quotient values `z`;

such that:

```text
|B| < min_i M_i,
```

and every forced non-tail root set `T_i\B` is a union of full fibers of
`x -> x^{M_i}`.

This is reduced to:

- `e22_kernel_invariance_full_fiber_criterion`, which proves that kernel
  invariance is equivalent to being a union of full quotient fibers; and
- `e22_cofactor_common_tail_kernel_invariance`, which remains to construct the
  common bounded tail and prove local kernel invariance from the cofactor
  divisibility constraints.

## Falsifier

A mixed/full-petal divisor pattern satisfying the cofactor constraints for
which no common bounded tail and local dyadic full-fiber structure exists.
