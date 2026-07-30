# Dependency sub-DAG

```text
rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler [PROVED]
rate_half_kb_m2_u2_colored_source_resultant_split_compiler         [PROVED]
                                  \                     /
                                   \                   /
rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction              [PROVED]
                                  |
                                  v evidence
                    rate_half_band_closure                         [TARGET]
```

The mixing obstruction and orbit census use only whole-fiber transport and
facet supports. The `c=6` quotient descent additionally uses the universal
colored partial-resultant split. Both conclusions apply to both branches of
the later source-subfield dichotomy and do not assume that the diagonal
automorphism descends to the source `X`-line.
