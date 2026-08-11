# Claim contract

- **Claim:** the `m+1` coefficient vectors of the clean kernel generator form
  a common totally isotropic plane for four adjacent endpoint Hankel forms,
  whose exact endpoint radicals are `q_0` and `q_m=q_inf`.
- **Dependencies:** the rational-normal kernel theorem and clean resultant
  boundary saturation.
- **Output:** equations `(FHB2)--(FHB7)`, coupling the resultants to the
  original syndrome pencil.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no classification or exclusion of the bi-isotropic frame.
- **Falsifier:** dependent coefficient vectors, an endpoint square block of
  rank other than `rho`, a nonzero pairing in `(FHB5)`, or failure of the
  diagonal frame translation.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_four_hankel_biisotropic_frame/verify.py`
  and `verify_audit.py`.
