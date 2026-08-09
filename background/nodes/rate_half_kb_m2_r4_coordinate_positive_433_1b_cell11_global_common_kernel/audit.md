# Audit

Run:

```bash
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_global_common_kernel/verify.py
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_global_common_kernel/verify_audit.py
```

The primary verifier checks artifact custody, four exact sign rows, one
kernel signature, 40 zero reductions, seven formal identities, and DAG
edges. The independent verifier reconstructs all common rows from the source
compiler and confirms that a one-coordinate mutation breaks a formal
identity.
