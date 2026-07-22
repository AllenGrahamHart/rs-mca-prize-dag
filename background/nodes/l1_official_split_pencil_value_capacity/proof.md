# Proof - L1 official split-pencil value capacity

For `beta in V_H(P)`, write

```text
X_beta={x in H:P(x)=beta}.
```

The hypothesis that `P(Z)-beta` has `p` distinct roots in `H` says exactly
that `|X_beta|=p`. If `beta!=gamma`, the fibers are disjoint: a common point
would satisfy `P(x)=beta=gamma`. Hence

```text
p |V_H(P)|
 = |disjoint union_(beta in V_H(P)) X_beta|
 <= |H|=n.
```

This proves the first inequality in `(SPV2)`. The official arithmetic gives
`p>n/24`, so `n/p<24` and the integral quantity `floor(n/p)` is at most 23.
Taking unordered pairs proves `(SPV3)`.

## Exact eliminant

Because `P(Z)-T` is monic of `Z`-degree `p`, division in `F[T][Z]` gives the
unique identity `(SPV4)`. Give `Z` weight one and `T` weight `p`. Replacing
`Z^p` by `T-Q(Z)` never increases weight because `deg Q<p`. Starting from
`Z^n`, every remainder monomial `T^jZ^i`, `i<p`, therefore satisfies
`pj+i<=n`. This proves `(SPV5)`.

For `beta` in an algebraic closure, all coefficient remainders vanish at
`beta` exactly when

```text
P(Z)-beta divides Omega(Z).                              (1)
```

The polynomial `Omega` is squarefree because `p` does not divide the
power-of-two integer `n`. Thus `(1)` is equivalent to `P-beta` having `p`
distinct roots in `H`. Moreover any such `beta` equals `P(x)` for one of
those roots `x in H`, so `beta in F`. This proves that the roots of `G_Q`
are exactly `V_H(P)` and all lie in `F`.

It remains to exclude multiplicity. Differentiate `(SPV4)` with respect to
`T`:

```text
0=(partial_T A_Q)(P-T)-A_Q+partial_T Rem_Q.              (2)
```

If `(T-beta)^2` divided every coefficient remainder, then both `Rem_Q` and
`partial_T Rem_Q` would vanish at `beta`. Reducing `(2)` modulo `P-beta`
would show that `P-beta` divides `A_Q(Z,beta)`. But `(SPV4)` at `beta` says
`Omega=A_Q(Z,beta)(P-beta)`, so `(P-beta)^2` would divide the squarefree
domain polynomial. This contradiction proves `(SPV7)` including
squarefreeness.

Finally, if `h=deg G_Q`, every row polynomial `R_(Q,i)` belongs to the
`(m-h+1)`-dimensional space

```text
G_Q(T) F[T]_(<=m-h).
```

Their coefficient rows therefore have rank at most `m-h+1`, proving
`(SPV8)`. For `h>=2`, this is at most `m-1`, which gives the stated rank
rejection.

## Low-complement closure

If `2p>n`, the disjoint union of two `p`-point fibers would have more than
`n` points. This proves `(SPV9)`.

Now suppose `2p<=n<3p`, put `s=n-2p`, and assume two split values exist.
The official power-of-two `n` cannot equal twice the odd prime `p`, so
`s>0`. Then `m=2`; by `(SPV7)`, `G_Q` is the monic quadratic whose roots are
exactly those two values. Therefore

```text
G_Q(P(Z))=(P(Z)-beta)(P(Z)-gamma)
```

is a monic degree-`2p` divisor of `Omega`. Write

```text
Omega(Z)=G_Q(P(Z)) C(Z),       deg C=s,
```

where `C` is monic. Apart from its leading `Z^(2p)` term,
`G_Q(P)` has degree at most `p+r`: indeed

```text
G_Q(P)=P^2-uP+v
      =Z^(2p)+(2Q-u)Z^p+(Q^2-uQ+v),
```

and `r<p` while the characteristic is odd.

If `r+s<p`, every contribution from the nonleading part of `G_Q(P)` times
`C` has degree strictly below `2p`. Thus the coefficients in degrees
`2p,...,2p+s-1` of the product come only from `Z^(2p)C`. Since `Omega` is a
binomial, all the lower coefficients of `C`, including its nonzero constant
term, would vanish. This would give `C=Z^s`, making the constant term of
`Omega` zero, a contradiction. Hence `r+s>=p`, proving `(SPV10)`.

In the supplied first-checkpoint representation, `r<=2p-d-1`. At
`d>=n-p`, this upper bound is at most `3p-n-1`, contradicting `(SPV10)`.
This proves `(SPV11)`. For `(n,p)=(8192,3583)`, `n-p=4609`; the earlier
ratio boundary is `2p-1-1566=5599`.

For the complement compiler, the union locator of a genuine pair is

```text
D_S=F_XF_Y=(P-beta)(P-gamma).
```

Since `X`, `Y`, and `S` partition `H`, it is also `Omega/C_S`. Complete the
square:

```text
D_S=(P-(beta+gamma)/2)^2-((beta-gamma)/2)^2=R^2+c.
```

