# Claim contract

- **claim id:** `rate_half_mca_direction_support_affine_basis_payment`
- **status:** `PROVED`
- **input:** a minimum-lift codeword direction gauge with `1<=e<=R`, exact
  pair-noncontained witnesses, and transformed explanation affine rank at
  most `r`
- **output:** support-sensitive incidence bound `(AB1)` and exact uniform
  rank/support walls for all shortened dimensions `r<=K<=R`
- **nonclaims:** no forced rank/support condition, first-match owner,
  bankable row atom, or prize closure
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_direction_support_affine_basis_payment/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_direction_support_affine_basis_payment/verify_audit.py`
