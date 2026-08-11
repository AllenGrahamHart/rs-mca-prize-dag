# Proof

Let `U=S_alpha union S_beta`. The only padded roots in the exact quadratic
packets are the named heavy rows, and those rows are absent from every
actual error. Hence every point of `X union Y` and every point of
`U\{s_0}` is light.

We first remove the orientation restriction from the rank-two theorem.
Apply the complete coefficient chain in the orientation `(alpha,beta)`.
The weighted Vandermonde nullspace has dimension two and gives forms `A,B`
with

```text
eta_x L_X'(x)Qbar(-;x)=A+xB,       x in X.          (1)
```

Suppose `A,B` were dependent. The `|X|` row forms would share a squarefree
set `B_0` of `e` supported slopes. For `delta in B_0`, lightness gives
`X subset S_delta`. Together with the fixed core point,

```text
|U union S_delta|
 <=rho+3+(rho-r_delta)-(r_alpha+4)
 <=2rho.                                             (2)
```

Minimum distance puts all centers indexed by `B_0` on the codeword line
through the endpoint centers. Add `alpha`, which is not in `B_0`; this gives
`e+1` selected slopes on that line. Its joint support is exactly `U`.

Remove `s_0`. Every light point of `U\{s_0}` occurs in exactly `e` supported
locators globally. Its nonzero error value on the codeword line is a
nonzero projective linear form, so among the `e+1` selected slopes it is
missing at most once. It therefore occurs exactly `e` times and is missing
exactly once. But a selected slope `gamma` misses

```text
(rho+2)-(rho-r_gamma-1)=r_gamma+3                  (3)
```

points of `U\{s_0}`. Summing `(3)` over `e+1` slopes gives at least
`3e+3` misses, while `|U\{s_0}|=rho+2=3e+1`. This contradiction proves
rank two. The same argument in the reverse orientation proves the two
normal forms without any condition on `r_alpha,r_beta`.

Let their gcds be `G_X,G_Y`. Every root of `G_X` is supported and its
locator contains all of `X`. The root `beta` is common and `alpha` is not.
For any other root `delta`, equation `(2)` again puts its center on the
endpoint codeword line. At every `y in Y`, the line error is nonzero at
`alpha` and zero at `beta`; it is therefore nonzero at the third slope
`delta`. Thus `Y subset S_delta` and `delta in Z(G_Y)`. Reversing the
argument proves

```text
Z(G_X)\{beta}=Z(G_Y)\{alpha}.                       (4)
```

This is `(BHL3)` and gives one common degree `g`.

Within each orientation, roots outside the gcd are disjoint by the affine
rank-two normal form. Take such a residual root `delta` belonging to the row
at `x in X`. Then `x,s_0 in S_delta`. If `r_delta>=1`,

```text
|U union S_delta|
 <=rho+3+(rho-r_delta)-2
 <=2rho.                                             (5)
```

Its center would lie on the endpoint line, where every point of `X` is in
its support. It would then be a common gcd root, a contradiction. Hence
every residual root has deficit zero.

If a root `delta` were residual in both orientations, its support would
contain `s_0`, one point of `X`, and one point of `Y`. The just-proved
deficit zero and

```text
|U union S_delta|<=rho+3+rho-3=2rho                (6)
```

would again put it on the endpoint line and hence in both gcds. This is
impossible for a residual root. All `n=R+6` residual root sets are therefore
pairwise disjoint and each has size `e-g`.

The two gcd root sets have union `L` of size `g+1`. Counting their disjoint
residual sets inside the `T=3e+3` supported slopes gives

```text
s=T-(g+1)-n(e-g)
 =(R+5)g-(R+3)e+2>=0,                               (7)
```

which proves `(BHL5)--(BHL6)`. Equation `(BHL4)` says every positive
deficit is supported on `L union W`.

All centers indexed by `L` lie on the endpoint line, whose joint residual
support is `U`; hence `S_delta subset U` for every `delta in L`. At each
light point of `U\{s_0}`, the line error vanishes at at most one slope of
`L`. Consequently the total number of missing incidences is at most
`rho+2`. By `(3)` it is

```text
sum_(delta in L)(r_delta+3)=d_L+3(g+1).             (8)
```

Using `rho+2=3e+1` in `(8)` proves `(BHL7)`.

Finally `sum r_delta=e-6` over all supported slopes. A double-root slope has
`r_delta<=1`, while a two-simple slope has `r_delta<=2`. Since residual
roots have deficit zero,

```text
d_L>=e-6-s                 (double root),
d_L>=e-6-2s                (two simple).             (9)
```

Insert `(7)` into `(9)` and then use `(BHL7)`. In the double-root arm this
rearranges to

```text
(R+2)g>=(R+1)e-6,                                  (10)
```

and in the two-simple arm to

```text
(2R+7)g>=2(R+2)e-8.                                 (11)
```

Taking ceilings together with `(BHL6)` gives `(BHL9)`. QED.
