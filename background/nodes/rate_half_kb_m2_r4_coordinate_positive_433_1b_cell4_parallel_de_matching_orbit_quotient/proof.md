# Proof

The signed-edge atlas orders the outside records as

```text
DE, DE, -DE, DF, sigma_o EF, BF, sigma_c CF.
```

The first two records have identical product, signed edge, and squared-sum
data. Their exchange therefore fixes every source and target equation and
guard; only record positions change.

If `xi=0` or `1`, the exchange swaps the omitted role. After deleting it,
the two residual lists are value-for-value identical in canonical order, so
the residual matching index is fixed. This gives fifteen two-element orbits
across the two positive missing roles.

For `xi>=2`, deletion leaves the first two residual positions occupied by
the identical positive copies. The exchange induces the transposition
`tau=(0 1)` on six positions. Applying `tau` to both endpoints of every
edge, sorting endpoints, and restoring canonical edge order sends matching
indices as follows:

```text
0->0, 1->1, 2->2,
3<->6, 4<->9, 5<->12, 7<->10, 8<->13, 11<->14.
```

This is `(KBP1B4-DE-QUOT-2)`. It gives nine matching orbits for each of the
five fixed missing roles, hence `15+5*9=60` total orbits.

The first-pair theorem closes pairings `0,1,2` for all three parallel-`DE`
missing roles. Across `xi=0,1` these are three two-element orbits; at
`xi=2` they are three fixed orbits. Thus six quotient orbits and nine labeled
slices are paid, leaving `60-6=54` representatives and `105-9=96` labeled
slices. QED.
