# Proof

The dual of cubic evaluation on `X` is

```text
{(P(x)/Lambda'_X(x))_(x in X): deg P<|X|-4}.           (1)
```

Let `W` be the two-dimensional row space of `Lambda`. Under `(1)`, choose
polynomials `F,G` of degree at most `|X|-5` whose scaled evaluations span
`W`. They have no common evaluation root on `X`, because such a coordinate
would be zero in every row and hence would not belong to the active union.

Write the four rows as

```text
lambda_i(x)=(a_i F(x)+b_i G(x))/Lambda'_X(x).           (2)
```

The coefficient vectors `(a_i)_i,(b_i)_i` span a two-dimensional subcode of
the dual degree-less-than-two evaluation code on the four slopes. That dual
code also has dimension two, so the inclusion is equality. A generator of
it has rows

```text
omega_i(1,gamma_i),       omega_i!=0.
```

Changing the basis `F,G` therefore shows that the projective row parameter
`[a_i:b_i]` is a nonconstant fractional-linear function of `gamma_i`.

For `x in X`, equation `(2)` vanishes precisely when

```text
[F(x):G(x)]=[-b_i:a_i].                                (3)
```

Compose the rational map `[F:G]` with the two projective linear changes in
`(3)` and in the row-parameter/slopes identification. The result is a
rational function `phi` satisfying `(RF2)`. Its degree is no larger than
`max(deg F,deg G)<=|X|-5`, proving `(RF3)`. The zero sets in `(RF1)` are
disjoint and cover `X`, so they are exactly the displayed fibers within the
active set.

Every profile has a two-point fiber, so `phi` is not fractional-linear. For
`|X|=7`, `(RF3)` forces `deg phi=2`. In odd characteristic the function-field
extension `F(X)/F(phi)` is a separable quadratic extension. Its nontrivial
automorphism is an `F`-automorphism of the rational function field, hence a
Mobius involution, and it exchanges the two points of every split
two-point fiber. This proves the seven-coordinate claim. The same argument
applies to the degree-two eight-coordinate branch. For `|X|=8`, the degree
bound permits degree three as well.

Sharpness follows from explicit polynomial pencils. Over `F_101`, use
`phi(X)=X^2` on

```text
{0,+-1,+-2,+-3}       or       {+-1,+-2,+-3,+-4};
```

these give the two quadratic profiles and involution `X |-> -X`. For the
cubic profile, the cube map on `F_103` has nonzero fibers of size three.
Choose two points from each of four distinct nonzero cube fibers. On their
eight-point union, `phi(X)=X^3` has four fibers of size two. If the four
fiber values are `gamma_i`, put

```text
c_i=1/product_(j!=i)(gamma_i-gamma_j),
lambda_i(x)=c_i(phi(x)-gamma_i)/Lambda'_X(x).           (4)
```

The barycentric identities through degree two prove both trade identities
for `(4)`, and its row space has rank two. The quadratic constructions use
the same formula. Thus all printed branches occur as exact dual-product-code
trades, completing the proof.
