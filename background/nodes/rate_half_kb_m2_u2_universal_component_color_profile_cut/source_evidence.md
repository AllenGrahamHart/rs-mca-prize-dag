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

Not yet vendored. It is a direct refinement of the universal source-facet
packet in draft PR `przchojecki/rs-mca#1132`.
