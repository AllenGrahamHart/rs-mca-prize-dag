# conditional: midlarge_h7_20

## Predicate nodes

- `m720_mitm_gate`
- `m720_complete_calibration_certificates`
- `m720_official_exclusion`

## Claim

Conditional on the gate, complete calibration certificates, and the
official-shape exclusion lemma, the band `h in (6,20]` contributes no
unpaid active cores beyond the midlarge budget.

## Proof

The predicate `m720_mitm_gate` proves that the MITM scanner and descent
pipeline detect the known small-h trades and distinguish toral/paid cores from
non-toral active cores.

The predicate `m720_complete_calibration_certificates` supplies complete
zero-active-core certificates for the feasible calibration rows in the band
`h=7..20`, while marking n=1024 window slices as slice evidence only.

The predicate `m720_official_exclusion` is the proof step transferring the
calibration/certificate structure to official-shape rows: every candidate in
the band is either empty or charged by the paid ledger.

Together these predicates give the zero/unpaid-exclusion statement required by
`midlarge_h_certification`.
