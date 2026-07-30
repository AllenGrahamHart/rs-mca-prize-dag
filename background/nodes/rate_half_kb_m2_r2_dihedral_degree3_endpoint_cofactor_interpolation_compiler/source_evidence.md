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
  theorem commit `2f11adb0d7971dd1b9f386b92d3520d0f344d409`.
- Upstream note blob: `56cff6f1891949ea690272a6bcfb6ba481eb4014`.
- Upstream verifier blob: `7b778dd1c2f9fa7a31405040fda7c34f1ee3162f`.
- Upstream certificate blob: `0cae10be98fa6fb30aff01a3d82c97d3d14f7c90`.
- Canonical certificate payload SHA-256:
  `c3d18d3bd47908726021a4b05964b45610ebe454355629494b4fdfcc356c63fc`.
- The fail-closed upstream replay binds the exact geometric parent and
  rejects 24 of 24 hostile mutations.

The fail-closed upstream replay now also reconstructs the six canonical
square holonomies and rejects 26 of 26 hostile mutations. The upstream PR
remains provisional until review. Local `PROVED` rests on the in-tree proof
and independent replay, not on merge status.
