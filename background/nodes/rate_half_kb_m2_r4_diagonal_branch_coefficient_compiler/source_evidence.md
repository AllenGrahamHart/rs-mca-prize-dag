# Source evidence

- The exhaustive lifting/non-lifting split and geometric normal form are
  `rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy`.
- The endpoint pullback factorization by the source component and its deck
  conjugate is
  `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`.
- The even-odd norm identities and quartic-resolvent equivalence are proved
  locally and replayed by two small exact verifiers. No remote computation
  or unproved classification is imported.

## Upstream custody

Vendored with the source-subfield dichotomy and source-row gate in draft PR
`przchojecki/rs-mca#1132` at
`6127f7c4c315428507ad05ba814c0b540edc7ac7`:

```text
note blob:        a58381fe3d80f9a604197b7c5eea3c6ef6bc4b5c
verifier blob:    b88c1ab56ee8a4a5a0a091f563697417c75ef51d
certificate blob: 3b0f45160567a4b5d1aef6ee9d8e556782b5a043
payload SHA-256:  bbdab9cb571c6c6bfcdd477598aa38f4f69b43e0c3480da28b74a725faab8e33
```

The fail-closed verifier rejects 15 of 15 hostile mutations. The sole PR
check failure at this pin is unrelated Vercel deployment authorization.
