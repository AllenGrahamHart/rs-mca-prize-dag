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
`3000bb6bb384302ad72d960ac60ebc7b440dd8ab`. The immutable
note/verifier/certificate blobs are
`04015b26fee58fdc16c093adbc91dd3053b77ae6`,
`d053e14f13736b3d970acee3858253a1382b8732`, and
`ab5eaf2e4ef44a58005554344187f550f92b5d41`, with canonical payload
`677782fc5ad5f028595f4b71b3383252bc104fd8cbf569c58ade300383421461`.
The verifier pins Corollary 9.28 and rejects 24 of 24 hostile mutations.
