# Source Evidence

- Primary compiler:
  `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi5_finite_source_pairing_solver_modal.py`
- Primary census:
  `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi5_finite_source_pairing_solver_census_result.json`
- Primary pilot app: `ap-ASPspplGjYppHtU1SgOt0P`.
- Primary census app: `ap-ktYckYqQlxXbMlDWHZFlrA`.
- Primary compiler SHA-256:
  `059bebe72375f5adcb215aaf9a3fa41ba1ecf56e5078decf19f073b1a1cdef60`.
- Primary census SHA-256:
  `bd5819475633a6f188635c2fefdd338cd1707db2249cb5e4276ef7687db248a2`.
- Independent compiler:
  `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi5_finite_source_pairing_audit_modal.py`
- Independent census:
  `experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi5_finite_source_pairing_audit_census_result.json`
- Independent census app: `ap-vpzdSl63FgUGaAxRyaD9pl`.
- Independent compiler SHA-256:
  `10a830f0e2864393548e50e8705e2b2c8c3a408b32fbf7d38b47e9f19cb64401`.
- Independent census SHA-256:
  `fbdeb02f8baaa12af3c9240299eed49f932b24b9f0dde66fdf872fdc6b9d49c0`.

Both censuses use the hash-pinned endpoint source census and compact kernel.
They agree on all 24 sources, all 1440 subcases, the per-source outer-root
counts, the 2208-root aggregate, and the empty inner-root ledger.
