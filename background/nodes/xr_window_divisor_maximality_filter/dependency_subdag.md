# Dependency sub-DAG

```text
unique RS interpolation + finite binomial inversion
  -> xr_window_divisor_maximality_filter [PROVED]
       +-> xr_band_maximal_window_divisor_count [CONDITIONAL]
       +-> xr_band_fullrank_window_divisor_count [TARGET]
       `-> xr_band_forced_commonroot_syzygy_count [TARGET]
```

The proved router is elementary and has no unproved DAG prerequisite. Its
three consumers still require a row-sharp bound on a signed support-moment
aggregate or an equivalent exact maximal census.
