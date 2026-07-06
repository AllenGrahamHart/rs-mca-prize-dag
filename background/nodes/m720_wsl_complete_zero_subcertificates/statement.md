# m720_wsl_complete_zero_subcertificates

- **status:** PROVED
- **closure:** verifier

## Statement

The WSL-safe complete `h=7..20` calibration cells selected by the Modal scan
ceiling have `complete=true` and zero unpaid non-toral anchored active cores.
These cells are:

```text
n=16, h=7, p=257
n=16, h=7, p=4129
n=32, h=7, p=1153
n=32, h=7, p=32801
n=16, h=8, p=257
n=16, h=8, p=4129
```

The h=8 n=16 cells contain one anchored toral core each, but no unpaid
non-toral core.

## Falsifier

A complete replay of any listed cell returning nonzero unpaid non-toral
anchored cores, or failing the complete-cell condition `W=n` with no abort.
