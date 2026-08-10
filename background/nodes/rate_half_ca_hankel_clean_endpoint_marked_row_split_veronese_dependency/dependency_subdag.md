# Dependency sub-DAG

```text
rate_half_ca_hankel_clean_endpoint_four_hankel_biisotropic_frame [PROVED]
rate_half_ca_hankel_clean_endpoint_picard_two_projection_socle_frame [PROVED]
rate_half_ca_hankel_clean_endpoint_irreducible_norm_corollary [PROVED]
                              |       |       |
                              +-------+-------+
                                      |
                                      v
rate_half_ca_hankel_clean_endpoint_marked_row_split_veronese_dependency [PROVED]
                                      |
                                      v evidence
rate_half_band_crossing_location [TARGET]
```

The frame supplies the two shifted/unshifted identities, the Picard frame
pins the marked point in domain coordinates, and the norm parent proves that
every remaining row locator is saturated and supported-split.
