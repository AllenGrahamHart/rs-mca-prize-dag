# Proof

The E23 router exhausts every candidate with four profiles on eight affine
templates.  Each census engine scans all `binom(124,3)` heavy supports and 64
relative signs.  One engine forms oriented folded chord classes; the other
multiplies the sparse polynomial by its negacyclic reverse.  They agree on
every profile count, conductor count, and retained vector.  A separate Python
checker recomputes the direct product and profile of all 484 retained vectors.

The proper-conductor theorem removes 1,404 of the 1,888 actual vectors,
including every `(1,1,2)` vector.  For the 484 full-conductor representatives,
FLINT and PARI/GP independently compute `abs(Res(X^128+1,F))` and agree entry
by entry.  Every norm is positive and the maximum printed in `statement.md`
is strictly below `2^250`.  The collision norm criterion requires a live
prime greater than `2^250` to divide one of these nonzero norms, which is
impossible.  All four profiles are therefore excluded.
