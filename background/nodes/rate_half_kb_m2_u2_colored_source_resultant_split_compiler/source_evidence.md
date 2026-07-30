# Source evidence

- `rate_half_kb_m2_r4_source_row_interpolation_compiler` supplies the
  stabilizer-independent source equation, resultant product formula, and
  complete-source square identity.
- `rate_half_kb_m2_u2_universal_component_color_profile_cut` supplies the
  four-edge component color class and its exact correspondence with the
  outside-`K` `J` incidences.
- Corollaries 9.27 and 9.28 of the pinned equality-wall source theorem at
  `przchojecki/rs-mca` commit
  `44542e91e459364a521870ed2ebde7f6fe5055bf` prove that the twelve `L^c`
  edge roots are simple and free under the source deck involution. The
  theorem and certificate blobs are
  `356ff4b47d0bb429d11ea10382762a6e95b5ce24` and
  `91643b5b9020f52764a77cfbc8aa6279ce2d5ef8`.
- The partial resultant split is proved locally by exact divisor addition;
  no finite-field experiment or genericity assumption is used.

## Upstream custody

Vendored in the universal source-interface packet in draft PR
`przchojecki/rs-mca#1132` at commit
`3000bb6bb384302ad72d960ac60ebc7b440dd8ab`. The immutable
note/verifier/certificate blobs are
`04015b26fee58fdc16c093adbc91dd3053b77ae6`,
`d053e14f13736b3d970acee3858253a1382b8732`, and
`ab5eaf2e4ef44a58005554344187f550f92b5d41`, with canonical payload
`677782fc5ad5f028595f4b71b3383252bc104fd8cbf569c58ade300383421461`.
The verifier replays all 495 four-root divisors and rejects 24 of 24 hostile
mutations.
