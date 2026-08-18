# Dependency sub-DAG

```text
dli_primitive_haar_event_correlation (PROVED)
                    |
                    | req
                    v
dli_fixed_weight_ambient_q_bridge (PROVED)
                    |
                    | ev
                    v
dli_c2pp_joint_reserve (TARGET)
```

The incoming requirement supplies the exact Haar joint event and first-owner
normalization. The present node proves the Fourier-positive marginal floor
and the fixed-weight image/ambient dictionary. The outgoing edge is evidence,
not a requirement: the finite ambient-Q payment `(AQ5)` remains open.

