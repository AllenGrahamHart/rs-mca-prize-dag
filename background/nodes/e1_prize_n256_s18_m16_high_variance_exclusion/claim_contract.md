# Claim contract

## Claim

For the prize-envelope `N=256` profile `(4,2,0)`, a collision with local-norm
cofactor `m=16` cannot have variance `V>=114`. Combined with the parent
congruence and window, the residual is `10<=V<=106`, `V=2 mod 8`.

## Dependencies

- `e1_prize_n256_s18_variance_cofactor_windows` supplies the exact profile,
  norm equation, variance congruence, field floor, and initial `m=16` window.

## Scope fences

1. This theorem excludes only the `m=16` high-variance chambers.
2. It does not exclude any variance from `10` through `106`.
3. It does not count vectors, edges, or prime collisions in the residual.
4. The counts-only Modal census in the parent notes is route-planning
   evidence, not a premise of this proof.
5. No claim is made for cofactors `m=2` or `m=4`.
