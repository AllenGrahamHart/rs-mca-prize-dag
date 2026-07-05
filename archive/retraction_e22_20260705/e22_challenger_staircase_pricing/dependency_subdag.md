# dependency sub-DAG: e22_challenger_staircase_pricing

Edges are directed from dependency to consumer.

```text
e22_staircase_parametrization
    -> e22_staircase_arithmetic_pricing
    -> e22_challenger_staircase_pricing

e22_tail_coset_locator_algebra [PROVED]
    -> e22_staircase_parametrization

e22_agreement_coset_support_forcing
    -> e22_staircase_parametrization

e22_agreement_cofactor_equations [PROVED]
    -> e22_cofactor_petal_divisibility [PROVED]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
    -> e22_cofactor_common_tail_quotient_structure [CONDITIONAL]
    -> e22_local_quotient_factor_extraction [CONDITIONAL]
    -> e22_fixed_tail_local_saturation [CONDITIONAL]
    -> e22_cofactor_divisor_quotient_gluing [CONDITIONAL]
    -> e22_cofactor_coset_saturation
    -> e22_agreement_coset_support_forcing

e22_fiber_locator_saturation [PROVED]
    -> e22_tail_removed_quotient_factor_passthrough [PROVED]
    -> e22_local_quotient_factor_extraction [CONDITIONAL]

e22_fiber_locator_saturation [PROVED]
    -> e22_fixed_tail_local_saturation [CONDITIONAL]

e22_dyadic_local_to_common_saturation [PROVED]
    -> e22_cofactor_divisor_quotient_gluing [CONDITIONAL]
    -> e22_cofactor_coset_saturation
    -> e22_agreement_coset_support_forcing

e22_staircase_injectivity
    -> e22_staircase_arithmetic_pricing
    -> e22_challenger_staircase_pricing

e22_fixed_scale_staircase_injectivity [PROVED]
    -> e22_staircase_injectivity

e22_cross_scale_planted_degeneracy_control
    -> e22_staircase_injectivity

e22_planted_profile_disjointness [PROVED]
    -> e22_cross_scale_planted_degeneracy_control

e22_fixed_scale_staircase_injectivity [PROVED]
    -> e22_cross_scale_rootset_recovery [PROVED]
    -> e22_cross_scale_support_canonical_form [PROVED]
    -> e22_cross_scale_equivalence_specification
    -> e22_cross_scale_duplicate_control
    -> e22_cross_scale_planted_degeneracy_control

e22_cross_scale_pricing_multiplicity
    -> e22_cross_scale_equivalence_specification
    -> e22_cross_scale_duplicate_control
    -> e22_cross_scale_planted_degeneracy_control

dyadic_profile_evaluation [PROVED]
    -> e22_staircase_arithmetic_pricing

e22_staircase_arithmetic_pricing
    -> e22_challenger_staircase_pricing
```

## Status

- `e22_challenger_staircase_pricing`: CONDITIONAL. The assembly implication is
  explicit.
- `e22_staircase_parametrization`: CONDITIONAL. It now depends on the proved
  forward locator algebra and the open support-forcing theorem.
- `e22_tail_coset_locator_algebra`: PROVED. Shows tail-plus-full-coset
  supports have locator `L_B(X)G(X^M)` and top-coefficient invariance when
  `M > t`.
- `e22_agreement_coset_support_forcing`: CONDITIONAL. The generic cofactor
  equations and petal-divisibility translation are proved; quotient gluing
  remains open.
- `e22_agreement_cofactor_equations`: PROVED. Factors zero agreements and
  rewrites every petal agreement as a locator-cofactor equation.
- `e22_cofactor_petal_divisibility`: PROVED. Converts pointwise cofactor
  equations into petal-locator divisibility constraints.
- `e22_cofactor_coset_saturation`: CONDITIONAL. It now assembles the proved
  divisibility translation with the conditional quotient-gluing theorem.
- `e22_common_tail_invariance_payload`: TARGET. Needs the petal
  divisor constraints to isolate one bounded tail and local dyadic
  quotient-kernel invariance in the sunflower notation of `e22_core.py`.
- `e22_cofactor_common_tail_quotient_structure`: CONDITIONAL.
- `e22_local_quotient_factor_extraction`: CONDITIONAL.
- `e22_tail_removed_quotient_factor_passthrough`: PROVED. Once the common
  tail and full fibers are supplied, the quotient factors pass through the
  cofactor divisibility formally.
- `e22_fiber_locator_saturation`: PROVED. Quotient factors are exactly full
  quotient fibers.
- `e22_fixed_tail_local_saturation`: CONDITIONAL.
- `e22_dyadic_local_to_common_saturation`: PROVED. Local dyadic quotient
  blocks glue to the minimum local modulus.
- `e22_cofactor_divisor_quotient_gluing`: CONDITIONAL. It assembles the
  fixed-tail extraction with dyadic common-modulus gluing.
- `e22_staircase_injectivity`: CONDITIONAL. Fixed-scale injectivity is
  proved; cross-scale equivalence and planted degeneracy remain open.
- `e22_fixed_scale_staircase_injectivity`: PROVED. At fixed `M`, the root
  set recovers the selected full quotient fibers and the tail.
- `e22_cross_scale_planted_degeneracy_control`: CONDITIONAL.
  Planted-overlap exclusion is proved; cross-scale duplicate control remains.
- `e22_planted_profile_disjointness`: PROVED. Planted words have exactly the
  one-petal profile, so they are disjoint from nondegenerate mixed/full-petal
  staircase challengers.
- `e22_cross_scale_duplicate_control`: CONDITIONAL. The root-set recovery and
  support-canonicalization components are proved; the active leaf is now
  `e22_cross_scale_pricing_multiplicity`.
- `e22_cross_scale_rootset_recovery`: PROVED. Equal staircase locators have
  the same root set, and fixed-scale recovery recovers each scale's tail and
  selected fibers.
- `e22_cross_scale_support_canonical_form`: PROVED. Equal supports have one
  canonical set of admissible scales, tails, and full fibers.
- `e22_cross_scale_equivalence_specification`: CONDITIONAL. The remaining
  content is pricing compatibility.
- `e22_cross_scale_pricing_multiplicity`: TARGET. Needs the canonical
  cross-scale classes to match the dyadic quotient staircase pricing column.
- `dyadic_profile_evaluation`: PROVED. Supplies the exact dyadic quotient
  staircase column and row arithmetic used by the consumer.
- `e22_staircase_arithmetic_pricing`: CONDITIONAL. It is now only the
  arithmetic consumer of the formula and injectivity leaves.

The n=16 exact cells are useful calibration data only; they are not a proof of
the staircase formula.
