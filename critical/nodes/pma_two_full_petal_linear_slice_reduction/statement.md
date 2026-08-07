# PMA two-full-petal linear-slice reduction

- **status:** PROVED
- **consumer:** `l1_fpc5_m4_t2_payment`

## Statement

Let `L_1,L_2` be pairwise-coprime monic polynomials of degree `ell` over a
field `K`, let `c_1!=c_2`, and put

```text
d=ell+s,       0<=s<ell.
```

Let `V_s` be the space of pairs `(F,W)` with `deg F,deg W<=d` and

```text
L_i | W-c_iF       for i=1,2.                       (TF1)
```

Then the map from pairs `deg A_i<=s` given by

```text
F=(L_1A_1-L_2A_2)/(c_2-c_1),
W=c_1F+L_1A_1                                      (TF2)
```

is a linear bijection onto `V_s`. Consequently

```text
dim_K V_s=2s+2.                                    (TF3)
```

The induced locator slice in `K[X]_<=d` has the same dimension and
codimension

```text
(d+1)-(2s+2)=ell-s-1.                              (TF4)
```

If `gcd(F,L_1L_2)=1`, then

```text
gcd(F,W)=1       iff       gcd(A_1,A_2)=1.          (TF5)
```

For a full-petal PMA contributor, `F` is a split locator on the source core,
so it is automatically disjoint from `L_1L_2`. Thus every two-touched-petal
FPC5 contributor injects into the primitive cofactor-pair locus for which
(TF2) is a monic degree-`d` polynomial split on the core.

This is an exact description of the two petal equations, not of the entire
fixed PMA cell. If `R_P` is the exact background-agreement set, the full cell
also imposes

```text
W(x)=0       for x in R_P,
```

as well as exact nonagreement and first-owner guards. Those conditions can
only shrink the slice, but must be retained before calling a contributor
description exact.

## Scope

This is a petal-equation normal-form theorem, not a split-divisor count or a
complete PMA-cell parametrization. At `s=ell-1` the unguarded locator slice is
the full degree-`d` space, so petal-equation codimension alone cannot pay that
formal endpoint. Official source arithmetic and the background-root guard can
remove or sharpen it.
