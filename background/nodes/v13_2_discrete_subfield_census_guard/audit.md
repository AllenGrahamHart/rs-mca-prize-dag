# Source and scope audit

Audited on 2026-07-19 against upstream commit
`4bea7abb2d9455583c8864b980e39d11d550f51d` (Paper D v13.2 promotion).

- revision-note blob:
  `2043c69a34b100a514366e5b0768777f28cf952f`
- TeX blob:
  `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb`
- source formula: `prop:capg-census-floor`
- correction record: revision notes section 3.1

The local v13 correspondence note had used the unclamped product for
several interior displays and inferred that nonbase tower levels were
numerically empty. Exact replay refutes that inference: a below-one
prefix mean still has discrete floor one before support multiplication.

The structural proof of `f1_case_tower` does not consume the old table;
it descends to the minimal field and invokes proved routing mechanisms.
No critical node is demoted. Finite upper ledgers are now explicitly
guarded to retain the mean-plus-one support term.
