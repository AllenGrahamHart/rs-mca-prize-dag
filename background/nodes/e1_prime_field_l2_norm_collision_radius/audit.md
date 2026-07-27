# Audit

Date: 2026-07-27.

The proof replaces the existing `L1` conjugate bound
`(2s)^phi(N)` by an `L2`/Parseval bound on the folded coefficient vector. The
all-even extremal profile must be divided by two; omitting that step would
leave a false apparent `2^256` boundary at `N=256,s=4`.

The verifier exhausts every antipodal coefficient profile through `s=8`,
checks exact orthogonality at small power-of-two orders, and replays the exact
integer endpoint inequalities. No resultant scan or Modal computation is
load-bearing.
