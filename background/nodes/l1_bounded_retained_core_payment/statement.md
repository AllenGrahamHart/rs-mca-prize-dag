# L1 bounded retained-core payment

- **status:** PROVED
- **role:** remove bounded retained-core size from the mixed-petal tail
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart with ordered core `C`,
`N=|C|=k-1`, and `M` petals of size `ell`. For an exact non-planted pair put

```text
d=|D|,       D subset C,
a=N-d=|C\D|,
p=sum_i min(|S_i|,ell-|S_i|).                         (RC1)
```

For every fixed `A,P>=0`, the full per-source-chart class

```text
a<=A,       p<=P                                      (RC2)
```

is polynomial. At the L1 cutoff `2^M<=n^(1/c_0)`, an explicit bound is

```text
(A+1)(P+1)n^(1/c_0+A+P).                              (RC3)
```

Consequently, a bounded-polarity per-chart counterfamily in the sub-Johnson
tail must have retained-core size `a=N-d` escape every fixed upper bound.
Writing the chart background gap as `g=ell-b`, the existing tail inequality
`d^2<=N(d-g)` is equivalently

```text
a(N-a)>=Ng.                                           (RC4)
```

## Scope

This is an ambient per-chart payment. It does not control growing retained
core, unbounded petal polarity, or non-intrinsic first-match chart supply.
