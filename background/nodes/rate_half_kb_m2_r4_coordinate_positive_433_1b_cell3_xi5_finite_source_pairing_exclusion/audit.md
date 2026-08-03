# Audit

- The endpoint ledger contains exactly six compatible `xi=5` sources for
  each of four source signs.
- Every source reconstructs `f=m/b` and directly replays `m=bf` and
  `s=(b+f)^2`.
- All 24 sources, 15 matchings, and 4 lanes are present: 1440 subcases.
- Each subcase computes all three pairwise resultants; all 4320 primary and
  all 4320 independent resultants are nonzero.
- Every selected resultant has degree eight.
- Primary `v` elimination enumerates 2208 `u` roots; every specialized
  three-equation gcd in `v` is the constant one.
- Independent `u` elimination enumerates 2208 `v` roots and no `u` root.
- The per-source outer-root multiset is eight each of 44, 108, and 124 in
  both directions.
- Boundary, witness, solution, free-fiber, and unresolved ledgers are empty.
- Primary and independent verifiers pin all four compiler/census hashes.
