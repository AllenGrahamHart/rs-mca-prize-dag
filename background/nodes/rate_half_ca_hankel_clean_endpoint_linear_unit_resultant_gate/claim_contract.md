# Claim contract

- **Claim:** the clean weld forces the exact resultant product `(LUR3)` and
  splits the exceptional fibre orders as `1+(m-1)` in `(LUR5)`.
- **Dependency:**
  `rate_half_ca_hankel_clean_endpoint_two_sided_complement_weld`.
- **Output:** a genuinely parameter-dependent degree-`<m` element whose norm,
  away from the chosen infinity fibre, has one simple zero and no other
  finite zero; both weld factors and the weld quotient are nonzero.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no exclusion of the low-degree unit and no classification of
  the factors supported on `q_inf`.
- **Falsifier:** a clean weld violating the resultant product, an exceptional
  valuation other than `1` for `B`, or a resultant factor away from
  `q_inf(X)(X-x_0)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_linear_unit_resultant_gate/verify.py`
  and `verify_audit.py`.
