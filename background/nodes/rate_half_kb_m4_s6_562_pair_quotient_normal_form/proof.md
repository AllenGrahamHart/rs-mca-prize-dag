# Proof

## 1. Companion and pair curve

Use the BelyiDB degree-six map `phi=N/D`, whose branch factorizations are

```text
N=1458x^5(24x-41)/17689,
D=(4256x^3-20172x^2-20172x+68921)^2/18113536,
N-D=(8x+41)^2(22x-41)^3(26x+41)/18113536.
```

For an unordered pair represented by `q(X)=X^2-yX+z`, reduce `N` and `D`
modulo `q`. Proportionality of the two remainder vectors gives the
irreducible quintic

```text
C=-2780548824y^5+1627638336y^4z+4750104241y^4
  +1389447360y^3z^2+8341646472y^3z-819790080y^2z^3
  -7256554248y^2z^2-14250312723y^2z-137681280yz^4
  -1378420000yz^3-2780548824yz^2+82396160z^5
  +1054995600z^4+4001277576z^3+4750104241z^2.       (1)
```

## 2. Adjoint normalization

The affine singular scheme consists of two rational points and three
conjugate points arising from pairs of distinct roots of the cubic factor of
`D`. A cubic adjoint through that scheme, two rational regular points, and
the infinitely-near tangent at `(0,0)` has a two-dimensional space. One basis
is

```text
h0=z(1586864y^2-289952yz-2343314y-319744z^2
     -1728068z-2825761)/1586864,

h1=(97592136y^3-166719899y^2-24010912yz^2-124609168yz
    -3678464z^3-18780132z^2-42386415z)/97592136.
```

The exact resultant of `C` and `h0-u h1` has fixed-factor degree rows

```text
(1,0,1),(1,0,1),(1,0,2),(1,0,4),(3,0,2)
```

and one moving factor of bidegree `(1,5)` in `(y,u)`. Solving that factor and
the pencil gives

```text
y=(25444u^2-50922u+15129)
  (36517864u^3-276920478u^2+608911992u-414973341)
  /(3E),

z=-41(188u-287)(25444u^2-50922u+15129)^2/(4E),

E=144800664832u^5-559791696960u^4-97900305120u^3
  +3171741595920u^2-4974655751100u+2391178738527.
```

These formulas satisfy `(1)` and `h0-u h1` identically. The single moving
resultant factor proves birationality away from the finite base locus.

## 3. Branch fibers

On the pair curve, the common proportionality scalar is `t=N0/D0=N1/D1`.
Substitution gives `(KBM4-3)`, and direct subtraction gives `(KBM4-4)`.
The printed cubic and sextic are squarefree and coprime. The zero factor is
one linear and one quadratic factor, each to the fifth power. Thus the three
fiber profiles are exactly those in the statement. Their branch indices are
`12,10,6`, summing to `28=2*15-2`; no additional branch value exists.

The degree-six companion has natural monodromy `S6`, so its unordered-pair
quotient has the retained two-subset monodromy and passport.

## 4. Pole descent

The discriminant of `A2` is

```text
1053280980=14514^2*5.
```

The three roots printed in the statement are distinct in the deployed
characteristic. Every base-field unit becomes a square in the even extension
`F_(p^6)`, since `(p^6-1)/(p-1)` is even. Therefore the zero divisor of `T`,
and hence the pole divisor of `1/T`, splits over `K`.

No active fiber or quartic source-star condition is asserted.
