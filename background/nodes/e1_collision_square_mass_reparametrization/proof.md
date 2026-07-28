# Proof

## Class coordinates

Partition the `N=2h` roots into `h` antipodal pairs. By `acl_count`, a class
is determined by its signed singleton positions and the number `u` of full
pairs. Writing `t` for the number of singleton positions gives
`t+2u=ell`. The full pairs must fit among the `h-t` remaining positions, so

```text
0 <= (ell-t)/2 <= h-t.
```

Together with `0<=t<=ell`, this is exactly
`t<=T=min(ell,2h-ell)` and `t=ell mod 2`.

Represent the signed singleton positions by `x in {0,+-1}^h`. Full pairs sum
to zero because `zeta^(i+h)=-zeta^i`, so the class value is
`sum_i x_i zeta^i`. Two class values therefore differ by
`alpha=sum_i(x_i-y_i)zeta^i`.

At a coordinate common to both singleton supports with opposite signs,
`x_i-y_i=+-2`; this contributes four to `S` and two to `H`. At a coordinate
in exactly one support it is `+-1`; this contributes one to each. Common
singletons cancel. Hence `S=4a+b` and `H=2a+b`.

Every contribution to `H` consumes one singleton entry from `x` or `y`, so

```text
H <= |supp(x)|+|supp(y)| <= 2T.
```

Also `S<=2(|supp(x)|+|supp(y)|)<=4T`: a `+-2` coordinate consumes two
singleton entries and contributes four, while a `+-1` coordinate consumes
one and contributes one. Equality is attained by opposite signs on a common
support of size `T`. Finally,

```text
S = |supp(x)|+|supp(y)|-2<x,y>
```

is even because both support sizes have parity `ell`.

For raw representatives, a full antipodal pair present on one side and empty
on the other contributes two raw differences of the same sign and folds to
zero. If there are `c` such positions, counting the `2s` raw differences gives
`s=a+b/2+c`. This explains why `c` is invisible to the class difference. At
fixed `h` it is bounded by available positions; no claim of literal
unboundedness is needed.

## Norm floors

For `N=256`, `h/2=64`. In the `b>0` branch, `S^64<2^250` for every even
`S<=14`, whereas `16^64>2^250`. In the `b=0` branch write `alpha=2 beta`;
an odd row prime divides `Norm(alpha)` exactly when it divides `Norm(beta)`,
and `|Norm(beta)|<=a^64`. Thus `a<=14` is excluded and `a=15` is the first
integer not excluded by this bound.

For `N=512`, the exponent is `128`. The corresponding thresholds are even
`S>=4` in the `b>0` branch and `a>=4` in the all-even branch. This recovers the
correct first possible raw collision distance `s>=2`, not `s>=3`.

## Feasibility of every live `S=16` split

Fix `ell` equal to 33 or 65. For one of

```text
(a,b) in {(3,4),(2,8),(1,12),(0,16)},
```

put `t0=a+b/2`. Let `r=0` if `t0` is odd and `r=1` otherwise. Choose disjoint
coordinate sets:

```text
|A|=a, |U|=|V|=b/2, |R|=r,
|F|=u=(ell-(t0+r))/2.
```

There is ample room in `h=128`; the largest union uses 29 coordinates when
`ell=33` and 45 when `ell=65`. Define
`x=+1,y=-1` on `A`; put a singleton only in `x` on `U` and only in `y` on
`V`; and put the same signed singleton in both on `R`. Use the same `u` full
pairs `F` in both raw representatives. Each representative has
`t0+r+2u=ell` elements. Their class difference has exactly `a` coefficients
of magnitude two and `b` of magnitude one, with no raw full-pair discrepancy,
so `c=0` and `S=4a+b=16`.

The `(4,0)` split is different: after division by two it has `a=4<=14`, so it
is excluded by the all-even norm branch. The four displayed splits all have
`b>0` and `S=16`, so none is excluded by the current norm floor. This proves
both their class feasibility and the claimed scope boundary. QED.
