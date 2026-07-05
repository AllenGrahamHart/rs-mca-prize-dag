# conditional: m720_official_exclusion

## Predicate nodes

- `m720_complete_calibration_certificates`
- `m720_official_paid_branch_alignment`
- `m720_official_h7_20_norm_gate_certificates`

## Claim

Conditional on the structural paid/norm-gate dichotomy and the admissible-
family or named-exhibit norm-gate certificates, the `h=7..20` official-shape
band contributes no unpaid active cores.

## Proof

The complete calibration certificates establish that the M720 bounded-band
scanner and certificate semantics are aligned with the intended active-core
object and that complete calibration cells carry no unpaid non-toral cores.

The proved predicate `m720_official_paid_branch_alignment` supplies the
structural transfer: every official-shape `h=7..20` active-core candidate lies
in one of two branches. The paid full-fiber/toral branch is charged by the
existing paid ledger. The only branch that could contribute unpaid mass is the
primitive `p`-specific x83 norm-gate branch.

The predicate `m720_official_h7_20_norm_gate_certificates` excludes that
remaining branch uniformly over the admissible family, or for the named
exhibit fields used by the certificate packet. Hence every official-shape
candidate is empty or paid, proving the statement of `m720_official_exclusion`.
