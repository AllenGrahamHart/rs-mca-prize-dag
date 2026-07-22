# Audit

- Peeling tests the density of the current family, not the original family.
- A fresh minimal core and trade are recomputed after each deletion.
- The terminal estimate uses the current union before replacing it by `N`.
- Exceptional slopes and terminal normalized blocks are disjoint and are
  added exactly once in `(PO2)`.
- Canonical ownership removes within-cell core/trade duplication but does not
  prove a cross-cell aggregate.
- The `<n` remainder is much smaller than `8n^3`; it is not claimed to be
  zero.
- No Modal or large local computation is used.
