# Proof

The E22 router exhausts every candidate with eight profiles on 1,321 affine
templates.  Each census engine scans all `binom(124,3)` heavy supports and 64
relative signs.  One engine forms oriented folded chord classes; the other
multiplies the sparse polynomial by its negacyclic reverse in
`Z[X]/(X^128+1)`.  A count-only pass and a collecting pass agree exactly on
every per-template profile count, conductor count, and pair of content
fingerprints.  They additionally agree on every retained vector.  A separate
Python checker recomputes the direct negacyclic profile and conductor of all
15,002 retained representatives.

The proper-conductor theorem removes 12,996 of the 27,998 actual vectors,
including every `(0,1,2)` vector.  For the 15,002 full-conductor
representatives, FLINT and PARI/GP independently compute

```text
abs(Res(X^128+1,F)).
```

They agree entry by entry.  Every norm is positive and the exact maximum in
`statement.md` is strictly below `2^250`.  The collision norm criterion says
a live pair-feasible prime `p>2^250` must divide one of these nonzero norms.
Since every residual norm has absolute value less than `p`, this is
impossible.  All eight profiles are excluded.
