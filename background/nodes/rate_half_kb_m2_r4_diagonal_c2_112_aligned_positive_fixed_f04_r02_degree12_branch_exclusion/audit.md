# Audit

- This is a logical composition node; it introduces no new computation.
- The verifier checks all four required node IDs, statuses, and the exact
  partition labels in this statement.
- `L6=0` and `s=0` were replayed literally in `F04-R02`; the composition does
  not rely on transport from another cell.
- The result is intentionally scoped to one resultant factor, not the full
  fixed cell.
