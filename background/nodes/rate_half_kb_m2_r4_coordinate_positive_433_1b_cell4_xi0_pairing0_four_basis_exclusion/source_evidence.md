# Source Evidence

Exact compiler and result:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_result.json`

Proof inputs:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json`

Final four-sign Modal replay: `ap-7c3gryhV1UAm4x1DxpxfgM`.

The primary verifier pins the compiler and result, checks input custody and the
full sign ledger, and replays every boundary guard.  The independent audit
uses a separate polynomial arithmetic implementation to recompute the exact
`F_p` roots of the norm and all inverse polynomials from the stored
coefficients.
