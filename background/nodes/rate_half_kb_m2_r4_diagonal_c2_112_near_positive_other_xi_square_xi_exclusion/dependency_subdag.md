# Dependency sub-DAG

```text
source_line_internal_star_reconstruction --req--\
                                              > this exclusion --ev--> rate_half_band_closure
source_line_q_slice_resultant_gate -------req--/
```

The node consumes only the two printed parent interfaces. It contributes
scoped evidence to the target and does not become a required premise of it.
