# Source evidence

- Actual bidegree-`(2,4)` component, distinct deck conjugate, birational
  map to the bidegree-`(4,4)` endpoint component, and endpoint stabilizer:
  `rate_half_kb_m2_v4_outer_recurrence_router`.
- Sets `I,L,K` and the complete source facets:
  `rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`, importing
  Corollaries 9.25 and 9.27 of the equality-wall source theorem pinned
  there.
- The interpolation equivalence is proved in this node and independently
  replayed over a finite field. It imports no classification or owner
  claim.

## Upstream custody

The diagonal compiler and the companion coordinate source-facet result are
exported together in draft PR `przchojecki/rs-mca#1132` at
`77b0971ebb443efd8487ee3809cd988ba183d00c`:

```text
note blob:        a74eb30e46d8941c1cc4c598b2fdff6a3daad657
verifier blob:    8c1fd1318b180f27a3114a3a3beedd7e2ed3efbd
certificate blob: c0f6f9496e4bf43b60358133372ce47bc9b5c8dd
payload SHA-256:  96c47c813c41f4b268b9826ed4866e14d44c5a8187487266a3de6f550cbbf6b6
```

The fail-closed verifier rejects 17 of 17 hostile mutations. The sole PR
check failure at this pin is unrelated Vercel deployment authorization.
