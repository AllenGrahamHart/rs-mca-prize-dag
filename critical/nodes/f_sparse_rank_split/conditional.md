# f_sparse_rank_split conditional proof

## Predicate nodes

- `f_weight2_inverse`

## Claim

Many-sparse flats split exhaustively by the rank `d_sp` of the span of their
sparse dual words.

## Proof

Let `d_sp` be the dimension of the span of the sparse dual words carried by the
flat. There are only two cases.

If `d_sp` is bounded, quotient by that sparse span. The quotient has fixed
dimension, so the fixed-d lattice machinery and the already recorded strip
reduce this branch to the proved bounded-dimensional case.

If `d_sp` grows, the flat contains many independent sparse dual words. Split
those words by weight. Abundant weight-2 words are exactly the hypothesis of
`f_weight2_inverse`, which places the flat in the pullback/dihedral structure
recorded there. If the sparse abundance is not weight-2, then the surviving
higher-weight accumulation is the Face-4 configuration object under the proved
syzygy-flat transport dictionary.

This case split is exhaustive by the definition of `d_sp` and by the
weight partition of sparse dual words. The local split is therefore proved
conditional on the weight-2 inverse theorem for the weight-2 branch.
