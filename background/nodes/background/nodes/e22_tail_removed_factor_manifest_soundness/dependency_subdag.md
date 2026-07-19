# dependency sub-DAG: e22_tail_removed_factor_manifest_soundness

Edges are directed from dependency to consumer.

```text
e22_fiber_locator_saturation [PROVED]
    -> e22_tail_removed_factor_manifest_soundness [PROVED]
    -> e22_common_tail_invariance_payload [CONDITIONAL]

e22_kernel_invariance_full_fiber_criterion [PROVED]
    -> e22_tail_removed_factor_manifest_soundness [PROVED]
```

This node proves only manifest semantics. The actual E22 factor manifest is
the separate payload node.
