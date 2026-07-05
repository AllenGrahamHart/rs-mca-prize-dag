# dependency sub-DAG: e22_common_tail_invariance_payload

Edges are directed from dependency to consumer.

```text
e22_fiber_locator_saturation [PROVED]
    -> e22_tail_removed_factor_manifest_soundness [PROVED]
    -> e22_common_tail_invariance_payload [CONDITIONAL]

e22_kernel_invariance_full_fiber_criterion [PROVED]
    -> e22_tail_removed_factor_manifest_soundness [PROVED]

e22_tail_removed_factor_manifest_payload [TARGET]
    -> e22_common_tail_invariance_payload [CONDITIONAL]

e22_common_tail_invariance_payload [CONDITIONAL]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
    -> e22_cofactor_common_tail_quotient_structure [CONDITIONAL]
```

This node is now an assembly from factor-manifest soundness plus the actual
E22 cofactor factorization manifest.
