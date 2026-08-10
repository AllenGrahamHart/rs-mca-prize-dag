# Proof

Let `D` be the order-32 subgroup of `F_97^*`. Select six nontrivial inverse
pairs `{x,x^(-1)}` and put them in `W`. Their six values

```text
nu=x+x^(-1)
```

are distinct. Use one inverse pair as `S_0 intersect S_1`; split each of the
other five pairs with one point in `S_0\S_1` and one in `S_1\S_0`. At an
exclusive point, make `nu` the second incidence owner and the opposite
selected slope the fibre root. At the intersection pair, make `nu` the fibre
root. Every normalized highest-clone polynomial on `W` is then

```text
H_x(Y)=Y(Y-1)(Y-nu_x).                                (1)
```

The seven residual slopes are the six `nu` values plus one unused field
value. Complete their outside incidences from `K_7`: remove edges
`(1,2),(1,3),(4,5)`, duplicate `(0,6)`, and use one singleton at vertex 1.
The outside degrees are `(7,5,5,5,5,5,7)`. The five residual slopes used on
exclusive inverse pairs already have two incidences each, so every residual
row has size seven. Pair multiplicity is at most two, the selected pair
intersects in two points, and all pair unions are therefore at least 12.
The singleton is the unique deficient point. This proves `(IRF1)--(IRF2)`.

Put

```text
P(X)=X,       Q(X)=X^2+1,
lambda_x=P(x)/sigma'_W(x).                            (2)
```

All points of `D` are nonzero, so every `lambda_x` is nonzero. Equation
`(IRF3)` gives `lambda_x nu_x=Q(x)/sigma'_W(x)`. From `(1)`, every coefficient
of `H_x` is an affine combination of `1` and `nu_x`. The barycentric identity

```text
sum_(x in W) F(x)/sigma'_W(x)=0       for deg F<=10
```

therefore annihilates all rows `x^i H_x`, `0<=i<=8`: the relevant numerators
have degree at most `i+2<=10`. Hence `lambda` is an all-nonzero kernel of
`M_W`. Exact elimination gives rank 11, proving `(IRF4)`.

For the extension layer, the locator values are

```text
Q_Y(x)=lambda_x product_(gamma in A_x)(Y-gamma).
```

The exact Reed-Solomon checks `(LEK2)` do not all vanish; equivalently, no
three coefficient vectors extend with `X`-degree at most seven. Exact
elimination of `[M_W;E_W]` gives rank 12, proving `(IRF5)`. Every stated
integer and rank is independently reconstructed by the two verifiers. QED.
