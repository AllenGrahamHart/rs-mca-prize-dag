# dependency sub-DAG: midlarge_h7_20

Promoted subclaims.

```text
m720_mitm_gate
    -> m720_complete_calibration_certificates
    -> m720_official_exclusion
    -> midlarge_h7_20
    -> midlarge_h_certification

m720_certificate_semantics [PROVED]
    -> m720_complete_calibration_certificates

m720_off_laptop_zero_certificates
    -> m720_complete_calibration_certificates
```

## m720_mitm_gate

Statement: the MITM scanner reproduces known h=3,4,5 census facts and detects
non-toral active cores when they exist.

Status: scripted, not replayed here except syntax.

## m720_complete_calibration_certificates

Statement: complete calibration cells for h=7..20 have zero non-toral active
cores. Window slices must be labeled as slices and cannot certify global zero.

Status: CONDITIONAL. Certificate semantics are proved; no completed
off-laptop zero-certificate payload is available in this working copy.

## m720_official_exclusion

Statement: at official-shape rows, every h=7..20 active-core candidate is
empty or belongs to a charged paid structure.

Status: open. This is the theorem needed by `midlarge_h_certification`.
