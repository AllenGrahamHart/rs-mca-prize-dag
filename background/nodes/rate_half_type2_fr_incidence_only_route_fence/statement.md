# Rate-half type-2 FR incidence-only route fence

- **status:** PROVED
- **role:** separate the support-incidence content of `(FR)` from its
  remaining Hankel/GRS algebra
- **consumer:** `rate_half_band_crossing_location`

The numerical endpoint axioms used in the Round-31 `(NEWCAP)` argument do
not imply the proposed max-intersection bound `(FR)`.

There is an explicit set system at the power-of-two scale `m=64` with

```text
N=16m=1024,       rho=4m-1=255,       T=rho+2=257,
a=7m-1=447.
```

It consists of `T` blocks `S_gamma` and one distinguished `a`-set `W` such
that

```text
|S_gamma|=rho,
sum_x (m-d_x)=1,
|S_gamma union S_gamma'|>=a              for gamma!=gamma',
|S_gamma \ W|>=m+2=66                    for every gamma,
```

but

```text
max_gamma |S_gamma intersect W|=3m-3=189>2m=128.
```

The maximum exceeds `2m` by `m-3=61`, so this is not a one-point
small-scale anomaly. Consequently no proof using only these cardinalities,
the exact saturation deficit, pairwise union `(OV)`, and the individual MDS
distance spend `(C2)` can establish `|S_gamma intersect W|<=2m`.

This theorem does **not** construct a strict-`A=3` Hankel pencil and does
not refute `(FR)` for realizable pencils. Any positive `(FR)` theorem must
use information absent from the set-system axioms, such as the generalized
locator polynomials `f_gamma`, the common syndrome pencil, or the apolar
Hankel equations.
