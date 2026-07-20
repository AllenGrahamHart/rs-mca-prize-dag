# Audit - L1 two-petal small-support anchor closure

## Checked axes

1. Both petal supports are positive because they are touched; `z>=1`.
2. The inequality `ell-r<=z` uses `a<=d`, not merely `a<=ell`.
3. The inequality `ell-a<=z` uses `r<=d`, which requires `W!=0`.
4. The defect ceiling uses the strict maximality fact `r<ell`; replacing it
   by `r<=ell` loses one at the B11 boundary.
5. `G_R` uses the deficit of the larger support, namely `ell-a`.
6. The singleton conclusion is a paid-subclass theorem, not a statement that
   all two-petal words are absent.

## Remaining attack

For the critical singleton bucket, only profiles touching at least three
petals remain. More generally, a two-petal residual must have its smaller
support grow with the row.
