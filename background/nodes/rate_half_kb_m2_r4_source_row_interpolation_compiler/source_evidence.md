# Source evidence

- The actual bidegree-`(2,4)` source component and twelve distinct labels
  are pinned by `rate_half_kb_m2_v4_outer_recurrence_router` and its source
  dependencies.
- The branch-independent divisibility
  `H(alpha_i,X) divides B/z_i` is imported by the source reduction pinned
  in `rate_half_kb_q6_u2_complete_source_conic_exclusion`; item 1 of that
  node's claim contract is the unqualified twelve-row saturation result,
  proved before conic invariance is used. The square identity is rederived
  locally from this input and the exact degree ledger. The recurrence router
  supplies the actual residual bidegree-`(2,4)` source model.
- The interpolation and resultant equivalences are proved locally and
  independently replayed over finite fields. No external computation or
  classification is imported.

## Upstream custody

Vendored as a shared `K3` source-component interface with the diagonal
branch compilers in draft PR `przchojecki/rs-mca#1132` at
`6127f7c4c315428507ad05ba814c0b540edc7ac7`:

```text
note blob:        a58381fe3d80f9a604197b7c5eea3c6ef6bc4b5c
verifier blob:    b88c1ab56ee8a4a5a0a091f563697417c75ef51d
certificate blob: 3b0f45160567a4b5d1aef6ee9d8e556782b5a043
payload SHA-256:  bbdab9cb571c6c6bfcdd477598aa38f4f69b43e0c3480da28b74a725faab8e33
```

The verifier independently replays the `45 x 12` kernel and rejects 15 of
15 hostile packet mutations. The sole PR check failure at this pin is
unrelated Vercel deployment authorization.
