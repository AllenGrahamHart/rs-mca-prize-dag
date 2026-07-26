# Frontier audit: Zone-(b)

Status: CONDITIONAL on the route-local `e1_fullness` theorem.

`collision_norm_criterion` is proved, but it is not enough by itself.  It
reduces non-quotient `e_1` collisions modulo `p` to divisibility of explicit
bounded nonzero norms.  The node still needs a prize-scale decision for the
value sets with quotient orders `80 < N' < 512` (for Row C, `N' = 128, 256`).

Remaining route-local closure options are:

- prove `e1_fullness` directly;
- extend the norm threshold far enough via `norm_threshold_ext`;
- or prove a quantitative collision profile. A generic “collided” label is
  insufficient for the universal unsafe-side occupancy branch.
