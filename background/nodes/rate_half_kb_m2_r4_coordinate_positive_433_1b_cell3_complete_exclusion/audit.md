# Audit

- The rank split is exhaustive because the five-row product block has rank at
  most five.
- Cell 3 appears explicitly in the rank-drop classifier's unit-ideal list.
- The principal Cartesian ledger contains exactly `7*15*4*4=1680` tuples.
- The parallel-`DE` suppliers cover exactly `(xi,matching)` in
  `{0,1,2}*{0,...,14}`.
- The six `xi=3` suppliers are disjoint and cover all fifteen matchings.
- The exact transport pays only `xi=4`; the finite-source and endpoint
  theorems pay only `xi=5` and `xi=6` respectively.
- A set-theoretic verifier constructs every raw tuple supplied by each node,
  rejects overlap, and proves equality with the full principal Cartesian set.
- No common-target exchange or transport to source role cell 6 is used.
