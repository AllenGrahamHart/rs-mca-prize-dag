# Proof

The colored parent excludes the two 120-system missing-edge packets.  The
uncolored parent excludes the signed `DE` and `DF` packets of size 240 each
and the `EF` packet of size 120.  These five disjoint missing-record classes
partition the seven possible missing records, so

```text
120 + 120 + 240 + 240 + 120 = 840.
```

The full-system transport parent is an involution on all root signs, target
signs, missing records, and residual matchings.  It maps cell 3 to cell 6 and
preserves the `BC` sign.  Applying it to the complete cell-3 exclusion gives
all 840 cell-6 exclusions.  QED.
