# Proof

The common Vieta compiler fixes cell `12` as singleton `BC-`, with roots

```text
(LA,AB,AC,BC+,BC-) = (1, epsilon_1*iota, r,
                       epsilon_2*iota*r, t).
```

For each of the four sign pairs and six primitive product-cofactor charts,
the pivot compiler selects `AC`, forms the three remaining maximal Vieta
determinants, and saturates by the selected cofactor and every printed route
guard.  Singular returns dimension one, compact basis size `15`, and lex
basis size `8` in all 24 cases.  Adding the raw `AC` pivot scale to each
guarded ideal gives the unit ideal, so these charts lose no guarded common
point.  The six lex signatures agree within each sign pair.

Let the first, second, and fifth lex elements be `F`, `G`, and `H`.  The
tower replay separately saturates the full ideal and `(F,G,H)` by all route
guards and by the leading coefficients of `G` and `H`.  All eight full lex
elements reduce to zero modulo `(F,G,H)`, in every sign row.  Conversely
`F,G,H` belong to the full ideal, proving equality on that open set.  Direct
coefficient extraction shows that `F` is quadratic in `t`, `G` is quadratic
and palindromic in `b`, and `H` is linear in `c`.  This gives the four-basis
tower in the statement.  Repeating with the sixth lex element gives an
independent linear recovery and the same localized common ideal.

Factoring `disc_t(F)` in each sign row gives multiplicities `(1,2,1)` and
factor degrees `(1,1,3)`.  The multiplicity-two factor is `r-1` or `r+1`,
which is already a route boundary.  After removing its square, the remaining
degree-four polynomial is square-free.  Since `p` is odd, completing the
square gives a square-free quartic double cover of the `r`-line, whose
normalization has genus one.

It remains to restore the leading boundaries removed by the tower
localization.  Exact substitution of every route-guarded deployed root of
the two leading coefficients produces three fibers per sign pair.  FGLM
returns dimension zero and lex basis size `4` in all 12 fibers.  The
`b`-leading eliminant splits into the same two linear factors in every sign
row, and back-substitution gives two points whose full guard product is
nonzero.  Each of the two `c`-leading eliminants is an irreducible quadratic
in `b`, so neither contributes a deployed point.  This exhausts the
leading-open complement and proves all four claims. QED.
