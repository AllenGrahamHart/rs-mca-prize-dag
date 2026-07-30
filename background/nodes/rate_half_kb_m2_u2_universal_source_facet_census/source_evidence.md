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
`e0ef6ca0cc64465f3b73d3f324efa9cc294eebb5`. The immutable note, verifier,
and certificate blob OIDs are respectively
`02322ebba4847b072a5856e02d3bcfc3f0590b26`,
`10888f6d5996c04cd635939731cacecb5c170937`, and
`d2c681b33918ff1490dfa5b8388295a422b56ca7`; the canonical certificate
payload is
`17b8e640ed4e8e55f81864067c50dc40db86798abbc90bd58f3472eae098b902`.
The upstream verifier pins the independent complete-source and source-facet
parents and rejects all 20 hostile mutations.
