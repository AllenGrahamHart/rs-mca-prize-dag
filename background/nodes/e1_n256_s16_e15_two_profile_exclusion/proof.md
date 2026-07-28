# Proof

The E15 router exhausts every candidate with two profiles on eight affine
templates. Each census engine scans all `binom(124,3)` heavy supports and 64
relative signs. One engine forms oriented folded chord classes; the other
multiplies the sparse polynomial by its negacyclic reverse in
`Z[X]/(X^128+1)`. They agree on every profile count, conductor count, and
retained vector. A separate Python checker recomputes the direct negacyclic
profile and conductor of all 64 retained representatives.

The proper-conductor theorem removes 230 of the 294 actual vectors, including
every `(2,1,1)` vector. For the 64 full-conductor representatives, FLINT and
PARI/GP independently compute `abs(Res(X^128+1,F))` and agree entry by entry.
Every norm is positive.

The whole-norm shortcut is unavailable because 32 norms reach `2^250`. For
each norm `R`, write `R=2^mu R_odd`. The pair-feasible prime `p>2^250` is odd,
so `p|R` implies `p|R_odd`. The exact dual ledger and checker show that every
`R_odd` is positive and at most the `odd_max` printed in `statement.md`, which
is strictly below `2^250<p`. Thus `p` divides no residual norm. The collision
norm criterion excludes both routed profiles.
