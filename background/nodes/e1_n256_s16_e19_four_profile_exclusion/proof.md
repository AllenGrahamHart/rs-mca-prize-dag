# Proof

The E19 router exhausts every candidate with four profiles on eight affine
templates. Each census engine scans all `binom(124,3)` heavy supports and 64
relative signs. One engine forms oriented folded chord classes; the other
multiplies the sparse polynomial by its negacyclic reverse in
`Z[X]/(X^128+1)`. They agree on every profile count, conductor count, and
retained vector. A separate Python checker recomputes the direct negacyclic
profile and conductor of all 136 retained representatives.

The proper-conductor theorem removes 438 of the 574 actual vectors, including
every `(1,0,2)` and `(3,0,0,1)` vector. For the 136 full-conductor
representatives, FLINT and PARI/GP independently compute
`abs(Res(X^128+1,F))` and agree entry by entry. Every norm is positive and the
maximum printed in `statement.md` is strictly below `2^250`. The collision
norm criterion requires a live pair-feasible prime greater than `2^250` to
divide one of these nonzero norms, which is impossible. All four profiles are
therefore excluded.
