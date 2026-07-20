# L1 affine split-pencil cross-determinant uniqueness

- **status:** PROVED
- **role:** pay the wide arbitrary-locator part of each affine syndrome
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use one cell of `l1_bounded_mark_affine_split_pencil_compiler`. Thus one
source chart, defect degree `d`, exact support pattern, and missing-equation
syndrome are fixed. Let `T_1,...,T_t` be the selected dense `ell`-point
petals, put

```text
S_i subset T_i,       V_i=T_i\S_i,
J=product_i L_(V_i),       v=deg J.                     (CD1)
```

For any two exact saturated monic points `(F_0,W_0),(F_1,W_1)` in this cell,
with

```text
deg F_j=d,       deg W_j<=d,       gcd(F_j,W_j)=1,     (CD2)
```

their cross determinant

```text
Delta=W_0F_1-W_1F_0                                  (CD3)
```

satisfies

```text
product_i L_(T_i) | J Delta,       deg(J Delta)<=2d+v. (CD4)
```

Consequently, if

```text
t ell>2d+v,                                             (CD5)
```

the cell contains at most one exact saturated monic point.

For the bounded-polarity L1 branch, `v<=p`. Hence every fixed support and
syndrome cell with

```text
t ell>2d+p                                              (CD6)
```

is a singleton. Combining the complementary inequality with the proved list
threshold lower pin gives the arbitrary-locator survivor window

```text
ceil((d-p+1)/ell)
 <=t_dense<=floor((2d+p)/ell).                         (CD7)
```

In strip notation `d=m ell+eta`, a particularly useful paid region is

```text
t_dense>=2m+1,       2eta+p<ell.                       (CD8)
```

For fixed `p<=P`, the support-pattern and syndrome compiler therefore gives a
polynomial per-source-chart count throughout `(CD6)`, uniformly in arbitrary
petal locators and without a common constant-shift hypothesis.

## Scope

This theorem does not count cells in the survivor window `(CD7)`, supply the
non-intrinsic source-chart census, or treat growing `p`. Its conclusion is
uniqueness inside one fixed affine syndrome, not emptiness of the support
profile.
