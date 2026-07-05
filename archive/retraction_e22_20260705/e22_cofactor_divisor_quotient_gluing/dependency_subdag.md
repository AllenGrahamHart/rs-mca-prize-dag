# dependency sub-DAG: e22_cofactor_divisor_quotient_gluing

Edges are directed from dependency to consumer.

```text
e22_agreement_cofactor_equations [PROVED]
    -> e22_cofactor_petal_divisibility [PROVED]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
    -> e22_cofactor_common_tail_quotient_structure [CONDITIONAL]
    -> e22_local_quotient_factor_extraction [CONDITIONAL]
    -> e22_fixed_tail_local_saturation [CONDITIONAL]
    -> e22_cofactor_divisor_quotient_gluing [CONDITIONAL]
    -> e22_cofactor_coset_saturation [CONDITIONAL]

e22_fiber_locator_saturation [PROVED]
    -> e22_tail_removed_quotient_factor_passthrough [PROVED]
    -> e22_local_quotient_factor_extraction [CONDITIONAL]

e22_fiber_locator_saturation [PROVED]
    -> e22_fixed_tail_local_saturation [CONDITIONAL]

e22_dyadic_minimal_scale_selector [PROVED]
    -> e22_dyadic_local_to_common_saturation [PROVED]
    -> e22_cofactor_divisor_quotient_gluing [CONDITIONAL]
```

The active mathematical leaf is
`e22_common_tail_invariance_payload`. It contains the E22-specific
mixed-petal completion, common-tail isolation, tail-bound, and local
kernel-invariance proof. The full-fiber criterion, tail-removal passthrough,
fiber-locator conversion, and dyadic common-modulus gluing are proved
separately.
