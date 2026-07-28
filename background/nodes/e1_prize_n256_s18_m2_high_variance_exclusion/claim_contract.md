# Claim contract

## Claim

For the prize-envelope `N=256` profile `(4,2,0)`, a collision with local-norm
cofactor `m=2` cannot have variance `V>=106`. Combined with the parent
congruence and window, the residual is `10<=V<=98`, `V=2 mod 8`.

## Dependencies

- `e1_prize_n256_s18_variance_cofactor_windows` supplies the exact profile,
  norm equation, variance congruence, field floor, and initial `m=2` window.

## Scope fences

1. This theorem excludes only the `m=2` high-variance chambers.
2. It does not exclude any variance from `10` through `98`.
3. The exact third-moment frontiers are load-bearing through `V=194`.
4. The normalized-vector counts are not weighted class-pair counts.
5. No aggregate E1 pair-budget claim is made.
