# Audit

- The exact computation covers only `xi=0`; identical-copy transport supplies
  `xi=1`.
- Matching 13 is pinned as `((0,5),(1,3),(2,4))`.
- The first paired cut uses `-de` and `sigma_o*u` for `u=ef`; the second
  uses `de` and `sigma_c*cf`.
- Norm and inversion numerator/denominator roots all enter direct replay.
- Every candidate root reaches a guard, no-lift, or finite terminal.
- The first pilot inherited matching 8's scalar replay order even though its
  symbolic eliminant used matching 13. The independent verifier detected the
  mismatch; the scalar inputs were repaired and both pilot and census rerun.
- The previously transported negative omission is not counted in this node.
