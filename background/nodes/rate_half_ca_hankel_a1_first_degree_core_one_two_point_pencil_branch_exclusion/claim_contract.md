# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_two_point_pencil_branch_exclusion`
- **mathematical statement:** the two modification directions are supported
  nilpotents in distinct double fibre factors and project independently to
  the negative pushforward block, so only the unique-section splitting occurs
- **scope:** the `(u,v,I_0,c)=(0,2,0,2)` packet
- **dependencies:** two-point normal form and pushforward dichotomy
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a modification direction with nonzero value on another
  fibre factor, intersection of `W` with the constant line, or the PENCIL
  splitting
- **nonclaims:** the remaining CANONICAL packet is not excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_two_point_pencil_branch_exclusion/verify.py`
- **upstream mapping:** primitive shift-pair control / local fibre algebra
