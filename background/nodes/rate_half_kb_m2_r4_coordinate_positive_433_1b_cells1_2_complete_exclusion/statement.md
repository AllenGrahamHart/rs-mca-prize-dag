# KoalaBear m2 r4 positive 433-1b cells 1-2 complete exclusion

- **status:** PROVED
- **scope:** role cells `1` and `2` of deployed positive `433-1b -> O0a`
- **dependencies:** the positive common-minor compiler, product-rank-drop
  classifier and complete exclusion, signed atlas, complete-fiber Vieta
  compiler, and order-two source-facet signature
- **consumer:** `rate_half_band_closure`

The two role shapes are

```text
cell 1: singleton LA; pairs (AB,BC+), (AC,BC-),
cell 2: singleton LA; pairs (AB,BC-), (AC,BC+).  (KBP1B12-1)
```

The global product-rank-drop dependency removes `rank(P)<=4`.  On product
rank five, at least one of the six maximal cofactors of the `5 x 6` product
block is nonzero.  For each cell, four source-root sign rows, and six
cofactor charts, the six exact common-minor equations are localized by all
common guards and the selected cofactor.

All

```text
2 cells * 4 source signs * 6 charts = 48          (KBP1B12-2)
```

localized ideals complete over `F_2130706433` with dimension `-1`, basis
size one, and basis `1`.  Hence the principal product-rank-five common
branch is empty in both cells.  Together with the rank-drop dependency,
the complete deployed route is empty in cells `1` and `2`.

This theorem does not close any principal cell among `3..14`, all of
`433-1b -> O0a`, positive coordinate parity, K3, LIST, MCA, or either Prize
result.

## Falsifier

A missing cell/sign/chart row, a nonunit localized ideal, an invalid product
cofactor cover, or a common guard that excludes an admissible packet.
