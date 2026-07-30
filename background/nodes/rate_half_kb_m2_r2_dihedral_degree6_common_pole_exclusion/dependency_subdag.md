# Dependency sub-DAG

```text
rate_half_kb_m2_r2_dihedral_outer_factor_reduction [PROVED]
rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier [PROVED]
                                  \                 /
rate_half_kb_m2_r2_dihedral_degree6_common_pole_exclusion [PROVED]
                                  |
                                  v evidence
                    rate_half_band_closure [TARGET]
```

The child uses the common pole divisor and the already-forced relative
branch pair. It deletes `n=6` only; the `n=3` profile and the full-V4 type
remain open.
