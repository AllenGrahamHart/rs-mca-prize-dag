# Audit

1. `T_i intersect X` lies inside `Z_i`; it cannot contain another row's zero
   fiber because that fiber is part of `S_i`.
2. The three extra intersection terms in `(EC3)` are disjoint. No inclusion-
   exclusion correction is missing.
3. The pair slack is `z_i+z_j-d-1`, not `z_i+z_j-d`.
4. A zero-slack edge forces both inside reuse sets empty, not only their
   intersection.
5. In `(EC5)`, every inside reuse is charged `t-1` times, while each outside
   point is charged by its exact multiplicity pair count.
6. The aggregate right side may be zero but is never negative for an allowed
   shell profile.
7. The compatibility characterization retains the actual external zero sets
   `E_i`; it does not replace them by the whole ambient domain.
8. No bound on the number of compatible packings is claimed.
9. No Modal or candidate-row computation is used.
