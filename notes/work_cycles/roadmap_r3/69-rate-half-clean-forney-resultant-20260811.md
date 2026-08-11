# Cycle 69: clean Forney resultant normalization (2026-08-11)

## Cycle pins

```text
our start:       56ef2814c
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## Canonical Forney numerator

Write the primitive moving locator and its leading coefficient as

```text
q(t;X)=sum_(j=0)^rho q_j(t)X^j,       a(t)=q_rho(t).
```

The reciprocal locator and the first `rho` syndrome moments define a
canonical numerator

```text
q^vee(t;Z)=Z^rho q(t;Z^(-1)),
N(t;Z)=[q^vee(t;Z)sum_(i=0)^(rho-1)y_i(t)Z^i]_(<rho),
P(t;X)=X^(rho-1)N(t;X^(-1)).
```

It has bidegree at most `(rho-1,m+1)`. At a squarefree supported
specialization, if

```text
q(gamma;X)=a(gamma)product_(x in S_gamma)(X-x),
y_i(gamma)=sum_(x in S_gamma)theta_(gamma,x)x^i,
```

then every weight is nonzero and

```text
P(gamma;x)=theta_(gamma,x)partial_X q(gamma;x).
```

## Resultant collapse

The same rectangular-pencil compound used by the marked adjugate theorem
gives the top-square identity

```text
adj H_0(t)=c_0 a(t)Delta(t)q(t)q(t)^T.
```

Its corner cofactor and the Forney evaluation formula imply

```text
c_0 Delta(gamma)a(gamma)^3
 =Vandermonde(S_gamma)^2 product_(x in S_gamma)theta_(gamma,x).
```

Homogeneity of the formal degree-`(rho,rho-1)` Sylvester determinant then
removes all apparent quadratic parameter degree:

```text
Res_X^(rho,rho-1)(q(t;X),P(t;X))
 =c_1 a(t)^(2rho+2)Delta(t),
deg Delta=m-1.
```

Thus the large Forney resultant carries no unknown high-degree factor. The
only unprinted motion is the degree-`m-1` regular determinant `Delta`. The
normalization and exponent were independently replayed on the exact `m=1`,
`F_17` pencil, where the resultant is constant on all 17 parameters.

The proved node is
`rate_half_ca_hankel_clean_endpoint_forney_resultant_regular_factor`.

## Burn-down

```text
result:                  NARROWED; exact normalized Forney resultant
DAG delta:               +1 PROVED leaf, +1 req edge, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next theorem must exploit that the Forney products at at least `2m+3`
good supported slopes interpolate the single degree-`m-1` polynomial
`Delta`. The normalization itself is an identity and supplies no value
bound; a contradiction must use shared supported-root incidence and the
degree-`m` coefficient motion of `q`.
