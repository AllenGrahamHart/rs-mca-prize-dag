# dependency sub-DAG: e22_cofactor_common_tail_kernel_invariance

Edges are directed from dependency to consumer.

```text
e22_cofactor_petal_divisibility [PROVED]
    -> e22_common_tail_invariance_certificate_soundness [PROVED]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
    -> e22_cofactor_common_tail_quotient_structure [CONDITIONAL]

e22_common_tail_invariance_payload [TARGET]
    -> e22_cofactor_common_tail_kernel_invariance [CONDITIONAL]
```

The open E22 cofactor target is now the common-tail invariance payload. This
node records only the conditional assembly from a verified certificate to the
kernel-invariance predicate.
