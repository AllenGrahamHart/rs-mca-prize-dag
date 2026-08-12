# Dependency sub-DAG

```text
rate_half_kb_active_balanced_core_witness_compiler [PROVED contract]
                         |
                         v
rate_half_mca_near_rational_line_bc_guard_rejection [PROVED]
                         |
                         +--ev--> mca_safe [CONDITIONAL]
```

The incoming dependency supplies only the candidate BC guard being tested.
The outgoing edge is evidence: it records a survived hostile regression and
does not prove a safe-side bound.
