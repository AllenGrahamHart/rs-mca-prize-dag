# proof: e1_folded_certificate_manifest_soundness

The named folded-certificate route in `e1_open_cell_control_payload` requires
exactly two open-cell entries, one for `N'=128` and one for `N'=256`.

Assume the manifest supplies both entries. Each entry names the exhibit field
being certified, marks the folded kernel search as complete, and records zero
nonzero non-cyclotomic folded vectors.

Those are precisely the fields required by the payload's second accepted
route: named exhibit fields with complete folded kernel certificates returning
no nonzero non-cyclotomic folded vector. Therefore the manifest satisfies
`e1_open_cell_control_payload`.

This proof is only route-shape soundness. The actual certificate transcripts
for the two open cells are isolated in
`e1_folded_certificate_manifest_payload`.
