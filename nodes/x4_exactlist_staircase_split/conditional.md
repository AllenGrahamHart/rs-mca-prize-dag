# x4_exactlist_staircase_split conditional proof

## Predicate nodes

- `moment_trade_staircase`
- `x4b_moment_trade_exclusion`
- `u1_pullback_dichotomy`

## Claim

The corrected exact-list split follows from the charged staircase mechanisms,
the p-specific moment-trade handling, and the post-dictionary primitive cap.

## Proof

Partition an exact-list family by the first cancellation mechanism visible in
the locator differences.

The quotient and dihedral staircase families are explicit charged columns:
their locator forms are printed in the node statement, and their counts are
the exact binomial columns already checked by the QA.22 arithmetic.

If the cancellation comes from a primitive `t`-moment-null block, then
`moment_trade_staircase` shows that it is a genuine staircase column of the
same kind: the top `t` locator coefficients vanish, so unions of such blocks
preserve the top coefficients and produce exact-list witnesses. The predicate
`x4b_moment_trade_exclusion` either removes these families at the official row
or emits their exact charged column.

After quotient, dihedral, and moment-trade columns are stripped, every
remaining same-top-`t` locator family is in the primitive no-trade remainder.
The predicate `u1_pullback_dichotomy` is precisely the post-dictionary
compression statement for that remainder: all but `<= n^2` canonical trades are
charged by the finite pullback dictionary. Hence the PrimitiveExactList term is
bounded by the advertised `n^2` target.

The quotient-row transport is identical because each ingredient is formulated
in terms of locator coefficients and stable pullback dictionaries, which
commute with the quotient-row substitution. Thus the corrected split is
conditional exactly on the three predicate nodes above.
