# Dependency sub-DAG

```text
rate_half_list_budget_three_multifiber_vandermonde_exclusion [PROVED]
  --req--> rate_half_list_budget_three_fiber_two_path_exclusion [PROVED]
             --ev--> rate_half_list_adjacent_crossing [TARGET]
```

The dependency supplies the common-fiber path setup and already pays every
fiber size `m>=3`. This node supplies the missing `m=2` parity argument. The
evidence edge does not promote the target because the `m=1`, mixed-map,
partial-fiber, and primitive branches remain.
