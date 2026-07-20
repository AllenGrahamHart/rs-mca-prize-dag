# Claim contract

- **claim id:** `f3_h3_quotient_anharmonic_antipodal_twin`
- **mathematical statement:** `(AAT1)--(AAT3)` in `statement.md`
- **scope:** every odd-characteristic subgroup row; the official dyadic rows
  are a special case
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependencies:** the product/quotient fiber definitions and the
  antipodal target classification
- **new open content:** none
- **falsifier:** unequal `R` values in one anharmonic orbit, or an antipodal
  target with unequal `P` values under `tau` or odd `P`
- **nonclaims:** no invariance of generic members, signed-support edges,
  `N_6^disj`, or the DSP8 summand
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_quotient_anharmonic_antipodal_twin/verify.py`
