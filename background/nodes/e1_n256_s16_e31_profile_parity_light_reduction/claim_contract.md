# Claim contract

## Claim

Every pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=62` collision has
one of the three profiles `(3,7)`, `(2,5,1)`, `(1,3,2)` and one of the eight
light-support templates printed in the statement.

## Dependencies

- `e1_n256_s16_e32_endpoint_exclusion` for the preceding variance frontier;
- `e1_n256_s16_sparse_l1_variance_exclusion` for the relaxed slack recurrence;
- `e1_n256_s16_signed_chord_collision_gate` for the signed-chord identity and
  mod-two light-chord rule;
- `collision_norm_criterion` for the cubic norm exclusion.

## Nonclaims

- no exclusion of any profile in `(1)`;
- no claim about `V<=60`, folded profile `(4,2,0)`, or later swap bands;
- no promotion of either universal E1/unsafe target.

## Falsifier

A sixteenth energy-31 profile at `L<=17`, failure of either cubic sign, a
parity-surviving profile outside `(1)`, a valid light support outside the eight
orbits, or an additional diameter ledger refutes the reduction.
