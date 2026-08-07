# Claim contract

- **claim id:** `dli_wcl_ell2_weight7_quadruple_cubic_prime_filter_router`
- **status:** `PROVED`
- **scope:** the complete four-plus-three presentation of reduced WCL
  `(ell,w)=(2,7)` relations at order `1024`
- **consumer:** `dli_wcl_slot_2_7_emptiness`
- **proved content:** exact cleared-cubic recurrence; exclusion of `u=0` on
  official relations; embedding-aware repair of `Norm(u)` saturation; exact
  affine orbit count `94,652,815`
- **new open content:** exclude every official prime surviving the exact
  filter, or find a smaller quotient/independent obstruction
- **falsifier:** a legal relation not routed by `(QCR1)--(QCR4)`, a shared
  norm prime misclassified by `(QCR6)`, or an orbit count different from
  `(QCR8)`
- **nonclaims:** no candidate orbit, official prime, or WCL slot is excluded
- **replay:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell2_weight7_quadruple_cubic_prime_filter_router/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/dli_wcl_ell2_weight7_quadruple_cubic_prime_filter_router/verify_audit.py`
- **compute decision:** the complete route is an external no-go at current
  scale; do not launch the 94.7-million-orbit census
- **upstream mapping:** `OURS_ONLY`; Przemek's workboard has no WCL tower
  terminal
