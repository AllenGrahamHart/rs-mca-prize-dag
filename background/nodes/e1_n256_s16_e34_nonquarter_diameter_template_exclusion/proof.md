# Proof

The weld reduction proves that every vector in this branch has one of the 31
normal forms `H={0,64,t}`, `1<=t<=31`, and one of exactly 915,125 admissible
light supports. Global sign normalization leaves four heavy-sign choices and
sixteen light-sign choices, so the 31 disjoint chambers contain exactly

```text
31 * 915,125 * 64 = 1,815,608,000
```

signed vectors.

The primary census constructs each positive-half autocorrelation coefficient
from the 21 unordered support chords. The audit independently constructs
`F(X)F(X^-1)` in `Z[X]/(X^128+1)` from all 49 ordered products. It also
recognizes the two required welds by direct circular-distance tests rather
than the primary five-position formula. Each implementation uses one shard
per `t`. The checker proves that the shard set is exactly `1,...,31`, that
each shard has 915,125 supports and 58,568,000 vectors, compares all six
count/maximum fields shardwise, and replays the retained witnesses.

The two exact packets agree on 899,456 full-conductor profile-`(6,7)` vectors
and maximum `M_3=1560`. Every pair-feasible residual vector has full conductor
by `e1_n256_proper_conductor_collision_exclusion`. The rational cubic-Hermite
certificate inherited from the E34 three-profile reduction has positive norm
margin at `M_3=1947`; hence `M_3<=1560` puts the nonzero collision norm
strictly below `2^250`. The collision-norm criterion and row threshold exclude
every vector in the branch. QED.
