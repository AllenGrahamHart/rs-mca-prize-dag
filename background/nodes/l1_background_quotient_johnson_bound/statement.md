# L1 background-quotient Johnson bound

- **status:** PROVED
- **role:** pay positive-Johnson cells in the derived background list
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart with

```text
N=k-1,       |B|=b=ell-g,
```

one defect degree `d`, and one exact labelled petal support `X` of size `h`.
Assume `h<=N` and put

```text
a=N-d,       s=h-d,       c=N-h=a-s,
u=ell-s.                                                  (BQ1)
```

If the derived-background Johnson denominator is positive,

```text
u^2-bc>0,                                                 (BQ2)
```

then the cell contains at most

```text
b(u-c)/(u^2-bc)                                          (BQ3)
```

compatible listed codewords. This is at most `n^2`.

For every fixed petal-polarity cap `p<=P`, the union of all cells satisfying
`(BQ2)` is polynomial per source chart. An explicit bound at the L1 cutoff is

```text
(P+1)n^(1/c_0+P+3).                                     (BQ4)
```

Consequently the bounded-polarity balanced tail may be restricted further to

```text
(ell-a+c)^2<=(ell-g)c,                                   (BQ5)
```

together with

```text
a^2/N<=c<=2a-ell-g.                                     (BQ6)
```

Strict positivity is load-bearing. The exact `F_17`, `ell=2` equality chart
from `l1_background_overlap_singleton_payment` has

```text
(b,u,c)=(1,1,1),       u^2-bc=0,
```

and two compatible contributors.

## Scope

This theorem is per source chart. It does not count the simultaneous
nonpositive region `(BQ5)--(BQ6)`, unbounded petal polarity, or
non-intrinsic first-match chart multiplicity.
