# Cycle 185: rate-half `A=1` collision companion norm gate (2026-08-12)

The factorwise four-shape theorem leaves only `(2,3)` and `(4,6)` ordinary
companions. For either factor `Q`, take its product norm over all `3e`
off-line supported slopes. Exact simple roots on every classified row give

```text
product_delta Q(delta,X)=L_U0(X)^m S_Q(X),
deg S_Q<=7m/2,       gcd(S_Q,L_U0)=1.
```

The factorwise padding ledger forces the heavy-row divisor:

```text
(X-x_*)^(m/2) divides S_Q.
```

After removing that factor, the companion is governed by one polynomial of
degree at most six or twelve. Its values on `U_0` are explicit products of
incident tangents and nonincident evaluations, so the gate is globally and
uniquely reconstructible. Its value at `x_*` remains open: local curve
transversality does not imply vertical simplicity.

```text
start:                   01298a193
result:                  NARROWED, new PROVED supporting node
DAG delta:               +1 PROVED node, +3 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: candidate extension to Lane-T PR #1161
delta-star movement:     none
compute:                 exact arithmetic replay only; no Modal spend
next route action:       couple E_Q to correction/source values
```
