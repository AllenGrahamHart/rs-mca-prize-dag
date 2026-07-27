# Dependency sub-DAG

```text
identity_prefix_flexible_budget_unsafe_floor [PROVED]
    --req--> identity_prefix_clean_anchor_route_classification [PROVED]

identity_prefix_clean_anchor_route_classification [PROVED]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The evidence edge narrows route ownership; it does not discharge the universal
target.
