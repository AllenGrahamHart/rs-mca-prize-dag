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

## Round-32 addendum (2026-08-10, coordinator): the missing axiom was combinatorial after all

The round-32 rh_fr_algebraic pilot (coordinator-replayed,
exhaustive over all 32896 pair unions of this node's own blocks):
the fence's W is NOT any pair union of its blocks, and at EVERY
canonical W* = S_g u S_h the same set system satisfies (FR) with
max |S_gamma ^ W*| = 115 <= 2m = 128 (the 3m-3 = 189 violation
occurs at no pair-union W). The scope line's suggestion that a
positive (FR) needs f_gamma / the syndrome pencil / apolarity is
therefore true in letter but misleading in emphasis: the axiom the
list omits is "W = S_g u S_h for two of the blocks" — a set-system
axiom — under which |S_gamma ^ W*| <= 4rho - 2a* - 2o_gamma - o_g
- o_h is a two-line cardinality identity (FR-CANONICAL, proved,
needs no saturation). The fence remains PROVED and correct for
arbitrary a-sets W; the theorem it fences is the arbitrary-W form,
which is also REALIZABLY false at m = 3 (j >= 1 stratum, T = 3).
