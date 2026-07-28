# Claim contract

## Claim

Every pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=50` collision lies
in one of the nine printed profiles over one of 111 proved affine light
templates.

## Dependencies

- `e1_n256_s16_e26_endpoint_exclusion` for the preceding variance frontier;
- `e1_n256_s16_sparse_l1_variance_exclusion` for the exact slack DP;
- `e1_n256_s16_signed_chord_collision_gate` for the diameter identity;
- `e1_n256_s16_e27_profile_parity_light_reduction` for the complete
  one-diameter light atlas;
- `collision_norm_criterion` for the exact cubic-Hermite boundary.

## Output supplied

An exhaustive 111-template router for the `V=50` chamber.

## Scope exclusions

- no profile is excluded by this node;
- no claim at `V<=48`;
- no claim about folded profile `(4,2,0)` or later bands.

## Falsifier

A compatible profile omitted from the 12-profile ledger, an incorrect
`M_3=13/14` sign, a surviving support outside the pinned atlas, or a
pair-feasible `V=50` vector outside the nine printed profiles refutes the
claim.
