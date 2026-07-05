# e1_folded_certificate_manifest_soundness

- **status:** PROVED
- **closure:** proof

## Statement

If a manifest covers `N' in {128,256}` with named exhibit fields and complete
folded kernel certificate records, each returning zero nonzero
non-cyclotomic folded vectors, then `e1_open_cell_control_payload` holds by
the named folded-certificate route.

## Falsifier

A manifest covering both open cells with complete zero folded certificates
while the E1 open-cell payload route is not satisfied.
