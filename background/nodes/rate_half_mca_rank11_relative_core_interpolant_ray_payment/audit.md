# Audit

1. Empty common support is used only to prove every coordinate error
   polynomial is nonzero.
2. The core-compatible bound counts roots and is valid on every punctured
   evaluation set.
3. Clone classes of size at least `K'` force polynomial identity by RS
   injectivity. No `n'=2K'` assumption is used.
4. The number of large affine clone classes is charged by the crude bound
   `n'`, avoiding the deployed proof's nonportable bound of two.
5. After removing large classes, `m'>K'-1` guarantees at least one
   heterogeneous pair. The proof does not reuse the deployed two-part
   partition formula.
6. The count is in correction pairs and therefore safely overcounts slopes.
7. The final endpoint uses only `n'<=n` and invariant `n'-m'=R-d`.

No Modal computation is used; the replay is constant-size exact arithmetic.
