# Audit

Run:

```bash
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_rational_boundary_complete_exclusion/verify.py
python3 background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_rational_boundary_complete_exclusion/verify_audit.py
```

The first verifier checks pinned custody, 32 exact shards, 105 labels per
shard, zero primary witnesses/unresolved rows, zero audited guarded-root
degree/free branches, and DAG wiring.  The second independently checks point
coverage, modular square-root identities, and the two endpoint obstructions.
