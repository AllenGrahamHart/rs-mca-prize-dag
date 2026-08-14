# Cycle 311: MCA rank-11 relative core/ray payment (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_relative_core_interpolant_ray_payment` transfers the
first two spread-residual rungs to Cycle 310's arbitrary shortened row.

For the fixed `(H_C)` tuple, every coordinate error polynomial has slope
degree at most 31 and is nonzero because the residual maximal supports have
empty common intersection. Therefore

```text
core-interpolant slopes <= floor(31n'/m') <= 481,
extra slopes after the 32 anchors <=449.
```

For one fixed nonzero correction direction, clone classes of size at least
`K'` are global affine codeword graphs. Charging their number by the coarse
uniform bound `n'` costs `n'(n'-m'+1)`. After removing them, every rich
support contains a heterogeneous coordinate pair, and each pair supports at
most 31 correction parameters. Hence

```text
one ray <= n'(n'-m'+1)+31*C(n',2)
        <= 70227214729216,
core plus ray = 70227214729697 < B_*.
```

This avoids the deployed proof's nonportable `n=2K` assertions about two
large clone classes and a two-part support partition. It uses only RS
injectivity, root capacity, `n'<=n`, and invariant `n'-m'=R-d`.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RELATIVE_CORE_INTERPOLANT_RAY_PAYMENT_PASS
  core=481 ray=70227214729216 slack=274910500896665390 controls=6/6
RATE_HALF_MCA_RANK11_RELATIVE_CORE_INTERPOLANT_RAY_PAYMENT_AUDIT_PASS
  total=70227214729697 controls=5/5
```

The verifier caught and repaired an `819200` transcription offset in each of
the two summands; their accidentally unchanged total was never accepted as
sufficient evidence. No Modal computation was used.

```text
start:                   69de25652
DAG delta:               +1 PROVED relative core/ray payment,
                         +1 requirement edge, +1 evidence edge
critical status delta:   none
upstream terminal delta: H_C cannot live on its interpolant plus one ray
delta-star movement:     none
compute:                 constant-size exact local arithmetic only
next route action:       transfer proper-intersection and clone-tolerant
                         correction-space bounds to the shortened row
```
