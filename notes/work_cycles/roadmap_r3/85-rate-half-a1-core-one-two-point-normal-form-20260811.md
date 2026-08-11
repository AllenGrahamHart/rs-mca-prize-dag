# Cycle 85: first core-one packet becomes a two-point Picard obstruction (2026-08-11)

## Cycle pins

```text
our start:       9edee075f
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
compute:         symbolic only
critical open:   28
```

## Two-point normal form

The packet `(u,v,I_0,c)=(0,2,0,2)` exhausts all regular defect at one
distinguished row. Omission and local cube multiplicities force

```text
D=P_ord L_alpha L_beta,
Qbar(U,V;x_*)=P_ord L_alpha^2 L_beta^2.
```

The squarefree adjugate factor is the row radical. The Forney specialization
is `D` times a nonzero cubic, while the first `X`-jet is `P_ord` times a
quartic. The contact divisor is the vertical fibre with one copy removed at
each doubled point, so

```text
O_C(rho+2,-e-1)=O_C(P_alpha+P_beta).
```

This is an effective line bundle of degree two. The proved leaf is
`rate_half_ca_hankel_a1_first_degree_core_one_gap_zero_two_point_normal_form`.

## Burn-down

```text
result:                  REDUCED first tangent packet to degree-two Picard data
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next decide whether the extreme bidegree line bundle in the two-point
relation can be effective on a reduced core-one Hankel kernel curve, then
extend the normal form to the other five packets.
