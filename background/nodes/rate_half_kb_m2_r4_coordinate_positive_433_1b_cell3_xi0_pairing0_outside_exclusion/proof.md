# Proof

Fix a source-sign pair.  By `(KBP1B3-QUOT-1)`, the guarded common curve is
presented by a cubic equation in `t` over `F_p(r)`, a monic quadratic
extension in `b`, and linear recovery of `c`.  Hence every common-curve
function used by the Vieta kernel can be represented in the six-element
basis

```text
1, t, t^2, b, bt, bt^2.
```

The compiler reduces products by the cubic and quadratic relations and uses
extended Euclid modulo the cubic whenever a denominator is inverted.  It
then evaluates the eight proved kernel coefficients.  At the missing label
`-t^2`, let `de=b_missing/a_missing`; the root replay checks
`a_missing != 0` on every retained point.  For `xi=0` and `pairing=0`, the
first residual matched pair is `(de,-de)`.  The printed paired Vieta
determinant `T` for this pair is a necessary target-free equation.

Multiplication by `T` on the six-dimensional algebra gives a `6 x 6`
matrix.  Its determinant is the norm used for elimination.  Independently,
the compiler first takes the determinant of the quadratic extension and
then the `3 x 3` cubic norm.  Exact cross multiplication in `F_p(r)` shows
that the two norms agree in every source-sign row.  A target point has
`T=0`, hence its `r` coordinate must annihilate the norm numerator.  Taking
the gcd with `r^p-r` finds every base-field root without enumerating the
field.  There are eleven roots per sign: five route boundaries and six live
norm roots.

The second compiler lifts all eleven roots directly through the original
base, `b`, and `c` equations.  It replays the sixteen route guards and all six
product cofactors before evaluating `T` itself.  This leaves twelve guarded
common points and exactly four `T=0` points per source sign.  Thus no target
solution can occur away from those four points.

For each retained point and target lane `(sigma_c,sigma_o)`, write the
remaining outside representatives as `d=u/f` and `e=v/f`.  The final solver
uses the exact five equations

```text
de*f^2-u*v = 0,
paired(de,-de) = 0,
paired(u,sigma_o*v) = 0,
paired(b*f,sigma_c*c*f) = 0,
f^2*(-t^2)*(beta_0+beta_1*(-t^2))^2-(u+v)^2*a_missing^2 = 0.
```

It first solves the colored quartic in `f`.  In twelve of the sixteen
point/lane rows there is no base-field root.  In each of the other four rows
there are four nonzero `f` roots.  Substitution
`v=de*f^2/u` clears the two remaining equations to univariate polynomials in
`u`; their gcd has degree zero at all sixteen `f` roots.  Consequently no
`u`, and therefore no guarded target tuple, exists.  This calculation is
repeated independently for all four source-sign pairs.  The four target
lanes are exhaustive by the signed-edge atlas, so all sixteen raw cases in
the stated subfamily are empty. QED.
