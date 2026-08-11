# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_gap_zero_two_point_normal_form`
- **mathematical statement:** the `(u,v,I_0,c)=(0,2,0,2)` core-one packet
  has exactly two double parameter roots, adjugate factor equal to the row
  radical, a cubic residual Forney numerator, and an effective degree-two
  Picard relation
- **scope:** only the first of the six core-one packets at the first live
  `A=1` degree
- **dependencies:** constant triple-tangency packets, the general core-one
  adjugate factorization, and the contact section
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** another root of the distinguished row, a nonsimple zero of
  `D`, failure of the divisibilities in `(ZTP4)`, or failure of `(ZTP6)`
- **nonclaims:** the effective degree-two relation is not excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_gap_zero_two_point_normal_form/verify.py`
- **upstream mapping:** primitive shift-pair control / exact middle-Hankel
  defect ledger
