# Claim contract

- **Claim:** the (C2) per-slope floor `(R+1) - w*` is negative at the
  adversarial `w* = 2r` for every offset in the half-open bracket
  `[k+2^34, 3n/4)` at rate one half, equalling `-1065151889407` at razor
  shape, with the sign flipping to exactly `+1` at the excluded top
  `a = 3n/4`.
- **Dependencies:** none — exact integer arithmetic on the banked razor
  constants; the (C2) floor definition from the round-35 R-FG-RAZOR
  addendum.
- **Output:** a scope fence — no transport of `(C2)`/`(C3)`/`(C4)`/
  `X_gamma`/layer-A instruments into the bracket can bind.
- **Consumer:** the far-CA lane inside `rate_half_band_crossing_location`.
- **Nonclaims:** nothing about the true value of `B_ca^far` on the bracket
  (that is the value ledger's question); no field-dependent or measured
  content; the `w*` measurements in the source (24-locator cap) are not
  re-verified, only noted to point in the fence's favour.
- **Falsifier:** any admissible-`W` forcing theorem giving
  `|S_g ^ S_h| >= 62r/63` on the bracket, or an arithmetic error in the
  replayed integers.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_type2_ledger_vacuous_by_sign_fence/verify.py`
  and the independent monotonicity audit `verify_audit.py`.
