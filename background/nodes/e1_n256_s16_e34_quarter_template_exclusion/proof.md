# Proof

The heavy-template reduction gives the displayed normalization, including
the absent position `96` and opposite outer heavy coefficients. Global sign
fixes `c_0=2`; the middle heavy sign contributes two choices. The remaining
124 positions contain the four light positions, and their signs contribute
16 choices. Hence the exact search space has

```text
binom(124,4)*32=300,200,032
```

vectors.

The primary census builds each positive-half autocorrelation coefficient by
grouping the 21 unordered support chords. The audit instead constructs
`F(X)F(X^-1)` directly in `Z[X]/(X^128+1)` from 49 ordered products. They use
the same 121-shard support partition but independent autocorrelation code.
The checker proves the shard set is exactly `0,...,120`, verifies shard `i`
contains `binom(123-i,3)` supports and 32 vectors per support, compares all
six reported fields shard by shard, and replays eight retained witnesses.
The two packets agree exactly on the counts and maximum in the statement.

Every pair-feasible residual has full conductor by
`e1_n256_proper_conductor_collision_exclusion`. On the complete
full-conductor quarter class the exact weighted cyclic third moment satisfies

```text
M_3<=1188<1947.
```

The rational cubic-Hermite certificate inherited from the E34 reduction has
positive norm margin at `M_3=1947`. It therefore bounds the nonzero collision
norm strictly below `2^250`, which the collision-norm criterion and the
pair-feasible row threshold exclude. QED.
