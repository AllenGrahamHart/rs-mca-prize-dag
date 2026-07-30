# Source evidence

## Primitive degree-20 catalogue

- GAP PrimGrp commit:
  `5612e113d50ac23a7d10945383936e20440b4e14`
- File: `data/gps1.g`, entry `PRIMGRP[20]` including trailing newline
- Exact extracted size: 342 bytes
- SHA-256:
  `cbc9ca7fda9b0de36a4034a4d59e24bb6c07aff0e54458604990919583007133`
- Raw source:
  https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g

The entry gives exactly four primitive groups, each with the sole
nontrivial subdegree 19. The independent verifier reconstructs the two
projective-line actions locally.

Accessed 2026-07-29. The source hash pins classification completeness; the
finite projective action claims are replayed without GAP.

## Upstream custody

The import-free export is pinned to PR `#1132` at
`bf173815d0a51d880c94c833be125769715f2c49`:

```text
note blob:        77b9a0cd08a71fbcce3d2a37151010c3f24fb80a
verifier blob:    c1684fd20cf6d7a7a81d83d1c4b2fec18b1eb136
certificate blob: 24f406d8bdb72d8562c91b28890eae59befd6d91
payload SHA-256:  0f7c0134c723875d66dd19d96f9c68c7299079b5560e63780910afc6d86f21d4
```

The verifier binds five parent terminals by Git blob and canonical payload,
reconstructs both projective actions, and rejects 18 of 18 mutations.
