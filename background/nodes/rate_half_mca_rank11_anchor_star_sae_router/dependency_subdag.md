# Dependency sub-DAG

```text
rate_half_mca_rank11_dense_pair_degree18_seed_compiler [PROVED]
                         |
                         v
rate_half_mca_rank11_shortened_partial_relative_router [PROVED]
                         |
                         +-------------------------------+
                                                         |
rate_half_mca_whole_line_global_core_router [PROVED]     |
                         |                               |
rate_half_mca_order32_partial_relative_harvest [PROVED]  |
                         |                               |
rate_half_mca_pole_tolerant_scalar_locator_harvest [PROVED]
                         |                               |
                         +-------------------------------+
                                      |
                                      v
rate_half_mca_rank11_anchor_star_sae_router [PROVED]
                    /       /        |        \
       global-core (C)    (S)       (A)       (E)         [OPEN terminals]
```

The new theorem makes the common-core decision once for the complete line.
Only the zero-global-core branch enters the fixed-anchor S/A/E star. It
creates no conditional child.
