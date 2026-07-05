# e22_cross_scale_equivalence_specification

- **status:** CONDITIONAL
- **closure:** proof

## Statement

After the E22 staircase parameter set is fixed, specify the exact declared
cross-scale equivalence relation on recovered root-set data and prove it
contains every equal-support representation across quotient moduli.

The specification must also be compatible with the quotient staircase pricing
column, so every declared class has the intended multiplicity.

## Conditional decomposition

This node is conditional on:

- `e22_cross_scale_support_canonical_form`;
- `e22_cross_scale_pricing_multiplicity`.

## Falsifier

An equal-support cross-scale representation pair not included in the declared
equivalence relation, or an equivalence class whose pricing multiplicity is
wrong.
