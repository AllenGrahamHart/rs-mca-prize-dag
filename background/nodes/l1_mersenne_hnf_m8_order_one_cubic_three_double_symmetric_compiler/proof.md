# Proof - L1 Mersenne HNF m=8 order-one cubic three-double symmetric compiler

Retain

```text
F_i=W^2+u_iW+v_i,       v_i=u_i^2-Uu_i+V,
L=F_1F_2F_3.                                           (1)
```

Newton's identities for the three `u_i` give (TSC1). Comparing the first
three coefficients of the product gives

```text
l_1=sum_i u_i=s_1,
l_2=sum_i v_i+sum_(i<j)u_iu_j=s_1^2-s_2-Us_1+3V,
l_3=s_1s_2-2s_3-2Us_2+2Vs_1.                        (2)
```

The official characteristics are not two or three, so (2) solves exactly
as (TSC2).

For `l_4`, the two types of choices from the three quadratics are

```text
l_4=sum_(i<j)v_iv_j+sum_i v_i u_j u_k.              (3)
```

The first sum is `(A_0^2-B_0)/2`, because `A_0=sum_i v_i` and
`B_0=sum_i v_i^2`. Direct substitution of `v_i=u_i^2-Uu_i+V` gives (TSC3).
The second sum in (3) is `(s_1-3U)s_3+Vs_2`, proving (TSC4).

For the next coefficient,

```text
l_5=sum_i u_i v_jv_k.                                (4)
```

Expanding (4) and collecting elementary symmetric functions gives

```text
s_2s_3-2Us_1s_3+V(s_1s_2-3s_3)
 +3U^2s_3-2UVs_2+V^2s_1,
```

which is (TSC5).

Finally `l_6=product_i v_i`. In each factor choose one of
`u_i^2`, `-Uu_i`, and `V`. Grouping the ten choice types gives, in order,

```text
s_3^2,
-Us_2s_3,
V(s_2^2-2s_1s_3),
U^2s_1s_3,
-UV(s_1s_2-3s_3),
V^2(s_1^2-2s_2),
-U^3s_3,
U^2Vs_2,
-UV^2s_1,
V^3,
```

proving (TSC6).

The dependency supplies the rational HNF coefficients

```text
l_1=6/d,
l_2=(15+rd/2)/d^2,
l_3=(20+rd(d+8)/3)/d^3,
l_4=(15+rd(d^2+7d+23)/4+r^2d^2/8)/d^4,
l_5=-6g(1)/(d^5(r-1)),       l_6=g(1)/d^6.          (5)
```

Insert (5) in (TSC2)--(TSC6). The first three equations eliminate
`s_1,V,s_3`, so the last three involve only `(U,s_2,r,d)`. Every displayed
denominator is invertible on the inherited saturated chamber, and `g(1)`
remains a separate nonzero saturation factor. Clearing the denominators
introduces no survivor. Adjoining the h=7 conic produces the claimed square
p-free system. QED.
