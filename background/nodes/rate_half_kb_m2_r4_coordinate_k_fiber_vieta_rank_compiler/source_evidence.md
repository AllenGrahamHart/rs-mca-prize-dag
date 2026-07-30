# Source evidence

- `rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler`
  supplies the coordinate normalization, preserving source lift, five
  `J-J` stars over `K`, and the two 8/7-dimensional source forms.
- The edge coordinates and all matrix rows are derived locally by Vieta
  coefficient comparison. No interpolation genericity, endpoint search,
  or computation is used in the proof.
- The direct verifier checks both matrix systems over a finite field. The
  independent audit replays the rank identities over the rationals and
  checks deck-choice invariance separately.

## Upstream custody

Vendored as the coordinate five-fiber extension of the universal source-
interface packet in draft PR `przchojecki/rs-mca#1132` at commit
`780520c4399815451f30a28ec22bdff075629242`. The immutable
note/verifier/certificate blobs are
`f86109bbabbe1a0448e91178492651d4081d2397`,
`0a2405f848b6d032de3f77e81882ee7f04a38e0a`, and
`be6e9aaef8a3f215e61fc5f3719b50dc584fdb0f`, with canonical payload
`ba77d21b4da577dcb4eafc375d36e4df18644c6c284cf0e53a3350c4011d8a85`.
The verifier checks both parity ranks, both positive ramified fibers, and
rejects 34 of 34 hostile mutations.
