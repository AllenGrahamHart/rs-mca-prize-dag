# Audit

- The claim is a 960-case route cut, not complete cell-14 exclusion.
- The five shards are disjoint and cover exactly missing indices `3,4,5,6`,
  all 15 matchings, all four source signs, and all four target lanes.
- Every eliminant is exact over `F_2130706433`; no sampled prime, floating
  arithmetic, or heuristic root search is used.
- `gcd(H,r^p-r)` enumerates every deployed-field parameter root. Every live
  finite fiber is replayed against the original reduced equations.
- The compressed eliminants are decompressed and hash-checked by the aggregate
  verifier.
- An independent FLINT implementation reparses all 960 eliminants and
  recomputes all field-root gcds rather than trusting the primary root lists.
- The quadratic leading-coefficient boundary is checked globally rather than
  only at eliminant roots.
- The `A_xi=0` ratio boundary is checked using the original division-free
  equations `F=A_xi=B_xi=0`; all its deployed roots are route boundaries.
- Remaining inversions are parent-proved map/kernel denominators or target
  products known nonzero from the target guards.
