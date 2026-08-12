# Dependency sub-DAG

```text
direction-support affine-basis payment [PROVED] --+
support-wise affine-span compiler [PROVED] --------+--> common-zero envelope [PROVED]
                                                           |
                                                           +--ev--> rate_half_band_crossing_location
```

The support-basis node supplies the subtracted numerator.  This node retains
and optimizes the zero-normal parameter instead of separating its support
factor from the affine-incidence envelope.
