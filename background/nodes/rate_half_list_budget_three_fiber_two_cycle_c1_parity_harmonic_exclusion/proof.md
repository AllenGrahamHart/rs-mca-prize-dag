# Proof

The dependency proves that every harmonic survivor lies in the positive
quadratic field class and that its characteristic occurs in the exact
interval `(CHE2)`. It also proves that the two remaining source equations
are equivalent to the terminal tests `(CHE3)`.

The preregistered launcher partitions all `4,495,441` consecutive
`k`-values into 32 disjoint contiguous shards. Every shard returns its
range, processed count, factor-five count, rolling digest, hits, and elapsed
time. The result packet records

```text
processed=expected=4,495,441,
coverage_exact=true,
all_complete=true,
hits=[].
```

The independent checker reconstructs the exact interval and shard
partition, verifies the launcher hash, recomputes each no-hit digest and
factor-five count, and directly replays both terminals on boundary and
midpoint samples from every shard. It passes.

Therefore no integer modulus in the complete characteristic superset
supports either necessary harmonic torsion trace. In particular no official
prime characteristic supports a harmonic survivor. This proves
`(CHE1)`. QED.

