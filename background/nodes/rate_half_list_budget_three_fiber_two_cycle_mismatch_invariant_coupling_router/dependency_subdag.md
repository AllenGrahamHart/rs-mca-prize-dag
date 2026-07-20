# Dependency sub-DAG

```text
rate_half_list_budget_three_fiber_two_cycle_boundary_transfer [PROVED]
  |
  +--req--> rate_half_list_budget_three_fiber_two_cycle_mismatch_invariant_coupling_router [PROVED]
                 |
                 +--ev--> rate_half_list_adjacent_crossing [TARGET]
```

The dependency supplies the split denominator quartic, its exact `c=1,2`
root inventory, and the canonical outer quartic. This node proves the missing
completion-root coupling only; the evidence edge cannot promote the target
because none of the 30 invariant classes is yet excluded.
