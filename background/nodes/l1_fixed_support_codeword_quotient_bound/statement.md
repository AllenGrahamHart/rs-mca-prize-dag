# L1 fixed-support codeword quotient bound

- **status:** PROVED
- **role:** pay bounded petal-support codimension without split descent
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one received word, one maximal-sunflower source chart with core size

```text
N=k-1,
```

and one exact labelled petal-support pattern `X` of size `h`. Let `Z_X` be
the compatible listed codewords `P` of degree at most `N`. If `Z_X` is
nonempty and `P_0 in Z_X`, then

```text
Psi:Z_X -> F_q[X]_(<=N-h),
Psi(P)=(P-P_0)/L_X                                      (CQ1)
```

is well defined and injective when `h<=N`. If `h>N`, then `|Z_X|<=1`.
Consequently

```text
|Z_X|<=q^max(0,N-h+1).                                  (CQ2)
```

For fixed `P_0,E>=0`, the full per-source-chart class

```text
p<=P_0,       N-h<=E                                    (CQ3)
```

is polynomial at the L1 cutoff. Under `q<=n^gamma`, an explicit bound is

```text
(P_0+1)n^(1/c_0+P_0+gamma(E+1)).                        (CQ4)
```

Inside the sub-Johnson tail put

```text
a=N-d,       s=h-d.
```

Then `N-h=a-s`. Hence a bounded-polarity per-chart counterfamily may be
restricted further to

```text
a-s=N-h -> infinity.                                   (CQ5)
```

## Scope

This is a per-source-chart support-codimension payment. It does not sum
non-intrinsic first-match charts, handle unbounded petal polarity, or count
the growing-codimension tail. The quotient in `(CQ1)` is arbitrary; no
base-field splitting claim is made.
