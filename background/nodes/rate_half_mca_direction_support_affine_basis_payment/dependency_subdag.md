# Dependency sub-DAG

```text
codeword-direction gauge rank router [PROVED] --+
support-wise affine-span compiler [PROVED] ------+--> direction-support affine-basis payment [PROVED]
                                                             |
                                                             +--ev--> rate_half_band_crossing_location
```

The gauge identifies a support of size at most `R`.  The incidence compiler
supplies the basis lower bound and endpoint envelope; this node removes all
candidate bases supported wholly outside that direction support.
