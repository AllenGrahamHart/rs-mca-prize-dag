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
`b19ae81742844071adcc1b6d7344b2f13d481775`:

```text
note blob:        7d06a35d087f3422c235bc27e4d280866e16fb85
verifier blob:    97efe5ba9ccdbf74818c6d983dc52d3067087f3b
certificate blob: 6d6b96dceaed853660fa4d1c64717aa2606a32ee
payload SHA-256:  fea1c3f3f414067746329ef0ab65882c826e2f1cc34cf756433b0d549ed9fedb
```

The upstream replay reproduces `1560/123` and `96/12`, checks `2700/900`
aligned/near source-line quotient rows, preserves the nonrealization and
exceptional-orbit warnings, checks the internal odd-part gate and ramified
coefficient repair, and rejects `106` of `106` hostile mutations.
