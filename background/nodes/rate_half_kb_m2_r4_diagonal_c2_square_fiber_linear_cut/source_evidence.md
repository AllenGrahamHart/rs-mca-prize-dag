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
commit `ddfae529bf6e5fdee5e8b4810b9e034d617d2290`:

```text
note blob:        ba1cf54af98edae0941b40522022733eb4f32bdc
verifier blob:    f29d8b0a5db575075c802f9b99ce259313f0e151
certificate blob: c5c0a9e508514abbd721b2d6cd87f1e98ba16d05
payload SHA-256:  f0a7dc4fd1d7f099aefaac879914aad504a11fc4b9d858cbcd95cdd7b6a93dbb
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, the precise general retention of the
ramified orbit, its `(2,0,2)` defect exclusion, and the full packet against
`74` hostile mutations.
