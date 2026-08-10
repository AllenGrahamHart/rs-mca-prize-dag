# Proof and convention bridge

Theorem 2 of Haboeck, *A note on mutual correlated agreement for
Reed-Solomon codes* (IACR ePrint 2025/2110), proves `(HJ1)` for the event
printed in `statement.md`. The event uses one support chosen per slope, tests
the affine combination on that support, and excludes joint containment of
the received pair on the same support. These are exactly the repository's
support-wise MCA quantifiers for its finite-affine slope sampler.

Haboeck writes `RS[F_q,D,d]` for polynomials of degree at most `d`, with
dimension `d+1` and reduced rate `rho=d/n`. The repository writes
`RS[F,D,K]` for polynomials of degree less than `K`, with dimension `K`.
Therefore `d=K-1`, proving `(HJ2)` with no inequality or conservative rate
replacement.

The source proof runs the Guruswami-Sudan decoder over `F_q(Z)`, partitions
the exceptional slopes by irreducible components and Hensel starting data,
and then applies the same-support collinearity count. The pinned upstream
audit checked the deferred BCIKS steps, the inseparable branch, and the
same-support endpoint. This node uses that public proof by citation; it does
not treat the later BCHKS25 sketch of a sharper bound as proved. QED.
