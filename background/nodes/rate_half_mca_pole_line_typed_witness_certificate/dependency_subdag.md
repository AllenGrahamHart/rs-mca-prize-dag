# Dependency sub-DAG

```text
rate_half_mca_degree_guarded_shifted_lattice_witness_adapter [PROVED]
                              |
upstream #1159 actual record  |
                \             |
                 v            v
rate_half_mca_pole_line_typed_witness_certificate [PROVED]
                              |
                              +--ev--> mca_safe [CONDITIONAL]
```

The dependency supplies the local guard semantics.  The upstream record is
pinned source evidence.  The outgoing edge records a typed hostile/control
instance and pays no slopes.
