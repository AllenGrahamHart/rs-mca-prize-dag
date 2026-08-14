# Dependency sub-DAG

```text
rate_half_mca_support_local_transversality_compiler [PROVED]
rate_half_mca_rank10_margin_interleaving_split_payment [PROVED]
                         |                 |
                         +--------+--------+
                                  |
rate_half_mca_rank11_anchor_star_sae_router [PROVED]
rate_half_mca_rank11_shortened_partial_relative_router [PROVED]
rate_half_mca_order32_partial_relative_harvest [PROVED]
                         |        |        |
                         +--------+--------+
                                  |
                                  v
rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router [PROVED]
                         /        |        \
                    paid r<=9   (H_C)     (A)/(E)
```

The node creates one exact residual label, `(H_C)`, and no conditional
proof premise. Shared `(A)/(E)` payments remain upstream terminals.
