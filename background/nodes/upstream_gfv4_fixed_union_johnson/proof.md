# Proof

The MDS column property makes

```text
C_U=ker(H_U)
```

an `[R+nu,nu,R+1]` generalized Reed-Solomon code.

## Ray compiler

The right side of `(FU1)` is at least one, so there is nothing to prove when
`|Z|<=1`. If `Z` contains two distinct slopes, subtracting their two
syndromes shows that `y_1` lies in the column span on `U`, and then so does
`y_0`. Choose lifts `b_0,b_1` of `y_0,y_1` and a generator matrix `K` for
`C_U`.
Write each selected error uniquely as

```text
e_gamma=b_0+gamma b_1+Kc_gamma
```

and put `p_gamma=(gamma,c_gamma)` in affine `(nu+1)`-space. A zero
coordinate of `e_gamma` is an affine-hyperplane incidence whose normal is

```text
n_x=(b_1(x),K_x).                                    (1)
```

Each `p_gamma` lies on at least `h=N-t` such hyperplanes.

The incident normals span the full `(nu+1)`-space. Otherwise a nonzero
`(delta,v)` orthogonal to them gives

```text
q=delta b_1+Kv
```

supported inside `supp(e_gamma)`. If `delta=0`, this is a nonzero `C_U`
word of weight below its distance `R+1`. If `delta!=0`, the two words
`q/delta` and `e_gamma-gamma q/delta` represent `y_1` and `y_0` and are
both supported inside `supp(e_gamma)`, contradicting transversality.

Every coordinate normal is nonzero: puncturing one coordinate of the MDS
restriction lowers the kernel dimension from `nu` to `nu-1`, so the
corresponding coordinate functional on `C_U` cannot vanish. The incident
normals therefore form a loopless rank-`nu+1` matroid. Fix one incident
basis. Each further incident element enters a distinct basis by a
fundamental-circuit exchange. Hence every `p_gamma` is incident with at
least

```text
h-(nu+1)+1=R-t                                      (2)
```

independent `(nu+1)`-subsets of hyperplanes. An independent subset has at
most one affine intersection point. There are only `C(R+nu,nu+1)` such
subsets, so double counting proves `(FU1)`. Substituting `nu=1` proves
`(FU2)`.

## Fixed-syndrome list compiler

When `nu=0`, the columns in `U` are independent and a syndrome has at most
one lift. Assume `nu>=1`, choose one lift `b` of `y`, and identify the
syndrome fiber with `b+C_U`. Its weight-at-most-`t` members correspond to
codewords of the `[N,nu]` GRS code `C_U` agreeing with `-b` on at least
`h=N-t` coordinates.

Choose an `h`-subset `A_i` of each agreement set. Distinct `C_U` words agree
on at most `nu-1` coordinates. If there are `L` chosen sets and `d_x` counts
the sets containing coordinate `x`, then

```text
sum_x d_x=Lh,
sum_x C(d_x,2)<=C(L,2)(nu-1).                        (3)
```

Cauchy-Schwarz also gives

```text
sum_x C(d_x,2)>=(L^2 h^2/N-Lh)/2.                   (4)
```

Combining `(3)--(4)` and dividing by `L` yields

```text
L(h^2-N(nu-1))<=N(h-nu+1).
```

The assumed positive denominator proves `(FU3)`. QED.
