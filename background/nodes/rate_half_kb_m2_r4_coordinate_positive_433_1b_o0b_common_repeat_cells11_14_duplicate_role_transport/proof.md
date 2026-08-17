# Proof

In the compiler's canonical cell atlas,

```text
cell 11: singleton BC1; pairs (LA,BC2),(AB,AC)
cell 14: singleton BC2; pairs (LA,BC1),(AB,AC).
```

The duplicate records `BC1,BC2` both have product `sigma_bc*b*c` and sum
`b+sigma_bc*c`. Exchanging them therefore sends the five product, sum, and
source-label triples of cell 11 to those of cell 14 by a row permutation,
with no parameter substitution. The full common Vieta matrix, rank
conditions, and guards are preserved.

The outside records depend on the common coefficient kernel but not on the
names `BC1,BC2`; hence the outside packet is fixed. Every missing record and
perfect matching label maps identically. Four source-sign rows, two BC signs,
two outside-cycle signs, and 105 labels give `4*2*2*105=1,680` systems. QED.
