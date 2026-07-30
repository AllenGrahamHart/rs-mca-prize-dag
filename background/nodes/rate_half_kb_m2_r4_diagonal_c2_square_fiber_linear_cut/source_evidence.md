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
commit `5b8a8dfe12af2236fe28665ff6fc66f54322a4a7`:

```text
note blob:        d69e5c6673a5bff7f181e84dcc10c56a9e1dc71a
verifier blob:    16dcab7f81e033b4f0a40b947ccdd3edc3cfc049
certificate blob: 96c0fd785bec2f761336893db251a349ee2b4e74
payload SHA-256:  ca878fb3aa4e41ab5b7184413decdb50522716fd70267ddd529dc37d57d9bce6
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, the precise general retention of the
ramified orbit, its `(2,0,2)` defect exclusion, and the full packet against
`69` hostile mutations.
