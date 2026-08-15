# Proof

The universal completion theorem gives `0<=M_c<=q`.  If
`M_c>q-(10-c)`, then the unique integer `s=q-M_c` lies in `0..9-c`, giving
exactly one terminal leaf.  Otherwise the fallback inequality holds.  The
alternatives are disjoint and exhaustive, with `10-c` terminal leaves and
one fallback leaf.

Every inherited cap describes the parent branch and therefore remains true
on each sub-branch.  On a terminal leaf, a deletion attaining `q-s`
completions invokes the cross-support carrier theorem for exactly the target
supports satisfying `(BL3)`; ordinary deletion counting gives the source
ceiling.  On the fallback leaf, ordinary deletion counting uses the retained
ceiling `q-(10-c)`.  Intersecting upper bounds preserves all of them.

Applying the same argument to any resulting leaf proves repeatability and
the finite branch-lattice claim.  QED.
