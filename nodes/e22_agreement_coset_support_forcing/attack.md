# ATTACK - e22_agreement_coset_support_forcing

Status: conditional.

The generic locator/cofactor reduction is proved in
`e22_agreement_cofactor_equations`, and the pointwise-to-divisor translation
is proved in `e22_cofactor_petal_divisibility`. The active target is now
`e22_local_quotient_factor_extraction`: show that the petal divisor
constraints isolate one bounded tail and local quotient factors. The proved
fiber-locator and dyadic local-to-common lemmas then give saturation on fibers
of one quotient map `x -> x^M`, with `M > t`. Once that support statement is
proved, `e22_tail_coset_locator_algebra` gives the `L_B(X)G(X^M)` form.

Toy profile matching is only a check on proposed formulas; it is not enough
to promote this node.
