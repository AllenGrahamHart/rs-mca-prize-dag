# Dependency sub-DAG

```text
xr_strip_classification_rungs [PROVED] ----------------\
f5_lineray_saturation_instrument [PROVED] --------------+
f5_wcollision_pair_moment_identity [PROVED] ------------+
xr_generic_mds_kernel_ray_bound [PROVED] ---------------+
xr_highcore_component_union_atlas [PROVED] -------------+
xr_direction_distance_ray_bound [PROVED] ---------------+
xr_all_lineray_affine_core_bound [PROVED] --------------+
xr_affine_core_cogirth_ray_bound [PROVED] ---------------+
xr_highcore_collision_line_basis_ledger [PROVED] --------+--> P-A1 OPEN
xr_trade_circuit_arity_segre_atlas [PROVED] -------------+
xr_rank_two_fundamental_circuit_owner [PROVED] ----------+
xr_rank_two_three_anchor_grs3_factorization [PROVED] ----+
xr_rank_two_four_anchor_quadric_centroid_atlas [PROVED] -+
xr_rank_two_dual_support_extension_factorization [PROVED]+
xr_rank_two_received_pair_alternating_router [PROVED] ---+
xr_rank_two_actual_block_extension_router [PROVED] ------+
xr_rank_two_extension_family_collision_ledger [PROVED] -/

xr_tangent_support_mismatch_bridge [PROVED] -------------------------------\
xr_supportwise_transverse_lineray_rank_charge [PROVED] --------------------+
xr_tangent_mismatch_full_external_zero_canonicalization [PROVED]           |
       |                                                                   |
       v                                                                   |
xr_mismatch_nongeneric_invariant_excess_descent [PROVED]                   |
       |                                                                   |
       v                                                                   |
xr_mismatch_descent_dimension_area_law [PROVED]                            |
       |                                                                   |
       v                                                                   |
xr_nongeneric_explanation_plotkin_width [PROVED] --------------------------+--> P-A2 OPEN

P-A1 OPEN ---------------------------------------------------------------\
P-A2 OPEN ----------------------------------------------------------------+--> xr_highcore_collision_count [TARGET]
                                                                                          |
                                                                                          v
                                                        xr_smallcore_spread_count [CONDITIONAL with P-B]
```

The upper branch is P-A1. The component atlas supplies its aggregate
first-match and deduplication step. DDR and the affine-core theorem are
independent proved inputs to P-A1, not premises of the atlas. The
collision-line basis ledger and
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

The lower branch is P-A2. It retains the former bridge's combined `16n^3`
budget. Canonicalization, invariant-excess descent, the dimension-area law,
and terminal-width control are proved, but the pre-terminal generic-chart
union and nongeneric slope-to-explanation fibers are not yet aggregated.

The target remains red because neither P-A1's nonuniform higher-rank
selectors nor P-A2's two pre-terminal aggregate currencies are paid on every
row.
