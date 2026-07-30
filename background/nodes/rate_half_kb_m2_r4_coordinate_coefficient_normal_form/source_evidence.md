# Source evidence

- The preserving lift `(tau,b)`, exact coordinate source facets, and deck
  distinction are
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature` together
  with its recurrence parent.
- Uniqueness of the source interpolant is
  `rate_half_kb_m2_r4_source_row_interpolation_compiler`.
- The parity decomposition and norm identity are proved locally and replayed
  by two exact verifiers. No remote computation or classification is used.

## Upstream custody

Vendored in the order-two coefficient packet in draft PR
`przchojecki/rs-mca#1132` at
`c88438d7109cf7acd7caebaf006f21c776b74d74`:

```text
note blob:        f58c2ea9cea88dfc6be637e9f1f14e86e8862cc6
verifier blob:    7cc4eb6e0560ca5c587f91623dc407892a07e2ca
certificate blob: 033043e7a0969ea9f98207567b890b10e3077271
payload SHA-256:  f0b751301e56989bf6fbf19cf15e5ff8faa0d7d86e76278306950a488cdf5156
```

The verifier replays both coordinate parity spaces and rejects 18 of 18
hostile packet mutations. The sole PR check failure at this pin is
unrelated Vercel deployment authorization.
