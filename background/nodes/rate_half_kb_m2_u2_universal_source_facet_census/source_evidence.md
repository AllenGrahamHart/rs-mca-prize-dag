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
`de237ba4d6ffd03bddc3d3daa7e94d0dee06eedf`. The immutable note, verifier,
and certificate blob OIDs are respectively
`a1a84452ddcd2f407eefb89bea0ef6a710e9f5d2`,
`91a61152be9bb639f720554f080c01d424c5ecc8`, and
`2c8625cd0f2e51809a2696d4a69eb54fb3ec91e4`; the canonical certificate
payload is
`49131c6962e551c529d0681427ef9fee0eb10ea2bb42ffa5f46db3c63710ca8c`.
The upstream verifier pins the independent complete-source and source-facet
parents and rejects all 28 hostile mutations.
