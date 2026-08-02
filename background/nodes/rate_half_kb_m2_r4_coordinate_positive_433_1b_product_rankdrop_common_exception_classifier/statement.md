# KoalaBear m2 r4 positive 433-1b product-rank-drop common exception classifier

- **status:** PROVED
- **scope:** the product-row rank-drop branch in every common row of
  `433-1b -> O0a`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler`
- **consumer:** `rate_half_band_closure`

Use the five product rows and five sum rows of the parent compiler, and
write `P` for the `5 x 6` product block and `M` for the full `10 x 8`
common matrix.  Product-row rank drop is exactly

```text
rank(P) <= 4,                                      (KBP1BRD-1)
```

so it is cut out by all six maximal cofactors of `P`.  A genuine common
packet must also satisfy

```text
rank(M) <= 7,                                      (KBP1BRD-2)
```

which is cut out without a rank-chart assumption by all
`binom(10,8)=45` maximal minors of `M`.

For each of the fifteen role-matching cells and four source-root sign rows,
let `H` be the product of all source-label and target-record guards from the
parent compiler.  Over the deployed field `F_2130706433`, form the exact
localized ideal

```text
I = < six maximal cofactors of P,
      all 45 maximal minors of M,
      z H - 1 >.                                  (KBP1BRD-3)
```

All sixty standard-basis calculations complete.  For every root-sign row
in cells

```text
0, 1, 2, 3, 6,                                    (KBP1BRD-4)
```

the ideal is the unit ideal.  Hence those twenty common rows have no
product-rank-drop survivor.

Every row in the other ten cells is zero-dimensional.  In the fixed
degrevlex order `(z;t,r,c,b)`, their reduced standard-basis sizes are

```text
cells 4,5,7,8:  11,     cells 9,10,11: 21,
cells 12,13:    18,     cell 14:       15.        (KBP1BRD-5)
```

Thus the exceptional branch is empty in twenty rows and finite as a scheme
in the remaining forty.  The basis sizes are certificate metadata, not
geometric point counts.

This theorem does not classify those finite schemes, solve the principal
product-rank-five branch, append an outside row, close `433-1b -> O0a`, K3,
LIST, MCA, or either Prize result.

## Falsifier

A guarded rank-drop common packet in a cell from `(KBP1BRD-4)`, a
positive-dimensional guarded exceptional branch in any other cell, a
missing matching/root-sign row, or failure of the exact minor or
localization ledger.
