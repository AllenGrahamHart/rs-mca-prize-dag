# Proof

## Realizable energy-five spectra

For integer autocorrelations, the only partitions of

```text
E=sum_(d=1)^63 A_d^2=5
```

are

```text
1+1+1+1+1,                 4+1.                       (1)
```

Modulo two, the support of the odd `A_d` is exactly the positive-half folded
lag mask of the four singleton positions. Thus the first branch of (1)
requires a realizable weight-five mask; the second requires a realizable
weight-one mask, one separately chosen magnitude-two lag, and independent
signs.

Translation invariance fixes one singleton at zero. Exhausting the remaining
`C(127,3)=333375` supports gives `1785` distinct weight-five masks and `31`
distinct weight-one masks. Hence the signed spectrum count is exactly

```text
1785*32 + 31*(63-1)*4=64808.                          (2)
```

## Exact norm test

For a spectrum `A`, put `D=max supp(A)` and

```text
H_A(X)=20X^D+sum_d A_d(X^(D+d)+X^(D-d)).              (3)
```

As in the energy-at-most-four parent,

```text
|Res(X^128+1,H_A)|=|Norm(F(zeta_256))|^2.             (4)
```

Both pinned implementations enumerate all spectra in (2), compute the exact
FLINT resultant in (4), verify it is a square, and put `R` equal to its
positive square root. For the exact official prime interval
`[p_min,p_max]`, they compute

```text
m_min=ceil(R/p_max),       m_max=floor(R/p_min).        (5)
```

The interval in (5) has width at most one. The primary census has no exact
divisor hit. The independently ordered replay is stronger: across all
`64808` spectra, (5) contains no integer at all. Thus no energy-five norm
can equal `pm` on the official row.

The parent already excludes energies at most four, proving `(P44-E6)`. The
energy-adaptive product threshold at `V=12` gives `(P44-M6)`. Intersecting
the exact local cofactor list with `m<=853574` leaves `608` values. QED.
