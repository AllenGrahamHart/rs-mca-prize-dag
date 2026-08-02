# Source evidence

- Resumable batch probe:
  `probe_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch.py`.
- Exact result packet:
  `rate_half_kb_positive_433_1a_cell5_finite_candidate_batch_result.json`.
- Independent structural/root checker:
  `check_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch.py`.
- Packet SHA-256:
  `d74aa015c557d9497090b6085a4280e8a43d9dd5f4ec109e3e31b736271cd8c8`.

The packet was produced locally under the 1 GiB RAMguard fallback after two
Modal launches performed no remote work because the shared WSL PID ceiling
prevented the local Modal control thread from starting.
