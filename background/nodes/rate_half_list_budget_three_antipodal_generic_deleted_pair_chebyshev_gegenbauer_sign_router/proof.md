# Proof

Write `u=r^2`, so `t=r^4=u^2` and

```text
x=(u+u^(-1))/2=2((r+r^(-1))/2)^2-1=2y^2-1.          (1)
```

The Gegenbauer generating function gives

```text
((1-z)(1-tz))^(-1/4)
 =(1-2x(uz)+(uz)^2)^(-1/4)
 =sum_(n>=0)u^n C_n^(1/4)(x)z^n.                    (2)
```

Therefore `F_L(t)=u^L C_L^(1/4)(x)`. Since `u` is nonzero, the primary gap
`F_L(t)=0` is exactly the last equation in `(CGR2)`.

The source normalization has `r^(32M)=r^(16L)=1`. Hence

```text
epsilon=r^(8L) in {1,-1}.                            (3)
```

The defining identity

```text
T_n((r+r^(-1))/2)=(r^n+r^(-n))/2                    (4)
```

then gives `T_(8L)(y)=epsilon`, proving the remaining equations `(CGR2)`.

Apply the same generating-function calculation with exponent `-1/2`:

```text
H_n(t)=u^nP_n(x).                                    (5)
```

At `n=2L-1`, equations `(3),(5)` give

```text
tH_n(t)^2=u^2u^(2n)P_n(x)^2
          =u^(4L)P_n(x)^2
          =r^(8L)P_n(x)^2=epsilon P^2,              (6)
```

which is `(CGR3)`.

Finally `chi=r+r^(-1)=2y`. Substitute `(6)` into `(LCC6)`. Branch zero is
the first equation `(CGR4)` directly. Branches one and two have a common
nonzero factor four; dividing it gives the other two equations.

Because `epsilon^2=1` and `s^2=-epsilon`, every expression in `(CGR4)` has
the factorization

```text
epsilon(A^2-s^2B^2)=epsilon(A-sB)(A+sB),             (7)
```

with `(A,B)` equal to `(P,2y-1)`, `(P(y-1),y+1)`, or
`(Py,y-2)`. The characteristic is odd and both square roots `s` are present
in the official base field. Equation `(7)` proves the exact equivalence with
the six choices in `(CGR5)`. QED.
