# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_free_degree_two_packet_exclusion`
- **mathematical statement:** both core-free residual-degree-two scalar
  packets are impossible by full-omission overlap and vertical degree modulo
  three
- **scope:** only the two packets in `(CTP4)` at the first live degree
- **dependencies:** core-free bounded-divisor normal form and the local cube
  charge
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** an excess degree not producing omission despite `O=Delta`,
  or a degree-`e` vertical multiplicity partition satisfying `(4),(5)`
- **nonclaims:** core-free residual degrees `3,4,5` remain open
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_free_degree_two_packet_exclusion/verify.py`
- **upstream mapping:** primitive shift-pair control / exact regular-tail
  exclusion
