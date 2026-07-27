# Claim contract

## Claim

Every pair-feasible `N=256`, folded-profile `(3,4,0)`, `V=60` collision has
one of the eight profiles in (1), no light diameter, and light geometry in the
exact two-odd or six-odd ledger printed in the statement.

## Dependencies

- `e1_n256_s16_e31_endpoint_exclusion` for the preceding variance frontier;
- `e1_n256_s16_sparse_l1_variance_exclusion` for the relaxed slack recurrence;
- `e1_n256_s16_signed_chord_collision_gate` for the signed-chord identity and
  mod-two light-chord rule;
- `collision_norm_criterion` for the cubic norm exclusion.

## Nonclaims

- no exclusion of any profile in (1);
- no claim about `V<=58`, folded profile `(4,2,0)`, or later swap bands;
- no promotion of either universal E1/unsafe target.

## Falsifier

A nineteenth energy-30 profile at `L<=18`, failure of either cubic sign, a
parity-surviving profile outside (1), a valid two-odd light support outside the
87 orbits, a different support count, or an additional diameter ledger refutes
the reduction.
