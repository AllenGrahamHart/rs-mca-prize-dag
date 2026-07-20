# Claim contract

- **claim id:**
  `rate_half_list_budget_three_fiber_two_path_exclusion`
- **mathematical statement:** three pairwise-coprime one-root deletions from
  common `X^2`-fiber unions of common half-degree cannot satisfy the
  nondegenerate tight-triangle relation once the half-degree is at least two
- **scope:** every field and every common degree `s>=2`; in particular both
  official path-plus-singleton chambers at `d=2^39`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** budget-three multifiber Vandermonde exclusion
- **new open content:** path constructions with fiber size one, mixed maps,
  partial fibers, and primitive locators; all non-path chambers retain their
  previous residuals
- **falsifier:** pairwise-coprime `A_i` satisfying `(F2P1)--(F2P3)` at some
  common degree `s>=2`
- **nonclaims:** no four-cycle or primitive path construction is excluded;
  the rate-half adjacent crossing is not located
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_fiber_two_path_exclusion/verify.py`
- **upstream mapping:** exact SPI/split-pencil ledger; finite path chamber
  exclusion
