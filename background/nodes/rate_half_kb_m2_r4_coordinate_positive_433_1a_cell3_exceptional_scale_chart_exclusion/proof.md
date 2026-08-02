# Proof

The compact plane-kernel packet records six univariate scales: the rational
`r` and `c` denominators, their common denominator scale, the first removed
projective scale, the plane leading coefficient, and the second removed
projected scale.  FLINT factors each polynomial over `F_2130706433` and
reconstructs it from the factors.  The linear factors have exactly the six
roots `(KBC3E-1)`.  Every other factor is an irreducible cubic, so this list
contains every deployed-field exceptional parameter.

For each root, return to the original seven-element common lex basis rather
than the divided plane model.  Add `t-t_0` and saturate by the original twenty
common guards.  Five standard bases are `<1>`.  The remaining basis is the
five-element zero-dimensional basis `(KBC3E-2)`, together with the explicit
inverse-guard coordinate.  Its quadratic discriminant is a nonzero square.
Solving it gives the two roots and substitution gives exactly the two points
in `(KBC3E-3)`.  Thus the exceptional common-point ledger is exhaustive over
the deployed field.

It remains to test whether either common point can support the outside
records.  Every complete signed atlas contains records `DE+=de` and
`DE-=-de` at distinct unused source roots.  Let their unsquared source sums
be `s_0=d+e` and `s_1=d-e`.  The common Vieta map gives

```text
N_0/D_0=de,       N_1/D_1=-de,
Q_0/D_0=s_0,      Q_1/D_1=s_1.
```

The first pair implies the first equation in `(KBC3E-4)`.  Since
`s_0^2-s_1^2=4de`, clearing `D_0D_1` gives the second equation.  These are
therefore necessary independently of any target reconstruction converse.

Evaluate all eight compact kernel coefficients at each point; the vectors
are nonzero and retain `b11=-b10`.  For each vector form `(KBC3E-4)` in
`z_0,z_1` and saturate by nonzero roots and denominators, distinct squared
labels, and exclusion of the five common squared labels.  Exact Singular
standard bases are `<1>` at both points.  Hence neither exceptional common
point admits even the necessary `DE+/DE-` pair, and no complete packet can
occur there.  The source-sign and duplicate-role transport already proved
for this orbit carries the result from cell 3 to cell 6.  QED.
