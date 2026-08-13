# Dependency sub-DAG

```text
rate_half_mca_sparse_direction_punctured_johnson_profile (PROVED)
       |
rate_half_mca_sparse_direction_near_johnson_gram_rank_payment (PROVED)
       |
rate_half_mca_sparse_direction_mean_centered_gram_profile (PROVED)
       |
rate_half_mca_sparse_direction_terminal_deficit_line_payment (PROVED)
       |
rate_half_band_crossing_location (TARGET, evidence only)
```

The new node changes only the exact terminal layer.  It retains the proved
cumulative caps from the mean-centered node for every prefix layer.
