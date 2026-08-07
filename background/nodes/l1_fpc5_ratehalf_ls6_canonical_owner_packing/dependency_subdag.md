# Dependency sub-DAG

```text
l1_fpc5_ratehalf_ls6_pair_determinant_router [PROVED] --------+
l1_fpc5_ratehalf_ls6_determinant_coordinate_chart [PROVED] ---+
                                                                 v
l1_fpc5_ratehalf_ls6_canonical_owner_packing [PROVED]
  --ev--> l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET]
  --ev--> shared_census_kernel
```

The determinant chart identifies the owner exactly. The pair router supplies
the nonzero degree-`h` polynomial used only after fixing that owner. No
aggregate owner-count theorem is imported.
