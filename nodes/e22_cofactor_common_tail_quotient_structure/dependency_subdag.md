# dependency sub-DAG: e22_cofactor_common_tail_quotient_structure

Edges are directed from dependency to consumer.

```text
e22_cofactor_petal_divisibility [PROVED]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
    -> e22_cofactor_common_tail_quotient_structure [CONDITIONAL]
    -> e22_local_quotient_factor_extraction [CONDITIONAL]

e22_kernel_invariance_full_fiber_criterion [PROVED]
    -> e22_cofactor_common_tail_quotient_structure [CONDITIONAL]
```

The open node is `e22_common_tail_invariance_payload`: it supplies the
common tail, tail bound, local dyadic moduli, and kernel invariance needed by
the full-fiber criterion.
