# Dependency sub-DAG

```text
rate_half_mca_rank11_dense_pair_degree18_seed_compiler [PROVED]
                         |
                         v
rate_half_mca_rank11_shortened_partial_relative_router [PROVED]
                         |
                         +-------------------------------+
                                                         |
rate_half_mca_order32_partial_relative_harvest [PROVED]  |
                         |                               |
rate_half_mca_pole_tolerant_scalar_locator_harvest [PROVED]
                         |                               |
                         +-------------------------------+
                                      |
                                      v
rate_half_mca_rank11_anchor_star_sae_router [PROVED]
                    /       /        |        \
                  (C)     (S)       (A)       (E)         [OPEN terminals]
```

The new theorem globalizes local tuples while keeping the standard upstream
terminal names and explicitly retaining the locally common punctured-domain
residual rather than hiding it in `(E)`. It creates no conditional child.
