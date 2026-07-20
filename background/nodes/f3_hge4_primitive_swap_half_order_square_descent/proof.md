# Proof

Let `U=P union (-P)` be a primitive swap union. The odd-moment router gives
`h=2d+1` and

```text
L_P(X)=S(X)-e_h(P),       L_(-P)(X)=S(X)+e_h(P),
```

where `S` is monic, odd, and has degree `h`. There is therefore a unique monic
degree-`d` polynomial `T` with

```text
S(X)=X T(X^2).                                      (1)
```

Antipodal-freeness makes the squaring map injective on `P`. Thus
`Y=P^2` has size `h`, lies in `mu_N`, and

```text
L_Y(X^2)
 =prod_(x in P)(X-x)(X+x)
 =L_P(X)L_(-P)(X)
 =X^2T(X^2)^2-e_h(P)^2.                            (2)
```

Substitute `Z=X^2` in `(2)`. Since both sides are polynomials in `X^2`,

```text
L_Y(Z)=ZT(Z)^2-e_h(P)^2.                            (3)
```

The constant term of the odd-degree locator is
`L_Y(0)=-prod_(y in Y)y`, so `(3)` proves `(HOS1)` with
`c_Y=e_h(P)^2`.

The scaling stabilizer of `Y` is trivial. Indeed, if `alpha Y=Y` for some
`alpha in mu_N`, choose `gamma in mu_n` with `gamma^2=alpha`. Then
`gamma U=U`. The proved swap classification says the union stabilizer is
`{1,-1}`, so `gamma=+/-1` and `alpha=1`.

Conversely, let `Y` satisfy `(HOS1)` and have trivial scaling stabilizer.
The squaring map `mu_n -> mu_N` is onto, so every element of `mu_N`, including
`c_Y`, is a square in `F_p`; choose `a in mu_n` with `a^2=c_Y`. Substitution
of `Z=X^2` in `(HOS1)` gives

```text
L_Y(X^2)
 =(XT_Y(X^2)-a)(XT_Y(X^2)+a).                      (4)
```

The left side is the squarefree locator of
`U={x in mu_n:x^2 in Y}`. The two monic degree-`h` factors on the right are
coprime because `2a!=0`, so each splits into `h` distinct roots in `U`.
Writing those root sets as `P,Q`, their locators differ only by the nonzero
constant `2a`; hence they form a top shift pair. The polynomial
`XT_Y(X^2)` is odd, so negation exchanges the factors and `Q=-P`.

The ordered pair is primitive. If `gamma` preserves both `P` and `Q`, then
`gamma^2` stabilizes `Y`, hence `gamma^2=1`. Antipodal-freeness means `-1`
exchanges rather than preserves the sides, so `gamma=1`. The same argument
shows that the union stabilizer is exactly `{1,-1}`: any union stabilizer
squares to a stabilizer of `Y`, while `-1` always fixes `U` and exchanges its
sides.

The monic square root in `(HOS1)` is unique because a field of odd
characteristic is an integral domain: if monic `T_1^2=T_2^2`, then
`(T_1-T_2)(T_1+T_2)=0`, and monicity excludes `T_1=-T_2`.

Because `Y subset mu_N`, its locator divides `Z^N-1`; substituting `(HOS1)`
gives `(HOS3)`. Conversely, any monic divisor `ZT^2-c` in `(HOS3)` is
squarefree because `p` does not divide `N`, and has a root set
`Y subset mu_N`. Its odd degree gives
`c=prod(Y)`, so it satisfies `(HOS1)`. Uniqueness of `T` was just proved and
`c` is fixed by the constant coefficient. This proves the divisor
formulation.

Finally, scaling `U` by `gamma in mu_n` scales `Y` by `gamma^2`. The squaring
homomorphism has image `mu_N` and kernel `{1,-1}`, which already stabilizes
every swap union. It therefore identifies the two orbit sets and proves
`V_h^swap=W_h`. The anchored identity from the odd-moment router gives
`A_h^swap=hV_h^swap=hW_h`. Anchoring means `1 in Y`, so there are exactly
`binom(N-1,h-1)` raw support candidates. The test `(HOS1)` is deterministic
and reconstructs the signs through `(HOS2)`, removing the signed partition
search. QED.
