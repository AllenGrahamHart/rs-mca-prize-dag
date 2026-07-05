# conditional: e1_official_typicality_or_certificate

This node is conditional on:

- `official_row_primes_pinning`
- `e1_folded_certificate_soundness`
- `e1_open_cell_route_soundness`
- `e1_open_cell_control_payload`

The first three dependencies are proved. The fourth is now conditional on the
folded-certificate manifest payload. That manifest payload is itself
conditional on the two explicit cell certificate payloads for `N'=128` and
`N'=256`.
