# Dependency sub-DAG

```text
rate_half_list_integer_johnson_safe_anchor [PROVED]
  -> rate_half_list_low_budget_exact_crossing [PROVED]
       -> rate_half_list_adjacent_crossing [TARGET, evidence]
```

The requirement edge carries the safe side. The two explicit predecessor
constructions are proved inside this node. The outgoing edge is evidence
because only the `B*=1,2` branches are closed; the critical target remains a
logical leaf for all larger budgets.
