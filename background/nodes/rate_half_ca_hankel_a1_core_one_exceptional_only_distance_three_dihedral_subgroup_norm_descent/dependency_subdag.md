# Dependency sub-DAG

```text
dihedral_boundary_order_router [PROVED] ----+
                                             +--req--> dihedral_subgroup_norm_descent [PROVED]
sparse_subgroup_norm_router [PROVED] -------+                       |
                                                                    +--ev--> rate_half_band_closure [UNPROVED]
```

The descent introduces no premise. It supplies a smaller exact norm interface
for the still-open split perfect-power condition.
