# Proof

Put `K=(A-A) intersect ker H`, so `dim K=a`. In the flat-nullity
factorization, `u=v=0` says that the common zero set has size `k-a`, that
there are no surviving loop coordinates, and that division by its locator
identifies `K` with all polynomials of degree less than `a`. Puncturing the
common zeros therefore gives a normalized `GRS_a` code on

```text
N=n-(k-a)=R+a
```

coordinates. The general extension-list argument writes every selected
error as

```text
e_gamma=b+gamma q+w_gamma,       w_gamma in K.
```

Its zeros become agreements between one received word and a codeword in
`K+<q>`. Choose exactly `a+h` of them as the block `A_gamma`. The post-strip
high-core cap gives `|A_gamma intersect A_eta|<=a` at distinct slopes.

We also need that `q` is not a `GRS_a` word on a selected block. If it were,
then on that block the displayed zero equation would make `b` a `GRS_a`
word as well. Thus both `b` and `q` would differ from kernel codewords by
vectors vanishing on `a+h` punctured coordinates and on the `k-a` common
coordinates. The original received pair would be jointly `A=k+h` close to
a codeword pair. That is precisely the tangent-paid case excluded from the
generic P-A branch. This proves the split-pencil normalization and its
nondegeneracy.

Assume `(HR1)` and choose `G` inclusion-minimal among nonempty subfamilies
satisfying

```text
h|G|>=2|union G|-2a.                                  (1)
```

Such a family exists because the full union has size at most `N`. Write
`v_G=|union G|` and define `e` by

```text
h|G|=2v_G-2a+e.                                       (2)
```

Minimality gives `e>=0` and, for every nonempty proper `J subset G`,

```text
h|J|<2|union J|-2a,
```

which is the integer inequality in `(HR2)`. If `A in G` has `p_A` private
coordinates, apply that proper-subfamily inequality to `G\{A}`. This
subfamily is nonempty: a one-block family would require
`h>=2(a+h)-2a=2h`, impossible for `h>=1`. Hence

```text
h(|G|-1)<=2(v_G-p_A)-(2a+1).                          (3)
```

Substituting `(2)` into `(3)` gives `e+2p_A<=h-1`. In particular
`e<=h-1`; using `v_G<=N` in `(2)` gives the size bound in `(HR2)`.

Restrict to `V=union G`. Evaluation of degree-less-than-`a` polynomials has
dimension `a` there because every block has at least `a+1` points. Hence
`K x K` is a `2a`-dimensional subspace of `ker M_G`. The genuine pair
`(U,q)` is one more kernel direction: `q|V` is not in `K|V` because its
restriction to each block is non-`GRS_a`. Therefore

```text
rank M_G<=2v_G-(2a+1).
```

The matrix has `h|G|=2v_G-2a+e` rows, so its left kernel has dimension at
least `e+1`. This proves `(HR4)`.

Let a nonzero left relation combine the rows in block `A` to the word
`lambda_A`. Reading the first and second halves of the relation gives
`(HR5)`. The dual of degree-less-than-`a` evaluation on an `a+h` point block
has the locator form

```text
lambda_A(x)=P_A(x)/Lambda'_A(x),       deg P_A<h.
```

A nonzero numerator has at most `h-1` block roots, so every active row has
weight at least `a+1`. At an active coordinate, one nonzero coefficient
cannot sum to zero; two coefficients cannot satisfy both equations in
`(HR5)` because their slopes are distinct. Thus every active coordinate has
degree at least three.

If the trade matrix had rank one, all active rows would be proportional.
There are at least three of them by the active-coordinate degree, and two
would have the same support of size at least `a+1`, contradicting the block
intersection cap `a`.

Now suppose the trade rank is two. The two-dimensional column space is a
subcode of the dual degree-less-than-two slope code. If its support had at
most three rows, the two-row Vandermonde check on distinct slopes would have
nullity at most one, so `t>=4`. No two active rows are proportional by the
same support argument as above.

Let `rho` be their active-coordinate union. Evaluation at an active
coordinate is a nonzero functional on the two-dimensional row space, so it
vanishes on at most one of the `t` projectively distinct rows. Every active
column therefore has degree `t-1` or `t`. Double counting pairwise support
intersections gives

```text
rho C(t-1,2)
 <=sum_(i<j)|supp(lambda_i) intersect supp(lambda_j)|
 <=a C(t,2),
```

and hence `rho<=floor(a t/(t-2))`. The noncommon zero sets of the active
rows are disjoint. Since each row is supported on a block of size `a+h`,
the usual zero packing gives

```text
t(rho-(a+h))<=rho
```

when `rho>a+h`, and the resulting bound is automatic otherwise. Thus
`rho<=floor(t(a+h)/(t-1))` in all cases. Two row supports have union at
least `2(a+1)-a=a+2`; combining this lower bound with the first upper bound
gives `t<=a+2`. Since `t>=4`, the same upper bound is at most `2a`. This
proves `(HR7)`.

Finally, after the fixed GRS normalization the rank-two row space lies in
the dual of degree-less-than-`a` evaluation on its `rho` active coordinates.
It therefore has a basis represented by two polynomials `F,G` of degree
less than `rho-a`, with no common evaluation root. Each active row is a
linear combination `c_iF+d_iG`, so its zero set is the corresponding fiber
of `[F:G]`. The pencil degree is at most `rho-a-1<=a-1`. If `t=4`, the two
coefficient vectors span the whole two-dimensional dual `RS_2` code on the
four slopes; their projective parameters are consequently a projective
change of those slopes. This proves `(HR8)` and all claims. QED.
