# L1 joint core/background Johnson bound

- **status:** PROVED
- **role:** couple defect and background intersections in one degree budget
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart, one defect degree `d`, and one exact
labelled petal support `X` of size `h`. Put

```text
N=k-1,       |B|=b=ell-g,       s=h-d,       u=ell-s,
r=2d-h=d-s.                                             (CJ1)
```

For every compatible contributor choose canonically `u` of its background
agreement points. If two contributors have defect sets `D_1,D_2` and chosen
background sets `R_1,R_2`, then

```text
|D_1 intersect D_2|+|R_1 intersect R_2|<=r.             (CJ2)
```

If `r<0`, the cell is a singleton. If `r>=0` and

```text
J=b d^2+N u^2-N b r>0,                                  (CJ3)
```

then the number `m` of contributors satisfies

```text
m<=N b ell/J<=n^3.                                      (CJ4)
```

For every fixed petal-polarity cap `p<=P`, the union of all cells satisfying
`(CJ3)` is polynomial per source chart, with explicit bound

```text
(P+1)n^(1/c_0+P+4).                                    (CJ5)
```

In the tail coordinates

```text
a=N-d,       c=N-h,       u=ell-a+c,
```

the denominator identity is

```text
J=b a^2+N(ell-a+c)^2-N b c.                             (CJ6)
```

Thus a bounded-polarity per-chart counterfamily may be restricted to

```text
b a^2+N(ell-a+c)^2<=N b c.                              (CJ7)
```

For `b>0`, `(CJ7)` implies both separate nonpositive-Johnson inequalities.
The exact `F_17` chart attains `(CJ4)` with `m=2` and `J=4`. The exact
`F_23` nonsplit chart has `m=2` and `J=0`, so strict positivity is
load-bearing.

## Scope

This is a per-source-chart payment. It does not count `(CJ7)`, unbounded
petal polarity, or non-intrinsic first-match chart multiplicity. When `b=0`,
`(CJ7)` is vacuous and the separate core-defect Johnson condition remains in
force.
