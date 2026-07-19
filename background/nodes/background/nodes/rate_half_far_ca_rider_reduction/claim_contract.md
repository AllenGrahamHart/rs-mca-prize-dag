# Claim contract

- **Claim:** exact anchor/rider reduction of far-pair CA slopes to a deficient
  interleaved pair list, with at most `r+1` riders per list member and doubly
  sparse normalization.
- **Quantifiers:** every linear code and every integer radius `r<n/2`.
- **Dependencies:** linearity and the definitions of CA and column farness.
- **Consumer:** far-CA term exposed by `rate_half_mca_sparse_layer_reduction`.
- **Nonclaims:** no bound on `L_2(n-2r)` and no assertion that the resulting
  sufficient prize inequality holds.
- **Falsifier:** a non-anchor bad slope producing no pair-list member, or one
  member carrying more than `r+1` rider slopes.
- **Upstream crosswalk:** `tex/towards-prize.tex`, Theorem `thm:rider` and
  Corollary `cor:doubly`.
