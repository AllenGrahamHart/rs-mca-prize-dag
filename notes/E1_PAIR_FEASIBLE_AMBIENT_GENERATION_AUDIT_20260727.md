# E1 pair-feasible ambient-generation audit

Date: 2026-07-27.

## Finding

The exact E1 compiler splits on the size `b=|F_p(Q)|` of the quotient-
generated field. On the branch where its pair-loss currency is feasible,
ambient generation is forced rather than assumed.

If `F_p(Q)` is proper in `F_q`, finite-field tower structure gives

```text
b^2<=q<2^256,
b<2^128.
```

The six pair-feasibility thresholds have bit lengths

```text
188,134,170,188,134,170.
```

Hence no proper subfield reaches the pair target.

## Route impact

The open pointwise collision theorem can now be stated entirely in the
ambient field. Extension transfer and base-field normalization remain
important only below `b_pair_min`, where the pair compiler is unavailable
anyway.

This is not a collision bound and pays no unsafe row. It removes one logical
axis before the exact norm-divisor/kernel attack. No Modal computation was
used.
