# Proof - L1 Mersenne HNF m=8 order-one constant-color exclusion

Write

```text
g(y)=y*gbar(y),       L(W)=d^(-6)gbar(1+dW),
P(W)=(W+1/d)L(W),     d=c-1,       r=rho*c.          (1)
```

The hypergeometric normalization gives

```text
2A=r*d,
2A(g-ell*y)=(y-1)(y-c)(7g-y*g'),       g(1)=ell.     (2)
```

Put `R=g'(1)/g(1)`. Differentiating (2) once at `y=1` gives

```text
(r-1)R=r-7.                                          (3)
```

If

```text
L(W)=W^6+l_1 W^5+l_2 W^4+l_3 W^3+l_4 W^2+l_5 W+l_6,
```

then the top two coefficients and the first logarithmic derivative at one
give

```text
l_1=6/d,
l_2=(30+r*d)/(2d^2),
l_5/l_6=d(R-1)=-6d/(r-1).                            (4)
```

Suppose all six roots `x_i` of `L` have the same color
`epsilon=x_i^(p+1)`. Frobenius sends `x_i` to `epsilon/x_i`; hence

```text
L^[p](W)=W^6 L(epsilon/W)/L(0).                      (5)
```

The `W^5` coefficient in (5), together with
`d^p=zeta/d`, is

```text
(6/d)^p=epsilon*l_5/l_6,
r-1=-epsilon*zeta.                                  (6)
```

Thus, for `alpha=epsilon*zeta`, equation (CCE3) holds. If `alpha=1`, then
`r=0`, contrary to `rho*c!=0`.

Differentiate (2) twice at `y=1`. With `S=g''(1)/g(1)`, one obtains

```text
d(r-2)S=14-2(1+6d)R.                                (7)
```

When `r!=2`, equations (3) and (7) give

```text
l_4/l_6
 =d^2(S-2R+2)/2
 =6d(r+5d)/((r-1)(r-2)).                            (8)
```

The exceptional value `r=2`, equivalently `alpha=-1`, can be handled
directly in (7): its right side is `24+60d`, so `d=-2/5`. This puts `d` in
`F_p`, and then `zeta=d^(p+1)=d^2` lies in
`F_p intersect mu_8={+1,-1}`. It would force `4/25=+1` or `-1`, so the
characteristic would divide `21` or `29`, impossible on the official rows.

It remains to take `alpha!=+1,-1`. The `W^4` coefficient in (5) is

```text
l_2^p=epsilon^2*l_4/l_6.                             (9)
```

Use `r=1-alpha`, `alpha^p=alpha^(-1)`,
`d^p=zeta/d`, and `epsilon=alpha/zeta` in (4), (8), and (9). After cancelling
the nonzero factors, (9) becomes

```text
(1-alpha)[30alpha*d-(alpha+1)zeta-12alpha^2]=0.
```

This proves (CCE4). Every official prime is `7 mod 8`, so
`alpha,zeta in mu_8` lie in `F_(p^2)`. Equation (CCE4) therefore puts
`d` in `F_(p^2)`. Its norm `zeta=d^(p+1)` lies in `F_p`, and consequently

```text
zeta in F_p intersect mu_8={+1,-1}.                 (10)
```

Rewrite (CCE4) as

```text
d=(12alpha+zeta*(1+alpha^(-1)))/30.                 (11)
```

Taking its `F_(p^2)/F_p` norm and writing
`s=alpha+alpha^(-1)` gives exactly

```text
12zeta*s^2+(1+12zeta)s+146-924zeta=0.               (12)
```

For `zeta=1` this is `12s^2+13s-778=0`; at
`s=2,-2,0` its values are `-704,-756,-778`. If `s^2=2`, it becomes
`13s-754=0`, which would make the characteristic divide

```text
754^2-2*13^2=568178.                                (13)
```

For `zeta=-1`, equation (12) is `12s^2+11s-1070=0`; at
`s=2,-2,0` its values are `-1000,-1044,-1070`. If `s^2=2`, it becomes
`11s-1046=0`, which would make the characteristic divide

```text
1046^2-2*11^2=1093874.                              (14)
```

Neither integer is divisible by any of
`8191,131071,524287,2147483647`. These are all possible traces of an
eighth root, so the assumed constant color is impossible. QED.
