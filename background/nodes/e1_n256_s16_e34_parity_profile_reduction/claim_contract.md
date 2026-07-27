# Claim contract

## Claim

At `N=256`, folded coefficient profile `(3,4,0)`, and `V=68`, every
pair-feasible collision has autocorrelation profile `(6,7)`. Its six
unit-product chords occupy distinct non-diameter distance classes, and its
diameter/signed-cross-sum pair lies in the six-value ledger printed in the
statement.

## Dependencies

- `e1_n256_s16_e34_three_profile_reduction` for the three candidate profiles;
- `e1_n256_s16_signed_chord_collision_gate` for the chord model and
  `34=102-D_64+2C`.

## Nonclaims

- no exclusion of `(6,7)`;
- no realizability claim for every displayed diameter value;
- no classification of the remaining equal-chord templates;
- no unsafe-line payload.

## Falsifier

A pair-feasible `V=68` vector in either discarded profile, a unit chord at
diameter, two unit chords with the same unoriented distance, or a diameter
square mass outside the displayed set refutes the claim.
