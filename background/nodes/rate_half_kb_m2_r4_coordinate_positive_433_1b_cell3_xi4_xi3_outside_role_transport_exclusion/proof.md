# Proof

Fix a target lane `(sigma_c,sigma_o)`.  In canonical order the seven outside
product records and their signed squared sums are

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf,
(d+e)^2, (d+e)^2, (d-e)^2, (d+f)^2,
(e+sigma_o f)^2, (b+f)^2, (c+sigma_c f)^2.       (1)
```

Apply `(d,e,f) -> (D,E,F)=(sigma_o e,sigma_o d,f)`.  In the transformed
canonical atlas,

```text
DE=de,                 (D+E)^2=(d+e)^2,
-DE=-de,               (D-E)^2=(d-e)^2,
DF=sigma_o ef,         (D+F)^2=(e+sigma_o f)^2,
sigma_o EF=df,         (E+sigma_o F)^2=(d+f)^2.  (2)
```

The `bf` and `sigma_c cf` rows are fixed.  Therefore the full seven-row
product/squared-sum atlas is fixed except that positions 3 and 4 are
transposed.  In particular, the original missing `xi=4` row becomes the
transformed missing `xi=3` row.  After deletion, the compact residual lists
are identical in the same order:

```text
de, de, -de, df, bf, sigma_c cf                  (xi=4 original),
DE, DE, -DE, sigma_o EF, bF, sigma_c cF          (xi=3 transformed).
```

Equations `(2)` identify these lists term by term.  Hence every one of the
fifteen canonical perfect matchings retains its index and all three paired
Vieta equations.  The missing-product and missing-squared-sum equations also
agree.

The transformation permutes `d,e` and multiplies both by the unit
`sigma_o`.  It is an involution and preserves nonzero coordinates and every
condition `x != +/- y` among `(1,b,c,d,e,f)`.  On active edge signs it is the
swap `D <-> E` followed by the vertex gauge that multiplies both new outside
vertices by `sigma_o`.  Thus the canonical signs return to

```text
DE=+1,       DF=+1,       EF=sigma_o,
```

while the common signs and `sigma_c` are fixed.  Both cycle invariants, and
therefore the target lane, are unchanged.

Finally, source role cell 3 is the common assignment

```text
singleton AB;       pairs (LA,AC), (BC+,BC-).
```

The outside `D,E` operation does not act on these five common roles, so this
cell is fixed.  By contrast, exchanging common targets `B,C` swaps roles
`AB,AC` and sends this assignment to cell 6; this proves that the present
transport is not the previously rejected shortcut.

The positive complete-fiber Vieta equations depend on an outside row only
through its product and signed squared-sum records.  Equations `(1)--(2)`
therefore give a bijection from every guarded `xi=4` system to the
corresponding guarded `xi=3` system.  The six proved `xi=3` theorems partition
matching indices `0,...,14`, so every transported system is empty.  There are
`4*4*15=240` such raw cases. QED.
