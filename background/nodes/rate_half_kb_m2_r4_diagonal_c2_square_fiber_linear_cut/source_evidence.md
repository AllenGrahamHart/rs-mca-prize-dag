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
commit `b19ae81742844071adcc1b6d7344b2f13d481775`:

```text
note blob:        7d06a35d087f3422c235bc27e4d280866e16fb85
verifier blob:    97efe5ba9ccdbf74818c6d983dc52d3067087f3b
certificate blob: 6d6b96dceaed853660fa4d1c64717aa2606a32ee
payload SHA-256:  fea1c3f3f414067746329ef0ab65882c826e2f1cc34cf756433b0d549ed9fedb
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, the precise general retention of the
ramified orbit, its `(2,0,2)` defect exclusion, and the full packet against
`106` hostile mutations.
