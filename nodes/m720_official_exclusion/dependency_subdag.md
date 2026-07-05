# dependency sub-DAG: m720_official_exclusion

Edges are directed from dependency to consumer.

```text
x83_uniform_square_shift_obstruction_gate [PROVED]
    -> m720_official_paid_branch_alignment [PROVED]
    -> m720_official_exclusion

a_universal_trade_variety [PROVED]
    -> m720_official_paid_branch_alignment [PROVED]
    -> m720_official_exclusion

m720_complete_calibration_certificates [PROVED]
    -> m720_official_exclusion

m720_official_h7_20_norm_gate_certificates
    -> m720_official_exclusion

m720_official_norm_gate_case_manifest_payload [TARGET]
    -> m720_official_h7_20_norm_gate_payload [CONDITIONAL]
    -> m720_official_h7_20_norm_gate_certificates [CONDITIONAL]

m720_official_h7_20_norm_gate_payload [CONDITIONAL]
    -> m720_official_h7_20_norm_gate_certificates [CONDITIONAL]
```

## Status

- `m720_official_paid_branch_alignment`: PROVED. This is only the x83
  paid-versus-norm-gate dichotomy for the h=7..20 official band.
- `m720_official_norm_gate_certificate_soundness`: PROVED. Complete official
  payloads or uniform nonvanishing theorems soundly exclude the primitive
  norm-gate branch.
- `m720_official_norm_gate_case_manifest_payload`: TARGET. This is the
  remaining non-circular official case manifest for the admissible-family
  theorem or named-exhibit certificate payload.
- `m720_official_h7_20_norm_gate_certificates`: CONDITIONAL.
- `m720_official_exclusion`: CONDITIONAL on that payload leaf.

Do not replace the certificate leaf by `h4_sparse_norm_gate`: the broad
norm-gate chain currently depends on `midlarge_h_certification`, which consumes
this M720 branch.
