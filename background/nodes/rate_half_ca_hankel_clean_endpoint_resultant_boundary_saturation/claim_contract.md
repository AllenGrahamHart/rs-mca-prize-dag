# Claim contract

- **Claim:** the clean unit-resultant gate has `deg_z W=T`, assigns the full
  parameter-infinity resultant to `B`, and forces `deg_X B=N`.
- **Dependency:**
  `rate_half_ca_hankel_clean_endpoint_linear_unit_resultant_gate`.
- **Output:** the exact Bezout pin `(RBS2)`, resultant identities `(RBS5)`,
  and saturated dual-complement degree `(RBS6)`.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no value of `b`, no ambient factorization of `B`, and no
  exclusion of the saturated profile.
- **Falsifier:** a clean weld with `deg_z W<T`, a `q_inf` factor in
  `Res_z(Q,W)`, a missing `q_inf` factor in `Res_z(Q,B)`, or `deg_X B<N`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_resultant_boundary_saturation/verify.py`
  and `verify_audit.py`.
