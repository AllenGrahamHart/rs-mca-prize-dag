# Cycle 56: rate-half deficiency-clone kernel (2026-08-10)

## Posedness repair

Audit of Round 32's proposed bivariate route found that the printed
one-scalar coordinate formula applies only at parameter-saturated points.
At a point with deficit `Delta_x=m-d_x`, factorization gives

```text
Q_Y(x)=product_(gamma in A_x)(Y-gamma) R_x(Y),
deg R_x<=Delta_x.
```

The quotient `R_x` contributes `Delta_x+1` coefficients, rather than one.
This is not optional bookkeeping: omitting these variables can create a
false full-rank conclusion.

## New proved leaf

`rate_half_bivariate_deficiency_clone_kernel_reduction` extracts the exact
coefficient matrix from the apolar moment identity. Its rows are indexed by
the `m+2` parameter coefficients and `4m+1` parity moments; its columns are
the quotient coefficients `(x,t)`. Every putative endpoint failure supplies
a blockwise-nonzero kernel vector. The exact column count is

```text
U_W=|W|+Delta_W<=|W|+1+O<=|W|+m.
```

For the clean `O=0` frontier, `U_W` is exactly `|W|` or `|W|+1` depending on
whether the unique deficient point lies outside or inside `W`.

Two independent polynomial-expansion replays certify the matrix formula and
column accounting. This preserves the bivariate route but sharpens its next
obligation: prove structural rank on the bad incidence patterns. The raw
row count alone is explicitly fenced. No critical status changes.
