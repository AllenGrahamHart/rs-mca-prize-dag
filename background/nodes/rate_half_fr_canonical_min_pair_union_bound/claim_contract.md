# Claim contract

- **Claim:** the corrected `(FR)` intersection and outside-spend bounds at a
  minimum pair-union joint support.
- **Inputs:** a finite family of locator sets with sizes
  `u_gamma=rho-o_gamma` and a pair minimizing their union.
- **Output:** `(FRC2)--(FRC4)`.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaims:** no arbitrary-`W` bound, no proof that `a*=7m-1`, no
  saturation theorem, no closure of the type-2 capacity ledger, and no exact
  adjacent crossing.
- **Falsifier:** a finite set family, a minimizing pair `(g,h)`, and a third
  member violating `(FRC2)` or `(FRC3)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_fr_canonical_min_pair_union_bound/verify.py` and
  the independent four-set replay `verify_audit.py`.
