# Proof - L1 Mersenne HNF order-zero quadratic collision router

Write

```text
E_s(W)=A W^2+B W+C,       A!=0,       S=-B/A.        (1)
```

Every two-point fiber of `E_s` has root sum `S`. Let `x,y` be the roots in a
repeated color `epsilon`. Since `E_s(x)=x^(p+1)=epsilon`,

```text
x^p=epsilon/x,       y^p=epsilon/y,
xy=(C-epsilon)/A.                                    (2)
```

Taking the `p`th power of `x+y=S` and using `(2)` gives

```text
S^p(C-epsilon)=A epsilon S.                          (3)
```

If two distinct colors `epsilon_1,epsilon_2` are repeated, subtracting their
two equations gives

```text
S^p+A S=0,       C S^p=0.                            (4)
```

Thus either `S=0`, in which case every repeated pair is antipodal, or
`S!=0` and `C=0`.

Assume the latter. For every root `x` of `P_s`,

```text
x^p=E_s(x)/x=A x+B.                                  (5)
```

Put `t=s^p`. Frobenius sends the roots of `P_s` to those of `P_t`, so the
affine map `phi(W)=AW+B` carries the first root set to the second.

The truncated-binomial polynomial has the coefficientwise differential
identity

```text
W(W-1)P_u'(W)=(hW-h-u)P_u(W)+(h+u)P_u(0).           (6)
```

At a root its weighted derivative is therefore the same nonzero constant.
Using the affine root transport and the derivative scaling between `P_s`
and `P_t`, there is one nonzero scalar `lambda` such that every root `x` of
`P_s` satisfies

```text
(Ax+B)(Ax+B-1)=lambda x(x-1).                        (7)
```

The difference in `(7)` has degree two and at least seven roots, so it is
the zero polynomial. Its constant term gives `B in {0,1}`. Comparing the
linear and quadratic terms then gives exactly

```text
(A,B)=(1,0)       or       (A,B)=(-1,1).             (8)
```

The first case makes `t=s`, contrary to `s notin F_p`. In the second case,
`x^p=1-x`, so

```text
E_s(x)=x(1-x),       P_s(W) | [W(1-W)]^m-1.          (9)
```

Exact monic division by `P_s` gives the following coefficient of
`W^(h-1)` in the remainder. For `(m,h)=(8,7)` it is

```text
s(s+1)(s+2)(s+3)^2(s+4)^2(s+5)(s+6)(s+7)/22400,    (10)
```

and for `(m,h)=(16,15)` it is

```text
17 s(s+1)...(s+15)(s+7)(s+8)/188305108992000.       (11)
```

The repeated factors in `(11)` are in addition to those in the displayed
product. Every denominator is invertible at the official characteristic.
Vanishing of either coefficient puts `s` in `F_p`, a contradiction. Hence
the `S!=0` case is impossible, proving the first assertion.

It remains to sharpen the four `m=8` rows. Write the odd and even parts of
`P_s` as

```text
P_s(W)=W O_s(W^2)+V_s(W^2),
O_s(Y)=Y^3+b_2Y^2+b_4Y+b_6,
V_s(Y)=sY^3+b_3Y^2+b_5Y+b_7,
b_r=binom(s+r-1,r).                                  (12)
```

Two antipodal root pairs would make `O_s` and `V_s` have a common divisor of
degree at least two. Put `R_s=V_s-sO_s`. Since `s notin F_p`, `R_s` has
degree two, with leading coefficient `-s(s-1)(s+1)/3`. The common quadratic
would therefore be a scalar multiple of `R_s`, so `R_s` would divide
`O_s`. But exact pseudo-division gives the coefficient of `Y` in
`prem_Y(O_s,R_s)` as

```text
-s^2(s-3)(s-2)(s-1)^2(s+1)^2(s+2)(s+3)/4725.       (13)
```

It cannot vanish when `s notin F_p`. Thus there are not two antipodal pairs.
Together with the first assertion, a quadratic color interpolant on an
`m=8` row has at most one repeated color. QED.
