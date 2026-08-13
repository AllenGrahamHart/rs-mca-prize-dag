# Cycle 250: rate-half shape-A residual four-cycle rigidity (2026-08-13)

The global genus floor from Cycle 249 prompted a search for a source/Pade
genus upper bound. The split biform has full rectangular Newton support, so
no sparse-Newton upper follows. The exact locator/biform four-core is more
structured, but it does not produce a quartic pencil.

On the normalized source-locator curve, let `B` be the degree-two
double-root correction divisor. The root and contact normal forms are

```text
div(X-x_*)=R_*+3B,
div(s_F)=R_*+2B.
```

At every normalized point `b` of `B`, the Pade contact order is `2m_b`.
Restricting the Pade syzygy to `Q=0` shows that `G` has the same order.
Factorwise Bezout saturation and the exact projective four-core then give

```text
Z_4=2B.
```

The residual divisor is rigid. Starting from

```text
pi_*O_C(B)=O + O(1-d)^2 + O(-d)^(e-3),
d=3e-2,
```

the second positive modification is killed by `X-x_*`. Its principal-part
directions vanish on the nonempty residual fibre `R_*`, hence miss the
constant line. After removing their constant components by a bundle
automorphism, the modified bundle embeds in

```text
O + O(2-d)^2 + O(1-d)^(e-3).
```

Every nonconstant summand remains negative, proving

```text
h^0(C,O_C(2B))=1.
```

This avoids the smoothness/generic-gonality shortcut forbidden by the
existing two-point audit. It also decides the route: the four-core can close
shape A only if the source constructs a genuinely second section in this
same line bundle. Merely interpreting the four residual units as a quartic
pencil is invalid.

```text
start:                   189914339
canonical prize:         fdfb20a42 (clean; unchanged)
result:                  PROVED Z_4=2B and h^0(O_C(2B))=1
DAG delta:               +1 PROVED node, +5 req edges, +1 ev edge
critical status delta:   none; rate_half_band_crossing_location remains open
critical orbit delta:    none; 167 PROVED / 37 CONDITIONAL / 27 TARGET
upstream lane:           PR #1161 is the selected export target
delta-star movement:     none
compute:                 constant-space local arithmetic only; no Modal spend
next route action:       construct a second residual source section, or
                         leave the rigid four-core route
```
