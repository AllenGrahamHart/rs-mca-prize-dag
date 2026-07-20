# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality`
- **mathematical statement:** the exceptional middle-Hankel kernel is exactly
  the two coefficient shifts of `Q(gamma_0)`, and the local pencil lifts the
  second line transversely while continuing the generic-kernel line
- **scope:** only the official `b=0,D_*=1,c=z=1` corrected square
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependencies:** exceptional-root charge and exceptional Hankel
  factor pin
- **new open content:** combine the compact exceptional gate with the full
  reciprocal reconstruction, lower Hankel chain, and split fibers
- **falsifier:** a valid packet whose exceptional kernel is not `(KPT3)`,
  whose lift equation fails, or whose crossing pairing `v^TM_1v` vanishes
- **nonclaims:** no lower-coefficient classification, no converse from the
  three pairings, no reciprocal or splitting reconstruction, no profile
  exclusion, and no promotion of `rate_half_band_closure`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality/verify.py`
- **upstream mapping:** base-field-normalized exact SPI exceptional kernel
  plane and crossing ledger
