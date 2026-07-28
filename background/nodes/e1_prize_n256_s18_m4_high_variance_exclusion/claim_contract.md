# Claim contract

## Claim

For the prize-envelope `N=256` profile `(4,2,0)`, a collision with local-norm
cofactor `m=4` cannot have variance `V>=82`. Combined with the parent
congruence and window, the residual is `10<=V<=74`, `V=2 mod 8`.

## Dependencies

- `e1_prize_n256_s18_variance_cofactor_windows` supplies the exact profile,
  norm equation, variance congruence, field floor, and initial `m=4` window.

## Scope fences

1. This theorem excludes only the `m=4` high-variance chambers.
2. It does not exclude any variance from `10` through `74`.
3. The exact third-moment frontiers are load-bearing; the separate counts-only
   census is corroborating route evidence.
4. The normalized-vector counts are not weighted class-pair counts.
5. No claim is made for the remaining cofactor `m=2`.
