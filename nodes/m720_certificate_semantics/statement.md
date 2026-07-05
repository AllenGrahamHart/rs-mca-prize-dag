# m720_certificate_semantics

- **status:** PROVED
- **closure:** proof

## Statement

For M720 MITM outputs, a zero active-core count is a complete
calibration-cell zero certificate only when the run has `complete=true`,
equivalently `W=n` and the run did not abort. If `complete=false`, the output
is slice-local evidence only and cannot be promoted to a global zero
certificate.

## Falsifier

A certificate protocol that treats `W<n` or aborted output as a complete
global zero.
