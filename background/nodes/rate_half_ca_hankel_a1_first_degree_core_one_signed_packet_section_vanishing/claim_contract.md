# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_signed_packet_section_vanishing`
- **mathematical statement:** each of the three signed tangent packets has
  `h^0(C,O_C(rho+2,-e-1))=0`
- **scope:** packets `(1,1,1,4)`, `(2,0,1,5)`, and `(2,0,2,6)`
- **dependencies:** exact signed-packet local normal forms
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a positive coefficient equal to its full vertical-fibre
  multiplicity, a modification direction meeting the constant line, a
  second section of `O_C(P_3)`, or vanishing of its canonical section on
  `R_0`
- **nonclaims:** section vanishing is not an exclusion of the packet
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_signed_packet_section_vanishing/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
