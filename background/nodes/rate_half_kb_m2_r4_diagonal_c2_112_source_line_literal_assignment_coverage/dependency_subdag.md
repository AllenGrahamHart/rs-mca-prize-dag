# Dependency sub-DAG

```text
crosswalk + imports + ten moving cells ----------------+
complete fixed inversion transport --------------------+
all fixed R02 cells + all fixed cubic routes -----------+-> literal-assignment coverage (TARGET)
                                                         |
                                                         v
                                      complete source-line exclusion (CONDITIONAL)
```

The TARGET remains a logical leaf. Exact imported packets are evidence; no
unproved cell candidate is consumed as a theorem.
