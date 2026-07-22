# Dependency sub-DAG

```text
l1_exact_shell_balanced_shifted_lattice_reduction [PROVED]
  | req: every band exact shell is represented in one degree-capped
  |      interpolation-module split pencil
  v
l1_split_pencil_content_exact_shell_descent [PROVED]
  | ev: raw split-pencil points are partitioned by basis-invariant content;
  |     exact BC is exactly the coprime coefficient-pair locus
  v
l1_mixed_petal_amplification [TARGET]
```

The new node has no row-sharp counting premise.  Its unresolved consumer is
the number of primitive split-pencil points after the content partition.
