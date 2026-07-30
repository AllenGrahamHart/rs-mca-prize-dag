# Source evidence

- `rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction` supplies
  `(KBDM-9)`, exact crossing degrees, reduced stars, and whole-fiber
  transport.
- `rate_half_kb_m2_v4_outer_recurrence_router` supplies the complete-source
  defect budget three and the actual source-star interpretation.
- `rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy` supplies
  individual-star equivariance only in the source-line branch.
- The packet counts are exhaustive finite combinatorics, replayed by
  multiset canonicalization and independently by multiplicity vectors plus
  Burnside averaging. They do not claim algebraic realizability.

## Upstream custody

The complete classifier is vendored into the diagonal source-facet packet in
draft PR `przchojecki/rs-mca#1132` at commit
`7f084f2dd27fea2b0a231cc690fc70bdd25e0609`:

```text
note blob:        41bfa82cae8f3804e4287bd51da6d55c3872683a
verifier blob:    10cab32a0eba904164e26322374235c17d16e1ca
certificate blob: 7fb875dba06cd2a40854bf9e4415ff4c0acf3b64
payload SHA-256:  f1b0339b6b70a9f1055ba0910a53713712348b36d1b9e94ab7fd22d14f8a502b
```

The upstream replay reproduces `1560/123` and `96/12`, checks `2700/900`
aligned/near source-line quotient rows, preserves the nonrealization and
exceptional-orbit warnings, and rejects `90` of `90` hostile mutations.
