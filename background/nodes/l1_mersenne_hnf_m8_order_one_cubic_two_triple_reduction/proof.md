# Proof - L1 Mersenne HNF m=8 order-one cubic two-triple reduction

Write the cubic interpolant as

```text
E(W)=e_3(W^3+uW^2+vW+w),       e_3!=0.              (1)
```

Let the two distinct colors be `alpha,beta`. Each polynomial `E-alpha` and
`E-beta` has exactly the corresponding three reduced roots. Since `L` is
monic and squarefree of degree six,

```text
L=e_3^(-2)(E-alpha)(E-beta)=e^2-se+t,                (2)
```

where `e=E/e_3`, `s=(alpha+beta)/e_3`, and
`t=alpha*beta/e_3^2`. If

```text
L=W^6+l_1W^5+l_2W^4+l_3W^3+l_4W^2+l_5W+l_6,
```

coefficient comparison in (2) gives

```text
l_1=2u,       l_2=u^2+2v,
l_3=2w+2uv-s,       l_5=v(2w-s).
```

Eliminating `u,w,s` therefore gives the necessary relation

```text
l_5=v(l_3-2uv),
u=l_1/2,       v=(l_2-u^2)/2.                       (3)
```

Let `g` be the degree-seven hypergeometric polynomial before the affine
shift. The order-one HNF formulas give

```text
l_1=6/d,
l_2=(15+rd/2)/d^2,
l_3=(20+rd(d+8)/3)/d^3,
l_5=-6g(1)/(d^5(r-1)).                              (4)
```

For completeness, the last identity follows from
`L=d^(-6)(g(y)/y)|_(y=1+dW)` and

```text
(r-1)g'(1)=(r-7)g(1).                               (5)
```

Here `g(1)!=0` because `L(0)!=0`, and (5) makes `r=1` impossible. Substituting
(4) into (3) gives

```text
v=(12+rd)/(4d^2),
l_3-2uv=(12+rd(2d+7))/(6d^3),                       (6)
```

and hence

```text
144g(1)+(r-1)(12+rd)(12+rd(2d+7))=0.                (7)
```

The order-one curve makes the degree-seven coefficient vanish. The same
truncated-series expansion used in the HNF gives

```text
g(1)=1+r S_1+r^2 S_2+r^3d^3/48,
S_1=(10d^5+62d^4+163d^3+237d^2+213d)/60,
S_2=d^2(13d^2+55d+76)/72.                           (8)
```

Multiply (7) by five and substitute (8). The resulting integer polynomial
factors as

```text
720g(1)+5(r-1)(12+rd)(12+rd(2d+7))
 =r(q_2r^2+q_1r+q_0).                               (9)
```

The inherited saturation has `r!=0`, so division by `r` proves the second
equation in (CTR3). The first is the proved h=7 conic.

The quadratic resultant is (CTR4). Its leading terms are

```text
a_1=35d^2, b_1=154d^3, c_1=120d^4,
q_2=25d^3, q_1=130d^4, q_0=120d^5.
```

Thus the three minors in (CTR4) have respective leading terms
`1200d^7`, `700d^6`, and `2880d^8`. The degree-fourteen coefficient is

```text
1200^2-700*2880=-576000,                            (10)
```

so `R_33` is nonzero of exact degree fourteen. Finally every survivor has
`d^(p+1)=zeta` for some `zeta in mu_8`, proving the necessary gcd endpoint
(CTR5). QED.
