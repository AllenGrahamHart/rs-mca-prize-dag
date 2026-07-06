# dependency sub-DAG: e22_common_tail_invariance_certificate_soundness

Edges are directed from dependency to consumer.

```text
e22_cofactor_petal_divisibility [PROVED]
    -> e22_common_tail_invariance_certificate_soundness [PROVED]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
```

This node proves only certificate semantics. The E22-specific construction of
the tail, moduli, and invariance checks remains in the payload node.
