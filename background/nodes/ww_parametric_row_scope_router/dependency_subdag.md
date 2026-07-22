# Dependency sub-DAG

```text
official_row_primes_pinning [PROVED] --+
descriptor [PROVED] ------------------+--req-->
  ww_parametric_row_scope_router [PROVED]
    --ev--> ww_row_envelope_clause [TARGET, RETIRED]
                    ^
ww_spending_cell_fiber_layout_counterexample [PROVED] --ref--+
```

The first dependency fixes the challenge quantifiers.  The second supplies
the total exact row map. Those results made the exact unsafe-cell scope
counterexample admissible and checkable; they do not decide safe-side W3.
