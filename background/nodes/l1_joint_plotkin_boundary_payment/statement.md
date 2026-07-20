# L1 joint Plotkin-boundary payment

- **status:** PROVED
- **role:** pay the full joint-Johnson equality regime
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart, defect degree `d`, and exact labelled
petal support `X` of size `h`. Put

```text
N=k-1,       |B|=b,       s=h-d,       u=ell-s,
r=2d-h=d-s,       V=N+b.                               (PK1)
```

Choose canonically `u` background agreements `R_P` for every contributor and
form the constant-weight subset

```text
A_P=D_P disjoint_union R_P subset C disjoint_union B.   (PK2)
```

Distinct contributors satisfy

```text
|A_P triangle A_Q|>=2ell.                               (PK3)
```

Consequently, whenever

```text
V=N+b<=4ell,                                             (PK4)
```

the exact support cell has at most

```text
2V<=2n                                                  (PK5)
```

contributors. For every fixed petal-polarity cap `p<=P`, the entire region
`(PK4)` is polynomial per source chart, with explicit bound

```text
2(P+1)n^(1/c_0+P+2).                                   (PK6)
```

Thus a bounded-polarity per-chart counterfamily must satisfy the strict gate

```text
N+b>4ell.                                               (PK7)
```

In an official rate-`1/r` source, `(PK7)` is equivalent to

```text
r b>(4(r-1)-M)ell+r,                                   (PK8)
```

or, with `g=ell-b`,

```text
(M-3(r-1)+1)ell>r(g+1).                                (PK9)
```

In particular `M>=3(r-1)`, and at the first scale `M=3(r-1)` one must have
`ell>r(g+1)`. The arithmetic equality family in the source-scale gate is
paid by `(PK5)` rather than left live.

## Scope

This is a per-source-chart fixed-support payment. It does not count the
strict region `(PK7)--(PK9)`, growing petal polarity, or non-intrinsic
first-match chart multiplicity.
