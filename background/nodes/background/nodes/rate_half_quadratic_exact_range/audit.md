# Audit

The safe radius is `B-1`, not `B`. The quadratic upper theorem is used only
at `B-1`; unsafety at radius `B` uses the unconditional MDS tangent lower
construction. This one-step distinction is why the maximal budget is
`B_Q=r_Q+1` even though the maximal quadratic radius is `r_Q`.

The field cutoff is exclusive because
`floor(q/2^128)<=B_Q` iff `q<(B_Q+1)2^128`. The theorem is uniform over
admissible fields and domains; the explicit prime row in the source theorem
is an example at the top budget, not an additional hypothesis.

The post-cutoff unsafe radius `B` is restricted to `B<=k-1`, exactly the
range in which the MDS tangent construction is available below capacity. The
CA-only reduction uses radius `B-1`, so its half-distance endpoint is
`B<=2^39+1`; replacing this by `B<=2^39` would unnecessarily lose one budget
block.
