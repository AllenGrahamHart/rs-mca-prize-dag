# Proof - exceptional-E J-zero affine router

The definition `E_G=K_*-720bq^2`, with
`K_*=240bq(b-6)-P`, gives

```text
P=240bq(b-6-3q)-E_G.                                (1)
```

Substitute (1) into
`L_*=135b(b^2+6b+105+8q)-6P`. The part not containing `E_G` is

```text
45b[3(b^2+6b+105+8q)-32q(b-6-3q)]=45bB.
```

This proves the first identity in (FJ02).

For the second identity, use (1) in `R_J+5E_G`. Direct collection gives

```text
R_J+5E_G
 =3D_*+1200bq(b-6)-7200bq^2
 =-75bB+3(Tq-5bM).
```

Finally, the definition `X_*=Q_*-24D_*q^2` gives

```text
-D_*R_J+150bX_*
 =-3D_*^2-5PD_*+150bQ_*
 =J_*.
```

This proves all of (FJ02).

Assume first the original chart (FBC5). Since `b!=0`, the first identity
in (FJ02) gives `B=0`. The last identity and `D_*!=0` give `R_J=0`; the
middle identity then gives `Tq=5bM=R`. This proves (FJ03).

It remains to justify division by `T`. If `T=0`, then `Tq=5bM`, together
with the inherited `b!=0`, implies `M=0`. The elementary combination

```text
29(-280b^2+2241b+3465)+280(29b^2+234b+81)
 =9(14501b+13685)
```

proves (FJ04). The fixed integers `9` and `14501` are units at all four
official primes, so a common zero of `T,M` must have
`b=-13685/14501`. Substitution into `M` has numerator

```text
29(13685)^2-234(13685)(14501)+81(14501)^2
 =-23972710684.
```

Its four residues are exactly those in (FJ05), and none vanishes. Thus
`T` and `M` have no common zero over any extension of an official base
field. This proves (FJ06).

Now substitute `q=R/T`. Since `B,E_G,F_b` have `q`-degree at most two and
`X_*` has `q`-degree at most three, (FJ07) consists of integer
polynomials. The total-degree bounds follow term by term. Here
`deg T=2`, `deg R=3`, while the coefficient of `q^i` has `b`-degree at
most `2-i`, `3-i`, `6-2i`, and `5-i` for `B,E_G,F_b`, and `X_*`,
respectively. Therefore the four cleared degrees are at most
`6,7,10,11`.

Forward implication in (FJ08) follows from (FJ03), (FJ06), and the
definitions of the hats. Conversely, assume (FJ08) and the inherited
saturations. Since `T!=0`, denominator clearing recovers
`B=E_G=F_b=X_*=0`. The first identity in (FJ02) gives `L_*=0`; the middle
identity gives `R_J=0`; and the last identity gives `J_*=0`. Hence every
coefficient equation in (FBC5) is recovered, with no component introduced
or discarded. All equations outside this coefficient elimination remain
retained. QED.
