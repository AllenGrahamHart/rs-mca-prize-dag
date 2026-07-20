# Claim contract

- **claim id:** `f3_h3_dsp8_antipodal_quotient_mass_payment`
- **mathematical statement:** `(AQM1)--(AQM4)` in `statement.md`
- **scope:** every official H3 row, using the `E=6`, `P>=25` analytic
  interface
- **consumer:** `f3_h3_dsp8_global_overlap_cover_payment`, then
  `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependencies:** the support-overlap caps, the pointwise quotient
  affine-intersection bound, and the exact primitive-SP normalization
- **new open content:** estimate the disjoint `K_25^0,K_25^A` correlation in
  the downstream target; the payment implication itself is closed
- **falsifier:** an official row violating `(AQM1)`, `(AQM2)`, or the
  implication from `(AQM3)` to the `E=6` moment endpoint
- **nonclaims:** no bound on `K_25^0`, `K_25^A`, their sum, or their
  correlation with `S_A`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_antipodal_quotient_mass_payment/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  exceptional-stratum payment
