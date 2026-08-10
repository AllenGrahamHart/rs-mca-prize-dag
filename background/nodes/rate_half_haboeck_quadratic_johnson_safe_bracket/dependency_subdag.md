# Dependency sub-DAG

```text
haboeck_quadratic_johnson_mca_import [PROVED]
  --req--> rate_half_haboeck_quadratic_johnson_safe_bracket [PROVED]
              --ev--> rate_half_band_crossing_location [TARGET]
```

The incoming theorem supplies the MCA numerator bound. This node owns the
rate convention, integer budget, support ceiling, prize-cap cutoff, and
razor-row bracket. The outgoing edge remains evidence because no unsafe
predecessor is proved.
