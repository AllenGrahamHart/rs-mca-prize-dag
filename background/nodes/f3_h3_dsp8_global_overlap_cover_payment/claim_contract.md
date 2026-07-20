# Claim contract

- **claim id:** `f3_h3_dsp8_global_overlap_cover_payment`
- **mathematical statement:** `(GOP1)--(GOP3)` in `statement.md`
- **scope:** every official H3 row, using the `E=6`, `P>=25` analytic
  interface
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependencies:** the canonical two-cover overlap classification,
  the pointwise quotient affine-intersection bound, the antipodal quotient
  mass bound, and the primitive-SP normalization
- **new open content:** prove `(GOP2)` directly, or the stronger uniform
  estimate `(GOP3)`
- **falsifier:** a generic--generic overlapping edge not uniquely assigned to
  one cover parameter, more than `2n` such edges globally, or failure of the
  implication from `(GOP2)` to the `E=6` endpoint
- **nonclaims:** no bound on `K_25^0`, `K_25^A`, their sum, or their
  correlation with `S_A`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_global_overlap_cover_payment/verify.py`
- **upstream mapping:** primitive shift-pair control / exact second-moment
  exceptional-stratum payment
