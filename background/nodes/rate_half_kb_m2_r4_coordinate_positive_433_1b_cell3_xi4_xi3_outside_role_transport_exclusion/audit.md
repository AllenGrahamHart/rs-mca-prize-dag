# Audit

- The full seven product rows and all seven signed squared-sum rows are
  compared as exact sparse integer polynomials.
- The transport transposes only `xi=3` and `xi=4`; all other atlas rows are
  fixed.
- Deleting `xi=4` before transport and `xi=3` after transport gives
  byte-position-equivalent six-row lists, so all 15 matching indices are
  fixed rather than merely permuted.
- The full nonzero and pairwise-not-opposite target guard divisor is invariant
  up to unit signs.
- Both sign-cycle invariants and all four target lanes are fixed.
- The source role-cell census independently confirms that the outside map
  fixes cell 3, while the unrelated `B,C` exchange sends cell 3 to cell 6.
- The six supplier matching sets are disjoint and cover `{0,...,14}`.
- A separately written audit exhausts small integer targets and reconstructs
  the record, squared-sum, guard, and lane identities without importing the
  primary polynomial implementation.
