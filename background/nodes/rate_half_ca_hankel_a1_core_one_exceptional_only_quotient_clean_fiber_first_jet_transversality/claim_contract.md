# Claim contract

- **Claim:** every clean supported root in the exceptional-only corrected
  square is parameter-transverse and obeys `(QJT5)`; on the official smooth
  domain this becomes the cubic-numerator formula `(QJT7)`.
- **Scope:** every ordinary supported slope of the exceptional-only face,
  including both sharp high-distance endpoint profiles.
- **Dependencies:** the full reciprocal square, two-sided split saturation,
  and the active-core domain partition.
- **Consumer:** the high quotient-distance branch of
  `rate_half_band_closure`.
- **Falsifier:** a clean selected root with `F_t=0`, `W_vee=0`, or a failure of
  `(QJT4)` after replaying `(QJT1)`.
- **Nonclaims:** the velocity formula alone does not exclude either endpoint
  resultant profile or the interior high-distance interval.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality/verify.py`
