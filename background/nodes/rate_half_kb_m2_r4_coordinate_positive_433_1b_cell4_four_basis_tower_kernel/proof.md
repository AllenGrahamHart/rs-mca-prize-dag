# Proof

Write the five common source labels as `x_j`, target products as `p_j`, and
signed target sums as `q_j`.  The `LA` loop sum has `q_LA=0` and `x_LA=1`,
so it gives `beta_1=-beta_0` and reduces the eight-column Vieta matrix to
seven columns.  A selected nonzero maximal product cofactor gives rank five
for the product block.  The guarded `AB` sum row has nonzero last coordinate
`-x_AB(1-x_AB)`, while the product rows have last coordinate zero, so it
raises the base rank to six.  The other three nonloop sum rows lie in that
span exactly when their three `7 x 7` determinants vanish.

The compiler forms these determinants independently in every one of the
`4*6=24` source-sign/cofactor charts.  It strips only displayed route-guard
factors and saturates sequentially by the selected cofactor and all route
guards.  Each run completes with dimension one and basis size `16`.  Adding
the raw `AB` product-kernel scale and repeating every saturation gives the
unit ideal in every chart.  Thus the compact pivot loses no guarded common
point.

Changing to lex order `(c,b,t,r)` gives nine basis elements.  Let `F`, `G`,
and `H` be elements `1`, `2`, and `6`.  The compiler saturates the ideal
`(F,G,H)` by the same guards and reduces all nine lex elements by the result.
All `24*9=216` remainders are zero.  Conversely, `F,G,H` belong to the full
ideal, so they generate the same localized ideal.  Their shapes are exactly
those in the statement and all six cofactor charts have identical relation
digests for each source-sign pair.

Direct coefficient extraction gives the two displayed `L_b` identities,
`coeff_b^2(G)=coeff_1(G)`, and the two displayed `L_c` identities.  Their
factors are among `r`, `r-1`, `r+1`, `t-1`, and `t+1`, all inverted route
guards.  Hence `F` first gives a two-basis algebra over `F_p(r)`, `G` gives a
second two-basis extension, and `H` recovers `c` linearly.  The discriminant
of each quadratic `F` is degree six and has gcd one with its derivative.
Since the deployed characteristic is odd, completing the square gives a
square-free degree-six hyperelliptic model, whose normalization has genus
two.

For the kernel, let
`kappa=(A_0,A_1,A_2,B_0,B_1,B_2)` be the primitive product-row cofactor
vector, put `x=x_AB=t^2`, `s=x(1-x)`, and set

```text
gamma=q_AB(A_0+A_1 x+A_2 x^2).
```

Then

```text
(s kappa_0,...,s kappa_5,-gamma,gamma)          (KBP1B4-TOWER-2)
```

annihilates the five product rows, the `LA` row, and the `AB` row
identically.  Exact gcd removal and scalar normalization yield the same eight
coordinate digests for all four source signs.  Singular reduces the remaining
three row products by the compact ideal; all forty row remainders are zero.
Together with the empty pivot boundary, this makes `(KBP1B4-TOWER-2)` a
global kernel on the guarded principal cover. QED.
