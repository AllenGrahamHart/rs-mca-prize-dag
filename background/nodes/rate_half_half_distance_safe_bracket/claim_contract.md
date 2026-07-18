# Claim contract

- **Claim:** safe agreement `3n/4` for the official rate-half row whenever
  `q>=2^169`, and the resulting two-sided agreement bracket.
- **Dependencies:** the exact half-distance MCA-from-CA theorem and the
  published CA proximity-gap theorem already imported by
  `mca_from_ca_reduction`; exact integer arithmetic.
- **Consumer:** high-field upper bracket for `rate_half_band_closure`.
- **Nonclaims:** no self-contained CA proof, no field range below `2^169`, and
  no adjacent determination.
- **Falsifier:** failure of the imported endpoint convention, `2r>n-k`, or
  `n>floor(q/2^128)` in the stated field range.
- **Upstream crosswalk:** `tex/towards-prize.tex`, Theorem `thm:half` and
  Corollary `cor:import`.
