# Proof

Fix an eleven-set `T` and put `r=rank(ev_T:V'->F^T)`.

If `r<=9`, choose nonzero `u in ker(ev_T)`.  Whenever a retained point
`(gamma,R_gamma)` solves all eleven equations, so does

```text
(gamma,R_gamma+t u),       t in F.
```

Thus the point lies on a positive-dimensional affine kernel fiber and is not
isolated.

Now suppose `r=10`.  Choose a ten-set `B subset T` on which evaluation is an
isomorphism.  There are unique `U_0,U_1 in V'` whose values on `B` are
`-a_x` and `-b_x`, respectively.  On the open set `q(Z)!=0`, the ten
equations indexed by `B` are equivalent to

```text
q(Z)R=U_0+Z U_1.                                      (1)
```

Let `y` be the remaining point of `T`.  Substitution in its equation leaves

```text
(a_y+U_0(y))+Z(b_y+U_1(y))=0.                         (2)
```

If (2) is identically zero, (1) gives a one-parameter affine-owner component
through every retained solution.  Otherwise (2) is a nonzero polynomial of
degree at most one, so it has at most one root.  Retained records have
distinct slopes and avoid `Z(q)`, hence at most one of them can be an
isolated point on `T`.

There are `C(n',11)` choices of `T`.  Subtracting this isolated-incidence cap
from the exact total `N C(m',11)` proves `(SI2)`.  The argument counts actual
record incidences, so projective boundary points and intersection
multiplicities are irrelevant.  QED.
