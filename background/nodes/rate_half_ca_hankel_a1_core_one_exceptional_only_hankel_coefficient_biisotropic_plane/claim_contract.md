# Claim contract

- **Claim:** the `e+1` parameter coefficients of the minimal kernel vector
  form a maximal common totally isotropic plane with the endpoint
  intersections `(HBI5)`.
- **Scope:** the official `A=1,s=1,e=2m-1` exceptional-only face.
- **Dependencies:** the symmetric Kronecker profile, exceptional Hankel
  factor pin, and kernel-plane transversality.
- **Consumer:** the high-distance and remaining component branches of
  `rate_half_band_closure`.
- **Falsifier:** dependent coefficient vectors, a nonzero pairing in
  `(HBI4)`, or an endpoint radical intersection larger than `(HBI5)`.
- **Nonclaims:** the isotropic plane is not classified and no endpoint
  profile is excluded solely by its existence.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_biisotropic_plane/verify.py`
