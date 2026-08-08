# Audit

Run:

```bash
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_global_common_kernel/verify.py
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_global_common_kernel/verify_audit.py
```

The first command checks custody, kernel uniqueness, all 40 exact reductions,
the seven formal polynomial identities, and DAG wiring.  The second command
checks all 80 sign-specific row pairings at the eight rational leading-
boundary points.
