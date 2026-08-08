# Proof

The first-pair parent pays `{0,1,2} x {0,1,2}`. The six complete orbit
parents respectively pay `{0,1,2}` times

```text
{3,6}, {4,9}, {5,12}, {7,10}, {8,13}, {11,14}.
```

These seven matching sets are pairwise disjoint and their union is exactly
`{0,...,14}`. Taking the Cartesian product with the three parallel-`DE`
missing roles gives a disjoint union of `3*15=45` labels. Every parent is an
empty-slice theorem at fixed role cell, source signs, and target lanes, so
their union is empty. Each label has `4*4=16` raw cases; hence the paid census
is `45*16=720`. QED.
