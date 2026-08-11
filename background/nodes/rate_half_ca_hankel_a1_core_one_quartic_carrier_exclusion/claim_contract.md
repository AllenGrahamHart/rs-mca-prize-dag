# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion`
- **mathematical statement:** a core-one profile with
  `3(e+1)<rho+1` is impossible when
  `floor(p/5)+ell+3<e`; the possible `(4,1)` contact carrier is eliminated
  by descent to a forbidden degree-four Hankel recurrence
- **scope:** half-distance `A=1`, fixed core `s=1`
- **dependencies:** the core-stratified slope-slack ledger, the
  core-stripped Forney contact section, and the pole-cancellation ideal
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a contact-active contained component of another bidegree,
  failure of `Q_0` to divide the contact numerator, or a degree-four
  recurrence compatible with generic kernel degree `d>4`
- **nonclaims:** no core-free exclusion and no exclusion from
  `e=floor(16m/13)` upward
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion/verify.py`
- **upstream mapping:** exact symmetric-Hankel / Forney boundary ledger
