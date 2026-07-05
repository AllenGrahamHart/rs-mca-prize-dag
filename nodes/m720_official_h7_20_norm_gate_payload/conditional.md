# conditional: m720_official_h7_20_norm_gate_payload

## Predicate nodes

- `m720_official_norm_gate_case_manifest_soundness`
- `m720_official_norm_gate_case_manifest_payload`

## Claim

Conditional on the actual official norm-gate case manifest, the M720 official
h=7..20 norm-gate payload holds.

## Proof

The predicate `m720_official_norm_gate_case_manifest_payload` supplies a
manifest covering every official-shape primitive h=7..20 norm-gate case. Each
case is discharged either by a uniform nonvanishing theorem citation or by a
`complete=true` certificate record with zero unpaid non-toral survivors.

The proved predicate `m720_official_norm_gate_case_manifest_soundness` says
that such a complete manifest implies exactly this payload. Therefore this
node follows from the actual manifest payload.
