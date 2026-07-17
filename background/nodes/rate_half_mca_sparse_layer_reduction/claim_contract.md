# Claim contract

- **Claim:** exact equality of the support-wise MCA numerator with the maximum
  of the far-pair CA numerator and sparse mutual numerator.
- **Quantifiers:** every finite field, every linear code, and every integer
  agreement `1<=a<=n`.
- **Dependencies:** only linearity and the definitions of CA, MCA, common
  column distance, and support.
- **Consumer:** safe-side decomposition in `rate_half_band_closure`.
- **Nonclaims:** no bound on either numerator, no candidate crossing, and no
  use of the half-distance regime.
- **Falsifier:** a pair for which translation by a closest code pair changes
  the MCA-bad slope set, or a toy row violating `(MS1)`.
- **Upstream crosswalk:** `tex/towards-prize.tex`, Theorem `thm:sparsify`.
