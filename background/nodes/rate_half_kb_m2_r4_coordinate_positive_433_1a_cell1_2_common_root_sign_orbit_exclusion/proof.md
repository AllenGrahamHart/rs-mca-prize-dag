# Proof

The common Vieta compiler proves that, on the globally proved rank-six base
stratum, a common coefficient kernel exists exactly when all six minors
`M_ij` vanish.  Every factor removed by `strip_fast` is a factor of the
printed guard product `G`; division by those factors is therefore an
equivalence after adjoining `zG-1`.

The Modal launcher reconstructs the six minors and `G` directly from the
compiler over `F_2130706433`.  For each of the two cell-1 representatives it
runs an ordinary-polynomial Singular standard basis twice:

1. on `<M_12,M_13,M_14,zG-1>`;
2. on `<M_12,M_13,M_14,M_23,M_24,M_34,zG-1>`.

Both computations return the one-element basis `<1>` for both sign-product
classes.  The first computation alone is sufficient: its zero set is a
superset of the six-minor zero set.  The second computation is a direct
full-system replay.

The exact root-sign quotient proves that cells `1,2` have precisely two
orbits, distinguished by `epsilon_1 epsilon_2`, represented by the two rows
computed here.  Thus no admissible common record exists in any of their
eight raw rows.  The previous theorem deletes the separate `[5,8]` orbit,
so ten quotient representatives minus one minus two leaves seven. QED.
