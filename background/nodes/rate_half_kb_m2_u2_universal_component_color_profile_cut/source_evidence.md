# Source evidence

- The five-profile census and notation are supplied by
  `rate_half_kb_m2_u2_universal_source_facet_census`.
- The exact component edge coloring is Corollary 9.28 of
  `experimental/notes/frontier-adjacent/kb_mca_v4_equality_wall_geometry_v1/proof/pole_disjoint_conic_facet_collinearity_reduction.md`
  in `przchojecki/rs-mca` commit
  `44542e91e459364a521870ed2ebde7f6fe5055bf`, theorem blob
  `356ff4b47d0bb429d11ea10382762a6e95b5ce24`.
- The pinned certificate
  `experimental/notes/frontier-adjacent/kb_mca_v4_equality_wall_geometry_v1/verification/pole_disjoint_conic_facet_collinearity_certificate.json`
  has blob `91643b5b9020f52764a77cfbc8aa6279ce2d5ef8` and records both
  `q6_s6_component_edge_coloring_9_28=PROVED` and the exact color
  multiplicity formula `2*u`.
- The local proof uses only the color definition, the four-edge count at
  `u=2`, and left pole-graph degree two. It does not import the sufficient
  zero-migration condition of equation (9.112).

## Upstream custody

Vendored as a direct refinement of the universal source-facet packet in
draft PR `przchojecki/rs-mca#1132` at commit
`e0ef6ca0cc64465f3b73d3f324efa9cc294eebb5`. The immutable
note/verifier/certificate blobs are
`02322ebba4847b072a5856e02d3bcfc3f0590b26`,
`10888f6d5996c04cd635939731cacecb5c170937`, and
`d2c681b33918ff1490dfa5b8388295a422b56ca7`, with canonical payload
`17b8e640ed4e8e55f81864067c50dc40db86798abbc90bd58f3472eae098b902`.
The verifier pins Corollary 9.28 and rejects 20 of 20 hostile mutations.
