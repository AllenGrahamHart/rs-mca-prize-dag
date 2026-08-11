# Audit

- The exact identity `t=C_tot-O` is used before any local classification;
  this prevents a new excess root from being silently treated as an overlap.
- The one spare excess degree in `(2,0,1,5)` is tested at the ordinary point
  and away from the distinguished row. Both placements violate the ordinary
  cube divisibility, so it is forced onto one distinguished incidence.
- `A` and `B` are divisors, not assumed distinct points. Their possible
  overlap is retained in `(SLN2)`--`(SLN4)`.
- Vertical congruences are converted to divisor equations only after using
  the exact degree `e`; no transversality or reduced-fibre assumption is
  made.
- The resulting degree-two classes remain signed. The proof neither calls
  them effective nor imports the no-ordinary pushforward classification.
