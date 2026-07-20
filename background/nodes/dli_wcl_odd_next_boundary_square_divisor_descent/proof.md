# Proof

Let `a_j` be the elementary symmetric functions of the `w` signed roots.
The same Newton induction as in the short-window theorem gives

```text
a_1=a_3=...=a_(2ell-1)=0.                              (1)
```

The product `a_w` lies in `mu_(2N)`. Since `w` is odd and `2N` is a power
of two, the `w`th-power map is an automorphism. The two inverses are checked
by

```text
5*205=1 mod 512,       7*439=1 mod 1024.               (2)
```

Therefore `(OND3)` is the unique product-one normalization. Dilation
preserves all odd-moment vanishings and reducedness.

In the normalized monic locator, the vanished odd elementary coefficients
in `(1)` remove all even powers except the term arising from
`a_(2ell+1)`. The constant term is minus the product. Consequently

```text
F(X)=X A(X^2)-bX^2-1                                  (3)
```

for unique `A,b`, with `A` monic of degree `ell+1`. Put
`C(X)=bX^2+1`. Direct multiplication gives

```text
-F(X)F(-X)=X^2A(X^2)^2-C(X)^2=G(X^2).                 (4)
```

Reduced support makes the roots distinct and nonantipodal. Their squares
are therefore `w` distinct roots of `Y^N-1`. Equation `(4)` proves
`(OND5)--(OND6)`.

Conversely suppose `G` divides `Y^N-1`. This binomial is separable. If a
root `y` of `G` had both `A(y)=0` and `by+1=0`, then

```text
G'=A^2+2YAA'-2b(bY+1)                                 (5)
```

would vanish at `y`, contradicting squarefreeness. The equation `G(y)=0`
then forces both factors to be nonzero. Define `rho` by `(OND7)`. It obeys

```text
rho^2=y,       rho A(y)-by-1=0,                        (6)
```

so it is a root of `F`. The `w` values are distinct and nonantipodal because
their squares are distinct. They are all in `mu_(2N)`, their locator has
constant term minus one, and hence their product is one. The coefficient
gaps in `(3)` and reverse Newton identities recover all vanishings in
`(OND2)`. The unique signed representation relative to `omega` has distinct
base exponents, proving the converse and the bijection.

Monic Euclidean division proves the integrality assertion in `(OND9)`. If
one of those ideals were proper over `Q`, it would have a complex point. The
converse would produce a nonzero reduced signed polynomial

```text
sum_i s_i Z^e_i,       deg<N,                           (7)
```

vanishing at a primitive `2N`th root. This contradicts its minimal
polynomial `Z^N+1`, of degree `N`. Thus each ideal is the unit ideal over
`Q`; clearing denominators in a rational unit-ideal identity proves
`(OND10)`. Reduction of that identity proves the characteristic-divisor
claim. QED.
