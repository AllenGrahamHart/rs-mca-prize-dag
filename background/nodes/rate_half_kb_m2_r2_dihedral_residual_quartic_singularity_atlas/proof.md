# Proof

Write the quartic as a polynomial in `X=S^2`:

```text
R(X,P)=C X^2+(B P^2-4C P+E)X+M(P),                (1)
```

where direct substitution of the one-parameter coefficients gives

```text
M(P)=(a-2)(P+1)^2 N(P),                            (2)
N(P)=(a-b^2+2)P^2+2(a-2b+2)P+(a-2),
disc(N)=4(a+2)(b-2)^2.                             (3)
```

The discriminant of `(1)` in `X` is

```text
P^2(alpha P^2+beta),                               (4)
alpha=(a-2)(a+2)(b-2)^3(b+2),
beta=-4(a+2)(a-b)(b-2)^3.
```

Suppose first that `b!=a`. Then `C`, `alpha`, and `beta` are nonzero. The
quadratic `(1)` is irreducible over the geometric rational function field:
its discriminant is not a square. If `Q` split after replacing `X` by
`S^2`, then `X` would be a square in the quadratic function field of
`R`. Its norm `M/C` would be a square in the base field. Equations `(2)`
and `(3)` show that its square class is the nonsquare quadratic `N(P)`, a
contradiction. Hence `Q` is geometrically irreducible.

Direct differentiation gives the singular points `(KBMS-1)`. At the two
points with `P=0`, the Hessian determinant is

```text
16(a-2)(a+2)(b-2)^3,
```

and at `(0,-1)` it is

```text
-4(a-2)(a+2)(b-2)^4.
```

Both are nonzero for the allowed parameters, so all three are ordinary
nodes. An irreducible plane quartic has arithmetic genus three; the three
nodes already account for total delta three. Its normalization is rational
and there can be no further singularity.

Now let `b=a`. Then `C=E=0`, and `Q` is quadratic in `S` over the `P` line.
After removing square factors, its radicand is the quadratic `N(P)`, whose
discriminant in `(3)` remains nonzero. Thus `Q` is again geometrically
irreducible. The point `(0,-1)` has the same nonzero Hessian and remains a
node. In the projective chart `S=1`, centered at `[1:0:0]`, the lowest term
is `B P^2`, while the degree-four transverse term is `F U^4`; both `B` and
`F` are nonzero for `a=-1,1`. The two local branches have

```text
P=constant*U^2+O(U^3)
```

with distinct constants. They are smooth and meet to order two, so the
point is a tacnode of delta two. The node and tacnode again total three,
proving rationality and completeness. QED.
