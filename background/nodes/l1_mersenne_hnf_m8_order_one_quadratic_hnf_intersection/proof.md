# Proof - L1 Mersenne HNF m=8 order-one quadratic HNF intersection

For `2<=j<=6`, put

```text
q_j=((1+d)^(j-1)-1)/j.                              (1)
```

The logarithm of the hypergeometric series has coefficient `r*q_j` in
degree `j`. Since the degree-seven coefficient vanishes on the order-one
curve, the value of the degree-seven polynomial at one is

```text
g(1)=1+r S_1+r^2 S_2+r^3 d^3/48,                   (2)
```

where

```text
S_1=q_2+q_3+q_4+q_5+q_6
   =(10d^5+62d^4+163d^3+237d^2+213d)/60,

S_2=(q_2+q_3)^2/2+q_2q_4
   =d^2(13d^2+55d+76)/72.                           (3)
```

The pointwise-composition dependency gives `g(1)=(1-r)^3`. Subtract this
from (2), divide by the nonzero factor `r`, and multiply by `720`. The
result is the first quadratic in (QHI3), with coefficients (QHI1).

The residual conic equation in `(r,d)` is

```text
35d^2r^2+14d(11d^2+27d+27)r
 +120(d^4+4d^3+7d^2+6d+3)=0,                       (4)
```

which is the second quadratic in (QHI3). The resultant of
`a_0r^2+b_0r+c_0` and `a_1r^2+b_1r+c_1` is exactly the expression in
(QHI4), proving that every survivor has `R_2(d)=0`.

The leading terms are

```text
a_0=15d^3, b_0=130d^4, c_0=120d^5,
a_1=35d^2, b_1=154d^3, c_1=120d^4.
```

Thus the degree-fourteen coefficient in (QHI4) is

```text
(1800-4200)^2-(2310-4550)(15600-18480)
 =5760000-6451200=-691200,                          (5)
```

so `R_2` is nonzero of exact degree fourteen.

Finally every outer survivor has `d^(p+1)=zeta` with `zeta^8=1`. Hence it
gives a common root in one gcd from (QHI5). Unit gcds for all eight colors
exclude the complete quadratic chamber on that row. No converse is claimed.
QED.
