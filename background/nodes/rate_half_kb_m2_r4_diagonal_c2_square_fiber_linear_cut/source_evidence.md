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
commit `3584deccfc92aa4b1c1125b40017eabd15167079`:

```text
note blob:        20559b894d129dfe1094a0b3dac70ed1f8d595da
verifier blob:    73be19232ad839ac1be4fadc7c7d8cefd30a66f7
certificate blob: e82f08722dd2bfba564b51a25d3e7f4d6e692c67
payload SHA-256:  22e3cc5c5100d2b90e6487b6216fc8e5c0d6cd3f5eeefef90bac325643cbcd71
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, the precise general retention of the
ramified orbit, its `(2,0,2)` defect exclusion, and the full packet against
`83` hostile mutations.
