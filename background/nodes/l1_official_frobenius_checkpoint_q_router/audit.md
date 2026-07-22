# Audit - L1 official Frobenius-checkpoint Q router

1. Power sums with indices divisible by `p` are not independent coordinates:
   `S_(pj)=S_j^p`.
2. The missing coordinate at every positive multiple of `p` is the
   corresponding elementary symmetric function, not a power-sum correction.
3. Omitting even one checkpoint destroys injectivity at that depth.
4. The map is a coordinate equivalence on locator prefixes; splitness and
   first-match guards are imposed afterward by the consumer.
5. The bound 23 uses the generated-field order, strict cap, and `n>=8192`.
6. Checkpoint values must be conditioned on collectively. A `q^23` union is
   not authorized by this theorem.
7. The F2 summit remains TARGET and is not a requirement edge.
8. No computation or probabilistic evidence is load-bearing.
