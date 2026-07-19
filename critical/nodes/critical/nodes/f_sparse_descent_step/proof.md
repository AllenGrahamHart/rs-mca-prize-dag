# f_sparse_descent_step proof

Let `S` be the support of a minimal weight-`w` word in `P-perp`. By
`f_dual_distance_frame`, the trace conditions on `S` have exactly one
redundancy and satisfy the closure property.

For members of `P` vanishing on every point of `S`, the `w` vanishing
conditions impose codimension at most `w - 1`, because the sparse dual word
gives one linear relation among them. Such members have the locator factor

```text
ell_S = product_{x in S} (X - x),
```

so division by `ell_S` maps them to a residual instance of degree `j - w`.
The dimension drops by at most `w - 1`, while the degree drops by `w`; hence
the divisor-depth quantity gains at least one unit.

For all other members, closure says they cannot vanish on exactly `w - 1`
points of `S`: vanishing on all but one point would force vanishing on all of
`S`. Therefore they have at most `w - 2` roots inside `S`. Removing `S` from
the domain leaves a residual root budget at most `j - w + 2`.

This proves the single descent step. Iterating and summing such steps is the
separate content of `f_dim_induction` and `f_descent_termination`.
