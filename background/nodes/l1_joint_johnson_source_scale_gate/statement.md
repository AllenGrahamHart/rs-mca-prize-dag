# L1 joint-Johnson source-scale gate

- **status:** PROVED
- **role:** remove bounded-polarity mixed cells on small official source scales
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use one maximal-sunflower source chart in an official rate-`1/r` row,

```text
n=rk,       r in {2,4,8,16},
N=k-1,      (r-1)k+1=Mell+b,      0<=b<ell.             (SG1)
```

For every fixed petal-polarity cap `p<=P`, all exact mixed/partial support
cells are polynomial per source chart whenever

```text
M<3(r-1).                                               (SG2)
```

An explicit bound at the L1 lower cutoff is

```text
(P+1)n^(1/c_0+P+4).                                    (SG3)
```

Equivalently, a bounded-polarity per-chart counterfamily must satisfy

```text
N+b>=4ell,       N>=3ell+1,       M>=3(r-1).             (SG4)
```

Thus the first potentially live source-petal counts are

```text
rate 1/2:   M>=3,
rate 1/4:   M>=9,
rate 1/8:   M>=21,
rate 1/16:  M>=45.                                     (SG5)
```

The constant `3(r-1)` is sharp from source arithmetic alone. For every
official `r`, the parameters

```text
ell=2r,       b=2r-1,       k=6r+2,       M=3(r-1)      (SG6)
```

satisfy `(SG1)` and `N+b=4ell`. This is not a contributor-existence claim.

## Scope

The theorem pays bounded petal polarity only. It does not count growing
petal polarity on the excluded source scales, count the joint sub-Johnson
tail on scales satisfying `(SG4)`, or address non-intrinsic first-match
chart multiplicity.
