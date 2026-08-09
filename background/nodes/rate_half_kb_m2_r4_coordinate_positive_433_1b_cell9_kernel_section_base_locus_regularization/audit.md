# Audit

- An initial pilot incorrectly tried to use the zero polynomial section as a
  pointwise kernel and stopped with `zero stored kernel`; no result depended
  on that attempt.
- Rank and kernel are now reconstructed from the ten common rows at every
  point.
- The missing row is classified from the reconstructed values.  All points
  are constrained because reconstructed `A(-t^2)` is nonzero.
- Target-sign repetition is checked for identical source data.
