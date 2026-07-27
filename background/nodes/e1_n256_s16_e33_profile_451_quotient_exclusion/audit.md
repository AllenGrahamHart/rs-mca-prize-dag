# Audit

- The production run `ap-XlApOnmQmoX3P5Gd6qsVXb` and wrapper replay
  `ap-BnCaKbLKE6f99c19iKJ1D5` agree exactly.
- Sixteen shards cover 5,421,301 order-128 and 3,086,861 order-64 allocations.
- The primary checker recompiles the pinned source and reconstructs every
  shard objective with a separate Python implementation.
- The audit repartitions each chamber into seven shards and recovers the same
  totals and maxima, guarding shard-boundary omissions.
- Independent dynamic programming derives both allocation totals from the
  capacities and exact profile counts.
- The two-point top cubic is mutation-tested: restoring the generic cap two
  changes the boundary objective and is rejected.
- The `4Z` branch is checked directly with `L=17` and `50^32<2^250`.

The earlier CP-SAT threshold run timed out in its substantive shards and is
not used by the proof. The quotient census, not solver resistance, is the
load-bearing computation.
