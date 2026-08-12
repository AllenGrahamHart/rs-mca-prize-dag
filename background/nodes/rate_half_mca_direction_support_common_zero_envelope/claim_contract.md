# Claim contract

- **claim id:** `rate_half_mca_direction_support_common_zero_envelope`
- **status:** `PROVED`
- **input:** the direction-support affine-basis hypotheses, rank `r`,
  support `1<=e<=R`, and shortened dimension `r<=K<=R`
- **output:** exact envelope `(CZ1)` and exhaustive official uniform
  rank/support walls with adjacent failures
- **nonclaims:** no universal endpoint-maximizer theorem, forced residual
  structure, bankable row atom, or prize closure
- **replay:** `tools/ramguard local -- python3 background/nodes/rate_half_mca_direction_support_common_zero_envelope/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_direction_support_common_zero_envelope/verify_audit.py`
