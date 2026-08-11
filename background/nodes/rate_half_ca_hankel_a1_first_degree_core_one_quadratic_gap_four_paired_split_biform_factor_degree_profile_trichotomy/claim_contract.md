# Claim contract

- **Claim:** the extremal paired split biform has constant content, every
  irreducible factor lies on `n_j=ceil(Rm_j/T)`, and the odd/huge-even
  factor degrees have exactly one of the three profiles `(FDT6)`.
- **Dependencies:** the dual-MDS split-biform construction and the
  factorwise incidence-saturation theorem.
- **Output:** `(FDT3)--(FDT6)`, including exhaustion of all global
  `X`-degree slack.
- **Consumer:** the extremal paired-biform route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no profile exclusion, irreducibility, or analogous
  classification in another `A=1` branch.
- **Falsifier:** nonconstant content, a factor above the lower envelope,
  or a feasible degree partition outside profiles I--III.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_paired_split_biform_factor_degree_profile_trichotomy/verify.py`
  and `verify_audit.py`.
