# Proof

The canonical path row has

```text
deg(A_0,A_1,A_2,A_3)=(d-1,d-1,d,d-1),
p=(0,1,0,1,0,0),       delta=(0,0,0,0,0,1).
```

Hence all quotients in the `012` and `013` triangle identities are nonzero
constants. Substitution of the two nontrivial edge locators gives `(PM1)` and
`(PM2)`.

The root sets of `P_0,P_1,P_2,P_3` are respectively

```text
T_0 union {s},  T_1 union {r},  T_2,  T_3 union {w}.
```

These are disjoint and partition `D`, proving pairwise coprimality and
`(PM3)`. Equation `(PM1)` is a nontrivial constant relation among the first
three degree-`d` factors, so they are three distinct members of one
gcd-trivial pencil.

At a root of `A_2`, `(PM1)` gives `theta=tau`. At a root `x` of `A_3`,
`(PM2)` gives `A_1(x)/A_0(x)=c`, and therefore

```text
theta(x)=c (x-r)/(x-s).
```

All denominators are nonzero because the incidence blocks are disjoint. If
two points `x,y` have the same displayed value, then

```text
(x-r)(y-s)-(y-r)(x-s)=(r-s)(x-y)=0.
```

Since `r!=s`, the points are equal. Thus the `d-1` roots in `T_3` cast
distinct pencil parameters. The extra root `w` can coincide with at most one
of them. Any fourth projective member is disjoint from the first three and
must take all of its domain roots from `T_3 union {w}`; it has at most two.
For `d>=3` it cannot be fully split of degree `d`. This proves the first exact
three-member assertion.

Equation `(PM2)` similarly puts `A_0,A_1,A_3` in one gcd-trivial constant
pencil. At a root of `A_2`, solving `(PM1)` for `A_1/A_0` gives `(PM5)`.
The same cross-multiplication proves injectivity on the `d` roots of `T_2`.
A projective member different from `A_0,A_1,A_3` cannot use their roots, so
its roots lie among `T_2` and the three exceptional points `r,s,w`. Each
parameter receives at most one root from `T_2` and at most all three
exceptional roots, for a total at most four. If `d>=6`, a degree-`d-1`
fully split member would need at least five roots, which is impossible. QED.
