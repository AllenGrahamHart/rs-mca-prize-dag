# Claim contract

## Inputs

- `e1_n256_s16_sparse_l1_variance_exclusion`, including `E=38`, `L<=22`,
  the magnitude-profile enumeration, and the rational cubic certificate;
- `e1_n256_s16_autocorrelation_subfield_exclusion`, excluding support in
  `4 Z/128 Z` at `V=76`;
- `collision_norm_criterion`, including nonzero norm and the official
  row-prime lower endpoint.

## Output

No pair-feasible profile-`(3,4,0)` collision has `V=76`; the remaining
positive even variance satisfies `V<=74`.

## Guards

1. The quotient census bounds the absolute layered Schur count, which is an
   upper bound for the signed third central moment.
2. The residue bound uses symmetry, zero exclusion, and nesting. Dropping any
   of these hypotheses invalidates the exact subtraction in the pair ledger.
3. Division by two is used only when the complete outer autocorrelation
   support lies in `2 Z/128 Z`.
4. The `4 Z/128 Z` chamber is discharged by the separate proved subfield
   node, not by extrapolating the quotient census.
5. This node excludes exactly `V=76`; it does not claim that `V<=74` is empty.

## Falsifier

A pair-feasible profile-`(3,4,0)` collision at `V=76`, or an admissible
quotient allocation exceeding its certified maximum.
