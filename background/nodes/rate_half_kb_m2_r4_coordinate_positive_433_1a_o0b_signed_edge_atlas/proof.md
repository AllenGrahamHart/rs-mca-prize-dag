# Proof

The residual workboard fixes `(KBPSA-1)--(KBPSA-2)` and says this common
row has unavoidable defect three.  A loop contributes one.  A cross-pair
multiplicity three has only two signed deck-orbit types, so its minimum
defect two is attained exactly by a `2+1` split.  No further defect is
available.  Consequently the `DE` and `DF` multiplicity-two pairs must
split `1+1`; all remaining nonloop edges are singletons.

The deficient common pairs are `B,C`, and `O0b` puts one colored incidence
on each of two outside pairs.  Permuting those pairs normalizes the colored
edges to `B-E,C-F`, leaving `D` uncolored.

The only signs not already present as forced opposite pairs are the
majority sign on `AB` and the signs on `AC,BE,CF,EF`.  Flipping a target
representative at a vertex multiplies each incident sign by `-1`.  These
five active edges form the cycle `A-B-E-F-C-A`.  Vertex gauge makes four
edge signs positive; their product around the cycle is invariant and may
be either sign.  Hence there are exactly the two representatives in
`(KBPSA-3)`.  Exhaustive replay finds 32 raw assignments in two gauge
orbits of size 16.

The displayed multigraph has degree four at every one of `A,...,F`.
Its loop costs one and the repeated `AB` signed type costs two, while all
other signed target edges are unrepeated.  Thus its defect is exactly
three.  The product/squared-sum formula is the identity
`(u+epsilon v)^2=u^2+v^2+2 epsilon uv`. QED.
