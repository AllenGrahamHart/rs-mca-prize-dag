# Frontier audit: worst-word challenger pricing

Status: TARGET, intentionally left open.

This node is the conditional assembly for the low-slack non-planted
challenger class exposed by E15. Its sole open truth input is
`ww_row_envelope_clause`; W2 and Lemma A are proved.

To close it, one needs either:

- emit the official cell descriptor and paid-column subtraction inventory;
- prove that its ordered paid-plus-residual ownership map is exhaustive and
  disjoint;
- prove aggregate first-match allocations for every received word; or
- falsify W3 with one official word whose total challenger count exceeds its
  exact residual, then revise the safe-side strategy.

Per-cell comparison with the whole row residual is retired: it does not sum.
The undefined `K_cell` route remains a wall, not a premise.
The E15/staircase identification cannot be used to erase W3 until it is proved
at the full official scope; it currently serves only as the reason that column
ownership must be explicit.

The bounded source audit and exact missing registry fields are recorded in
`../ww_row_envelope_clause/specification_frontier.md`. Until those inputs are
materialized, more toy censuses do not advance the closing certificate.
