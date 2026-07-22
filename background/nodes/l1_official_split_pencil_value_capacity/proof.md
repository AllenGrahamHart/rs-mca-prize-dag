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
