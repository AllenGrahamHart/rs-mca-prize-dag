# Proof

Each coordinate of `W` has one projective root `mu_x` of `L_x`. There are at
most `|W|<q` such roots, so choose a parameter value outside their set and
send it to infinity by a projective basis change. In the resulting affine
coordinate no `L_x` vanishes at infinity, which is `(TVS1)`.

The column polynomial indexed by `(x,t)` is

```text
L_x(Y) A_x(Y) Y^t,
```

where `A_x` is monic of degree `d_x=m-Delta_x`. Its degree is at most `m+1`.
It reaches degree `m+1` exactly when `t=Delta_x`, and then its leading
coefficient is `c_(1,x)`. This proves `(TVS2)`.

Restrict `(TVS2)` to any `4m+1` distinct points `P`. Its determinant is

```text
product_(x in P)c_(1,x) product_(x<y in P)(y-x),
```

which is nonzero. Thus the block `V` in `(TVS3)` is invertible. Multiplying
on the left by the invertible block matrix that subtracts `CV^(-1)` times
the first block row gives

```text
[ V  B ],
[ 0  D-CV^(-1)B ].
```

This proves `(TVS4)` and the equivalence of full column rank.

There is one highest column per point and `Delta_W` lower clone columns, so
removing `4m+1` pivot columns leaves `(TVS5)`. From `Delta_W<=m` and
`|W|<=7m-1`,

```text
v_W<=7m-1+m-(4m+1)=4m-2.
```

When `O=0`, `Delta_W<=1`, giving

```text
v_W<=7m-1+1-(4m+1)=3m-1.
```

This is `(TVS6)`. QED.
