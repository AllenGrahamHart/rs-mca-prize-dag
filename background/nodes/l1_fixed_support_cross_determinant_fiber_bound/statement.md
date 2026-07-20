# L1 fixed-support cross-determinant fiber bound

- **status:** PROVED
- **role:** count bounded cross-slack arbitrary-locator cells
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one L1 source chart, one defect degree `d`, and one exact petal-support
pattern. Let `S_1,...,S_t` be the selected dense supports inside pairwise
disjoint `ell`-point petals and put

```text
v=sum_i (ell-|S_i|),
S=product_i L_(S_i),
r_cross=2d+v-t ell=2d-deg S.                           (FB1)
```

Let `Z` be the set of exact saturated pairs compatible with this pattern:

```text
deg F=d,       F monic,
deg W<=d,      gcd(F,W)=1,
W(x)=c_iF(x)   for x in S_i.                           (FB2)
```

Additional fixed sparse-petal or background equations may be imposed. Then

```text
|Z|<=q^max(0,r_cross+1).                               (FB3)
```

More precisely, if `Z` is nonempty and `(F_0,W_0) in Z` is fixed, the map

```text
Phi:Z -> K[X]_(<=r_cross),
Phi(F,W)=(W_0F-WF_0)/S                                 (FB4)
```

is well defined and injective when `r_cross>=0`. When `r_cross<0`, every
cross determinant is zero and `|Z|<=1`, matching `(FB3)`.

At the L1 cutoff, fix `P,E>=0`. The complete per-source-chart class

```text
p<=P,       r_cross<=E                                 (FB5)
```

is polynomial, uniformly in arbitrary petal locators and all
missing-equation syndromes. An explicit bound after summing the at most `n`
defect degrees is

```text
(P+1)n^(1+1/c_0+P) q^(E+1)
 <=(P+1)n^(1+1/c_0+P+gamma(E+1))                       (FB6)
```

under `M<=log_2(n)/c_0` and `q<=n^gamma`.

Consequently, a bounded-polarity super-polynomial family inside one source
chart must have

```text
r_cross=2d+v-t_dense ell
```

escape every fixed upper bound, in addition to lying in the survivor width
window from `l1_affine_split_pencil_cross_determinant_uniqueness`.

## Scope

This theorem is per source chart. It does not bound the unbounded-cross-slack
window, non-intrinsic first-match chart multiplicity, or growing petal
polarity. It counts exact pairs, not ambient coefficient vectors.
