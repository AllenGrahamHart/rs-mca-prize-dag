# Dependency sub-DAG

```text
xr_agreement_raise_quotient_safe_sum_fence [PROVED]
                         |
                         v
xr_threshold_quotient_image_lcm_normal_form [PROVED]
                         |
                         +--ev--> xr_tangent_support_mismatch_bridge
```

The fence shows why support counting is insufficient. The lcm theorem gives
the exact distinct-slope replacement but no degree bound, so its consumer edge
is evidence only.
