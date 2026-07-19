# Proof

Assume `K=0`. The first weld identity becomes

```text
WB=B_XE_Z.                                             (1)
```

The right side is a squarefree product of distinct linear factors in the two
separate variable groups. Unique factorization therefore gives

```text
W=w_Xw_Z,       B=b_Xb_Z,
w_Xb_X=B_X,     w_Zb_Z=E_Z.                            (2)
```

Since `deg E_Z=D_*<=1`, its possible linear factor is allocated wholly to
one of `W,B`.

## 1. The degree obstruction

The second weld identity with `K=0` is

```text
VB+AE_Z=0.                                             (3)
```

If the exceptional factor is absent or allocated to `B`, equations
`(2),(3)` and the domain complement show that `Q_*` divides

```text
P(U,V)-g(X),                                           (4)
```

where `deg P=T=4e+1`. If the nonconstant exceptional factor is allocated to
`W`, it divides `V`; after cancellation `Q_*` divides

```text
P_cl(U,V)-g(X),                                        (5)
```

where `deg P_cl=T-1=4e`.

Let `t_0` be the parameter degree in `(4)` or `(5)`, and let `g_0=deg g`.
On the normalization of the irreducible curve `Q_*=0`, equality of the two
separated functions gives

```text
t_0*r=g_0*e_*.                                         (6)
```

Since `r=2e_*+1` is coprime to `e_*`, equation `(6)` forces `e_*|t_0`.

Write `e=e_*+b`. The component theorem gives `b<=floor(e/5)`, and official
`e=3 mod 5`, so

```text
0<4b+1<e_*,       0<=4b<e_*.                           (7)
```

For `(4)`, one has

```text
t_0=4e+1=4e_*+(4b+1),
```

contradicting divisibility in `(6)`. For `(5)`,

```text
t_0=4e=4e_*+4b.
```

It is divisible by `e_*` only when `b=0`. Hence `K=0` forces a nonconstant
`E_Z`, allocated to `W`, together with `b=0`. This proves `(ZWB2)` and all
claims in `(ZWB6)`.

## 2. The quartic boundary

Now `e_*=e`, `r=2e+1`, and `t_0=4e`. Equation `(6)` gives

```text
g_0=4r=8e+4.                                           (8)
```

Factor `E_Z` from `W` and `V`, writing

```text
W=w_XE_Z,       V=V_0E_Z.
```

The domain complement cancels to

```text
Q_*V_0+P_Xw_X=P_cl.                                   (9)
```

The product `G_0=P_Xw_X` consists of residual-domain factors. Since
`D_0=8e+7`, equation `(8)` says exactly three factors remain in
`b_X=B_X/w_X`; hence `G_0` is squarefree and supported on all but three
points of `D\S`. Equation `(9)` is `(ZWB4)`.

The total separated difference has bidegree `(8e+4,4e)=4(r,e)`. Division by
the bidegree `(r,e)` component leaves `(3r,3e)=(6e+3,3e)` for `V_0`, proving
`(ZWB5)` and completing the proof. QED.
