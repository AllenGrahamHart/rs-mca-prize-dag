# Proof - L1 Mersenne HNF m=8 order-one base-field branch exclusion

The dependency already excludes the base-field-parameter branch at
`p=8191,131071`. Retain one of the two residual rows. It gives

```text
c^p=c^(-1),       rho^p=-c rho,       h=7.            (1)
```

Write `d=c-1` and

```text
U_(rho,c)(T)=(1-T)^(c rho)(1-cT)^(-rho).
```

Using (1),

```text
U_(rho^p,c^p)(T)
 =(1-T)^(-rho)(1-c^(-1)T)^(c rho)
 =U_(rho,c)(c^(-1)T).                                (2)
```

If `g(y)=sum_(r=0)^h u_r y^(h-r)`, equation (2) gives

```text
g^[p](y)=c^(-h)g(cy).                                (3)
```

Moreover `d^p=c^(-1)-1=-d/c`. From

```text
P(W)=d^(-h)g(1+dW)
```

and odd `h=7`, equations (3) give

```text
P^[p](W)
 =(-d/c)^(-h)c^(-h)g(c-dW)
 =-d^(-h)g(1+d(1-W))
 =-P(1-W),                                            (4)
```

which is (BBE1).

The inherited cyclotomic condition is `P | W^n-1`. Frobenius preserves that
divisibility, so `P^[p] | W^n-1` as well. Hence every root `x` of `P` has

```text
x^n=1,       (1-x)^n=1.                              (5)
```

Both factors are nonzero.

Put

```text
a=x^(p+1),       b=(1-x)^(p+1).                      (6)
```

Then `a^8=b^8=1`. Also `x^p=a/x` and
`1-x^p=b/(1-x)`. Eliminating `x^p` gives

```text
x^2-(1+a-b)x+a=0.                                    (7)
```

Because `p=7 mod 8`, all eighth roots lie in `F_(p^2)`. Equation (7) puts
`x` in `F_(p^4)`. The exact two-adic order is

```text
v_2(p^4-1)
 =v_2(p-1)+v_2(p+1)+v_2(p^2+1)
 =1+q+1=q+2.                                         (8)
```

Since `x` and `1-x` have power-of-two order, (8) sharpens (6) to

```text
a,b in mu_4.                                         (9)
```

Let `A=1+a-b`. Equation (7) and `x^p=a/x` give
`x^p=A-x`. Since `A in F_(p^2)`, applying Frobenius twice gives

```text
x^(p^2)=x+(A^p-A).
```

Applying it twice more and using `x in F_(p^4)` yields
`2(A^p-A)=0`; hence `A in F_p`. Frobenius acts by inversion on `mu_4`, so

```text
a-a^(-1)=b-b^(-1).                                   (10)
```

Equation (10) leaves six color pairs:

```text
a,b in {+1,-1},       or       a=b=+i,       or a=b=-i. (11)
```

The two imaginary pairs are impossible. There `A=1`, so `x^p=1-x` and
therefore `x^(p^2)=x`; but then `a=x^(p+1)` is a norm into `F_p`, whereas
`+/-i` is not in `F_p` because `p=3 mod 4`.

For `(a,b)=(1,1)`, equation (7) is `x^2-x+1=0`, whose roots have order six,
contradicting the power-of-two order in (5). The remaining three pairs are

```text
(a,b)=(1,-1), (-1,1), (-1,-1).                       (12)
```

Each contributes at most two roots of its quadratic (7), for at most six
possible values of `x` in total. But `P` is a degree-seven divisor of the
separable polynomial `W^n-1`, so it has seven distinct roots. This
contradiction closes both residual rows and hence the complete base-field
parameter branch. QED.
