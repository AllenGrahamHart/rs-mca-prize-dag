# Proof

In every target-sign lane the seven outside product records, in compiler
order, are

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf.
```

Their associated squared-sum rows begin

```text
(d+e)^2, (d+e)^2, (d-e)^2.
```

Thus the transposition of positions `0` and `1` fixes both complete
record rows pointwise.  It also fixes the target representatives
`(1,b,c,d,e,f)`, so all nonzero and pairwise-not-opposite guards are
unchanged.  The source role cell and its common four-basis presentation are
also fixed because the two outside-copy labels do not occur in the common
equations.

Canonical `pairing=0` pairs adjacent positions in the ordered six-record
residual.  Deleting position `0` gives

```text
de, -de, df, sigma_o ef, bf, sigma_c cf,
```

and deleting position `1` gives the same list.  In both cases the three
paired equations therefore use

```text
(de,-de), (df,sigma_o ef), (bf,sigma_c cf).
```

The missing product and missing squared-sum equations are identical because
positions `0` and `1` both carry `de` and `(d+e)^2`.  Common-curve
equations, source signs, target signs, and localization guards do not refer
to the label of a parallel copy.  Hence the complete guarded polynomial
systems for `xi=0,pairing=0` and `xi=1,pairing=0` are identical after
the displayed transposition.

The first system has no guarded solution by `(KBP1B4-X0P0-1)`.  Therefore
the second has none for every source-sign pair and target-sign lane. QED.
