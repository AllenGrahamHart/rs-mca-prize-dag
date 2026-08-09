# Audit

Run:

```bash
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_quadratic_four_basis_common_locus/verify.py
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_quadratic_four_basis_common_locus/verify_audit.py
```

The first verifier checks artifact custody, all 24 exact common charts, both
tower recoveries, the genus-three discriminant, all eight boundary fibers,
and DAG edges. The second reconstructs cell `11` and independently checks
the nonsplitting of every quadratic boundary eliminant.
