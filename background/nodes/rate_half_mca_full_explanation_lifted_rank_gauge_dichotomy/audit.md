# Audit

The proof distinguishes three ranks that must not be conflated:

1. explanation affine rank `K`;
2. lifted slope/explanation rank `K` or `K+1`;
3. error-vector affine rank, equal to the lifted rank only after proving
   `r_1 notin C`.

The primary verifier exhausts all 343 codeword gauges in independent
`GF(7)`, `K=3` controls for both lifted branches.  It observes exactly 49
rank-dropping gauges in the rank-three branch and none in the rank-four
branch.  The independent checker reconstructs the two kernels by separate
row reduction and checks hostile perturbations.

The theorem does not infer that the gauge minimizing direction support is a
rank-dropping gauge.  Accordingly, only the invariant direction-coset
distance is used for the improved high-support walls.
