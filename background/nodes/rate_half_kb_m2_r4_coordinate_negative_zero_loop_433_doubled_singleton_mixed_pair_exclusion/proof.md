# Proof

The zero-loop weld reconstructs the Mobius denominator from three product
rows and expresses the sum half by two quadratic-interpolation determinants.
Apply it to `(KBZ433M-1)--(KBZ433M-2)`.  Both product determinants are
linear in `x`.  Their compatibility, after exact division by `c(b-c)`, is
`(KBZ433M-3)`.

Write `S=(y+1)^2` and `Q=y^2-6y+1`.  The coefficient and constant of
`(KBZ433M-3)` are `bQ+S` and `b(bS+Q)`.  If both vanish, then
`Q^2-S^2=-16y(y-1)^2` vanishes.  This gives `y=0` or `y=1`, both source
label guards.  Thus

```text
c=-b(bS+Q)/(bQ+S).                                (1)
```

Substitution in the first product row writes `x=X_num/X_den`.  The exact
polynomials are

```text
X_num=b^2y^4-3b^2y^3-5b^2y^2-b^2y
      +2by^4-6by^3+22by^2-2by+y^4-3y^3-5y^2-y,
X_den=b^2y^3+5b^2y^2+3b^2y-b^2
      +2by^3-22by^2+6by-2b+y^3+5y^2+3y-1.        (2)
```

After `(1)--(2)`, each q determinant is affine-linear in `(t,r)`.  Preserve
the common scaling of its Cramer determinant and numerators.  Imposing
`t^2=x,r^2=y` gives two polynomials of degrees 27 and 22.  Their exact gcd
is

```text
X_den(y^2-1).                                     (3)
```

Both factors are excluded on the regular branch.  The residual degrees are
20 and 15.  In every sign row their lexicographic basis has six elements
and one degree-20 eliminant after deleting `b=0,+/-1`.  Binary modular
exponentiation computes the four Frobenius gcds in `(KBZ433M-4)`.

The quadratic in the `(+,-)` row splits into roots `583634928` and
`1547071499`; direct specialization makes `y=1`.  The quartic in the
`(-,+)` row splits into those two roots and `908031539,1517828908`.
The first pair again gives `y=1`.  The second pair gives
`y=681314713`, `X_den=0`, and respectively

```text
X_num=961591410, 1569092385,
```

so neither is a product solution.  Re-evaluation in the original two
product and two q determinants finds no guarded packet.

It remains to justify every division.  Exact lex elimination of numerator
and denominator for `(1)` and `(2)` gives precisely `(KBZ433M-5)`.  For
three sign rows, the singular Cramer system has only those same points.  In
the `(-,+)` row it additionally projects to the two `X_den=0,X_num!=0`
points above.  Hence no lost branch is valid.

Finally the two displayed target relabelings preserve products, sums, and
the complete product-q system while generating the four-cell orbit.  The
cell-`0` exclusion transports to cells `4,7,11`. QED.
