# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion`
- **mathematical statement:** a core-one profile is impossible when
  `floor(p/5)+ell+3<e`; any product of contact-active components contained
  in the degree-four clearer is eliminated by descent to a forbidden
  degree-at-most-four Hankel recurrence
- **scope:** half-distance `A=1`, fixed core `s=1`
- **dependencies:** the core-stratified slope-slack ledger, the
  core-stripped Forney contact section, and the pole-cancellation ideal
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** failure of the inactive component product to divide the
  contact numerator, or a degree-at-most-four
  recurrence compatible with generic kernel degree `d>4`
- **nonclaims:** no core-free exclusion; degrees from
  `e=floor(16m/13)` upward are narrowed but not excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion/verify.py`
- **upstream mapping:** exact symmetric-Hankel / Forney boundary ledger
