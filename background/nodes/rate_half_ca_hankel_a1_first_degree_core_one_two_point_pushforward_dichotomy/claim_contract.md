# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_two_point_pushforward_dichotomy`
- **mathematical statement:** the effective two-point Picard class has one
  of exactly two finite-pushforward splittings, with section count two or one
- **scope:** the `(u,v,I_0,c)=(0,2,0,2)` core-one packet
- **dependencies:** the core-one two-point normal form
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a third splitting, an exponent-two local modification, or a
  section count different from `(TPD4)`
- **nonclaims:** neither the low-degree-pencil nor unique-section branch is
  excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_two_point_pushforward_dichotomy/verify.py`
- **upstream mapping:** primitive shift-pair control / exact Picard ledger
