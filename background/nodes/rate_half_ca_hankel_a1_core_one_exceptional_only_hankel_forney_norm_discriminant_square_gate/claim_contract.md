# Claim contract

- **Claim:** the Forney unit norm divided by the exceptional discriminant is
  a field square, equivalently `(HNS1)`.
- **Scope:** both sharp high-distance endpoint profiles, without an MDS
  assumption.
- **Dependency:** the Forney-residue weighted self-dual algebra.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a valid endpoint packet with nonzero nonsquare `Xi_A`, or a
  sign mismatch in the discriminant conversion.
- **Nonclaims:** the square class of `Xi_A` is not yet evaluated uniformly on
  the official profiles.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_discriminant_square_gate/verify.py`
