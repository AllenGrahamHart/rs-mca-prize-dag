# e22_cofactor_coset_saturation

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For mixed/full-petal non-planted E22 challengers, the cofactor equations
supplied by `e22_agreement_cofactor_equations` force the non-tail roots to be
saturated on full fibers of a quotient map `x -> x^M` for some divisor `M`
with `M > t`.

## Conditional decomposition

This node is conditional on:

- `e22_cofactor_petal_divisibility`;
- `e22_cofactor_divisor_quotient_gluing`.

## Falsifier

A mixed/full-petal challenger satisfying the cofactor equations but whose
non-tail roots are not saturated on any such quotient fibers.
