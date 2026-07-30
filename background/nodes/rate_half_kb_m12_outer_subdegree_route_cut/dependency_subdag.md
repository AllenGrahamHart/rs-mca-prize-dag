# Dependency sub-DAG

```text
rate_half_kb_source_pencil_rank_transverse_compiler [PROVED]
                         |
                         +--req-->
rate_half_kb_m12_outer_subdegree_route_cut [PROVED]
      |
      +--req--> rate_half_kb_m12_diagonal_socle_route_cut [PROVED]
      |             |
      |             +--req-->
      |       rate_half_kb_m12_secondary_degree5_decomposition_exclusion [PROVED]
      |             |
      |             +--ev--> rate_half_band_closure [TARGET]
      |
      +--req--> rate_half_kb_m12_r4_low_genus_branch_profile_reduction [PROVED]
                    |
                    +--req--> rate_half_kb_m12_outer_normal_form_compiler [PROVED]
                                  |
                                  +--ev--> rate_half_band_closure [TARGET]
```

The normal-form compiler's audited calculations remain valid route history,
but the diagonal-socle and secondary-degree-five branch closes every actual
`m=12` producer.
