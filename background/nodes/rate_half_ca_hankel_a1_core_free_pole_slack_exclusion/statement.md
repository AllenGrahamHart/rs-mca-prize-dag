# `A=1` core-free pole-slack exclusion

- **status:** PROVED
- **closure:** adaptive pole interpolation and three-contact vanishing
- **consumer:** `rate_half_band_crossing_location`

Retain a failing core-free half-distance profile and write

```text
rho=4m,       T=4e-ell,       Delta=rho-e,
m+1<=e<=rho,  0<=O<=Delta.                            (A1P1)
```

Let `p<=O` be the actual colength of the pole-cancellation ideal `(H:G)` on
the kernel curve. Define

```text
alpha=2,  e<=rho/2-1;
alpha=1,  rho/2<=e<=rho-1;
alpha=0,  e=rho;
b=floor(p/(alpha+1)).                                 (A1P2)
```

If

```text
b+ell+3<e,                                             (A1P3)
```

then the profile is impossible. Thus every survivor satisfies

```text
p>=(alpha+1)(e-ell-3)                                (A1P4)
```

whenever the right side is positive.

At the first live degree `e=m+1`, necessarily `0<=ell<=2`, and every
survivor is confined to

```text
ell=0: p>=3m-6,       Delta-p<=5;
ell=1: p>=3m-9,       Delta-p<=8;
ell=2: p>=3m-12,      Delta-p<=11.                    (A1P5)
```

## Scope

This theorem narrows but does not close the core-free `A=1` branch. It does
not apply to fixed cores `s=1,2`.
