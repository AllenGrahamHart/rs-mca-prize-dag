# Collision-component profile, 2026-07-13

This is evidence and route selection, not a theorem premise. The banked P9
LineRay census was extended to compute the canonical exact-`k` slope graph,
its `(component size, union excess d)` profile, the affine rank of all
retained error vectors, and the minimum one-per-slope selector rank through
dimension three. Modal app `ap-EC3OVO0F8gifH3co7fMcj9` replayed all original
T1-T4 identities while adding these diagnostics.

Across the fourteen P9 jobs, thirteen raw exact-`k` graphs were nonempty and
every nonempty graph had exactly one collision component. After conservatively
deleting every ray participating in a cross-slope core greater than `k`,
eleven graphs remained nonempty and every one was still connected.

At `n=16,k=8`, the four far profiles were

```text
(size,d) = (50,8), (52,8), (33,8), (34,8).
```

In all four cases the affine error rank of the complete raw and far families
was `9=k+1`, the maximum allowed by a syndrome line over an `[n,k]` code. The
canonical collision-tree selector also had rank `9`. More importantly, an
exact RREF search found no selector of rank at most three for any of the four
far high-core slope families. The search anchors one slope and recursively
branches on a currently unmet slope fiber; any affine flat meeting every
fiber must take one of those extensions, so exhaustion through depth three is
exact. The return value `4` in the certificate means `>3`, not rank exactly
four.

The two raw near-pencil families did have rank-one selectors, but those
selectors disappeared after deleting rays with cross-slope core greater than
`k`; their far families returned `>3`. This is a useful mutation showing that
the tangent deletion is load-bearing. Thus union excess, full-family rank,
and canonical selector rank can all saturate after deletion. The component
atlas remains correct, and the selector theorem proves every rank-at-most-
three branch, but low transversal rank is not supported as a universal
premise. The next useful structure must exploit the joint Reed--Solomon/high-
core geometry of these high-transversal-rank components, or count them
directly; further raw connectivity censuses are not the priority.

The rows are toy `t=2` boundary rows, not transported official candidates.
They neither prove nor falsify XR P-A.
