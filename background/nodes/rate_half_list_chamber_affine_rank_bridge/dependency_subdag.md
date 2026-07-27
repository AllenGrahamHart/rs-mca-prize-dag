# Dependency sub-DAG

```text
upstream_gfv4_affine_span_list_compiler [PROVED] -----------+
rate_half_list_budget_three_intersection_reduction [PROVED] -+
rate_half_list_budget_three_affine_rank_rigidity [PROVED] ---+--> rank-flat cap >= 4
rate_half_list_budget_three_common_mismatch_zero [PROVED] ----+         |
                                                                      v
rate_half_list_chamber_affine_rank_bridge [PROVED route fence]
  -ev-> rate_half_list_adjacent_crossing [TARGET]
```
