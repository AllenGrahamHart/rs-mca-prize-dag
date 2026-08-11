# Proof

By the no-fixed-factor condition at `s=0`, every `Q_Y(x)` is a nonzero
polynomial of degree at most `m`. Its distinct supported roots are exactly
the members of `A_x`. The factor theorem therefore gives

```text
Q_Y(x)=A_x(Y)R_x(Y)
```

with `R_x!=0` and

```text
deg R_x<=m-d_x=Delta_x.
```

This proves `(DCK3)`.

The apolar relation for the joint representation is, coefficientwise,

```text
sum_(x in D) L_x(Y) Q_Y(x) x^i=0,       0<=i<=4m.     (1)
```

Outside `W`, both coordinates of the representation vanish and hence
`L_x=0`. Substituting `(DCK3)` into `(1)`, expanding each `R_x`, and taking
the coefficient of `Y^j` gives

```text
sum_(x in W) sum_(t=0)^Delta_x
 r_(x,t) x^i [Y^j](L_x A_x Y^t)=0
```

for every `0<=j<=m+1`. These are precisely the rows of `(DCK5)`.

For `x in W`, `L_x` is nonzero by definition of joint support, and `R_x` is
nonzero by `(DCK3)`. Thus every coordinate block of `r` is nonzero; in
particular `r` itself is nonzero and `rank(M_W)<=U_W-1`.

Counting the coefficients of `R_x` gives

```text
U_W=sum_(x in W)(Delta_x+1)=|W|+Delta_W.
```

The saturation identity `(DCK1)` gives

```text
Delta_W<=sum_(x in D)Delta_x=1+O<=m,
```

proving `(DCK6)`. If `O=0`, the nonnegative integer deficits sum to one, so
exactly one domain point has `Delta_x=1` and all others have zero deficit.
The two cases in `(DCK7)` follow. QED.
