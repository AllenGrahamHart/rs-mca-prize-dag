# Claim contract

## Claim

For the prize-envelope `N=256` profile `(4,2,0)`, no collision has norm
`R=4p` with a prize-row prime `p`.

## Dependencies

- `e1_prize_n256_s18_m4_high_variance_exclusion` reduces every possible
  cofactor-4 collision to the nine chambers `10<=V<=74`, `V=2 mod 8`.

## Scope fences

1. The exhaustive certificate applies only to cofactor `m=4` and the exact
   prize interval.
2. It proves emptiness of collisions, not a weighted edge multiplicity.
3. Normalized vector counts must not be inserted directly into the aggregate
   pair budget.
4. The remaining leading-profile cofactor `m=2` is not addressed.
