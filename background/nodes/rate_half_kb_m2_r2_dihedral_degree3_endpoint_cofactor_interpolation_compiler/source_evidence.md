# Source evidence

- Endpoint source identity and `Q=6,s=6` locator semantics:
  `przchojecki/rs-mca` source commit
  `44542e91e459364a521870ed2ebde7f6fe5055bf`, file
  `pole_disjoint_conic_facet_collinearity_reduction.md`.
- Parent geometric model: local PROVED node
  `rate_half_kb_m2_r2_dihedral_degree3_geometric_realization_fence`, audited
  upstream theorem commit `fce150e3323ce37f261b21c19685f4613552dd42`.
- New interpolation proof and split-field deleting fixture are reconstructed
  locally.
- Outbound custody: draft PR `https://github.com/przchojecki/rs-mca/pull/1132`,
  theorem commit `3d55c601bad0ea2a405e0b34eea14497b032c6a5`.
- Upstream note blob: `a1dd8323b23d7dfc69c55aa8032c5dd2599eae4f`.
- Upstream verifier blob: `6c3f41a1d08f79423fdfad8f152ee8bf54e7ad5b`.
- Upstream certificate blob: `e5481c811b76c258aa05a8b6833b8715341cae17`.
- Canonical certificate payload SHA-256:
  `bf5cfd6b06a9dcfa56601023ed497cdba1f7a37bc3fa47f4cff4855b6fa86a66`.
- The fail-closed upstream replay binds the exact geometric parent and
  rejects 24 of 24 hostile mutations.

The upstream PR remains provisional until review. Local `PROVED` rests on
the in-tree proof and independent replay, not on merge status.
