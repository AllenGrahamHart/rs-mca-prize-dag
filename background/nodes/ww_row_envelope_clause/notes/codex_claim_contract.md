# Claim contract: retired open W3 envelope

- **claim id:** `ww_row_envelope_clause`.
- **claim:** `N_nonplant(U)<=B*-p(U)` for every safe-side in-scope planted
  receiver.
- **status:** `TARGET`, retired from the prize requirement path.
- **scope-counterexample row:** prime field `q=1705*2^120+1`, `n=8192`,
  `k=2048`.
- **strict unsafe-cell failure:** six plants plus one factored non-plant
  exceed `B*=6`.
- **proof packet:**
  `background/nodes/ww_spending_cell_fiber_layout_counterexample/`.
- **consumer disposition:** evidence only; the repaired clean-rate crossing
  consumes `list_unsafe`, `list_safe`, and `list_corridor_ledger` directly.
- **nonclaim:** neither the list prize nor literal safe-side W3 is falsified,
  because the exhibited cell is on the unsafe side.
