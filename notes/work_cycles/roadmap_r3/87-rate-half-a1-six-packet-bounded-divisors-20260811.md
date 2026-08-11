# Cycle 87: all tangent packets have bounded divisor tails (2026-08-11)

## Cycle pins

```text
our start:       ef7624af6
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
compute:         none
critical open:   28
```

## Uniform normal form

For every core-one scalar packet, the distinguished row has deficit
`c=2+u+I_0<=6`. Its squarefree supported locator `P_*` factors all large
objects:

```text
Qbar(U,V;x_*)=P_* K_c,            deg K_c<=6;
D=P_* E_(c-2),                    deg E_(c-2)<=4;
N_F(U,V;x_*)=P_* C_(c+1),         deg C_(c+1)<=7.
```

The contact divisor leaves only

```text
O_C(rho+2,-e-1)=O_C(Z_c-R_0-E_u),
deg Z_c<=6,       deg(R_0+E_u)<=4,
deg(Z_c-R_0-E_u)=2.
```

The first packet is the effective two-point special case. The other five
are signed bounded-divisor packets. The proved leaf is
`rate_half_ca_hankel_a1_first_degree_core_one_six_packet_bounded_divisor_normal_form`.

## Burn-down

```text
result:                  REDUCED all six tangent packets to degree <=7 data
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next classify the bounded signed divisors using the adjugate and Forney
tails, and derive the matching core-free bounded-divisor form.
