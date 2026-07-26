# Dependency sub-DAG

```text
rs_tangent_flexible_budget_unsafe_floor [PROVED]
    --req--> tangent_clean_anchor_route_classification [PROVED]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The theorem is self-contained. The upstream source pin records provenance but
is not a logical assumption. The evidence edge does not claim every row
satisfies the exact tangent budget inequality.
