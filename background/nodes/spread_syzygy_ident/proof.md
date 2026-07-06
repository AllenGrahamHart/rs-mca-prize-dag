# spread_syzygy_ident proof

For a family of support constraints, form the stacked linear alignment matrix.
Rank loss below the expected cap means that the rows of this stacked system
have a nontrivial linear dependency. By duality, such a dependency is exactly a
tuple of dual-code words whose supports are constrained to the prescribed
support pieces and whose signed sum cancels on the shared coordinates.

Conversely, any such constrained-support dual syzygy gives a nontrivial row
dependency in the stacked alignment matrix, hence rank loss. This proves the
rank-loss/syzygy equivalence.

The overlap-budget part is the same as in face 4: Reed-Solomon MDS dual weight
depends only on support size, not on whether the supports arise from aligned
MCA pairs or from the general face-3 spread regime. Therefore the `k+1`
overlap budget and the E13 exception anatomy transport verbatim. The observed
AG/net, v-degenerate, and syzygy-circuit classes are the general-support
normal forms of the same eliminant/syzygy condition.

