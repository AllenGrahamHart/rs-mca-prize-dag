# Source evidence

- `rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair`
  supplies the common `4/3` forced-square cut and pinned nonzero odd part in
  both ramification cases.
- `rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier` supplies
  the five labeled pure multisets and the one-unit collision bound.
- The evaluation injectivity, edge-scalar reconstruction, and `2,2,4,2,2`
  assignment census are proved and replayed locally.

## Upstream custody

The theorem is vendored into the diagonal source-facet packet in draft PR
`przchojecki/rs-mca#1132` at commit
`cbb3aa26cbbd34dbacd284424a16f29518d7d242`:

```text
note blob:        88a0bd2a19913fdf689968d38628ded7c7645aed
verifier blob:    e0fe717b09701c6ec66674df37456ff8a9888a0d
certificate blob: 668246f6f97196848179d38f70136eceb37a43d1
payload SHA-256:  b290c08228370fad83a8f91ae47684e6a1f53a49104b545135f526075173c472
```

The upstream replay checks both evaluation ranks, assignment counts
`2,2,2,2,4`, the maximum of eight source-deck pairs, and rejects `114` of
`114` hostile mutations.