Here `R` is monic of degree `p`, and `c` is a nonzero negative square because
the two values are distinct and the characteristic is odd.

To prove uniqueness, suppose `D_S=R_1^2+c_1=R_2^2+c_2` for monic
degree-`p` polynomials. Then

```text
(R_1-R_2)(R_1+R_2)=c_2-c_1.                            (3)
```

The second factor has degree `p` because its leading coefficient is two. If
the first factor were nonzero, the left side would have positive degree and
could not be constant. Hence `R_1=R_2`, and then `c_1=c_2`. Choosing either
square root `delta` of `-c` gives the same unordered pair
`{R-delta,R+delta}`. Thus the complement determines the pair injectively.
There are `binom(n,s)` complements, proving `(SPV13)`.

## Exact classification by polynomial abc

Continue in the `m=2` band and write `D_S=R^2+c`. The factorization
`D_SC_S=Z^n-alpha` is equivalent to

```text
R^2 C_S+(cC_S+alpha)=Z^n.                              (4)
```

Let `nu=ord_0(R)`. Since `C_S(0)!=0` and `2nu<=2p<n`, equation `(4)` gives

```text
ord_0(cC_S+alpha)=2nu.
```

After division by `Z^(2nu)`, the three terms in `(4)` are pairwise coprime.
Indeed, a common nonzero root would divide their sum `Z^n`, while exact
valuation removes the root zero. If this reduced triple is not entirely in
`F[Z^p]`, polynomial Mason--Stothers gives

```text
n-2nu
 <= deg rad((R/Z^nu)^2 C_S)
    +deg rad((cC_S+alpha)/Z^(2nu))
    +deg rad(Z^(n-2nu))-1
 <= (p-nu+s)+(s-2nu)+1-1
 = p+2s-3nu.                                           (5)
```

But `n=2p+s`, so `(5)` would imply `p-s+nu<=0`, impossible because
`0<s<p`. Therefore the reduced triple is Frobenius-degenerate: all three
derivatives vanish.

In particular `p` divides `n-2nu`. Also `2nu<=s<p`, because
`cC_S+alpha` has degree `s`. Since `n=2p+s`, these facts force

```text
2nu=s.                                                  (6)
```

The polynomial `(cC_S+alpha)/Z^s` is now constant with leading coefficient
`c`, so

```text
cC_S+alpha=cZ^s,       C_S=Z^s-alpha/c.                 (7)
```

Write `R=Z^(s/2)U`. Dividing `(4)` by `Z^s` and using `(7)` gives

```text
U^2 C_S=Z^(2p)-c=(Z^2-c^(1/p))^p.                       (8)
```

The finite field is perfect. Since `C_S` is squarefree and divides the right
side of `(8)`, all its roots lie among the two roots of
`Z^2-c^(1/p)`. Hence `s<=2`. Equation `(6)` makes `s` positive and even, so
`s=2`, proving `(SPV14)`.

Put `b=alpha/c`. Equations `(7)--(8)` now give

```text
C_S=Z^2-b,       c=b^p,       alpha=b^(p+1),
U=C_S^((p-1)/2),       R=Z C_S^((p-1)/2).               (9)
```

The monic choice fixes the sign of `U`. The two roots of `C_S` are `x,-x`
in `H`, so `b=x^2`; conversely every antipodal pair in `H` satisfies
`b^(p+1)=x^n=alpha` because `n=2p+2`. Since `H` contains an element of order
four, `-1` is a square in `F`, so `delta^2=-b^p` has a solution. Directly,

```text
(R-delta)(R+delta)
 =Z^2(Z^2-b)^(p-1)+b^p
 =(Z^n-alpha)/(Z^2-b).                                  (10)
```

The right side is squarefree and split in `H`; the two coprime monic factors
on the left each have degree `p`, hence both split in `H`. The square map on
the even-order coset has antipodal fibers, giving exactly `n/2` values of
`b` and proving `(SPV15)--(SPV17)`.

Finally, expanding `R=Z(Z^2-b)^((p-1)/2)` shows that its `Z^p` leader is
followed by the nonzero `Z^(p-2)` coefficient `b/2`. Thus the normalized
`Q=R-Z^p` has degree `p-2`. The split-pencil converse allows precisely
`d<=2p-(p-2)-1=p+1`, proving the depth assertion.

For the collision consequence, normalize the constant term in the supplier's
representation

```text
F_X=Z^p+Q+b,       F_Y=Z^p+Q+b+c,       c!=0
```

by absorbing `Q(0)` into `b`. With `P=Z^p+Q`, the two root sets are the
distinct fibers with values `-b` and `-(b+c)`. Thus every unordered collision
pair injects into a two-element subset of `V_H(P)`, proving the stated cap.

Equivalently, the polynomials `sP-t` form a projective one-parameter pencil
with no common domain root. Every finite monic split member has `p` moving
roots, so the upstream moving-root incidence count gives `floor(n/p)`.
The disjoint-fiber argument above also shows directly why no multiplicity or
first-owner convention is hidden in this specialization.
