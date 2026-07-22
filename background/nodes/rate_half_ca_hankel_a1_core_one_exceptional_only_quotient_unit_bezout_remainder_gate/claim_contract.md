# Claim contract

- **Claim:** each triangular unit stage is one Euclidean division by
  `f_0`; its remainder is affine exactly when the stage survives.
- **Scope:** both sharp high quotient-distance endpoint profiles on the
  official exceptional-only face.
- **Dependencies:** triangular affine reconstruction and the exact reciprocal
  Bezout identity.
- **Consumer:** the high-distance branch of `rate_half_band_closure`.
- **Falsifier:** a stage satisfying the unit equation but not `(QBR3)`, or an
  affine correction paired with a remainder of degree at least two.
- **Nonclaims:** no endpoint profile is excluded merely because this gate is
  available; the actual deterministic remainder sequence is not evaluated.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_bezout_remainder_gate/verify.py`
