# Audit - L1 official Frobenius-checkpoint Q router

1. Power sums with indices divisible by `p` are not independent coordinates:
   `S_(pj)=S_j^p`.
2. The missing coordinate at every positive multiple of `p` is the
   corresponding elementary symmetric function, not a power-sum correction.
3. Omitting even one checkpoint destroys injectivity at that depth.
4. The map is a coordinate equivalence on locator prefixes; splitness and
   first-match guards are imposed afterward by the consumer.
5. The bound 23 uses the generated-field order, strict cap, and `n>=8192`.
6. A theorem for the larger coarse p-free fiber transfers to each mixed fiber
   with no checkpoint loss. This stronger route must not be confused with a
   per-checkpoint theorem.
7. A `q^23` union preserves qualitative polynomiality because
   `q^23<n^453`, but it cannot certify the finite prize threshold: with one
   checkpoint and any positive max bound its formal right side is already at
   least `q`.
8. The F2 summit remains TARGET and is not a requirement edge.
9. No computation or probabilistic evidence is load-bearing.
