# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_six_packet_bounded_divisor_normal_form`
- **mathematical statement:** every core-one scalar packet has a degree-at-
  most-six distinguished row tail, degree-at-most-four adjugate tail,
  degree-at-most-seven Forney tail, and the signed degree-two Picard relation
  `(SBN5)`
- **scope:** all six packets in `(CTP5)`, first live degree only
- **dependencies:** six-packet classification, core-one adjugate theorem,
  and the contact section
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** failure of a divisibility in `(SBN2)`, residual contact
  degree other than `u`, or failure of `(SBN5)`
- **nonclaims:** the signed divisor is not asserted effective and no packet
  is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_six_packet_bounded_divisor_normal_form/verify.py`
- **upstream mapping:** primitive shift-pair control / exact bounded-tail
  second-moment ledger
