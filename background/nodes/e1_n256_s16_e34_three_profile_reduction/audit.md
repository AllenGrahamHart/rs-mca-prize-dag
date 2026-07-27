# Audit

Date: 2026-07-27.

The proof uses two complete, independently replayed certificates:

- 42,413,558 exact quotient allocations for profiles `(2,8)`, `(5,5,1)`,
  and `(14,1,0,1)` in both live quotient chambers;
- 809,474 refined profile-`(2,8)` quotient allocations plus 7,927,920 exact
  weighted supports in its inner-`4Z` chamber.

The local checkers independently reconstruct all coverage counts, source
hashes, quotient objectives, chamber maxima, and exact support objectives.
The node verifier separately reconstructs all 24 energy profiles, the abstract
caps, the small-field inequality, and both rational cubic signs. The audit
verifier mutates objective values, layer counts, quotient chambers, support
sets, and shard coverage; every mutation is rejected.

The Modal apps were `ap-zx5C3lSHLdaYAZE2Ic0tZA` and
`ap-8xzV3fZniv8jms4V2EI19N`. Both completed under the registered time and cost
ceilings. No incomplete solver status, sampled maximum, floating-point sign,
or launcher terminal summary is load-bearing.
