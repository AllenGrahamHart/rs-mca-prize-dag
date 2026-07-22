# Claim contract

- **Claim:** every non-MDS annihilating pair satisfies the support residue
  equation `(HNR2)`, equivalently the top-remainder gate `(HNR3)` and the
  exceptional-side boundary identity `(HNR4)--(HNR5)`; deficiency `d`
  supplies the full `d`-by-`d` family `(HNR6)`.
- **Scope:** both exact-half and excess-zero non-MDS gcd profiles.
- **Dependencies:** the annihilator router, full Hankel coefficient isotropy,
  and the Forney support-weight formula.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a valid non-MDS endpoint packet violating any of
  `(HNR2)--(HNR5)`.
- **Nonclaims:** one scalar equation alone is not asserted to exclude either
  official endpoint profile.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_support_residue_gate/verify.py`
