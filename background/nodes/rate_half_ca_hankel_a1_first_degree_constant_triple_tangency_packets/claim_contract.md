# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_constant_triple_tangency_packets`
- **mathematical statement:** away from roots of the residual `X`-form,
  every heavy supported incidence has horizontal intersection multiplicity
  divisible by three and consumes two excess-recurrence degrees; the
  smallest core-zero and core-one residuals reduce to the packets in
  `(CTP4)` and `(CTP5)`
- **scope:** `e=ceil((rho-1)/3)`, `j=0`, and only `(s,a)=(0,2),(1,1)`
- **dependencies:** the ambient cube identity and constant heavy-incidence
  pin
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** an ordinary heavy incidence of horizontal multiplicity
  below three, failure of `(CTP2)`, or a packet outside the printed lists
- **nonclaims:** neither packet list is excluded; no ordinary incidence is
  assumed transverse
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_constant_triple_tangency_packets/verify.py`
- **upstream mapping:** exact SPI multiplicity ledger / primitive shift-pair
  control
