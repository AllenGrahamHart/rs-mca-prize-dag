# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_free_two_packet_bounded_divisor_normal_form`
- **mathematical statement:** both core-free degree-two packets have row and
  Forney tails of degree at most two and three, regular-determinant tail at
  most one, and the signed degree-one Picard relation `(CFN5)`
- **scope:** only the two packets in `(CTP4)`
- **dependencies:** constant triple-tangency packets, contact section, and
  the regular Kronecker determinant ledger
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** failure of `(CFN2)` or `(CFN3)`, residual contact degree
  other than one, or failure of `(CFN5)`
- **nonclaims:** the signed degree-one class is not asserted effective
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_free_two_packet_bounded_divisor_normal_form/verify.py`
- **upstream mapping:** primitive shift-pair control / exact regular-tail
  second-moment ledger
