# Claim contract

- **Claim:** the official `A=1,s=1,e=2m-1` distance-three external split
  design is impossible.
- **Scope:** the exact distance-three chart produced by the MDS-escape and
  pair-Lagrange routers.
- **Dependencies:** the support pair-crossing necessity theorem and the
  all-deficient Pade residual discriminant exclusion.
- **Consumer:** `rate_half_band_closure`.
- **Falsifier:** an exact external design whose pair-crossing packet escapes
  the all-deficient branch, or a packet satisfying every hypothesis of the
  residual exclusion.
- **Nonclaims:** high quotient-distance charts, other `A=1` component faces,
  and the strict or half-distance `A=3` profiles remain open.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_exclusion/verify.py`
