# Source evidence

- Canonical `prize` commit `38cb4d50` supplied the statement, proof, and
  exact verifier after auditing the inverse-flatness strategy.
- `verify.py` replays all 64 block convolutions and the rational telescoping
  identity at the full order-512 split-prime row `q=7681`.
- `experiments/prize_resolution/dli_c1_l1_block_owner_ledger_modal.py`
  runs the exact replay away from local WSL memory.
