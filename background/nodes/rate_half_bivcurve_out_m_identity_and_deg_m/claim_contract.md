# Claim contract

- **Claim (POSED):** at a minimising pair union with (SAT1)-(SAT4),
  `T = rho+2`, `a = 7m-1`: (OUT-m) `X'_gamma + 2X''_gamma >= m-1-eps_gamma`
  with the corrected aggregate `(m-1)(1+O)` (the original `1+O` rider is
  FALSE); the exact double-count identity (OUT-ID); and the (DEG-m)
  corollary `deg_Sh(gamma) + X''_gamma >= ceil((m-1-eps~)/2)` with middle
  budget `(m-1)(m-2)`, forcing middle support for degree-1 slopes at
  `m >= 4`.
- **Dependencies:** none for the arithmetic (checked by both verifiers);
  the geometry (the placement argument) is the source addenda's and is NOT
  re-derived.
- **Output:** a configuration-space constraint for the (BIV-CURVE) lane;
  the completion-level upgrade of the 2-sharing m=4 negative; the D11
  rename (`deg_Sh`) as the disambiguation of record.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaims:** no existence claim (the `T = rho+2` class is expected
  EMPTY at `m >= 2` by three instruments); no proof.md (POSED would be
  overstated); no DFS ceiling re-run; single witnesses are not
  distributions.
- **Falsifier:** a configuration violating (OUT-ID)'s double count
  (impossible — it is an identity); a sigma-design with a degree-1 slope
  and no middle support at `m >= 4`; or (for the POSED geometry) a
  placement argument counterexample.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivcurve_out_m_identity_and_deg_m/verify.py`
  and the deterministic-structures audit `verify_audit.py`.
