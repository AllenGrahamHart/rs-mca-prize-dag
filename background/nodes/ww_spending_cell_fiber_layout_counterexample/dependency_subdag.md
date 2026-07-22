# Dependency sub-DAG - unsafe spending-cell fiber-layout counterexample

```text
ww_spending_cell_fiber_layout_counterexample [PROVED]
    --ref--> ww_row_envelope_clause [TARGET, RETIRED]

list_unsafe [PROVED] --------------------\
list_safe [CONDITIONAL] ------------------+--> list_adjacency_closing [CONDITIONAL]
list_corridor_ledger [PROVED] ------------/

list_planted_arithmetic [CONDITIONAL] --ev--> list_adjacency_closing
```

The repaired route keeps the explicit unsafe witnesses and the independent
safe corridor. W3's literal safe-side claim remains open but is no longer a
prize requirement.
