# Claim contract

## Input

`e1_prize_n256_s18_profile_36_cofactor_windows`, specifically:

- cofactor `1538` forces `mu=1`;
- its only residual variances are `4,6,8,10,12`.

## Output

The complete `m=1538` profile-`(3,6,S=18)` class is empty on prize-envelope
rows.

## Guards

1. The support normalization uses an odd singleton difference guaranteed by
   `mu=1`; it is not available unchanged for the other cofactors.
2. Affine normalization acts only on positions. All induced coefficient-sign
   changes are restored by the 32 singleton and eight heavy sign ledgers.
3. Diameter chords are omitted because their two negacyclic correlation
   contributions cancel exactly.
4. The mod-four equation is only a candidate generator. Every retained heavy
   support is checked by exact integer autocorrelation for all signs.
5. Energy one (`V=2`) and energy zero are consumed from the parent theorem;
   the finite classifier proves exactly energies two through six empty.
6. This node removes one cofactor, not the whole `(3,6)` profile or the
   aggregate pair budget.

## Falsifier

A `mu=1` profile-`(3,6)` coefficient vector with energy in `{2,...,6}`, or a
normalization/sign class omitted from the two exact ledgers.
