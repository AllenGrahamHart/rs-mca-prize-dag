# Claim contract

- **Claim:** MDS forces the maximal allowed Schur-square dimension and a
  unique Forney weight line; non-MDS produces complementary dependent
  maximal minors.
- **Scope:** both sharp high-distance endpoint profiles.
- **Dependencies:** the Forney-residue product bound and weighted
  complementary-minor law.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** an MDS frame with product dimension below `2e-1`, or a
  vanishing maximal minor whose complement is nonzero.
- **Nonclaims:** no proof that the official frame is MDS and no exclusion of
  the dependent-complement branch.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_mds_schur_router/verify.py`
