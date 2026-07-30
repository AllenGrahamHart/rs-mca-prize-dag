# Source evidence

- The actual bidegree-`(2,4)` source component and twelve distinct labels
  are pinned uniformly on the residual `u=2` branch by
  `rate_half_kb_m2_v4_outer_recurrence_router` and its source dependencies.
- The branch-independent divisibility
  `H(alpha_i,X) divides B/z_i` is imported by the source reduction pinned
  in `rate_half_kb_q6_u2_complete_source_conic_exclusion`; item 1 of that
  node's claim contract is the unqualified twelve-row saturation result,
  proved before conic invariance is used. The square identity is rederived
  locally from this input and the exact degree ledger. The recurrence router
  supplies the actual residual bidegree-`(2,4)` source model for all three
  V4-stabilizer types. Neither input uses the order-two subgroup.
- The interpolation and resultant equivalences are proved locally and
  independently replayed over finite fields. No external computation or
  classification is imported.

## Upstream custody

Vendored as a shared `K3` source-component interface with the diagonal
branch compilers in draft PR `przchojecki/rs-mca#1132` at
`c88438d7109cf7acd7caebaf006f21c776b74d74`:

```text
note blob:        f58c2ea9cea88dfc6be637e9f1f14e86e8862cc6
verifier blob:    7cc4eb6e0560ca5c587f91623dc407892a07e2ca
certificate blob: 033043e7a0969ea9f98207567b890b10e3077271
payload SHA-256:  f0b751301e56989bf6fbf19cf15e5ff8faa0d7d86e76278306950a488cdf5156
```

The verifier independently replays the `45 x 12` kernel and rejects 18 of
18 hostile packet mutations. The universal quantifier is separately pinned
in the same draft PR by the source-facet packet at commit
`de237ba4d6ffd03bddc3d3daa7e94d0dee06eedf`, canonical payload
`49131c6962e551c529d0681427ef9fee0eb10ea2bb42ffa5f46db3c63710ca8c`;
that verifier binds the independent complete-source and source-facet
parents and rejects 28 of 28 hostile mutations. The sole PR check failure
at this pin is unrelated Vercel deployment authorization.
