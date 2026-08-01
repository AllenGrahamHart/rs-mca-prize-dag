# Proof

The source-facet structure puts five labels inside three opposite pairs,
so exactly two pairs are complete and the remaining label is a singleton.
Choosing the singleton and then one of the three pairings of the other
four roles gives `5*3=15` cells.  The two source square roots of an
opposite quotient pair differ by `+/-i`; projective source scaling gives
the displayed normalization and four root-sign rows per cell.  Directly
applying the transposition of the identical `AB+` roles gives `(KBPCM-2)`.

The positive coefficient normal form is

```text
H(T,X)=A_2(W)T^2+A_0(W)+XT B_1(W),    W=X^2.
```

Vieta product and sum at source lift `z_j` are respectively
`A_0(lambda_j)=p_j A_2(lambda_j)` and
`lambda_j B_1(lambda_j)+q_j A_2(lambda_j)=0`.
Writing these equations in the eight coefficients gives exactly
`(KBPCM-3)`.

Assume `rank B=6`.  Modulo the row span of `B`, the four nonloop sum rows
lie in a two-dimensional quotient.  The full matrix has rank at most seven
exactly when their four images span at most one dimension.  This is
equivalent to every pair being dependent, which is exactly the six
determinants `(KBPCM-4)`.  If `rank B<6`, pairwise minors alone need not be
sufficient, so that branch is explicitly separated.

The checker enumerates the fifteen cells and duplicate-role action.  The
Modal compiler constructs each determinant directly over the deployed
field and reports all sixty cases complete. QED.
