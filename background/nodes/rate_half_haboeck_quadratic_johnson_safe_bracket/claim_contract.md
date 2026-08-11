# Claim contract

- **Claim:** the strongest rate-half safe agreement supplied by Haboeck's
  proved quadratic theorem under the exact prize bad-slope budget.
- **Dependency:** `haboeck_quadratic_johnson_mca_import`.
- **Inputs:** `n=2^41`, `k=2^40`, an admissible field order `q<2^256`, and
  the finite-affine prize sampler.
- **Output:** `(RHJ3)` for every affordable `m`, the exact budget and support
  optimizers `(RHJ7)--(RHJ8)`, and the razor brackets `(RHJ9)`.
- **Consumer:** safe-side evidence for `rate_half_band_crossing_location`.
- **Nonclaims:** no adjacent-unsafe certificate, no exact crossing, no
  support-sensitive improvement between theorem thresholds, no ordinary LIST
  bound, no projective sampler, and no BCHKS25 linear bound.
- **Falsifier:** an incorrect source-to-prize normalization, a failed adjacent
  square inequality defining `Q_m` or `a_m`, or an admissible `q<2^256` for
  which `m>=96` meets the printed budget.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/verify.py`
  and the independent full-staircase checker `verify_audit.py`.
