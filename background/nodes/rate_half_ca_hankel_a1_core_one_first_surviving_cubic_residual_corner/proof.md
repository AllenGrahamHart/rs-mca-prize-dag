# Proof

Put

```text
m=2^37,       e=floor(16m/13).
```

Exact division gives

```text
16m=13e+6.                                             (1)
```

Substitution into the core-one ledger yields

```text
Delta=4m-1-2e=211444543803=5q+3,
q=floor(Delta/5)=42288908760,                          (2)
ell_max=4e-4m-1=126866726279=e-q-3.                   (3)
```

The carrier-descent theorem requires every survivor to satisfy

```text
ell>=e-3-floor(Delta/5)=ell_max.                       (4)
```

The slope ledger gives `ell<=ell_max`, so equality holds. Therefore

```text
T=4e+1-ell=rho+2,                                     (5)
```

proving `(CRC2)`.

Survival of the strict carrier inequality also gives

```text
floor(p/5)+ell+3>=e.
```

Using `(3)` shows `floor(p/5)>=q`, hence

```text
p>=5q=Delta-3.                                        (6)
```

The local pole, omission, and Smith ledgers give

```text
p<=O<=sum_gamma c_gamma<=Delta.                       (7)
```

Equations `(6),(7)` prove `(CRC3)`. Since all differences in `(7)` are
nonnegative and their sum is `Delta-p<=3`, each individual difference is at
most three.

The general adjugate factorization identifies the pushed-forward pole
divisor with an effective subdivisor `P_p<=div(D)`. Its complementary factor
has degree

```text
Delta-p<=3,
```

which proves `(CRC4)`.

Finally, the slope ledger makes at least `T-Delta` supported fibres clean.
Using `(5)` and `Delta=d-2e=rho-1-2e` gives

```text
T-Delta=(rho+2)-(rho-1-2e)=2e+3,
```

and exact substitution gives `(CRC5)`. QED.
