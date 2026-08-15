# Attack

Replay the exact rational LP, not a floating approximation. Check the
unknown-record normalization before replacing `R_actual` by `N_min`, and
verify the optimizer independently through its dual certificate.

The first wall is a genuine one-shadow wall: corank 1 is saturated and
corank 2 is partial. A continuation should add the eight-subset shadow or
another compatible resource; changing integer floors cannot bridge the
wall.
