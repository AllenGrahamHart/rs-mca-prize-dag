# Audit

This is an exact finite-field proof, not random search. The generic
quartic-by-quadratic division is not used at exceptional parameters without
replay: every branch denominator, division leading coefficient, source
tower inverse, and norm denominator contributes its roots to the candidate
union.

The independent verifier recomputes the complete root union from the printed
polynomials and rebuilds every finite lift from the pinned structure and
kernel. It does not trust stored terminal statuses.

The three `q` branches can overlap and are internal proof alternatives. The
32-case payment counts only source signs, target lanes, and the two matching
indices; it does not multiply by branch rows.
