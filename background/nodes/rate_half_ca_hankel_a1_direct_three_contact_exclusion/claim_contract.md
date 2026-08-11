# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_direct_three_contact_exclusion`
- **mathematical statement:** exact Forney pole absorption makes
  `s_F^3G/H` regular and forces `ell>=e-3+beta`; officially both live core
  ranges now begin at `ceil((rho-1)/3)`
- **scope:** every half-distance `A=1` residual core profile
- **dependencies:** the core-stratified slope ledger and Forney pole-ideal
  absorption
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a pole of `s_FG/H`, a component on which the three-contact
  product vanishes identically, or a section of the vanishing bundle in
  `(DTC3)` below the printed slack
- **nonclaims:** the six first-degree corners remain open
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_direct_three_contact_exclusion/verify.py`
- **upstream mapping:** exact Forney/SPI pole and contact ledger
