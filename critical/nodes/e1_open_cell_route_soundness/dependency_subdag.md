# dependency sub-DAG: e1_open_cell_route_soundness

Edges are directed from dependency to consumer.

```text
official_row_primes_pinning [PROVED]
    -> e1_open_cell_route_soundness [PROVED]
    -> e1_official_typicality_or_certificate [CONDITIONAL]

e1_folded_certificate_soundness [PROVED]
    -> e1_open_cell_route_soundness [PROVED]
```

This node proves only the route dispatch. It does not supply the actual
uniform typicality theorem or folded certificates.
