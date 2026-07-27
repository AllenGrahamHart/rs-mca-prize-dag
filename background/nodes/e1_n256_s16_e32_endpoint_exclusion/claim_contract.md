# Claim contract

## Claim

No pair-feasible folded-profile `(3,4,0)` collision at `N=256` has `V=64`;
the remaining positive even variance range is `0<V<=62`.

## Dependencies

- `e1_n256_s16_e32_profile_parity_diameter_reduction`;
- `e1_n256_s16_e32_profile_08_light_template_exclusion`;
- `e1_n256_s16_e32_profile_351_light_template_exclusion`;
- `e1_n256_s16_e32_profile_47_exact_norm_exclusion`.

## Nonclaims

- no exclusion of `V<=62`;
- no exclusion of folded profile `(4,2,0)`;
- no exclusion of later `N=256` or `N=512` swap bands;
- no promotion of either universal E1/unsafe target.

## Falsifier

A fourth surviving profile in the parent reduction, a pair-feasible vector in
any of the three excluded profiles, or a missing requirement edge refutes the
endpoint synthesis.
