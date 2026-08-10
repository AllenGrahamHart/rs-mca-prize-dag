# Dependency sub-DAG

```text
l1_fpc5_tpetal_hankel_grs_syndrome_shell [PROVED]
  -> l1_fpc5_grs_shell_constant_weight_shortening_cap [PROVED]
       -> l1_fpc5_grs_shortening_official_prefix_payment [PROVED]
            -ev-> l1_fpc5_large_source_payment [TARGET]

l1_fpc5_large_source_exact_prefilter [PROVED] --------^
l1_fpc5_official_rate_prefilter_scale_gap [PROVED] ---^
l1_general_first_layout_domination [PROVED] ----------^
```

The payment node owns all incoming requirement edges. Its outgoing edge is
evidence only because later source scales and two rate lanes remain open.
