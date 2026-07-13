# Dependency sub-DAG

```text
xr_strip_classification_rungs [PROVED]
f5_lineray_saturation_instrument [PROVED]
f5_wcollision_pair_moment_identity [PROVED]
xr_generic_mds_kernel_ray_bound [PROVED]
                |
                v
xr_highcore_component_union_atlas [PROVED] -------\
xr_direction_distance_ray_bound [PROVED] ----------+
xr_all_lineray_affine_core_bound [PROVED] ----------+-> xr_highcore_collision_count [TARGET]
xr_affine_core_cogirth_ray_bound [PROVED] -----------+
xr_highcore_collision_line_basis_ledger [PROVED]---/
                                                        |
                                                        v
xr_smallcore_spread_count [CONDITIONAL with P-B]
```

The component atlas supplies the missing aggregate first-match and
deduplication step. DDR and the affine-core theorem are independent proved
inputs to P-A, not premises of the atlas. The collision-line basis ledger and
affine-core cogirth bound together close selector rank four on all six rows.
The target remains red because nonuniform higher-rank selectors are not yet
paid on every row.
