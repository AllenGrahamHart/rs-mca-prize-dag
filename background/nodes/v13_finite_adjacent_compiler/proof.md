# proof: v13_finite_adjacent_compiler

Proof: LD-type counts are monotone nonincreasing in agreement. unsafe(a0) means count(a0) > B*; the disjoint/first-match integer ledger at a1 = a0+1 gives count(a1) <= B*. Monotonicity places the crossing in (a0, a1]; integrality of agreements makes a1 the first safe agreement; the closed-radius threshold is the a0/a1 boundary. QED. (This is the endpoint convention used by mca_grand and matched by the F_17^32 row: 7 at 506, 6 at 507, 6*2^128 < 17^32 < 7*2^128.)

Source: przchojecki/rs-mca towards-prize.md (2026-07-01) + cap25 v13 raw notes; imported as the v13 adapter layer 2026-07-06.
