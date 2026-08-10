# Proof

For each source row, form the `5 x 6` product matrix in the statement.  The
signed maximal minors give a division-free right-kernel vector by Laplace
expansion.  The selected-rank parent supplies a nonzero minor on its open, so
the product kernel has the required one-dimensional projective meaning there.

Choose the second common row as pivot.  Its known endpoint sum determines
`beta_0`; setting `beta_1=-beta_0` gives a degree-one beta.  Exact quotient
arithmetic in the degree-six or degree-four source algebra then reduces all
five equations
`(root_i s_i)A(lambda_i)+lambda_i beta(lambda_i)` to zero for every root-sign
and BC-sign row.

The product equation immediately gives `p=B/A` at a missing label.  Writing
`q=root*s`, the sum equation gives `q=-lambda beta/A`; because
`lambda=root^2`, division by `lambda` yields
`s^2=lambda beta^2/A^2`.  The audit's inversions record every nonzero rational
guard used in these formulas.  QED.
