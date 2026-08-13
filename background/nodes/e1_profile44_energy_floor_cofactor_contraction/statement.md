# E1 profile-(4,4) energy-floor cofactor contraction

- **status:** PROVED
- **closure:** analytic product majorant plus exact integer threshold
- **scope:** binding prize rate-`1/8` row, profile `(4,4,S=20)`

Every official profile-`(4,4)` collision has cofactor

```text
m<=932364.                                             (P44-C1)
```

Consequently, the former `1133`-cofactor local-norm frontier contracts to
exactly `657` values. Their counts by local valuation are

```text
mu:       1   2  3  4  5  6  8  9 10 12 16 17 18
count:  308 167 88 44 24 12  4  3  3  1  1  1  1.
```

In particular, the pure cofactor `2^20=1048576` is excluded. The remaining
thirteen pure powers still exceed the seven-orbit allowance, so this is a
strict frontier contraction rather than a profile payment.

## Falsifier

An official collision with `m>=932365`, or an exact replay leaving a
survivor count other than `657`.
