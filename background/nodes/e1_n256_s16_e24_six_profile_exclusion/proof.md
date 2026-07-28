# Proof

The proved E24 reduction is exhaustive: every candidate belongs to one of the
six printed profiles on one of 154 affine light templates.  For each template,
the census ranges over all `binom(124,3)` heavy supports and 64 relative sign
vectors.

The production engine forms oriented folded chord classes.  The audit engine
instead multiplies the sparse polynomial by its negacyclic reverse in
`Z[X]/(X^128+1)`.  In both a count-only pass and a collecting pass, the engines
agree exactly per template on profile counts, full-conductor counts, and two
64-bit content accumulators.  In the collecting pass they additionally agree
on every retained vector.  A separate Python checker recomputes the direct
negacyclic profile of all 6,834 retained representatives.

The census proves `(0,6)` and `(0,2,0,1)` empty.  It leaves 14,416 vectors in
the other four profiles.  Exactly 7,582 have proper conductor, so the proved
`e1_n256_proper_conductor_collision_exclusion` removes them.  This leaves the
6,834 full-conductor representatives printed in `statement.md`.

For a representative polynomial `F`, both FLINT and PARI/GP compute

```text
abs(Res(X^128+1,F)).
```

They agree entry by entry.  All norms are positive and the exact maximum is
the integer in `statement.md`, strictly below `2^250`.  The collision norm
criterion says a live pair-feasible prime `p>2^250` must divide the nonzero
norm.  Since every residual norm has absolute value less than `p`, this is
impossible.  Together with the empty and proper-conductor branches, all six
profiles are excluded.
