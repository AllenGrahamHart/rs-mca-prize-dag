# Source evidence

- `rate_half_kb_m2_r4_source_row_interpolation_compiler` supplies exact row
  divisibility by `B/z_i` and local equality with `2 div(B)`, including
  multiple source roots.
- `rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate`
  supplies source-deck distinction, the unramified internal orbit, its
  common-root equation, and the odd-part incidence formula.
- The order allocation and rank-four repair are proved locally. No
  square-fiber-only condition on `V` is imported.

## Upstream custody

The theorem is vendored into the diagonal source-facet packet in draft PR
`przchojecki/rs-mca#1132` at commit
`b19ae81742844071adcc1b6d7344b2f13d481775`:

```text
note blob:        7d06a35d087f3422c235bc27e4d280866e16fb85
verifier blob:    97efe5ba9ccdbf74818c6d983dc52d3067087f3b
certificate blob: 6d6b96dceaed853660fa4d1c64717aa2606a32ee
payload SHA-256:  fea1c3f3f414067746329ef0ab65882c826e2f1cc34cf756433b0d549ed9fedb
```

The upstream replay checks the unique `(2,2)` order allocation, rank four,
dimensions `4/3`, exact local expansions, and rejects `106` of `106`
hostile mutations.
