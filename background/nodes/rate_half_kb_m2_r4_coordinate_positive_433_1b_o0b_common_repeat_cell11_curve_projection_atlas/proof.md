# Proof

The existing Vieta compiler is specialized to role cell 11 and compiled on
all eight sign rows.  In each row, the six stripped common minors and the
full source/target guard define a localized ideal in `(t,r,c,b)`.

Singular computes a reduced standard basis of dimension one.  Eliminating
`t,r` leaves one polynomial in `(c,b)`.  All four epsilon rows agree for a
fixed BC sign, while the two BC signs give distinct polynomials of total
degrees eight and six.

A separate geometry pass factors the small-coefficient lifts over `Q`,
eliminates source coordinates in two stages, and reduces the plane equations
under `x-bc` and `y-b-c`.  This independently gives the two symmetric forms
recorded in the result packet.  The node claims only the guarded common
projection, not equality with a smaller source tower and not outside
exclusion.
