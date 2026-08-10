# Upstream crosswalk

Upstream PR #1125 at pinned head
`f1503e54024f4949cf6542683712729e730eb6ca` supplies the balanced exact-shell
determinant coordinate and now also banks this direct FPC5 realization:

```text
upstream determinant coordinate
  <-> E=(A_1A'_2-A'_1A_2)/L_0
```

at the level needed for ownership. Both coordinates recover exactly
`gcd(F_0,F)` and determine the neighbor injectively. No assertion that the
two polynomial coordinates are literally equal under a fixed basis is needed
or made.

The result is exported but remains unmerged while PR #1125 is open. It
strengthens the shared LIST interface but claims no upstream acceptance,
aggregate owner bound, or row payment.
