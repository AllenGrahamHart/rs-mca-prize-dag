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
`2b7fa7d31fac73f3b7bd2aa9dd5f55c5e3844c22`:

```text
note blob:        a1e14d6652687af8eb42b23f3c13feb1c510002e
verifier blob:    56e1d5fbc0fb30c8024c3689128c90fd1e190c65
certificate blob: fd9b4372e4a467b17d54f662169e9d75970206d0
payload SHA-256:  50d33764080e90fce4c75f74836f51897fbc5d1f2f20cbca2e65b659ef582468
```

The upstream replay reproduces `1560/123` and `96/12`, checks `2700/900`
aligned/near source-line quotient rows, preserves the nonrealization and
exceptional-orbit warnings, checks the internal odd-part gate, and rejects
`98` of `98` hostile mutations.
