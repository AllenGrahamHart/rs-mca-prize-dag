# Source evidence

- The exact `K`, `eta`, and one-exchange horizontal facets are
  `rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`, importing
  Corollaries 9.25 and 9.27 of the pinned source theorem.
- Nonzero quartic rows and complete-source divisor multiplicity are pinned
  by `rate_half_kb_m2_r4_source_row_interpolation_compiler` and its source
  reduction.
- The category and integer-profile enumerations are proved locally and
  replayed by two independent exact verifiers.

## Upstream custody

Vendored to draft PR `przchojecki/rs-mca#1132` at commit
`3000bb6bb384302ad72d960ac60ebc7b440dd8ab`. The immutable note, verifier,
and certificate blob OIDs are respectively
`04015b26fee58fdc16c093adbc91dd3053b77ae6`,
`d053e14f13736b3d970acee3858253a1382b8732`, and
`ab5eaf2e4ef44a58005554344187f550f92b5d41`; the canonical certificate
payload is
`677782fc5ad5f028595f4b71b3383252bc104fd8cbf569c58ade300383421461`.
The upstream verifier pins the independent complete-source and source-facet
parents and rejects all 24 hostile mutations.
