# Dependency sub-DAG

```text
f2_admissible_direct_sum_grs_reduction [PROVED]
  --req-->
           f2_admissible_generating_branch_classification [PROVED]
  --req-->
f2_minus_branch_coupled_negacyclic_reduction [PROVED]

f2_admissible_generating_branch_classification
  --ev--> f2_conditional_close [TARGET]
```

The node completes the admissible generating-row census. It does not pay
the separate mass or non-generating-row terminals.
