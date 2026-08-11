# Cycle 132: rate-half quadratic strict-boundary dual biform (2026-08-11)

## Cycle pins

```text
starting source:  1c967ff948037490f8e7903aa45d168e63ad843f
canonical prize:  3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:    93fba1be3f3299b0ba4708d88715377bbb656e45
compute:          finite-field audit at q=101; exact integer replay
critical open:    28
```

## Two-center split biform

Divide each source-locator row by the two endpoint parameter factors. The
resulting row has parameter degree at most `e-1` and satisfies the full
Hankel moment system on the `3p-1` noncore union points. Dual-GRS
interpolation therefore produces a unique biform

```text
G(t,X),        bidegree exactly (e-1,p-2).
```

At least `2p+r_A` fixed-domain rows split into their `e-1` distinct
off-line supported slopes. At least `(e+15)/2+r_A` clean fixed-parameter
fibers split into their `p-2` inside-support points and equal the monic
inside locator up to scalar. The official unconditional profile is

```text
bidegree:           (183251937962,274877906942)
split domain rows:  >=549755813888
clean fibers:       >=91625968989.
```

## Burn-down

```text
result:                  PROVED strict-boundary dual-MDS split biform
DAG delta:               +1 PROVED
critical status delta:   none
terminal delta:          strict branch reduced to a named split census
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The remaining question is whether the extremal `(e-2,p-3)` and strict
`(e-1,p-2)` split profiles are impossible from degree and incidence alone,
or require the extra marked-Hankel/contact-section coupling.
