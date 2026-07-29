# L1 Mersenne HNF m=8 order-one cubic three-double symmetric compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_factor_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `2+2+2`

Let `s_1,s_2,s_3` be the elementary symmetric functions of
`u_1,u_2,u_3`, and put

```text
p_1=s_1,
p_2=s_1^2-2s_2,
p_3=s_1^3-3s_1s_2+3s_3,
p_4=s_1^4-4s_1^2s_2+2s_2^2+4s_1s_3.                (TSC1)
```

Write `L=W^6+l_1W^5+...+l_6`. The first three coefficient equations in
the structured factorization are triangular:

```text
s_1=l_1,
V=(l_2-s_1^2+s_2+Us_1)/3,
s_3=(s_1s_2-2Us_2+2Vs_1-l_3)/2.                    (TSC2)
```

Define

```text
A_0=p_2-Up_1+3V,
B_0=p_4-2Up_3+(U^2+2V)p_2-2UVp_1+3V^2.             (TSC3)
```

The remaining three coefficient equations are exactly

```text
l_4=(A_0^2-B_0)/2+(s_1-3U)s_3+Vs_2,                (TSC4)

l_5=s_2s_3-2Us_1s_3+V(s_1s_2-3s_3)
     +3U^2s_3-2UVs_2+V^2s_1,                       (TSC5)

l_6=s_3^2-Us_2s_3+V(s_2^2-2s_1s_3)+U^2s_1s_3
     -UV(s_1s_2-3s_3)+V^2(s_1^2-2s_2)-U^3s_3
     +U^2Vs_2-UV^2s_1+V^3.                         (TSC6)
```

Substituting the known HNF coefficients and (TSC2), then clearing powers
of `2`, `3`, `d`, and `r-1` while retaining the inherited saturation
`g(1)!=0`, turns (TSC4)--(TSC6) into three explicit polynomial equations
in only

```text
(U,s_2,r,d).                                         (TSC7)
```

Together with the h=7 conic this is a square p-free core. A unit saturation
closes `2+2+2`; retained points must then pass the color-ratio, norm-color,
assignment-preserving Frobenius, cyclotomic, and inner tests.

No unit verdict or claim about another cubic profile is made here.
