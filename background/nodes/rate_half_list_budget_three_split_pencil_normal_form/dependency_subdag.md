# Dependency sub-DAG

```text
rate_half_list_budget_three_intersection_reduction [PROVED]
  -> rate_half_list_budget_three_split_pencil_normal_form [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The incoming edge is a requirement. The outgoing edge is evidence: the new
node replaces a large matrix-kernel search by a constant-degree split-pencil
classification target but does not exclude that target.
