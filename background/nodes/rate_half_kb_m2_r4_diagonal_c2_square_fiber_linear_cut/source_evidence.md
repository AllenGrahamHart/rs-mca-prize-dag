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
commit `7f084f2dd27fea2b0a231cc690fc70bdd25e0609`:

```text
note blob:        41bfa82cae8f3804e4287bd51da6d55c3872683a
verifier blob:    10cab32a0eba904164e26322374235c17d16e1ca
certificate blob: 7fb875dba06cd2a40854bf9e4415ff4c0acf3b64
payload SHA-256:  f1b0339b6b70a9f1055ba0910a53713712348b36d1b9e94ab7fd22d14f8a502b
```

The upstream verifier checks the exact `4/3` and `6/5` dimensions, both
reciprocal-minor sign identities, the precise general retention of the
ramified orbit, its `(2,0,2)` defect exclusion, and the full packet against
`90` hostile mutations.
