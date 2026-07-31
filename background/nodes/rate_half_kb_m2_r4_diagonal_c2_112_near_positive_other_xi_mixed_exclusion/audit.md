# Audit

1. The theorem is deployed-field only; no algebraic-closure claim is made.
2. The four primitive conditions are independently reconstructed and their
   degrees, term counts, and digests are pinned.
3. The finite-incidence square is divided only from the product equations;
   its zero set remains explicitly forbidden.
4. Both within-root parent resultants retain their full factor multiplicity
   census. Low and high components are selected by degree and digest.
5. Projection resultants are used only in the necessary direction.
6. Every modular factor is counted. A factor is omitted from field replay
   only when its irreducible degree does not divide six.
7. High/high is covered by the complete product cross-resultant. The direct
   high/high resultant is neither computed nor assumed.
8. The primary field engine checks relative c and b support before splitting
   roots. Degenerate linear b-relations fall back to the quadratic relation.
9. The audit field engine instead specializes all four primitive equations,
   takes their b-gcd, and independently applies the target/base Frobenius
   sieve. It does not import the primary helper.
10. Forbidden labels include zero, fixed and inverse-fixed values, all
    pairwise collisions and reciprocal collisions, `z=1`, and finite
    incidence.
11. Every verifier is a fail-closed shard with a 60-second wall envelope.
12. This theorem adds one affine positive chart only and is wired as evidence,
    not as a requirement that could manufacture the parent target.
