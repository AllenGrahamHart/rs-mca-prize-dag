# Claim contract

- **Claim:** the Forney norm-discriminant square gate reduces exactly to the
  determinant class of the original weighted self-dual frame.
- **Scope:** every exceptional endpoint packet satisfying the Forney identity
  and weighted self-duality; no MDS assumption.
- **Dependencies:** the norm-discriminant gate and Forney interpolation.
- **Consumer:** route selection under `rate_half_band_closure`.
- **Falsifier:** a valid packet violating `(HNC1)`, or a weighted self-dual
  frame for which `(HNC2)` is nonsquare.
- **Nonclaims:** an independently derived endpoint formula for `Xi_A` could
  still contradict `(HNC1)` and exclude a profile.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_square_cancellation_fence/verify.py`
