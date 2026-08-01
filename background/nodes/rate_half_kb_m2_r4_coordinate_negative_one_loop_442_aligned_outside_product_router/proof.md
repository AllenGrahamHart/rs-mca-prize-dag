# Proof

Apply the paired-product involution equation

```text
Gamma*y*z-Alpha*(y+z)-Beta=0.                     (1)
```

to the common pairs `(b,-b)` and `(c,-c)`.  The two equations are
`-Gamma*b^2-Beta=0` and `-Gamma*c^2-Beta=0`.
Their difference and `b^2!=c^2` give `Gamma=Beta=0`; nonsingularity gives
`Alpha!=0`.  Hence every paired product sums to zero.  The mate of the
singleton product `-b^2` is therefore `b^2`.  Product injectivity prevents
that forced value from occupying one member of any already complete
negation pair, since the other member would repeat the common `-b^2`.

In `S0`, the products `+/-d*e` and `+/-d*f` are already complete pairs.
The forced value must therefore be one of `alpha*c*e`, `beta*c*f`, and
`gamma*e*f`, while the other two must negate.  Any two of those three edges
share a vertex.  Cancelling its nonzero representative equates the other
two representatives up to sign, contradicting distinct target pairs.

For `S1`, abbreviate

```text
x=alpha*c*e, y=beta*c*f, z=-d^2,
u=gamma*d*e, v=delta*d*f.                         (2)
```

The pair `+/-e*f` is already complete.  If the forced value is `x` or `y`,
each of the three pairings of the four residual values contains an equation
that equates two target representatives up to sign.  If it is `z`, two
pairings have the same immediate defect.  The third pairs `x` with `v` and
`y` with `u`; multiplying those two equations gives `c^2=+/-d^2`.  But the
forced equality `z=b^2` says `d^2=-b^2`, so this identifies either `C` with
`D` or `C` with `B` as signed pairs.

If the forced value is `u`, only the residual pairing
`(x,v),(y,z)` avoids an immediate target collision.  This is `S1-DE`.
If the forced value is `v`, only `(x,z),(y,u)` survives, giving `S1-DF`.
Conversely, the displayed equations pair all residual products and hence
are sufficient at the product-multiset level.

In the first branch, substitute

```text
e=gamma*b^2/d,       f=beta*d^2/c
```

in `x+v=0`; multiplying by the guarded denominator and by `beta*delta`
gives `(KB41R-3)`.  In the second branch use
`f=delta*b^2/d` and `e=alpha*d^2/c` in `y+u=0`; the same equation follows.

Finally, `S2` already contains the three complete pairs
`+/-c*d,+/-d*f,+/-e*f`.  The only singleton is `-e^2`, so injectivity and
the forced-mate argument make `(KB41R-4)` necessary and sufficient.

The branches are not formal artifacts.  Over `F_73`, family A has

```text
i=27, r=8, b=70, c=49, t=7,
```

and the guarded `S2` choice `(d,e,f)=(2,8,4)` has outside products
`(25,48,9,8,65,32,41)`.  Family B has

```text
i=27, b=3, c=24, r=64, t=17,
```

and signs all `-1` with `(d,e,f)=(10,8,21)` give the guarded `S1-DF`
products `(27,7,46,66,9,22,51)`.  In each case the common and outside
products are disjoint and injective. QED.
