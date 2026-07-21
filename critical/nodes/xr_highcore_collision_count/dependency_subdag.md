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
                                                       ^
xr_trade_circuit_arity_segre_atlas [PROVED]            |
                |                                      |
                v                                      |
xr_rank_two_fundamental_circuit_owner [PROVED] --------+
                +------------------------\             |
                v                        v             |
xr_rank_two_three_anchor_grs3_factorization [PROVED]   |
xr_rank_two_four_anchor_quadric_centroid_atlas [PROVED]
                |                        |             |
                +------------------------+-------------/
xr_rank_two_dual_support_extension_factorization [PROVED]
                |                                      |
                +--------------------------------------/
xr_rank_two_received_pair_alternating_router [PROVED]
                |                                      |
                +--------------------------------------/
xr_rank_two_actual_block_extension_router [PROVED]
                |                                      |
                +--------------------------------------/
xr_rank_two_extension_family_collision_ledger [PROVED]
                |                                      |
                +--------------------------------------/
                                                        |
                                                        v
xr_smallcore_spread_count [CONDITIONAL with P-B]
```

The component atlas supplies the missing aggregate first-match and
deduplication step. DDR and the affine-core theorem are independent proved
inputs to P-A, not premises of the atlas. The collision-line basis ledger and
affine-core cogirth bound together close selector rank four on all six rows.
The rank-two branch supplies bounded circuit arity and a canonical owner for
every non-anchor inside a fixed trade; first-core support ownership remains
at the target. Its three-anchor subbranch additionally has an exact
dual-`GRS_3` scalar factorization on every support shell, while its
four-anchor subbranch has an exact quadric-centroid atlas. The dual support-
extension node supplies the common-cofactor certificate for both branches,
and the received-pair router supplies their alternating/zero interaction
constraints. The actual-block router closes per-support extension counting.
The collision ledger closes family compatibility, but not the number of
compatible support/packing records.
The target remains red because nonuniform higher-rank selectors are not yet
paid on every row.
