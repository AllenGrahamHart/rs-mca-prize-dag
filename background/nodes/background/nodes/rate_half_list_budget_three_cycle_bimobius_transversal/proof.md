# Proof

In the canonical 4-cycle, the edge-degree and slack rows are

```text
p=(0,1,1,1,1,0),       delta=(1,0,0,0,0,1).
```

Hence the four middle edge factors are the nonzero constant multiples of the
four distinct linear edge locators printed in the statement. In particular,
the ratios

```text
M_2(X)=q_12(X-r_12)/(q_02(X-r_02)),
M_3(X)=q_13(X-r_13)/(q_03(X-r_03))
```

are nonconstant. Cross multiplication shows that a map
`c(X-a)/(X-b)` with `a!=b` is injective wherever it is defined, since equality
at `x,y` gives `c(a-b)(x-y)=0`. Thus both maps are injective on their
respective block sets.

The `012` triangle identity is

```text
A_2 b_01 + A_0 b_12 = A_1 b_02.                     (1)
```

At a root of `A_2`, all other factors in `(1)` are defined and nonzero, so
`theta=b_12/b_02=M_2`. The analogous `013` identity gives
`theta=M_3` on `T_3`. The values on `T_0,T_1` follow directly from the
definition of `theta` and the disjoint block partition. This proves `(CBM1)`.

The Plucker edge identity is

```text
b_01 b_23-b_02 b_13+b_03 b_12=0.
```

Dividing its rearrangement by `b_02b_03` gives `(CBM2)` wherever both sides
are defined, hence as an identity of rational functions.

Now consider a projective pencil member different from `A_0` and `A_1`.
Because `A_0,A_1` are coprime, it has no roots in `T_0 union T_1`. On `T_2`,
its root condition is `M_2(x)=lambda` for one fixed projective parameter;
injectivity supplies at most one root. The same argument supplies at most one
root in `T_3`. The four edge points are the only remaining members of `D`, so
even charging all of them gives at most six roots.

A fully `D`-split member of degree `d-1` needs `d-1` distinct domain roots.
When `d>=8`, one has `d-1>=7>6`, so no further member can be fully split.
The locators `A_0,A_1` themselves are distinct fully split members, proving
the exact count two. QED.
