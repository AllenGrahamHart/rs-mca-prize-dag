# Proof

The higher-rank split-pencil reduction gives `t>=4`, distinct projective row
classes, row weight at least `a+1`, pairwise block intersection at most `a`,
and a two-dimensional polynomial-pencil model on `X` of degree at most

```text
|X|-a-1=2.                                           (1)
```

At an active coordinate, evaluation on the two-dimensional row space is a
nonzero linear functional. Its kernel contains at most one of the distinct
projective row classes. Therefore the row zero sets `Z_i` are pairwise
disjoint.

Put `z_i=|Z_i|`. The row-weight floor gives

```text
z_i<=|X|-(a+1)=2.                                    (2)
```

For distinct rows `i,j`, disjointness gives

```text
|supp(lambda_i) intersect supp(lambda_j)|
 =|X|-z_i-z_j.
```

Both supports lie in their selected blocks, so their intersection is at most
`a`. Using `|X|=a+3` yields

```text
z_i+z_j>=3.                                          (3)
```

Equations `(2)--(3)` imply `z_i in {1,2}` and show that at most one zero set
is a singleton. Since the zero sets are disjoint subsets of `X`,

```text
2t<=a+3                 if every z_i=2,
2t-1<=a+3               if one z_i=1.
```

Together with `t>=4`, these are `(FR2)`.

Normalize the dual `GRS_a` code on `X`. By the pencil model there are
polynomials `F,G` of degree at most two such that

```text
lambda_i(x)=(c_iF(x)+d_iG(x))/Lambda'_X(x).          (4)
```

Divide `F,G` by their polynomial gcd. This does not alter their projective
map or any zero on `X`, because a common root on `X` would be absent from
the active union. At least three rows have two-point zero sets. One member
of the coprime pencil therefore has two distinct roots, so the rational map
`phi=[F:G]` cannot have degree zero or one. The upper bound `(1)` makes its
degree exactly two.

The characteristic is odd. Hence the degree-two function-field extension

```text
F(T)/F(phi)
```

is separable and quadratic, so it has one nontrivial automorphism. Every
`F`-automorphism of `F(T)` is fractional-linear; call this automorphism
`iota in PGL_2(F)`. It exchanges the two points in every split unramified
fiber of `phi` and fixes the ramification points.

The zeros of row `i` are precisely the points of `X` in the projective fiber

```text
[F(x):G(x)]=[-d_i:c_i].                              (5)
```

A two-point `Z_i` exhausts the degree-two fiber in `(5)`, so its points are
exchanged by `iota`. A singleton contributes either one point of a fiber
whose other point is outside `X`, or a ramification point fixed by `iota`.
This proves `(FR3)`.

Finally substitute `(4)` in the two trade identities. Linear independence
of the evaluation vectors of `F,G` gives

```text
sum_i c_i=sum_i d_i=0,
sum_i gamma_i c_i=sum_i gamma_i d_i=0,
```

which is `(FR4)`. When `t=4`, the dependency identifies the projective row
parameters with a projective change of the slopes. If `a=4`, the row-count
bound forces `t=4`; disjointness inside `|X|=7` then forces the profile
`{1,2,2,2}`. QED.
