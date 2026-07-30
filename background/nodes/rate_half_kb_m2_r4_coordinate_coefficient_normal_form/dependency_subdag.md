# Dependency sub-DAG

```text
rate_half_kb_m2_r4_order2_coordinate_source_facet_signature [PROVED]
rate_half_kb_m2_r4_source_row_interpolation_compiler [PROVED]
                         \             /
                          \           /
rate_half_kb_m2_r4_coordinate_coefficient_normal_form [PROVED]
                                  |
                                  v evidence
                    rate_half_band_closure [TARGET]
```

The child compiles the coordinate source equations but does not prove that
either eigenspace is empty.
