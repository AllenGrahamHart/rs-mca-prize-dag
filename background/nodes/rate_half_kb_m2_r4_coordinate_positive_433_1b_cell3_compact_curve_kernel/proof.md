# Proof

Write the five source labels as `x_j`, the target products as `p_j`, and the
signed target sums as `q_j`.  The LA loop sum gives `beta_1=-beta_0`, so the
eight-column Vieta matrix reduces to seven columns.  The five product rows
have rank five on a selected product-cofactor chart.  The AB sum row has last
coordinate `-x_AB(1-x_AB)`, which is nonzero under the route guards, while all
product rows have last coordinate zero.  It therefore raises the base rank to
six.  Each of the other three nontrivial sum rows belongs to this rank-six row
span exactly when the corresponding `7 x 7` determinant vanishes.  This proves
the compact three-determinant presentation.

The structure compiler constructs these determinants independently for all
`4*6=24` source-sign/cofactor charts.  It strips only printed guard factors,
then saturates sequentially by the selected product cofactor and all route
guards.  Every run completes with dimension one and basis size 21.  For each
fixed sign row, all six charts give byte-identical elimination relations.  The
four projection shapes are exactly those in the statement.  Independent
FLINT factorization reconstructs each polynomial and returns one factor of
multiplicity one.  The `(r,b)`, `(b,t)`, and `(r,c)` polynomials are
palindromic in `b,b,c`, respectively; substitution of `u+u^-1` reconstructs
each from its recorded quotient exactly.

It remains to justify a global kernel normalization.  Let
`kappa=(A_0,A_1,A_2,B_0,B_1,B_2)` be the signed cofactor vector of the five
product rows, let `x=x_AB=t^2`, and put

```text
s=x(1-x),
gamma=q_AB (A_0+A_1 x+A_2 x^2).
```

Then

```text
(s kappa_0,...,s kappa_5,-gamma,gamma)          (KBP1B3-CURVE-2)
```

annihilates the five product rows, the LA loop row, and the AB row
identically.  The apparent beta-zero intersection before re-saturation has
dimension zero and basis size 44, but its eliminant contains explicitly
inverted guard factors.  Re-saturating the intersection by every route guard
and the selected product cofactor gives the unit ideal in all 24 charts.
Thus `gamma` is nonzero everywhere on the guarded principal cover, so
`(KBP1B3-CURVE-2)` is a global normalization rather than a generic chart.

Finally, the kernel compiler divides the common polynomial gcd exactly and
normalizes a shared scalar.  Seven row products are identically zero.  For
each source-sign pair, Singular reduces the other three row products by the
three compact common determinants; all thirty remainders are zero.  The four
compiled kernel vectors have identical coordinate digests.  This proves the
claim. QED.
