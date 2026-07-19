# Audit

1. Agreement subsets are chosen with exactly `3d-1` points, so all incidence
   equations are equalities even when an original codeword agrees more often.
2. Pairwise intersections are bounded by `k-1=2d-1` because the four
   codewords are distinct.
3. The raw degree-count classification follows from two scalar equations;
   the individual agreement equations then remove `(0,2,0,0)` and leave six
   labeled graph types.
4. The intersection matrix is not claimed singular merely from its row and
   column counts. The missing official theorem is exactly its full-column-rank
   behavior on fixed subgroup evaluation points.
5. A singular matrix is relevant only when its kernel contains four
   pairwise-distinct polynomials. The theorem and verifier retain that guard.
6. The `F_17` witness is a route fence, not an official counterexample: its
   field and length are outside the prize row.

The independent audit recomputes the five viable degree-count patterns and
rejects the sixth. It also mutates one toy coefficient and checks that the
printed kernel certificate fails.
