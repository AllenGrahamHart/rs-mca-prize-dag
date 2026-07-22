# Claim contract

- **Claim:** the quotient-ring trace of the clean-fiber logarithmic
  derivative is the printed scalar in `(QLT2)`, independently of
  `deg_X W`.
- **Scope:** every clean fiber in both sharp high-distance endpoint profiles.
- **Dependencies:** the exact unit resultant and quotient-ring jet compiler.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a valid corrected square with a nonunit `w`, failure of the
  resultant logarithmic derivative, or a trace unequal to `(QLT2)`.
- **Nonclaims:** the scalar gate has not yet been evaluated uniformly on
  either endpoint profile and is not itself an exclusion.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_unit_resultant_log_trace_gate/verify.py`
