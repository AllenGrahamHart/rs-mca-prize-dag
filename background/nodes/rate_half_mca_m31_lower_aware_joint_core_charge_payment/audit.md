# Audit

- The lower bounds are total-core lower bounds, not merely inside-core
  bounds; `(LA6)` supplies exactly that quantity.
- Sorting is legitimate because line labels do not occur in the objective.
  The exchange proof explicitly preserves the sorted lower constraints.
- The rational line-charge sum is floored only after summing all lines.
- The final line is not included in the removed-line charge that forces it;
  it is included in the packing contradiction.
- Zero inside-core bounds are omitted from the pair penalty in `(LA7)`.
- The primary verifier recomputes every cap and guard.  The independent audit
  uses only the three endpoint ledgers and exact `Fraction` arithmetic.
- The adjacent record is a failure of this compiler.  It is not evidence
  that `e=130222` is unsafe.
- A rank-by-rank subset-core audit was also tested at the adjacent row.  It
  removes the artificial five-full-core concentration but still fails to
  force a second positive core; it is retained as route information, not as
  part of this theorem.
