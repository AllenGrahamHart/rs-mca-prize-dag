# Intrinsic dyadic scales have a geometric quotient-row ledger

- **status:** PROVED
- **consumer:** `petal_small_scale_staircase_census`

Let `n=2^s` and `B>0`. Suppose a family is partitioned by its unique
intrinsic dyadic scale `M=2^j>=2`, and the scale-`M` class injects into a
primitive quotient-row family of size at most

```text
C (n/M)^B.
```

Then its aggregate size is strictly less than

```text
C n^B/(2^B-1).
```

For the official petal exponent `B=6`, the aggregate is less than
`C n^6/63`. If the current-row primitive class is also at most `C n^6`, the
combined primitive-plus-descended contribution is less than
`(64/63)C n^6`; therefore `C<=63/64` is sufficient for an `n^6` allocation.

