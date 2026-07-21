# Proof

Identify a Segre column with the rank-one matrix

```text
R_i = ((c_i,d_i),(gamma_i c_i,gamma_i d_i)).         (1)
```

For arbitrary scalars `beta_i`, expansion of the two-by-two determinant gives

```text
det(sum_i beta_i R_i)
 =sum_(i<j)(gamma_j-gamma_i)(c_i d_j-d_i c_j)
             beta_i beta_j
 =Q_B(beta).                                         (2)
```

The anchor slopes are distinct and their projective row classes are distinct,
so every coefficient `p_ij` is nonzero. Since `M_B` is invertible, `(2)`
exhibits `Q_B` as the pullback of the determinant quadric under a projective
linear isomorphism. The determinant quadric is the split Segre surface and is
smooth, proving the corresponding assertions about `Q_B`.

For a non-anchor `e`, equation `(QC1)` says that `M_B beta_e=v_e`. The right
side is a Segre column, so its determinant is zero. Equation `(2)` proves
`Q_B(beta_e)=0`. The vector `beta_e` cannot have support one, because then
`v_e` would be proportional to an anchor despite distinct slopes and row
classes. It cannot have support two, because `(QC4)` would then be a nonzero
row-scaling relation on at most three blocks, contrary to the proved circuit
arity. Hence its support is three or four. The basis expansion immediately
gives `(QC4)` and the owner arity claim.

The original all-one trade vector says

```text
0=sum_i v_i
 =M_B((1,1,1,1)+sum_(e notin B) beta_e).
```

Invertibility of `M_B` proves `(QC5)`, and the same calculation proves its
converse. More explicitly, start with anchors and vectors satisfying
`(QC3)--(QC5)`. Equation `(2)` makes every `M_B beta_e` a nonzero rank-one
matrix. The finite-slope and distinct-projection hypotheses put it in the
required Segre chart without repeated blocks. The centroid identity gives
the unweighted and slope-weighted trade equations simultaneously, while the
anchors keep coefficient rank four. This proves the coefficient-level
converse and all claims. QED.
