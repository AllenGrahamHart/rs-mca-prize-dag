# Dependency sub-DAG

```text
xr_threshold_quotient_image_lcm_normal_form [PROVED]
                         |
                         v
xr_quotient_image_remainder_one_boundary_descent [PROVED]
                         |
                         +--req--> xr_quotient_boundary_agreement_raise_owner
                         |
                         +--ev---> xr_tangent_support_mismatch_bridge
```

The image-lcm theorem identifies distinct slope factors. This node localizes
all factors introduced above the base agreement to remainder-one tangent
boundaries. The downstream owner carries that image into `B_(A+1)`.
