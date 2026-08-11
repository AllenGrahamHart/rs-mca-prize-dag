# Dependency sub-DAG

```text
rate_half_ca_hankel_clean_endpoint_two_axis_resultant_picard_pin [PROVED]
rate_half_ca_hankel_clean_endpoint_picard_residual_evaluation_direction [PROVED]
                                  |        |
                                  +--------+
                                      |
                                      v
rate_half_ca_hankel_clean_endpoint_picard_two_projection_socle_frame [PROVED]
                                      |
                                      v evidence
rate_half_band_crossing_location [TARGET]
```

The first parent fixes the marked point in both coordinates. The second
parent supplies the local-socle calculation; this node applies it to the
reciprocal finite projection.
