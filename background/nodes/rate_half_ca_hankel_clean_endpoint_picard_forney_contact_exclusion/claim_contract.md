# Claim contract

- **Claim:** the full Hankel recurrence gives order `2rho+2` contact of the
  Forney numerator with the domain-infinity fibre; after the clean degree-one
  Picard pin, four residual sections would give a forbidden section of
  `O_C(-8,3)`.
- **Dependencies:** the normalized Forney numerator/resultant theorem and
  the two-axis resultant/Picard pin.
- **Output:** unconditional exclusion of the `O=0` endpoint for `m>3`.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** no positive-defect endpoint stratum or adjacent unsafe
  witness is closed.
- **Falsifier:** a missing final Hankel recurrence row, contact below
  `2rho+2`, the opposite Picard-line-bundle sign, a nonzero
  `H^0(C,O_C(-8,3))` for `m>3`, or a zero Forney section on `C`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_picard_forney_contact_exclusion/verify.py`
  and `verify_audit.py`.
