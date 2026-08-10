# Audit

## Checked points

- The support map is injective because locators are monic and squarefree.
- The MDS distance controls the support union, which is enough to obtain the
  binary symmetric-difference bound even when error values cancel.
- Complementation is performed before shortening and preserves distance.
- Shortening fixes a common `j`-subset; it does not puncture arbitrary
  coordinates and therefore preserves the full pairwise distance.
- The positive denominator is checked after shortening. No division is made
  when `Delta_j<=0`.
- The required-background factor is retained exactly.

## Route fence

The theorem can be exponential when `j` grows. It cannot be promoted to the
large-source target without an exact outer aggregation and a finite budget
check.
