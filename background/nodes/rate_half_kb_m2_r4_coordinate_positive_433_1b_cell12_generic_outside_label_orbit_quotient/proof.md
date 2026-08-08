# Proof

The atlas orders records as

```text
DE, DE, -DE, DF, sigma_o EF, BF, sigma_c CF.
```

The first two entries have identical products and squared sums, so their
exchange is an exact system automorphism.  The cited universal transport
swaps `D,E`, gauges both by `sigma_o`, and induces record permutation
`(3 4)` without changing the source role cell or target lane.

For a label `(xi,j)`, delete record `xi`, apply a record permutation to all
three edges of matching `j`, restore canonical residual order, and look up
the resulting matching index.  The deterministic router closes each seed
under permutations `(0 1)` and `(3 4)`.  It obtains 36 disjoint orbits with
size profile `1:3,2:15,4:18`; their sizes sum to 105 and their canonical
serialization has digest
`b5ec5e8418af3385dc83aeeb9aca9c8b851eae9e23794e6637f1b42a37576cb6`.
Thus one representative covers each orbit. QED.
