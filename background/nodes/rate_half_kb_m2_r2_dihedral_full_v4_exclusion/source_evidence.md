# Source evidence

The synthesis consumes only in-tree proved nodes:

- `rate_half_kb_m2_r2_dihedral_outer_factor_reduction`;
- `rate_half_kb_m2_r2_dihedral_degree2_source_star_exclusion`;
- `rate_half_kb_m2_r2_dihedral_degree3_source_facet_exclusion`;
- `rate_half_kb_m2_r2_dihedral_degree5_source_star_exclusion`;
- `rate_half_kb_m2_r2_dihedral_degree6_common_pole_exclusion`.

Each dependency carries its own proof, source pins, and independent
verification. This node adds only the exhaustive four-case elimination.

The aggregate synthesis is also vendored in `przchojecki/rs-mca` draft
PR `#1132` at commit
`2b0acfe0cc382fd5b399960b435887c6b20e3f82`. Its theorem, verifier, and
certificate blobs are respectively
`5993ce183caa18e804245c5abfeb6ffdaf8a06fe`,
`e3dcb5644b9e60fc71eafdaaa7f831241adf1e3b`, and
`75fce13ee5cee43dc2d74565505641adf114f6f2`, with canonical payload
`f48a46f22bc15098f5fc566e6f009d76afa4751c4fd4b4b8edaf481e619c5a01`.
Upstream status remains draft/open; no merge or K3 close is inferred.
