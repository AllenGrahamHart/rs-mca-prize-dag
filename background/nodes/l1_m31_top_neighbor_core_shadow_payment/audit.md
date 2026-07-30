# Audit - M31 top-neighbor core-shadow payment

1. The affine object is a flat of actual codewords, not a projective locator
   line: `R F[X]_(<=r)` is a polynomial subspace of degree below `k`.
2. The affine-span theorem counts the anchor, so the neighbor cap subtracts
   one.
3. The `r=1` cap is `240` neighbors, not `241`; `241` is the total listed
   population of the plane.
4. Scalar multiplicity is retained. Several neighbors with the same `J_j`
   are all charged against the same fixed-core cap.
5. Squarefreeness follows because `J_j` is a locator on a distinct
   evaluation domain. It has exactly `C(t,r)` degree-`t-r` divisors.
6. `(CS4)` is a lower bound on realized cores, not an upper bound or a
   contradiction.

The support-only `67449` construction is therefore harmless inside one
actual affine plane, but the theorem does not control a union of millions of
such planes.
