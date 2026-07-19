# conditional: e22_minimal_scale_pricing_compatibility

## Predicate nodes

- `e22_minimal_scale_tail_criterion`
- `e22_minimal_scale_count_formula`

## Claim

Conditional on the exact tail-minimal count formula, the dyadic quotient
staircase pricing column counts the selected minimal-scale representatives
with exactly the declared multiplicity.

## Proof

The proved node `e22_minimal_scale_tail_criterion` gives an intrinsic
criterion for being selected at scale `M`: the canonical tail at `M` has size
`<M`, and all smaller admissible dyadic scales have tails of size at least
their modulus. This translates the selected-representative problem into a
property of the canonical support-scale data.

The predicate `e22_minimal_scale_count_formula` now assembles the proved
minimal-scale partition with `e22_minimal_scale_column_evaluation`, which says
that the dyadic quotient staircase pricing column, after any declared
duplicate subtraction or multiplicity factor, counts exactly the support
classes satisfying that tail-minimality criterion.

Therefore the pricing column counts the minimal-scale representatives selected
by `e22_dyadic_minimal_scale_selector` with the declared multiplicity.
