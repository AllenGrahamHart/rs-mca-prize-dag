# Dependency sub-DAG

```text
rate_half_cyclic_rotated_prefix_floor [PROVED]
  --req--> rate_half_cyclic_simple_pole_mca_floor [PROVED]

rate_half_cyclic_simple_pole_mca_floor [PROVED]
  --ev----> rate_half_band_closure [TARGET; rowwise crossing]

rate_half_band_closure [TARGET]
  --req--> {adjacency_closing, mca_safe} [CONDITIONAL consumers]
```

The simple-pole proof is included locally. The Paper D labels in the claim
contract are correspondence references, not hidden logical imports.
