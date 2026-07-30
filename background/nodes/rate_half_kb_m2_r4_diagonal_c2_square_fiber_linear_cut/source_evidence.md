# Source evidence

- `rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler` supplies the
  exact norm form, reciprocal coefficient relations, and dimensions `8/7`.
- `rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction` supplies the
  square fiber and identifies its reduced quadratic root locator as
  `P_(J_1)`.
- The distinction between two source points and one ramified point is
  retained from the fiber-resultant interface. No unramifiedness assumption
  is imported.
- The rank and reciprocal-minor calculations are proved locally and replayed
  with exact rational arithmetic.

## Upstream custody

The complete theorem and ramification warning are vendored into the diagonal
shift-pair/source-facet packet in draft PR `przchojecki/rs-mca#1132` at
commit `2b7fa7d31fac73f3b7bd2aa9dd5f55c5e3844c22`:

```text
note blob:        a1e14d6652687af8eb42b23f3c13feb1c510002e
verifier blob:    56e1d5fbc0fb30c8024c3689128c90fd1e190c65
certificate blob: fd9b4372e4a467b17d54f662169e9d75970206d0
payload SHA-256:  50d33764080e90fce4c75f74836f51897fbc5d1f2f20cbca2e65b659ef582468
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, the precise general retention of the
ramified orbit, its `(2,0,2)` defect exclusion, and the full packet against
`98` hostile mutations.
