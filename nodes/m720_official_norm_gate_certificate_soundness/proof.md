# proof: m720_official_norm_gate_certificate_soundness

By `m720_official_paid_branch_alignment`, every official-shape h=7..20
active-core candidate is in exactly one of the two relevant branches for this
consumer:

1. the paid/toral branch, already charged elsewhere; or
2. the primitive p-specific norm-gate branch.

The present node concerns only the second branch. Suppose a uniform
nonvanishing theorem covers that primitive branch. Then no primitive
norm-gate event can occur, so there is no unpaid non-toral survivor.

Alternatively, suppose a certificate payload covers every official primitive
norm-gate case. By `m720_certificate_semantics`, only records with
`complete=true` are complete zero certificates; incomplete slices are local
evidence only. If every covered primitive record is complete and reports zero
unpaid non-toral survivors, then every primitive norm-gate case has been
checked globally and has no survivor.

Thus either accepted payload type excludes the entire primitive norm-gate
branch. Since the other branch is paid, this is exactly the soundness rule
needed by `m720_official_h7_20_norm_gate_certificates`.
