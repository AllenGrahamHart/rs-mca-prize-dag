# Claim contract

- **claim id:** `f3_h3_distance_four_fiber_degree_cap`
- **mathematical statement:** small generic vectors have norm three and the
  unique possible antipodal vector has norm one; the generic distance-four
  graph has maximum degree three and an orientation of indegree at most one,
  and the complete fiber obeys `(D4C1)`
- **scope:** every nonzero product fiber in an odd-characteristic dyadic row,
  restricted to squared-norm-at-most-three representations
- **consumer:** `f3_h3_mobius_excess_half`, high-excess distance split
- **status:** `PROVED`
- **proved dependency:** distance-four cross-overlap router
- **new open content:** bound the distance-six edge–quotient moment forced by
  the cap
- **falsifier:** one generic representation with four generic distance-four
  neighbors, or a generic fiber with more edges than vertices
- **proof route:** classify the three local certificates, then orient each
  edge toward its product-monomial pair and reconstruct the unique tail
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_distance_four_fiber_degree_cap/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  ledger
