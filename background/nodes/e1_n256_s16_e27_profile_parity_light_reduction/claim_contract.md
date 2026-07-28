# Claim contract

## Claim

Every pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=54` collision has
one of the six profiles in (1), exactly one light-light diameter, and light
geometry in the exact eight-orbit router printed in the statement.

## Dependencies

- `e1_n256_s16_e28_endpoint_exclusion` for the preceding variance frontier;
- `e1_n256_s16_sparse_l1_variance_exclusion` for the relaxed slack recurrence;
- `e1_n256_s16_signed_chord_collision_gate` for the signed-chord identity and
  mod-two light-chord rule;
- `collision_norm_criterion` for the cubic norm exclusion.

## Nonclaims

- no exclusion of any profile in (1);
- no claim about `V<=52`, folded profile `(4,2,0)`, or later swap bands;
- no promotion of either universal E1/unsafe target.

## Falsifier

A thirteenth energy-27 profile at `L<=15`, failure of either cubic sign, a
parity-surviving profile outside (1), a one-diameter light support outside the
printed 119-orbit atlas, an incorrect orbit count, or another diameter ledger
refutes the reduction.
