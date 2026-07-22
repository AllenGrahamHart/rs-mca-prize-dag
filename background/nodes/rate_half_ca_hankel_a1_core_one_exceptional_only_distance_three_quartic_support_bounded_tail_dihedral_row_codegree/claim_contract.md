# Claim contract

- **Claim:** with `t` exceptional pairs outside one antipodal or
  constant-product involution, every nonidentical outside orbit has row
  codegree at most `t`, and there is at most one identical normalized-row
  orbit.
- **Scope:** exact pair-Lagrange packets; tails are arbitrary matched pairs.
- **Dependencies:** pair-Lagrange normal form and the pullback-only support
  routing.
- **Consumer:** `rate_half_band_closure`; first tail-stability input for the
  dihedral trace-collision proof.
- **Falsifier:** a nonidentical outside orbit with more than `t` common
  external slopes, or two distinct identical normalized-row orbits.
- **Nonclaims:** the complement trace dimension and final collision
  contradiction are not proved here.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_bounded_tail_dihedral_row_codegree/verify.py`
