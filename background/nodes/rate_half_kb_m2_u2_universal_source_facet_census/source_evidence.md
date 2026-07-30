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
`788012a0daaf32e8eec0186a599c0ced42d28749`. The immutable note, verifier,
and certificate blob OIDs are respectively
`e9420deaeaa1ec9fbf30094af13ad5a8d72cf45e`,
`0dff47b2b24eb25ccc5e252ce704c9315633b0d5`, and
`602744282e3b009c615ce89b497f31f79804228c`; the canonical certificate
payload is
`a72b8699c4eccc7b5428c78ca539733eec6ac2055dbfa73c8b7d508bba7ed3bf`.
The upstream verifier pins the independent complete-source parent and
rejects all 16 hostile mutations.
