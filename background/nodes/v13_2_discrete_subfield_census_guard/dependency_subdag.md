# Dependency sub-DAG

```text
Paper D v13.2 prop:capg-census-floor [external proved source]
    |
    v
v13_2_discrete_subfield_census_guard [PROVED]
    | ev                         | ev
    v                            v
shared_census_kernel          f1_case_tower
```

Both outgoing edges are evidence-only. The guard changes no critical
status and is not a safe-side closure theorem.
