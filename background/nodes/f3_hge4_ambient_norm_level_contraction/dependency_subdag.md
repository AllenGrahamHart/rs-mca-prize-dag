# Dependency sub-DAG

```text
f3_hge4_exact_ratio_tower_orbit_compiler [PROVED]
                         |
                         v
f3_hge4_ambient_norm_level_contraction [PROVED]
                         ^
                         |
f3_hge4_cyclotomic_norm_quarter_width_exclusion [PROVED]
                         |
                         v (evidence)
f3_hge4_norm_gate_count [TARGET]
```

The tower compiler supplies the ambient/exact-level typing. The quarter node
supplies the norm packet and retains responsibility for `h>=m/4`.
`f3_hge4_nonfull_complement_third_gate` is an additional required supplier
for the full live-range conclusion `(ALC4)` and deletes `h>=m/3`.
The exact per-width strengthening also consumes
`f3_hge4_vandermonde_defect_band_exclusion`,
`f3_hge4_primitive_swap_odd_moment_router`, and
`f3_hge4_swap_norm_haar_band_exclusion` for the exhaustive free/swap split.
