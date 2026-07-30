# Source evidence

- The actual bidegree-`(2,4)` source model, its birational map to the
  bidegree-`(4,4)` endpoint component, and the diagonal stabilizer are pinned
  by
  `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`.
- Odd characteristic and separability are part of the deployed KoalaBear
  challenge-field scope.
- The intermediate-field dichotomy, reciprocal normal form, and tame
  fixed-point calculation are proved locally. No group catalogue,
  computation, or unproved source lift is imported.

## Upstream custody

Vendored with the two coefficient compilers in draft PR
`przchojecki/rs-mca#1132` at
`c88438d7109cf7acd7caebaf006f21c776b74d74`:

```text
note blob:        f58c2ea9cea88dfc6be637e9f1f14e86e8862cc6
verifier blob:    7cc4eb6e0560ca5c587f91623dc407892a07e2ca
certificate blob: 033043e7a0969ea9f98207567b890b10e3077271
payload SHA-256:  f0b751301e56989bf6fbf19cf15e5ff8faa0d7d86e76278306950a488cdf5156
```

The verifier pins the preceding order-two packet by commit, three blobs,
and payload, and rejects 18 of 18 hostile mutations. The sole PR check
failure at this pin is unrelated Vercel deployment authorization.
