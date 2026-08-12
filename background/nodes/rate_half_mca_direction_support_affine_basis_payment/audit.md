# Audit

The primary checker evaluates both rational endpoint terms, verifies that
the ambient-cap endpoint owns every printed rank, checks support-factor
monotonicity by its exact finite difference, validates every adjacent wall,
pins both supplier statements and proofs, and rejects four mutations.

The independent checker builds falling products by recurrence and reduces
rational products by gcd.  It exhaustively counts ordered active-coordinate
tuples in small models to verify the subtraction in `(1)`, checks small
support-factor monotonicity, recomputes every printed boundary, and rejects
three controls.

Both checks use bounded exact arithmetic under RAMguard.  No Modal compute
is used.
