# Dependency sub-DAG

```text
pma_ratehalf_complement_linear_slice_reduction [PROVED] --------+
l1_general_first_layout_domination [PROVED] --------------------+
l1_fpc5_ratehalf_m4_t3_first_layout_atom_collapse [PROVED] -----+
l1_fpc5_ratehalf_m4_t3_master_flat_descriptor [PROVED] ----------+
                                                                  v
  l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET]
    --req--> l1_full_petal_fpc5_payment [CONDITIONAL]
```
