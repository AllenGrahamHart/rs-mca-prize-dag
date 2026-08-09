# Proof

The common Vieta compiler fixes cell `11` as singleton `BC+`, with roots

```text
(LA,AB,AC,BC+,BC-) = (1, r, epsilon_2*iota*r,
                       t, epsilon_1*iota).
```

For each of the four sign pairs and six primitive product-cofactor charts,
the pivot compiler selects `AB`, forms the three remaining maximal Vieta
determinants, and saturates by the selected cofactor and every printed route
guard. Singular returns dimension one, compact basis size `20`, and lex
basis size `8` in all 24 cases. Adding the raw `AB` pivot scale gives the
unit ideal in every chart, so the pivot loses no guarded common point. The
six lex signatures agree within each sign pair.

Let the first, second, and fifth lex elements be `F`, `G`, and `H`.
The tower replay separately saturates the full ideal and `(F,G,H)` by all
route guards and by the leading coefficients of `G` and `H`. All eight
full lex elements reduce to zero modulo `(F,G,H)`, in every sign row.
Conversely `F,G,H` belong to the full ideal, proving equality on that open
set. Direct coefficient extraction shows that `F` is quadratic in `t`,
`G` is quadratic and palindromic in `b`, and `H` is linear in `c`.
Repeating with the sixth lex element gives an independent linear recovery
and the same localized common ideal.

Directly recomputing `disc_t(F)` gives degree eight. Its recorded
factorization has degrees `1,1,2,4`, all with multiplicity one, and
`gcd(disc_t(F), d disc_t(F)/dr)=1`. Hence it is square-free. Completing
the square gives a square-free degree-eight double cover of the `r`-line;
its normalization has genus `(8-2)/2 = 3`.

It remains to restore the leading boundaries removed by localization.
Exact substitution of every route-guarded deployed root of the two leading
coefficients produces two fibers per sign pair. FGLM returns dimension zero
and lex basis size `4` in all eight fibers. Each has one linear `t`
factor and one quadratic `b` factor. Independent Euler-criterion checks
show that every quadratic discriminant is a nonsquare in `F_p`, so the
fibers contain no deployed point. This exhausts the leading-open complement.
QED.
