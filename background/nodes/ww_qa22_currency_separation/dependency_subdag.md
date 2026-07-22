# Dependency sub-DAG

```text
xr_target_budget_audit [PROVED] ---------------------+
ww_two_class_minimal_ledger_reduction [PROVED] ------+--req-->
  ww_qa22_currency_separation [PROVED]
    --ev--> ww_row_envelope_clause [TARGET, RETIRED]
    --ev--> worst_word_challenger_pricing [CONDITIONAL]

xr_target_budget_audit [PROVED] --ev--> worst_word_challenger_pricing
```

The first dependency supplies the exact QA.22 arithmetic and its MCA
currency. The second supplies the correct list-side composition law. Both
remain proved; neither decides the retired safe-side W3 target.
