# Claim contract

## Inputs

- `collision_norm_criterion` and the pair-feasible prime-field reduction;
- `e1_prize_field_floor_even_norm_exclusion`, including the exact prize
  lower endpoint;
- the local reciprocity identity proved in
  `e1_n256_local_norm_cofactor_collapse`;
- the folded square-mass and weighted-profile conventions.

## Output

Every prize-envelope profile-`(3,6,S=18)` collision lies in one of the twelve
cofactor classes and finite even-variance windows printed in `statement.md`.

## Guards

1. `(3,6)` means three coefficients of magnitude two and six of magnitude
   one; it is not the older first-band profile `(3,4,0)`.
2. The residue calculation is modulo `(X+1)^16`; paired residues are retained
   through parity, not silently treated as six distinct residues.
3. The list is necessary, not sufficient. No listed chamber is asserted to
   contain a collision.
4. The variance has only been proved even. No `V=2 mod 4` or `V=2 mod 8`
   restriction is claimed for six singleton coefficients.
5. The logarithmic windows use `L1=12` and cannot reuse the stronger
   profile-`(4,2)` denominator 2367.
6. This theorem applies to prize-envelope rows. It does not alter the RowC
   cofactor interface.

## Falsifier

A pair-feasible prize collision in this profile with a cofactor outside (1),
with `V=0` or `V=2`, or at/above its printed exclusion onset.
