# Dependency sub-DAG

```text
crosswalk + imports + ten moving cells ----------------+
complete fixed inversion transport --------------------+
all fixed R02 cells + all fixed cubic routes -----------+-> literal-assignment coverage (TARGET)
all fixed R20 complete-cell exclusions ----------------+
                                                         |
                                                         v
                                      complete source-line exclusion (CONDITIONAL)
```

The TARGET remains a logical leaf. Its aligned-positive residual is exactly
the moving `M01/M02-R11` pair. Exact imported packets are evidence; no
unproved cell candidate is consumed as a theorem.
