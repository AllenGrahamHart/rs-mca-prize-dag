# Source Evidence

Exact compiler and result:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell4_xi2_pairing0_four_basis_norm_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell4_xi2_pairing0_four_basis_norm_result.json`

Proof inputs:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json`

Final four-sign Modal replay: `ap-C5xgTLe8Q7qlCfVyGg0Mbi`.

The primary verifier pins the compiler and result, checks input custody and
the full sign ledger, directly replays all finite common points, and certifies
the no-`b` terminals. The independent audit recomputes exact `F_p` roots of
the norm and every inverse polynomial from stored coefficients.
