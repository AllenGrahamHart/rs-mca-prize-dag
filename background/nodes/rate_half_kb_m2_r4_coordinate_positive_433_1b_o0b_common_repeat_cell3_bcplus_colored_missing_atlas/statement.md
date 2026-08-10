# Repeated-BC cell-3 BC+ colored-missing atlas

- **status:** PROVED
- **scope:** missing `BE` and `CF` records on the cell-3 `BC+` torus, plus exact cell-6 transport

Let `A(x),B(x),beta(x)` be the direct rank-five common coefficient kernel,
let `x=-r^4` be the missing source label, and write

```text
am=A(x), bm=B(x), betam=beta(x).
```

If a colored target record joins a known nonzero coordinate `k` to an
unknown coordinate `y`, its missing product and squared-sum equations imply

```text
bm-k y am=0,
x betam^2-(k+y)^2 am^2=0.
```

Eliminating `y` gives the necessary common-only cut

```text
r^4 k^2 betam^2+(k^2 am+bm)^2=0.        (CM-1)
```

For `BE`, `k=b`; for `CF`, `k=u`. In every root-sign row, guarded standard
bases for the torus equation, `b u^3+1`, and `(CM-1)` are zero-dimensional.
Their deployed-field root ledgers are:

```text
missing  resultant degree  u roots  raw r lifts  guard boundary  live
BE       116               9        12           12              0
CF       124               11       16           12              4
```

The counts are independent of the four root-sign rows. Therefore no guarded
cell-3 `BC+` point can support missing `BE`. This excludes all
`4 root signs * 2 outside signs * 15 matchings = 120` such formal systems.
The exact cell transport sends cell-3 `BE` to cell-6 `CF`, so it excludes the
corresponding 120 cell-6 systems as well.

The four `CF` points per cell-3 root-sign row are only necessary-cut points,
not outside witnesses. Their residual matchings remain open, as do all other
missing records, `BC-`, split-BC lanes, the route, K3, and both Prize results.

## Falsifier

A missing deployed-field resultant root, an unlifted common `r` root, a
guarded `BE` point, an invalid missing-equation eliminant, or a failure of the
cell-3/cell-6 transport on the closed labels.
