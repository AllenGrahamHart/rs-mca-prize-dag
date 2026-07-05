# dependency sub-DAG: e22_cofactor_coset_saturation

Edges are directed from dependency to consumer.

```text
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
```

## Status

- `e22_cofactor_petal_divisibility`: PROVED. Pointwise cofactor equations are
  exactly petal-locator divisibility constraints.
- `e22_common_tail_invariance_payload`: TARGET. This is the
  remaining E22-specific common-tail and local kernel-invariance extraction
  from the divisor constraints.
- `e22_cofactor_common_tail_quotient_structure`: CONDITIONAL.
- `e22_local_quotient_factor_extraction`: CONDITIONAL.
- `e22_tail_removed_quotient_factor_passthrough`: PROVED. Tail removal
  preserves the supplied quotient factors in the cofactor divisibility.
- `e22_fiber_locator_saturation`: PROVED. Quotient factors are full local
  fibers.
- `e22_fixed_tail_local_saturation`: CONDITIONAL.
- `e22_dyadic_local_to_common_saturation`: PROVED. Local dyadic saturated
  blocks glue to the minimum local modulus.
- `e22_cofactor_divisor_quotient_gluing`: CONDITIONAL.
- `e22_cofactor_coset_saturation`: CONDITIONAL.
