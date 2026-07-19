# m720_residual_off_laptop_zero_certificates

- **status:** PROVED
- **closure:** proof

## Statement

Every `h=7..20` calibration cell not covered by
`m720_wsl_complete_zero_subcertificates` is either explicitly outside the
complete-cell certificate set as a window slice, or is one of the over-ceiling
`n=32,h=16` complete-window cells with a separate zero certificate.

## Falsifier

A residual complete calibration cell with nonzero unpaid non-toral active
cores, or missing/false completeness metadata.
