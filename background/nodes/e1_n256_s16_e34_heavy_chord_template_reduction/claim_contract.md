# Claim contract

## Claim

Every pair-feasible `(3,4,0)`, `V=68` collision lies in one of four exact
heavy-position templates: quarter, nonquarter diameter, progression, or
generic. Singleton non-diameter heavy-heavy classes contain heavy-light
chords. The quarter template has no heavy-light diameter and has opposite
outer heavy signs.

## Dependencies

- `e1_n256_s16_e34_parity_profile_reduction` for profile `(6,7)` and the
  light-Sidon property;
- `e1_n256_s16_signed_chord_collision_gate` for the signed distance classes.

## Nonclaims

- no exclusion of any template;
- no assertion that every template is realizable;
- no bound on the 41 heavy-light collision signatures;
- no collision-norm or unsafe-line conclusion.

## Falsifier

A residual vector whose heavy positions fit none of the four templates, a
singleton non-diameter heavy-heavy class without a heavy-light chord, or a
quarter-template vector with a light at the missing quarter or equal outer
heavy signs refutes the claim.
