# Source Evidence

The theorem is an exact combinatorial composition of three PROVED parents:

- `rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi0_pairing0_four_basis_exclusion`
- `rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi1_pairing0_parallel_edge_transport`
- `rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi2_pairing0_four_basis_exclusion`

`verify.py` regenerates all fifteen canonical perfect matchings, checks the
first-three pair block and residual record order, binds the parent statuses,
and checks DAG wiring. `verify_audit.py` uses an explicit independent
matching table and audits the `144`-case Cartesian count.

No new numerical or computer-algebra result is used.
