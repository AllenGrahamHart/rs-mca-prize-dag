# Proof

The independent source reconstruction uses the edge pair

```text
fixed-moving:  (2,1/2), (2,b),
moving-moving: (2,b),   (2,1/b).
```

These are literally `{E01,E02}` and `{E02,E03}`, proving the source-axis
identification.

Let the residual quadratic at a root `r` of `q` be

```text
L_r W^2 + M_r W + C_r,
```

with `L_r != 0` on the declared quadratic-target chart. The local pair
compiler imposes the following equations after evaluation at `r`:

```text
same:  r M_r + 2 L_r = 0,       r^2 C_r - L_r = 0;
swap:  p M_r + 2 r L_r = 0,     p^2 C_r - r^2 L_r = 0;
mixed: p M_r - t L_r = 0,       p C_r - L_r = 0.   (1)
```

For `same`, division by `L_r` gives coefficients
`(1,-2/r,1/r^2)`, so the target is `(W-1/r)^2`. At `c,d` this is the
identity distribution `R20`.

For `swap`, let `s=p/r` be the other root. Equation `(1)` gives
`(1,-2/s,1/s^2)`, so the target at `r` uses the reciprocal of the other
root. This is the crossed distribution `R02`.

Finally `t=-(c+d)` and `p=cd`. The mixed equations give

```text
M_r/L_r=t/p=-(1/c+1/d),      C_r/L_r=1/(cd),
```

at both roots. Hence both residuals are proportional to
`(W-1/c)(W-1/d)`, which is `R11`. This proves `(KBCW-1)--(KBCW-2)`.

It remains to delimit the scope. Every nondegenerate map

```text
g(x)=(a x+b)/(b x+a)
```

commutes with inversion. Take `a=2`, `b=1`, and `c=3`. Then

```text
g(c)=7/5,        g(1/c)=5/7=1/g(c).
```

If the endpoint coordinate is normalized by `g` while `W` is fixed, the
target square changes from `(W-1/3)^2` to `(W-5/7)^2`; the two monic
quadratics are not projectively proportional. Applying `g` to `W` repairs
that target but also moves the source `W` divisor. Consequently endpoint
orbit transitivity alone is not covariance of the full source/q-slice
system. Only literal symmetries proved for the complete system may transfer
a cell. QED.
