# Audit

- Joint-census production app: `ap-kByaSsYhxYgKb4TJqkEuLT`.
- Joint-census audit app: `ap-FqluYkBc3DLz687GeYxBgp`.
- Joint production/audit worker times: 219.666239084 and 331.165567033 seconds.
- Exact-norm FLINT app: `ap-iEm8zqbRcOWdVO9qSVwi4o`.
- Exact-norm PARI app: `ap-pBUnRmFuHfemCN6jBFUmG6`.
- Norm production/audit worker times: 217.814118729 and 340.729670766 seconds.
- Every campaign uses 87 checkpointed rows, 512 MiB or less per worker, and a
  60-second per-worker timeout.
- Independent engines agree on every profile count, conductor count, maximum,
  exact-norm count, and exact-norm maximum.
- Hostile checks reject a missing template, a changed census maximum, omission
  of a conductor complement, a single norm at `2^250`, or a changed global
  maximizing witness.

No floating-point comparison enters the closure.
