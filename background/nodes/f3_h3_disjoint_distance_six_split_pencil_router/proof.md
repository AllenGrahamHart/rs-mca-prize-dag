# Proof

Suppose first that `t=(1-x)(1-y)` and put `r=xy`. Expanding gives

```text
x+y=1+r-t.
```

Hence `x,y` are the roots of `Q_(t,r)`. Conversely, if
`Q_(t,r)=(X-x)(X-y)` with `x,y in H\{1}`, its sum and product coefficients
give

```text
(1-x)(1-y)=1-(x+y)+xy=t.
```

The parameter is necessarily `r=xy`, so the maps are inverse. An unordered
pair with distinct entries contributes two ordered pairs to `P(t)`, while a
repeated pair contributes one. This proves `(DSP2)--(DSP3)`.

For a generic representation `E={x,y}`, its coefficient vector is

```text
v_E=+xy-x-y
```

and has three unit signed atoms. Two generic representations in one product
fiber cannot share a root: after cancelling the common nonzero shifted
factor, their other roots agree as well. They are then the same unordered
representation. Therefore two distinct generic members indexed by `r,s`
have squared distance six and disjoint support exactly when their two
three-coordinate supports are disjoint. This proves `(DSP4)`.

Write an ordered quotient representation as

```text
c=1-z,       d=1-w,       d/c=t.
```

Since `c,d` are nonzero, `z,w` lie in `H\{1}`, and the quotient equation is

```text
w=1-t(1-z).
```

Each `z` determines one `w` and conversely every ordered quotient
representation arises this way. This proves `(DSP5)`.

Now expand the two cubics in `(DSP6)`. Their cubic coefficients are one,
their quadratic coefficients are both

```text
-(1+r+s-t),
```

and their constants are both `-rs`. The difference of their linear
coefficients is

```text
[s+r(1+s-t)]-[r+s(1+r-t)]=t(s-r).
```

This proves `(DSP6)`. If `Q_(t,r)` has roots `x,y` and `Q_(t,s)` has roots
`u,v`, the two cubic root sets are `{r,u,v}` and `{s,x,y}`. These are exactly
the positive-product and negative-root atoms on the opposite sides of the
distance-six collision, so `(DSP4)` is precisely their disjoint-support
locus.

It remains only to account for orientation. A disjoint generic edge has no
nontrivial stabilizer. It has two endpoint orders and two internal root
orders at each endpoint, hence exactly

```text
2*2*2=8
```

raw ordered presentations. The quotient representation is already ordered
in the definition of `R(t)`. This proves `(DSP7)`. Multiplying

```text
D_6,25^0+(17/10)D_6,25^A <=(223/20)n^2
```

by `80` and applying `(DSP7)` gives `(DSP8)`. QED.
