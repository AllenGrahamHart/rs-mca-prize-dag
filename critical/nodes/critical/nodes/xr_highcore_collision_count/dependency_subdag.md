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
xr_highcore_collision_line_basis_ledger [PROVED]-----+
xr_higher_rank_uniform_split_pencil_reduction [PROVED]-+
xr_higher_rank_minimal_face_syzygy_dichotomy [PROVED]-/
                                                        |
                                                        v
xr_smallcore_spread_count [CONDITIONAL with P-B]
```

The component atlas supplies the missing aggregate first-match and
deduplication step. DDR and the affine-core theorem are independent proved
inputs to P-A, not premises of the atlas. The collision-line basis ledger and
affine-core cogirth bound close selector rank four on five rows. At RowC
`1/16`, the line-free/line-uncovered rank-four subcase remains open.
The uniform higher-rank split-pencil reduction supplies a bounded trade
certificate at every rank in the `u=v=0` cell. The target remains red because
those trades are not counted and nonuniform higher-rank selectors are not yet
paid on every row. The minimum rank-two union is classified into local face
syzygies and a common `k+2` near-tangent branch, but the latter still needs its
exact `h-2` deficit paid when `h>2`.
