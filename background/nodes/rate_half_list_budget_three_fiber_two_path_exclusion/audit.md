# Audit

- Kept the three-term tight-triangle support; the four-cycle relation has a
  two-dimensional parity kernel and is not covered.
- Used pairwise coprimality of the actual omitted-triple block locators. This
  follows from their disjoint coordinate blocks and is load-bearing.
- Did not assume that the squares `r_i^2` are distinct. Only the deleted roots
  `r_i` themselves must be distinct.
- The odd/even monomial split is valid in characteristic two as well, although
  the official application has odd characteristic.
- The degree threshold `s>=2` is sharp: at `s=1`, the three linear locators
  `X+r_i` are pairwise coprime and have a nondegenerate relation.
- The proof applies only when all three completions use the same `X^2` map.
  It does not silently cover mixed quotient maps or partial fibers.
- Exact finite-field controls include both distinct-square and antipodal-root
  triples. No Modal computation was used.
