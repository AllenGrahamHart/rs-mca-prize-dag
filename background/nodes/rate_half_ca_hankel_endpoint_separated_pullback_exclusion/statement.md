# Separated-pullback exclusion at the strict endpoint

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Use the official strict endpoint

```text
m=2^37,       N=16m,       T=4m+1,
```

and let the dominant irreducible component supplied by
`rate_half_ca_hankel_endpoint_component_defect_localization` have bidegree

```text
(r,e)=(4e-1,e),
ceil((3m+1)/4)<=e<=m.                                (SPX1)
```

This component is not a separated rational pullback.  More precisely, there
do not exist rational maps over the algebraic closure

```text
f:P^1_X -> P^1,       deg f=r,
g:P^1_(U:V) -> P^1,   deg g=e,                       (SPX2)
```

whose fiber-product equation

```text
f(X)=g(U:V)                                             (SPX3)
```

is the dominant component.

The obstruction uses only the exact grid defect.  If a separated pullback
existed, its number `I_*` of zeros on `D x Z` would satisfy

```text
C_*=N*e-I_*>m,                                        (SPX4)
```

whereas component-defect localization proves

```text
0<=C_*<=sum_i C_i=1+O-E<=m.                           (SPX5)
```

Thus the remaining nonlinear cover cannot arise by equating one rational
function of the domain variable with one rational function of the parameter.
This includes polynomial separated-variable and Kummer pullback models.  The
theorem does not exclude a genuinely mixed biform.

Equivalently, the dominant component has separation rank at least three.  If

```text
Q_*(U,V;X)=sum_(j=1)^h A_j(X)B_j(U,V)                 (SPX6)
```

with each `A_j` of degree at most `r` and each `B_j` homogeneous of degree
`e`, then every such expression has `h>=3`.  In particular both coefficient
spans of the dominant biform have dimension at least three.

The full primitive generator `Q`, of bidegree `(4m-1,m)`, also has
separation rank at least three.  A rank-two expression would define rational
maps of degrees `4m-1` and `m`; applying the same capacity bound with

```text
q=4,       s=1,       L=4
```

would give total column deficit at least `4(m-1)>m`, contradicting its exact
value `1+O<=m`.
