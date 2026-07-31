# Dependency sub-DAG

```text
first all-row S2 exclusion --+
all-row common product data -+--> S2 forced-EF guarded exclusion
```

The exclusion supplies product-level evidence to `rate_half_band_closure`.
