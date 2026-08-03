# Source Evidence

Exact generators and pinned outputs:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_compact_structure_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_compact_structure_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_projection_profile_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_projection_profile_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_compact_kernel_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json`

Modal runs:

- compact 24-chart structure census: `ap-AGqPPKN3W9rfwjFIqffQrB`
- repaired 24-chart beta-boundary census: `ap-SrNopezdI7zgrke9RrPYIK`
- projection factor and reciprocal profile: `ap-LuSwHZu7pT3DhViknVB1Wa`
- four-sign polynomial kernel compiler: `ap-6qVkMVGOgnUN7LeauQtkaL`

The primary verifier pins all six evidence files by SHA-256.  It checks source
custody, the complete Cartesian chart cover, chart-uniform projections, exact
factor reconstruction records, reciprocal reconstruction, the 24 unit
beta-boundary ideals, kernel digest equality, and all ten row checks.
