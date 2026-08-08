# Audit

Run:

```bash
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_elliptic_four_basis_common_locus/verify.py
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_elliptic_four_basis_common_locus/verify_audit.py
```

The first verifier checks artifact custody, all 24 exact common charts, both
tower recoveries, discriminant normalization, all 12 boundary fibers, and DAG
edges.  The second verifier reconstructs cell `12`, checks every listed
rational point against its exact lex basis and route guards, and independently
tests the nonsplitting of every quadratic boundary eliminant.
