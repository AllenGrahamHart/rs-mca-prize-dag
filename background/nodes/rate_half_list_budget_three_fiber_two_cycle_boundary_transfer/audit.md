# Audit

- Recomputed every doubled-order integer rather than replacing `2^37` by
  `2^38` textually.
- The intermediate rounding changes: at order `2^40`, its minimal
  differential residual is linear, not quadratic.
- Both generic and intermediate floors now have the same two-zero primary
  gap ending at index `2^38+1`.
- Applied the deleted-pair parity theorem only when the roots of `D_*` itself
  form two antipodal pairs. The cycle-router count `c` concerns completion
  roots and is a different classification.
- Replayed the canonical-span proof with completion roots `rho_i`. For
  `c=1,2`, denominator square-root lifts are not substituted for them.
- Did not import the later Mobius-ratio, scalar, Jacobi, or norm gates into
  mismatch strata.
- Arithmetic controls cover several even and odd dyadic exponents and trip on
  a one-unit mutation of the intermediate floor. No Modal computation was
  used.
