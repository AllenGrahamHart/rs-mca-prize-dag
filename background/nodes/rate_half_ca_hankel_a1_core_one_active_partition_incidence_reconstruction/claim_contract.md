# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction`
- **status:** PROVED
- **claim:** the clean/saturated partition data of either live active system
  has a connected nonincidence graph. Its monic locator ratios factor into
  unique row/column potentials, and coefficientwise degree-`e_*`
  Reed--Solomon membership is necessary and sufficient to reconstruct the
  unique compatible biform up to scalar. The clean-locator,
  saturated-locator, and core value matrices all have exact rank `sr(Q)`, at
  least five and exactly `e+1` when `b=0`.
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition`.
- **consumer:** `rate_half_band_closure`.
- **new open content:** classify the incidence packets that pass `(AIR5)` and
  `(AIR6)` and also satisfy the official Hankel, adjugate, component, and
  active-trace constraints.
- **nonclaim:** cycle consistency alone is not sufficient; the theorem does
  not prove irreducibility, the Hankel coefficient chain, or exclusion of an
  active system.
- **falsifier:** an official partition packet whose nonincidence graph is
  disconnected, whose actual locator labels violate a cycle identity, or
  whose actual scaled clean locators fail `(AIR6)` or the rank identity
  `(AIR8)`.
- **verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/verify.py`;
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_active_partition_incidence_reconstruction/verify_packet_checker.py`.
- **upstream mapping:** exact SPI / split-fiber incidence reconstruction and
  finite classification preprocessing.
