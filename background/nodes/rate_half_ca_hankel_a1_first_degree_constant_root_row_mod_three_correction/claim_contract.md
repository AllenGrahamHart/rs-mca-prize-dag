# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_constant_root_row_mod_three_correction`
- **mathematical statement:** every heavy root row of the scalar residual
  obeys `c_x+epsilon_x-t_x=0 mod 3`, with the resulting corrected rank budget
- **scope:** official first degree, core zero or one, parameter-constant
  profile
- **dependencies:** constant-residual triple-tangency theorem
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a root row whose complete vertical cube ledger violates
  `(RMC3)`, or overlap/new-root accounting inconsistent with `(RMC2)`
- **nonclaims:** no remaining scalar degree is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_constant_root_row_mod_three_correction/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
