# m720_official_norm_gate_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Assume `m720_official_paid_branch_alignment`: every official-shape
`h=7..20` active-core candidate is either paid/toral or belongs to the
primitive x83 norm-gate branch.

If a payload or uniform theorem covers every primitive official h=7..20
norm-gate case and certifies zero unpaid non-toral survivors in each covered
case, with complete records in the sense of `m720_certificate_semantics`, then
the primitive norm-gate branch contributes no unpaid active cores.

## Falsifier

A complete zero payload covering every primitive norm-gate case while an
unpaid non-toral official h=7..20 active core still survives.
