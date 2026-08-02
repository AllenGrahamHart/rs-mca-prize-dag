# Proof

FLINT factors and reconstructs the rational `r,c` denominators, their combined
denominator scale, the first and second removed common scales, and the plane
leading coefficient over `F_2130706433`.  The linear factors have exactly the
five roots `(KBC4E-1)`.  Every remaining factor in the six factorizations is
an irreducible cubic, so this is the complete base-field exceptional set.

The original guarded common ideal is localized by, among other factors,
`t(1-t^2)(1+t^2)`.  Direct modular evaluation gives zero at `t=0`, at
`t=1,-1`, and at `t=16711679,-16711679` because `16711679^2=-1` in the
deployed field.  Thus imposing any exceptional root together with the guard
inverse equation `uG-1=0` yields `-1=0`.  Every exceptional chart is empty in
the original localization, before any denominator clearing or
pseudo-division.  Source transport proves the cell-7 statement.  QED.
