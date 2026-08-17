## Preregistered K'=87 simultaneous support-4/5/6 witness probe

- **decision:** test whether retaining the shared support-5 stratum in the
  two proved adjacent-flat inequalities pays the exact support-disjoint
  counterexample
- **scope:** one fixed witness and its dimension-six charge `(u,g)=(34,6)`;
  no residual lane scan
- **probe SHA-256:**
  `e4869f37c3eab008a2d17e829ec33bfba1612018c8b99be8f908af389fa7a986`
- **dispatcher SHA-256:**
  `d62f08a5741d4720bef0b0e43d15cb2d74617e0569e62db0b1ef20feb8bacfd3`
- **K'=87 witness adapter SHA-256:**
  `a66f4235d0651bd35d3ccbe749beb6ea5f52c6b2198bc1460bf13f3fe7907a00`
- **base witness analyzer SHA-256:**
  `44faccd0305d374557650c8bfc3b40f3aaa97717e46b154568cbadb3ec77bf3a`
- **theorem code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **envelope:** one CPU, 256 MB, 20-second child wall and 30-second container
  wall; projected cost below `$0.01`
- **local safety:** one RAM-guarded Modal client; no local mathematical run

For each intersection stratum `i=0,1,2`, the probe simultaneously imposes
the proved `(4,5)` and `(5,6)` instances of `(FAS1)`, together with the
proved `(FAS2)` individual caps on supports 4 and 5. It maximizes the weighted
`C4+C5+C6` objective over the resulting rational polytope. One implementation
uses the explicit support-5 breakpoints; the audit independently enumerates
all LP vertices with exact rational arithmetic. The remaining strata use the
same direct completion caps printed in the proved fixed-union theorem.

This does not add overlapping pair bounds. It uses two simultaneous
inequalities sharing one variable and solves their joint feasible region.
`PASS` requires exact agreement of both LP implementations and prints the
resulting witness price. A nonpositive margin is a route wall. A positive
margin authorizes theorem packaging and a separately preregistered lane
falsifier; this probe alone cannot promote `K'=87`.
