# Audit

- This is a logical composition node; it introduces no new computation.
- The verifier checks all four required node IDs, statuses, literal-cell
  coverage, and the exact partition labels.
- `s=0`, `L6=0`, `K8!=0`, and both `K8=0` leaves were replayed literally in
  each of the four cells.
- The result is intentionally scoped to one resultant factor, not the full
  fixed cells or the four `R20` degree-12 branches.
