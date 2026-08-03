# Audit

## Independent reconstruction

On the exact joint error support, the `r'+1` moment equations have an
`(r'+1) x r'` Vandermonde matrix, so every syzygy relation vanishes
pointwise. At a point outside the common forced set, the syzygies vanishing
in both components form a proper subspace of `K_d`. The union of the at
most `n-|G_d|` such subspaces has size below `q^dim(K_d)` when `q>n`,
which supplies one exact-root syzygy.

For a pair in `N_d^out`, choose a selected off-core point outside `G_d`.
Its projective slope lies in the rational image of `H\G_d`, of size at most
`n-|G_d|`. Two pairs assigned the same slope are subordinate to the same
globally first-match ray. Since `2d>=h`, the interaction strip excludes two
distinct generic pairs on that ray. This proves injectivity.

For a pair in `N_d^G`, two selected slopes supply two disjoint off-core
blocks of size `h-d`, both inside `G_d`. Their disjointness follows by
inverting the two scalar error equations. Hence `|G_d|>=2(h-d)`.

## Boundary checks

- The rational direction is projective, so the `(0:1)` slope is included.
- The image bound is `n-|G_d|`, not the weaker `n`.
- Exact-`A` selection makes each off-core block have exactly `h-d` points.
- The payment counts pairs/locators, not slopes with multiplicity.
- The full-rank and deficient-rank budgets remain alternative; only the
  disjoint outside/local partition inside deficient rank is summed.

## Residual risk

The theorem does not control a pair whose complete selected off-core
geometry lies in `G_d`. That precise family is the remaining
`xr_band_forced_commonroot_syzygy_count` target.
