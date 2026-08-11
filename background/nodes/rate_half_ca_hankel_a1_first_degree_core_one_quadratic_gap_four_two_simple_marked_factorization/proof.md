# Proof

The two-simple normal form gives exact vertical divisors

```text
V_i=2R_i+3P_i,       deg P_1=1,       deg P_2=3.     (1)
```

The distinguished divisor degrees are

```text
deg R_1=e-c_1=(e-3)/2,
deg R_2=e-c_2=(e-9)/2.                               (2)
```

The intersection of the vertical row `X=x_i` with the apolar curve is cut
out by the homogeneous binary form `Q(U,V;x_i)`. Push `(1)` to the parameter
line. Since `R_i` is reduced and supported, its pushforward is cut out by
the squarefree form `G_i`; the pushforward of `P_i` is cut out by `S_i`.
Equality of divisors of homogeneous degree-`e` forms gives

```text
Q(U,V;x_i)=c_iG_i^2S_i^3                            (3)
```

for one `c_i in F^x`. The divisors and the row polynomial are base-field
rational, so the factors may be chosen over `F`; no algebraic-closure
constant is introduced. Equations `(1)--(3)` prove `(TSF1)--(TSF2)`, and
the degree checks are

```text
2(e-3)/2+3=e,
2(e-9)/2+9=e.                                        (4)
```

The marked-Hankel determinant theorem applies to every domain row of the
core-one pencil:

```text
det(M_1+tau nu(x)nu(x)^T)=tau D_1Q(U,V;x)^2.         (5)
```

Substitute `(3)` into `(5)` to obtain `(TSF4)`. In characteristic three,
division by the nonzero square `G_i^2` gives `c_iS_i^3`, whose affine
derivative is zero. This proves `(TSF5)`. QED.
