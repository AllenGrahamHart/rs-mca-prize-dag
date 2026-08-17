# Proof

The common cell-11 records use only `A,B,C` and are independent of the
outside endpoint `d`. On the seven outside records, direct substitution gives

```text
(BE,CF,DE+,DE-,DF+,DF-,EF)
   -> (BE,CF,DE-,DE+,DF-,DF+,EF).
```

The same permutation holds for both the products and squared sums. Removing
any one record, transporting the three pairs of a residual perfect matching,
and reindexing gives an involution of all `7*15=105` labels. Its exact orbit
census is nine fixed labels and 48 pairs. In particular, every missing-`DE-`
label is paired with a missing-`DE+` label and every missing-`DF-` label with
a missing-`DF+` label. Since the common packet is fixed, emptiness transports
on every cell-11 source row. QED.
