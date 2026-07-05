# proof: sov_forced_root_correctness

The node is the assembly of two proved inputs.

First, `sov_forced_root_recursion_algebra` proves the generalized forced
square-root construction for every `h`: the top coefficients of a monic
degree-`2h` locator determine the monic degree-`h` forced root `S`, and the
obstruction vector is exactly the coefficient list of `S^2 - L` in degrees
`1,...,h-1`.

Second, `sov_active_core_obstruction_vanishing` proves the row bridge: every
active `h`-core in the intended band is a finite `h`-trade support satisfying
the same square-shift obstruction equations, so each of those obstruction
coordinates is zero.

Together these prove both parts of the statement: the recursion computes the
correct SOV obstruction vector, and active cores force the relevant coordinates
to vanish.
