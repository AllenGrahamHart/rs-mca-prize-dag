# Dependency sub-DAG

```text
f3_hge4_cyclotomic_haar_near_quarter_swap_router (PROVED)
                         \
                          -> f3_hge4_vandermonde_defect_band_exclusion (PROVED)
                         /                                             |
f3_hge4_swap_norm_haar_band_exclusion (PROVED)                         ev
                                                                        v
                                             f3_hge4_norm_gate_count (TARGET)
```

The first dependency supplies the strict cyclotomic antipodal-defect
ceiling. The second excludes every swap in the larger dyadic swap band. The
new argument between them uses the consecutive even moments to prove that a
nonzero defect needs more than half the width in distinct coordinates.
