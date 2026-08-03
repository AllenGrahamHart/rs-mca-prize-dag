# Source Evidence

Exact projection compiler and five full shards:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_target_projection_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_simple_full_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_df_chain_full_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_ef_chain_full_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_bf_targetfree_full_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_cf_targetfree_full_result.json`

The frozen launcher predates the rank-one proof modes and retains its original
discovery-oriented filename and docstring. The theorem uses only
`rankone_resultant`, `rankone_chain`, and `rankone_targetfree`; the aggregate
checker rejects every other branch.

Boundary compiler and aggregate checker:

- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_census.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_census_result.json`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_root_replay_modal.py`
- `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell14_rankone_root_replay_result.json`

Final Modal apps:

- direct-resultant shard: `ap-aJegcixulC1hBDQ8PQtkSM`
- missing-`df` chain shard: `ap-dvxHxN0A3m8wcTyfoVs6uJ`
- missing-`ef` chain shard: `ap-nXDSKUDdqZVVpkHVYSQIwM`
- missing-`bf` target-free shard: `ap-1qgp8j9Fy2dWpV4meMnmeW`
- missing-`cf` target-free shard: `ap-vMwrRLuhBaBIVyQMrn08sW`
- division-free boundary census: `ap-1oux7CH8KaTbMbizmt9dbx`
- independent field-root replay: `ap-Q1nON1zHA2fDVllZQRjkrf`
