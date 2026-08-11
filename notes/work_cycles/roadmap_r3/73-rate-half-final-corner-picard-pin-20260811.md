# Cycle 73: final strict-corner Picard pin (2026-08-11)

## Cycle pins

```text
our start:       a60919fdf
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## Pole-length descent

In the sole corner

```text
rho=3e+1,       T=rho+2,       delta=1,       O<=1,
```

the actual pole length `d` of `G/H` is zero or one. A section of `O(d,0)`
clears it. Three copies of the degree-one contact section then lie in

```text
O_C(rho-5+d,0).
```

The restriction kernel is `O(-5+d,-e)`, whose `H^0` and `H^1` vanish.
Therefore the product descends uniquely to a nonzero univariate section:

```text
s_F^3(FG/H)=A_d(X),       deg A_d<=rho-5+d.
```

## Component collapse

An `X`-only polynomial cannot vanish identically on a mixed component. The
identity therefore forces `s_F` to be nonzero on every component. For a
component of bidegree `(r_i,e_i)`, put `a_i=4e_i-r_i`. Its contact degree is

```text
l_i=e e_i-(e+1)a_i>=0,
sum_i l_i=1.
```

The equation `l_i=0` would make `e+1` divide `e_i`, impossible for
`1<=e_i<=e`. Every component has positive contact degree, so total degree
one permits exactly one component. The curve is absolutely irreducible and

```text
O_C(-rho-3,e+1)=O_C(P_*)
```

for one effective Cartier point `P_*`.

The proved node is
`rate_half_ca_hankel_strict_a3_final_corner_integral_picard_pin`.

## Burn-down

```text
result:                  NARROWED final corner to one integral divisor identity
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next theorem should compare the divisor of `A_d(X)` with the supported
grid divisor. The exact alternatives are only `d=0` and `d=1`; no component
classification or broad parameter sweep remains.
