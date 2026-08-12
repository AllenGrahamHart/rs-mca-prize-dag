# Dependency sub-DAG

```text
(SAT4)-(SAT5) + (RNC1)-(RNC2)        rate_half_layer_a_saturation_count_route_fence [PROVED]
        |                                     |  (requires: the m=2 member + banked family)
        v                                     v
rate_half_layer_a_equivalence_and_geometry_counterexamples [PROVED / (LA-PADE) POSED]
        |
        +-- mechanism citation: rate_half_bivariate_single_coefficient_rational_interpolation_criterion [PROVED]
        +-- m=1 instance: rate_half_bivariate_row_surplus_route_fence [PROVED]
        |
        : evidence / retires the universal layer-A rank target
        v
rate_half_band_crossing_location [TARGET]
```

The requires edge carries the `m = 2` member and the banked `m = 2,3,4,6`
family measurements; the (RIC3) and row-surplus references are mechanism
citations (three faces of one mechanism), not dependencies.
