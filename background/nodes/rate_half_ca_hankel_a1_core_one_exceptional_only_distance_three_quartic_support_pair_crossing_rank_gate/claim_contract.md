# Claim contract

- **Claim:** every valid support matching supplies, for each omitted pair,
  a nowhere-zero-on-the-other-pairs quartic in the kernel of the explicit
  support-only matrix `R_l`.
- **Scope:** the official generic saturated distance-three chart; rank-five
  exclusion is available from `e>=6`.
- **Dependency:** quartic internal-slice lambda-cube kernel.
- **Consumer:** `rate_half_band_closure` and `CR-003-CLIFT`; first exact
  support/matching rejection gate.
- **Falsifier:** a valid exact design with `rank R_l=5`, or whose asserted
  quartic fails one pair crossing or vanishes on a retained exceptional
  root.
- **Nonclaims:** rank five is not asserted universally. Rank at most four is
  not sufficient for compatible cube labels, internal slopes, or an
  external design.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pair_crossing_rank_gate/verify.py`
