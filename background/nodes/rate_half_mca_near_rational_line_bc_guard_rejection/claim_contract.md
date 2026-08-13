# Claim contract

- **claim id:** `rate_half_mca_near_rational_line_bc_guard_rejection`
- **status:** `PROVED`
- **input:** the displayed deployed counterexample in upstream `#1160` and
  the necessary minimum-degree guard in the cycle-19 candidate BC contract
- **output:** all `67472` displayed bad slopes fail that guard
- **unit:** distinct finite base-field slopes on one actual received line
- **falsifier:** a failed support-locator identity or a BC contract without
  the pinned lower guard
- **nonclaims:** no frozen-owner equivalence, SEM-QBC closure, endpoint
  realization, selector theorem, slope payment, or row closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_near_rational_line_bc_guard_rejection/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_near_rational_line_bc_guard_rejection/verify_audit.py`
- **upstream mapping:** mandatory `#1160` regression proposed in the
  route-comparison dossier; appropriate for the `#1159/#1163` SEM-QBC line
