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
`3584deccfc92aa4b1c1125b40017eabd15167079`:

```text
note blob:        20559b894d129dfe1094a0b3dac70ed1f8d595da
verifier blob:    73be19232ad839ac1be4fadc7c7d8cefd30a66f7
certificate blob: e82f08722dd2bfba564b51a25d3e7f4d6e692c67
payload SHA-256:  22e3cc5c5100d2b90e6487b6216fc8e5c0d6cd3f5eeefef90bac325643cbcd71
```

The upstream replay reproduces `1560/123` and `96/12`, preserves the
nonrealization and exceptional-orbit warnings, and rejects `83` of `83`
hostile mutations across the complete packet.
