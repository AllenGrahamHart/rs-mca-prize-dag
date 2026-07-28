# Claim contract

## Imported facts

From `e1_prize_n256_s18_profile_36_sharp_product_window`:

- cofactor `1028` forces singleton multiplicity `mu=2`;
- its only residual energies are `{2,3,4,5,6}`.

## New theorem

The complete normalized low-energy geometry contains 16 vectors, all at
energy five. None has cyclotomic norm divisible by 257. Since
`1028=4*257`, the cofactor-1028 collision class is empty.

## Exclusions

1. The low-energy geometry is not empty; this node relies essentially on the
   factor-257 test.
2. Affine normalization is used only surjectively and no free-action quotient
   is assumed.
3. The finite-field test proves divisibility failure, not an exact norm or
   prize-interval comparison.
4. This removes one cofactor, not the full profile or aggregate pair budget.
