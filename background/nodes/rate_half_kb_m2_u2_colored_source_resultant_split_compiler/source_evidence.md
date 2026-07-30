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
`de237ba4d6ffd03bddc3d3daa7e94d0dee06eedf`. The immutable
note/verifier/certificate blobs are
`a1a84452ddcd2f407eefb89bea0ef6a710e9f5d2`,
`91a61152be9bb639f720554f080c01d424c5ecc8`, and
`2c8625cd0f2e51809a2696d4a69eb54fb3ec91e4`, with canonical payload
`49131c6962e551c529d0681427ef9fee0eb10ea2bb42ffa5f46db3c63710ca8c`.
The verifier replays all 495 four-root divisors and rejects 28 of 28 hostile
mutations.
