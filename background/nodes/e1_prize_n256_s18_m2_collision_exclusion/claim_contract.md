# Claim contract

## Claim

For the prize-envelope `N=256` profile `(4,2,0)`, no collision has norm
`R=2p` with a prize-row prime `p`.

## Dependencies

- `e1_prize_n256_s18_m2_high_variance_exclusion` reduces every possible
  cofactor-2 collision to the twelve chambers `10<=V<=98`, `V=2 mod 8`.

## Scope fences

1. The exhaustive certificate applies only to cofactor `m=2` and the exact
   prize interval.
2. Together with proved sibling nodes it excludes every prize cofactor of the
   profile `(4,2,0)`, but it does not exclude later square-mass profiles.
3. Normalized vector counts are not weighted class-pair counts.
4. The aggregate E1 pair budget and unsafe-family target remain open.
