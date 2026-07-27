# Claim contract

## Claim

The complete folded-profile `(3,4,0)`, `V=68` endpoint is excluded. The live
positive even variance frontier is at most 66.

## Dependencies

- `e1_n256_s16_e34_three_profile_reduction`;
- `e1_n256_s16_e34_parity_profile_reduction`;
- `e1_n256_s16_e34_heavy_chord_template_reduction`;
- the quarter, nonquarter-diameter, progression, and generic template
  exclusions.

## Nonclaims

- no exclusion of `V<=66`;
- no closure of the complete `(3,4,0)` profile;
- no result for `(4,2,0)` beyond its existing reductions;
- no promotion of the universal unsafe target.

## Falsifier

A pair-feasible `V=68` vector outside the three profiles, outside the four
templates, or surviving one of the four exact exclusion packets refutes the
claim.
