# Claim contract

- **Claim:** the marked square Hankel pencil has generic corank one and
  adjugate `Dqq^T`, where `D=Delta Q(-;x_0)` has factor degrees `m-1` and
  `m`; every cofactor has the printed `rho`-subset Cauchy-Binet expansion,
  and at least `2m+3` supported slopes give nonzero rank-one split-locator
  specializations.
- **Dependencies:** the marked-row support theorem and the primitive
  rational-normal kernel curve.
- **Output:** an exact finite subset ledger for the remaining clean Hankel
  obstruction.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no sign, positivity, or termwise noncancellation theorem.
- **Falsifier:** generic marked rank below `rho`, a scalar adjugate degree
  different from `2m-1`, failure of the `Delta Q(-;x_0)` factorization, a
  missing cofactor term/sign, or fewer than `2m+3` nonzero supported
  specializations.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_marked_adjugate_subset_ledger/verify.py`
  and `verify_audit.py`.
