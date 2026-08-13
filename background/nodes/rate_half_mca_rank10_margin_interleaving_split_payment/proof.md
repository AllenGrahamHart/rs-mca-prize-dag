# Proof

Partition the post-near slopes into

```text
Z_hi={gamma:theta_gamma>=T},
Z_lo={gamma:theta_gamma<=T-1}.
```

## High-margin part

Let the affine span of the explanations in `Z_hi` have direction dimension
`r<=s`.  If `r=0`, all explanations equal one word `h`.  On each selected
support there are at least `T` coordinates with `r_1!=0`; at any such
coordinate the equation `r_0+gamma r_1=h` determines `gamma`.  These
slope-coordinate incidences are therefore disjoint, and
`|Z_hi|<=floor(n/T)=ST_0(T)`.

Now suppose `r>=1`.  The direction space of the affine span is a subspace
of `C'`.  Therefore minimizing the mismatch count over that smaller
direction space cannot decrease any `theta_gamma`.  The support-local
transversality compiler applies with margin `T` and gives

```text
|Z_hi|<=ST_r(T)<=max_(0<=j<=s) ST_j(T).                 (1)
```

Thus every possible lower-rank high subfamily is covered; no exact-rank
assumption is hidden in `(1)`.

## Low-margin part

For each `gamma in Z_lo`, choose `b_gamma in C'` with at most `T-1`
mismatches on `S_gamma`, and put

```text
a_gamma=h_gamma-gamma b_gamma in c_0+C'.
```

On every coordinate of `S_gamma` where `r_1=b_gamma`, the support equation

```text
r_0+gamma r_1=h_gamma
```

also gives `r_0=a_gamma`.  Thus `(a_gamma,b_gamma)` agrees with the received
pair `(r_0,r_1)` on a common set of size at least

```text
A=m-(T-1).
```

Translate the first component by `c_0`.  These pairs lie in the two-fold
common-support interleaving of the linear code `C'`.  The ordinary
affine-span list compiler at agreement `A=K+(w-T+1)` bounds every projected
ordinary list by

```text
M_s(T)=floor(C(n-K+s,s)/C(w-T+1+s,s)).                  (2)
```

If the pair list is nonempty, its ordinary list maximum `L` obeys
`1<=L<=M_s(T)`.  Since `M_s(T)^2<|F|`, the sub-square-root interleaving
collapse bounds the pair list itself by `L<=M_s(T)`.  If it is empty the
same conclusion is immediate.

It remains to bound the number of slopes that can choose the same pair
`(a,b)`.  Its intrinsic common core

```text
H_(a,b)={x:r_0(x)=a(x) and r_1(x)=b(x)}
```

has size at least `A`.  Pair noncontainment supplies, for every owning
slope, a coordinate `x in S_gamma` with `r_1(x)!=b(x)`.  This coordinate is
outside `H_(a,b)`, and the support equation determines the slope uniquely:

```text
gamma=-(r_0(x)-a(x))/(r_1(x)-b(x)).                     (3)
```

Choose one such coordinate for each slope.  For a fixed pair, `(3)` makes
the choice injective in the slope, so that pair has at most

```text
n-|H_(a,b)|<=n-A
```

owners.  Combining this with the pair-list cap gives

```text
|Z_lo|<=(n-A)M_s(T).                                    (4)
```

Equations `(1)` and `(4)` prove `(MI1)`.  The near-rational theorem charges
the disjoint near part by `2w`, proving `(MI2)`.

For KoalaBear error rank ten, the reversible gauge gives `s=9`.  Substitution
of the official integers at `T=667` yields the displayed total and positive
slack.  The verifier scans every legal integer threshold with exact integer
and rational arithmetic, checks the first paying threshold and unique
minimum, and separately records that the minima at `s=10,11,12` exceed the
official budget.
