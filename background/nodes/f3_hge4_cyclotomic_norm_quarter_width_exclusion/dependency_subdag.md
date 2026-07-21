# Dependency sub-DAG

```text
f3_hge4_exact_ratio_tower_orbit_compiler (PROVED)
                         \
                          -> f3_hge4_cyclotomic_norm_quarter_width_exclusion
                         /                                      (PROVED)
f3_hge4_near_third_belyi_necklace_bound (PROVED)                 |
                                                                    ev
                                                                     v
                                             f3_hge4_norm_gate_count (TARGET)
```

The exact-ratio compiler supplies the pair and orbit scope. The Belyi theorem
is used only at the delicate odd width `h=m/4+1`, where it excludes an
antipodal-swap midpoint of deficient degree. The new node deletes widths but
does not replace the remaining HGE4 aggregate.
