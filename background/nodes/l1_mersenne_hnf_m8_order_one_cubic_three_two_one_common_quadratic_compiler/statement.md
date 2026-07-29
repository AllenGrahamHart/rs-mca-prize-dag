# L1 Mersenne HNF m=8 order-one cubic three-two-one common-quadratic compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `3+2+1`

Retain the notation `(F,G,B,lambda)` from (TOF2). Exact double multiplicity
is equivalent to a monic quadratic `Q` and values `y,z` such that

```text
Q=W^2+uW+v,
G=Q(W)(W-y),
F-B=Q(W)(W-z).                                     (TQC1)
```

Put `a=y-z`. Then

```text
a!=0,
F=G+aQ+B,
aQ(y)=(lambda-1)B.                                 (TQC2)
```

Write

```text
G=W^3+g_1W^2+g_2W+g_3.
```

Equations (TQC1) give

```text
u=g_1+y,
v=g_2+g_1y+y^2,
g_3=-vy.                                            (TQC3)
```

For `L=W^6+l_1W^5+...+l_6=FG`, the coefficient equations are

```text
l_1=2g_1+a,
l_2=g_1^2+2g_2+a(u+g_1),
l_3=2g_3+2g_1g_2+a(v+ug_1+g_2)+B,                 (TQC4)

l_4=g_2^2+2g_1g_3+a(vg_1+ug_2+g_3)+Bg_1,
l_5=2g_2g_3+a(vg_2+ug_3)+Bg_2,
l_6=g_3^2+avg_3+Bg_3.                              (TQC5)
```

The first three equations solve triangularly:

```text
a=l_1-2g_1,
g_2=(l_2-g_1^2-a(2g_1+y))/2,
B=l_3-2g_3-2g_1g_2-a(v+ug_1+g_2).                 (TQC6)
```

After substituting the HNF coefficients and (TQC3), (TQC6), the complete
p-free necessary core consists of (TQC5), the h=7 conic, and the role-color
equation

```text
a(3y^2+2g_1y+g_2)=(lambda-1)B                      (TQC7)
```

in only `(g_1,y,r,d)` for each fixed role value `lambda`. Saturate by
`a*B*(lambda-1)*Q(y)`, the HNF factors, and exact fiber discriminants. No
unit verdict for any of the at most 42 role packets is claimed here.
