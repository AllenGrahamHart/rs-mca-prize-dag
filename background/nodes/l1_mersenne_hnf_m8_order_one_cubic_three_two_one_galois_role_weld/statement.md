# L1 Mersenne HNF m=8 order-one cubic three-two-one Galois-role weld

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler`, `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_role_weld`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `3+2+1`

Let `X` be an indeterminate. The complete degree-42 ordered role polynomial
has the following twelve rational Galois packets:

```text
P_1=X^2+1,
P_2=X^2-2X+2,
P_3=2X^2-2X+1,

P_4=X^4-4X^3+6X^2-4X+2,
P_5=X^4-4X^3+8X^2-4X+1,
P_6=X^4-4X^3+12X^2-16X+8,
P_7=X^4+6X^2+1,
P_8=X^4+2X^2-4X+2,
P_9=X^4+1,
P_10=2X^4-4X^3+6X^2-4X+1,
P_11=2X^4-4X^3+2X^2+1,
P_12=8X^4-16X^3+12X^2-4X+1.                (GRW1)
```

More precisely,

```text
Gamma_321(X)=product_(j=1)^12 P_j(X)                 (GRW2)
```

is a nonzero rational scalar multiple of `Lambda_321(X)`. The three
quadratic packets correspond to the ordered exponent-pair orbits represented
by `(2,6),(2,4),(4,2)`. The nine quartic packets, in the displayed order
`P_4,...,P_12`, correspond to

```text
(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
(2,1),(2,3),(4,1).                                  (GRW3)
```

Retain `R,S` from (TRW1). For a packet of degree `e_j`, define

```text
widehat P_j(R,S)=S^e_j P_j(1+R/S).                  (GRW4)
```

This is a homogeneous polynomial of degree `e_j<=4`. On `R*S!=0`, the union
of the four high-degree welded role systems (TRW4) may equivalently be
refined to the following disjunction of twelve low-degree role systems:

```text
OR_(j=1)^12 [widehat P_j(R,S)=0].                   (GRW5)
```

In branch `j`, this one role equation is imposed together with the same
three coefficient equations (TQC5) and conic in `(g_1,y,r,d)`. This is an
exact lower-degree packet refinement, not twelve simultaneous constraints
and not a unit verdict.
