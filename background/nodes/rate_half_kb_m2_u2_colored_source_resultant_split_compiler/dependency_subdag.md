# Dependency sub-DAG

```text
rate_half_kb_m2_r4_source_row_interpolation_compiler       [PROVED]
rate_half_kb_m2_u2_universal_component_color_profile_cut  [PROVED]
                         \             /
                          \           /
rate_half_kb_m2_u2_colored_source_resultant_split_compiler [PROVED]
                                  |
                                  v evidence
                    rate_half_band_closure [TARGET]
```

The compiler replaces twelve independent row-product conditions by two
partial resultants and one squarefree colored quartic.
