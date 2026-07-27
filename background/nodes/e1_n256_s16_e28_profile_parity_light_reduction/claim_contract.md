# Claim contract

## Claim

Every pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=56` collision has
one of the eight profiles in (1) and light geometry in the exact 154-orbit
router printed in the statement.

## Dependencies

- `e1_n256_s16_e29_endpoint_exclusion` for the preceding variance frontier;
- `e1_n256_s16_sparse_l1_variance_exclusion` for the relaxed slack recurrence;
- `e1_n256_s16_signed_chord_collision_gate` for the signed-chord identity and
  mod-two light-chord rule;
- `e1_n256_s16_e32_profile_parity_diameter_reduction` for the complete
  four-odd light atlas;
- `collision_norm_criterion` for the cubic norm exclusion.

## Nonclaims

- no exclusion of any profile in (1);
- no claim about `V<=54`, folded profile `(4,2,0)`, or later swap bands;
- no promotion of either universal E1/unsafe target.

## Falsifier

A fifteenth energy-28 profile at `L<=16`, failure of either cubic sign, a
parity-surviving profile outside (1), a missing antipodal-pair or four-odd
orbit, or another diameter ledger refutes the reduction.
