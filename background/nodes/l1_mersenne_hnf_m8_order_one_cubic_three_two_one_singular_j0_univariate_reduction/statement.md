# L1 Mersenne HNF m=8 order-one cubic three-two-one singular-J0 univariate reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the determinant-singular `J=0` arm of the official h=7 cubic `3+2+1` profile

Put

```text
A(q)=q^2+132q+2916,
T(q)=-144q.                                          (JUR1)
```

On the inherited `q!=0` saturation, `F_J=0` forces `A(q)!=0` and is
equivalent to

```text
d=T(q)/A(q)=-144q/A(q).                              (JUR2)
```

Define

```text
B(q)=q^3+126q^2+5364q+87480,

P_W(q)=A(q)^2 B(q)+72576q^2A(q)-1492992q^3,          (JUR3)

P_C(q)=35q^2A(q)^4
 +14q(11T(q)^2A(q)^2+27T(q)A(q)^3+27A(q)^4)
 +120(T(q)^4+4T(q)^3A(q)+7T(q)^2A(q)^2
       +6T(q)A(q)^3+3A(q)^4).                       (JUR4)
```

Then `P_W` is monic of degree seven and `P_C` has degree ten with leading
coefficient 35. The three bivariate equations

```text
F_J(q,d)=F_W(q,d)=Conic(q,d)=0                      (JUR5)
```

are exactly equivalent to

```text
P_W(q)=P_C(q)=0,       d=-144q/A(q),                (JUR6)
```

on `q!=0`. Therefore, for each official characteristic `p`, a unit gcd

```text
gcd_Fp(P_W,P_C)=1                                    (JUR7)
```

excludes the entire determinant-singular `J=0` coefficient chamber before
`E_6`, role, norm, or lift tests. A nonunit gcd supplies only finite
candidate `q` values, each with the unique reconstructed `d`; all remaining
filters still apply. No gcd verdict is claimed here.
