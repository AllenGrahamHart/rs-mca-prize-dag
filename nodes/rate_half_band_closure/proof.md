# rate_half_band_closure proof status

No proof is currently known in this node folder.

The former AQB proof route is refuted: averaging is a convex combination of
single-box fiber counts and cannot create the required box-sharing gain.

The former P6 dihedral-sibling proof route is also refuted.  The local refutation
is recorded in `nodes/dihedral_sibling_window_certificate/proof.md`: the claimed
packet size is not a Chebyshev top-degree drop, true Dickson fibers are too
small in the first band, and the endpoint fixed-point sibling still fails the
degree audit.

The live full-determination target remains: cover the rate-`1/2` band
`2^33 < sigma <= 8,592,912,738` by a new priced mechanism.  A bracket-grade
obstruction for some band radius is a separate partial-result outcome, not a
proof of this node.
