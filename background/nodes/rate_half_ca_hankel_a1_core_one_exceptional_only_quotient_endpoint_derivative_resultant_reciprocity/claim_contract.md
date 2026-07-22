# Claim contract

- **Claim:** the endpoint resultant profile fixes the exact ratio
  `Res(A,q_1)/Res(A,q_e)` by `(QDR1)` or `(QDR2)`.
- **Scope:** the two sharp high-distance endpoint profiles.
- **Dependency:** the complete exceptional endpoint resultant profile.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a valid endpoint packet whose bottom or leading resultant
  coefficient violates the relevant identity.
- **Nonclaims:** the identities do not determine either resultant separately
  and do not exclude either profile.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_endpoint_derivative_resultant_reciprocity/verify.py`
