# Claim contract

This is an abstract incidence ledger.  It assumes:

1. one unique circuit in each full-rank eleven-set;
2. the exact rank-nine shadow multiplicity `q_c`;
3. one honest global capacity `G` for all marked rank-nine shadows; and
4. recordwise low-support cap vectors.

It does not produce `G` or the vectors `L_c`.  It does not apply separate
high and low capacities additively.  Its point is precisely to prevent that
double spending.

No kernel incidence, component-density demand, row closure, chronology, or
prize closure is asserted here.
