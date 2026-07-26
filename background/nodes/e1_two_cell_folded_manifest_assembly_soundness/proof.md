# proof: e1_two_cell_folded_manifest_assembly_soundness

The E1 folded manifest asks for exactly two entries:

```text
N'=128
N'=256
```

Assume `e1_folded_certificate_cell_128_payload` supplies a named exhibit
field, a complete folded kernel certificate, and zero nonzero non-cyclotomic
folded vectors for the first cell. Assume
`e1_folded_certificate_cell_256_payload` supplies the analogous data for the
second cell.

Form the manifest with those two records. Its cell set is exactly
`{128,256}`. Each entry names the field being certified, is marked complete,
and records zero nonzero folded vectors. These are precisely the fields
required by `e1_folded_certificate_manifest_payload`.

Therefore the two cell payloads assemble to the named folded-certificate
manifest for the E1 open cells.
