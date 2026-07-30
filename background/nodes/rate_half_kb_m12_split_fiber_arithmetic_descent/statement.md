# KoalaBear m12 split-fiber arithmetic descent

- **status:** PROVED
- **scope:** six geometric outer families at inner degree twelve
- **dependency:** `rate_half_kb_m12_outer_normal_form_compiler`
- **consumer:** `rate_half_band_closure`

The outer quintic `F` is defined over
`K=F_(2130706433^6)` and has a completely split unramified zero fiber. The
Frobenius at that rational fiber is the identity permutation. Hence the
arithmetic monodromy quotient has trivial Frobenius generator and

```text
G_arithmetic=G_geometric.                            (KBA-1)
```

Consequently each geometric outer self-correspondence component is defined
over `K`. Moreover the following rigid `r=4` forms admit affine source and
target normalizations over `K`, not only over the algebraic closure:

```text
A5: (3),(2,2)       x^3(12x^2-15(1+t)x+20t),
                     3t^2+4t+3=0
S5: (2),(3,2)       x^3(x-1)^2
S5: (2),(4)         x^4(5-4x).                      (KBA-2)
```

For the first row, the branch types distinguish both branch values and the
index-three point. The two index-two points split over `K`: the normalized
ratio satisfies the displayed quadratic, whose discriminant `-20` is a
square in the even-degree field `K`; a nonsplit pair would send the ratio to
its inverse, forcing `t=t^(-1)`, which neither quadratic root satisfies.

The exact unresolved twist list is now only:

```text
D5 Dickson;
A5 finite profile (3),(3);
S5 one-parameter profile (2),(2),(2,2).              (KBA-3)
```

This does not delete any family, classify the three twists, close `m=12`,
construct an owner, move the ledger, close `u=2`, establish cap `68`, or
close the KoalaBear row.

## Falsifier

A split unramified `K`-fiber with nontrivial arithmetic constant quotient,
failure of one of the three normalizations in `(KBA-2)` to descend to `K`,
or a missing family in `(KBA-3)`.
