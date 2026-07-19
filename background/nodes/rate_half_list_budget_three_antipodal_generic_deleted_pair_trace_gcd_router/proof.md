# Proof

Put `u=r^2`, as in the preceding trace router. Since

```text
x=(u+u^(-1))/2,
x-1=(u-1)^2/(2u),       x+1=(u+1)^2/(2u),           (1)
```

either equality `x=1` or `x=-1` would give `t=u^2=1`. Hence `x^2!=1` on
the retained deleted-pair branch.

Chebyshev composition gives

```text
T_(8L)(y)=T_(4L)(2y^2-1)=T_(4L)(x).                (2)
```

Using

```text
T_(4L)(x)=2T_(2L)(x)^2-1,
T_(2L)(x)^2-1=(x^2-1)U_(2L-1)(x)^2,                (3)
```

equation `(2)` equals `-1` exactly when `T_(2L)(x)=0`. It equals `1`
exactly when `(x^2-1)U_(2L-1)(x)^2=0`, which is equivalent to
`U_(2L-1)(x)=0` by `(1)`. This proves `(TGR3)`.

On `C(x)=0`, polynomial division gives `P(x)=R(x)`. For branch zero, the
signed equation is equivalent to

```text
P+s=2sy.                                             (4)
```

Using `x+1=2y^2`, squaring `(4)` gives `E_(0,s)=0`. Conversely, from that
equation define `y=(R+s)/(2s)`. Then `x=2y^2-1` and `(4)` hold, so the
signed branch is recovered.

Branch one can be written

```text
(P-s)y=P+s.                                         (5)
```

The value `P=s` cannot satisfy it in odd characteristic. Substitution of
`y=(P+s)/(P-s)` into `x+1=2y^2` gives exactly `E_(1,s)=0`. Conversely,
`E_(1,s)=0` cannot have `P=s`, because its value there is `8s^2`. Thus the
second formula in `(TGR6)` is defined and reverses the calculation.

Likewise branch two is

```text
(P-s)y=-2s.                                         (6)
```

Substitution of `y=-2s/(P-s)` gives `E_(2,s)=0`. At `P=s` the latter has
value `-8s^2`, so the denominator is again necessarily nonzero and the
calculation reverses.

In every converse, `(TGR3)` turns `G_epsilon(x)=0` back into the source
trace equation. The official split field contains the relevant dyadic
source lifts, so the reconstructed trace stays within the stated branch.
This proves `(TGR5)--(TGR6)`.

Finally, replacing a polynomial by its remainder modulo `C` does not change
its values on `C=0`. Three univariate polynomials have no common root over
the algebraic closure exactly when their monic gcd is one. This proves
`(TGR7)`. QED.
