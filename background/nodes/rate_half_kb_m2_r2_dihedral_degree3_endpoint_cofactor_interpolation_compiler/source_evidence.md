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
  theorem commit `a20c117f02b920fd306affac43c078e127953f5b`.
- Upstream note blob: `5da9cd9140d004078e80d1d4a0a64268413f551f`.
- Upstream verifier blob: `fe916a625502b02b50e386224aabe151fee7eb32`.
- Upstream certificate blob: `6503c0f322a22e4c921f260fe3eb3ca3794fa806`.
- Canonical certificate payload SHA-256:
  `2c3ee72d90e410378ab64b8c329ef30568d34889917919cb9a401f45959f454a`.
- The fail-closed upstream replay binds the exact geometric parent and
  rejects 24 of 24 hostile mutations.

The fail-closed upstream replay now also binds the exact complete
gain-flatness criterion, reconstructs the six canonical square holonomies,
and rejects 27 of 27 hostile mutations. The upstream PR remains provisional
until review. Local `PROVED` rests on the in-tree proof and independent
replay, not on merge status.
