# proof: e22_minimal_scale_pricing_compatibility

The proved node `e22_minimal_scale_tail_criterion` gives an intrinsic
criterion for being selected at scale `M`: the canonical tail at `M` has size
`<M`, and all smaller admissible dyadic scales have tails of size at least
their modulus.

The proved node `e22_minimal_scale_count_formula` assembles the
minimal-scale partition with the exact column evaluation, proving that the
dyadic quotient staircase pricing column counts exactly the support classes
satisfying this tail-minimality criterion, with the declared duplicate
subtraction or multiplicity factor.

Therefore the pricing column counts the minimal-scale representatives
selected by `e22_dyadic_minimal_scale_selector` with exactly the declared
multiplicity.
